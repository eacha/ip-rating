import argparse
import json
import time
import urllib
import os
from censys.export import CensysExport
from censys.query import CensysQuery
import keys
from HTTP import *
from Certificate import *
from HTTP.HTTPRule import HTTPRule
from Certificate.CertificateRule import CertificateRule
from Rules import Score
from asn import AS

os.environ["CENSYS_API_ID"] = keys.CENSYS_API_ID
os.environ["CENSYS_API_SECRET"] = keys.CENSYS_API_SECRET

HTTP_QUERY = "SELECT ip, p80.http.get.headers.server server, p80.http.get.headers.www_authenticate www_authenticate, " \
             "p80.http.get.headers.x_powered_by x_powered_by, p80.http.get.status_code status_code " \
             "FROM {0} WHERE autonomous_system.asn = {1} AND NOT (p80.http.get.status_code IS NULL)"
HTTP_DOWNLOAD_NAME = 'http-as{0}.json'
CERTIFICATE_QUERY = "SELECT flatter_table.ip ip, flatter_table.tls_version tls_version, flatter_table.trusted trusted, flatter_table.heartbleed_vulnerable heartbleed_vulnerable, " \
                    "flatter_table.ssl_3_support ssl_3_support, flatter_table.ssl_2_support ssl_2_support, flatter_table.cipher_suite cipher_suite, " \
                    "nested_table.chain_rsa_public_key_length chain_rsa_public_key_length, nested_table.chain_signature_algorithm chain_signature_algorithm, " \
                    "FROM (SELECT mid.ip ip, mid.tls_version tls_version, mid.trusted trusted, mid.heartbleed_vulnerable heartbleed_vulnerable, mid.ssl_3_support ssl_3_support, " \
                    "ssl2.ssl_2_support ssl_2_support, mid.cipher_suite cipher_suite FROM (SELECT country.ip ip, country.p443.https.tls.version tls_version, " \
                    "country.p443.https.tls.validation.browser_trusted trusted, country.p443.https.heartbleed.heartbleed_vulnerable heartbleed_vulnerable, " \
                    "NOT(ssl3.data.tls.server_hello.cipher_suite.hex IS NULL) ssl_3_support, country.p443.https.tls.cipher_suite.name cipher_suite, " \
                    "FROM (SELECT * FROM {0} WHERE autonomous_system.asn = {2} AND NOT (p443.https.tls.version IS NULL)) AS country LEFT OUTER JOIN {1} AS ssl3 " \
                    "ON country.ip = ssl3.ip) AS mid JOIN (SELECT ip, p443.https.ssl_2.support ssl_2_support FROM {0} WHERE autonomous_system.asn = {2}) AS ssl2 " \
                    "ON mid.ip = ssl2.ip) AS flatter_table LEFT OUTER JOIN (SELECT table_rsa_public_key_length.ip ip, " \
                    "table_rsa_public_key_length.chain_rsa_public_key_length chain_rsa_public_key_length, table_chain_signature_algorithm.chain_signature_algorithm, " \
                    "chain_signature_algorithm FROM (SELECT ip, IFNULL(CONCAT(STRING(p443.https.tls.certificate.parsed.subject_key_info.rsa_public_key.length), ',', " \
                    "GROUP_CONCAT(STRING(p443.https.tls.chain.parsed.subject_key_info.rsa_public_key.length))), " \
                    "STRING(p443.https.tls.certificate.parsed.subject_key_info.rsa_public_key.length)) chain_rsa_public_key_length FROM {0} WHERE autonomous_system.asn = {2} " \
                    "AND NOT (p443.https.tls.version IS NULL) GROUP BY ip, p443.https.tls.certificate.parsed.subject_key_info.rsa_public_key.length) AS table_rsa_public_key_length " \
                    "JOIN (SELECT ip, IFNULL(CONCAT(p443.https.tls.certificate.parsed.signature.signature_algorithm.name, ',', " \
                    "GROUP_CONCAT(p443.https.tls.chain.parsed.signature_algorithm.name)), p443.https.tls.certificate.parsed.signature.signature_algorithm.name) " \
                    "chain_signature_algorithm FROM {0} WHERE autonomous_system.asn = {2} AND NOT (p443.https.tls.version IS NULL) GROUP BY ip, " \
                    "p443.https.tls.certificate.parsed.signature.signature_algorithm.name) AS table_chain_signature_algorithm " \
                    "ON table_rsa_public_key_length.ip=table_chain_signature_algorithm.ip) AS nested_table ON flatter_table.ip=nested_table.ip"
CERTIFICATE_DOWNLOAD_NAME = 'certificate-{0}.json'
FOLDER_NAME = time.strftime('%Y-%m-%d')


def argument_parser():
    parser = argparse.ArgumentParser(description='Recollect IP data')
    parser.add_argument('-i', '--input', help='Input file name', required=False)
    parser.add_argument('--http', help='Rate the ips with the port 80 open', action='store_true', required=False)
    parser.add_argument('--certificate', help='Rate the ips with certificates', action='store_true', required=False)
    return parser.parse_args()


def append_if_not_none(collection, value):
    if value is not None:
        collection.append(value)
    return


def avg(scores):
    final_score = 0
    for score in scores:
        final_score += score

    final_score /= float(len(scores))
    return final_score


def make_dir(dir_name):
    try:
        os.mkdir(dir_name)
    except OSError:
        return


def download_file(job_answer, file_name):
    if job_answer['status'] == 'success':
        testfile = urllib.URLopener()
        testfile.retrieve(job_answer['download_paths'][0], FOLDER_NAME + '/' + file_name)
        return True
    return False


def file_rate(rules, input_filename):
    input_file = open(input_filename, 'r')
    output_file = open(os.path.abspath(os.path.dirname(input_file.name)) +
                       '/rated_' + os.path.basename(input_file.name), 'w')
    country = list()

    for line in input_file:
        json_line = json.loads(line)
        subclasses = rules.all_subclasses()
        score = Score()

        for sub in subclasses:
            sub().apply_rule(json_line, score)

        ip_avg = score.calc_avg()
        data = {
            'ip': json_line['ip'],
            'score': ip_avg
        }
        output_file.write(json.dumps(data) + '\n')
        append_if_not_none(country, ip_avg)

    input_file.close()
    output_file.close()

    return avg(country)


def http_rate(input_filename):
    return file_rate(HTTPRule, input_filename)


def certificate_rate(input_filename):
    return file_rate(CertificateRule, input_filename)


def export_data(query, filename):
    export = CensysExport()
    job = export.new_job(query, flatten=True)
    job_response = export.check_job_loop(job['job_id'])
    print job_response
    return download_file(job_response, filename.format(as_code))


if __name__ == '__main__':
    args = argument_parser()

    if args.input:
        if args.http:
            print http_rate(args.input)

        if args.certificate:
            print certificate_rate(args.input)
    else:
        make_dir(FOLDER_NAME)

        for as_code in AS.AS_CODE:
            if args.http:
                query_set = CensysQuery()
                success = export_data(
                    HTTP_QUERY.format(query_set.get_series_details('ipv4')['tables'][-1], as_code),
                    HTTP_DOWNLOAD_NAME
                )

                if success:
                    print str(as_code) + ': ' + \
                          str(http_rate(FOLDER_NAME + '/' + HTTP_DOWNLOAD_NAME.format(as_code)))

            if args.certificate:
                query_set = CensysQuery()
                success = export_data(
                    CERTIFICATE_QUERY.format(query_set.get_series_details('ipv4')['tables'][-1],
                                             query_set.get_series_details('p443_https_ssl_3_full_ipv4')['tables'][-1],
                                             as_code),
                    CERTIFICATE_DOWNLOAD_NAME
                )

                if success:
                    print str(as_code) + ': ' + \
                          str(certificate_rate(FOLDER_NAME + '/' + CERTIFICATE_DOWNLOAD_NAME.format(as_code)))
