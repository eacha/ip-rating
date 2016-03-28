import argparse
import json

import time
import urllib
import os

from censys.export import CensysExport

import keys
from HTTP import *
from Certificate import *
from HTTP.HTTPRule import HTTPRule
from Certificate.CertificateRule import CertificateRule
from Rules import Score
from country import Country

os.environ["CENSYS_API_ID"] = keys.CENSYS_API_ID
os.environ["CENSYS_API_SECRET"] = keys.CENSYS_API_SECRET

HTTP_QUERY = "SELECT ip, p80.http.get.headers.server server, p80.http.get.headers.www_authenticate www_authenticate, " \
             "p80.http.get.headers.x_powered_by x_powered_by, p80.http.get.status_code status_code " \
             "FROM ipv4.20160316 WHERE location.country_code = '{}' AND NOT (p80.http.get.status_code IS NULL)"
HTTP_DOWNLOAD_NAME = 'http-{0}.json'
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


def http_rate(input_filename):
    input_file = open(input_filename, 'r')
    output_file = open(os.path.abspath(os.path.dirname(input_file.name)) +
                       '/rated_' + os.path.basename(input_file.name), 'w')
    country = list()

    for line in input_file:
        json_line = json.loads(line)
        subclasses = HTTPRule.all_subclasses()
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


def certificate(data):
    subclasses = CertificateRule.all_subclasses()
    score = Score()

    for sub in subclasses:
        sub().apply_rule(data, score)
    return score.calc_avg()


def export_data(export_country_code):
    export = CensysExport()
    job = export.new_job(HTTP_QUERY.format(export_country_code))
    return export.check_job_loop(job['job_id'])


if __name__ == '__main__':
    args = argument_parser()

    if args.input:
        if args.http:
            print http_rate(args.input)

            # if args.certificate:
            #         append_if_not_none(country, certificate(json_line))
    else:
        make_dir(FOLDER_NAME)

        for country_code in ['CO', 'PY']:
            response = export_data()
            if download_file(response, HTTP_DOWNLOAD_NAME.format(country_code.lower())) is False:
                continue

            if args.http:
                print country_code + ': ' + str(
                    http_rate(FOLDER_NAME + '/' + HTTP_DOWNLOAD_NAME.format(country_code.lower())))
