import argparse
import json

from HTTP import *
from Certificate import *
from HTTP.HTTPRule import HTTPRule
from Certificate.CertificateRule import CertificateRule
from Rules import Score


def argument_parser():
    parser = argparse.ArgumentParser(description='Recollect IP data')
    parser.add_argument('-i', '--input', help='Input file name', required=True)
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


def http(data):
    subclasses = HTTPRule.all_subclasses()
    score = Score()

    for sub in subclasses:
        sub().apply_rule(data, score)
    return score.calc_avg()


def certificate(data):
    subclasses = CertificateRule.all_subclasses()
    score = Score()

    for sub in subclasses:
        sub().apply_rule(data, score)
    return score.calc_avg()


if __name__ == '__main__':
    args = argument_parser()
    input_file = open(args.input, 'r')
    # output_file = open('http_scored.json', 'w')

    country = list()
    for line in input_file:
        json_line = json.loads(line)

        if args.http:
            append_if_not_none(country, http(json_line))

        if args.certificate:
            print json_line['ip'] + ' ' + str(certificate(json_line))
            append_if_not_none(country, certificate(json_line))

    print avg(country)
