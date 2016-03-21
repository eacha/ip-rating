import argparse
import json
from HTTP import *
from HTTP.HTTPRule import HTTPRule
from Rules import Score


def argument_parser():
    parser = argparse.ArgumentParser(description='Recollect IP data')
    parser.add_argument('-i', '--input', help='Input file name', required=True)
    parser.add_argument('--http', help='Rate the ips with the port 80 open', action='store_true', required=False)
    return parser.parse_args()


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
        sub().apply_rule(json_line, score)
    return score.calc_avg()


if __name__ == '__main__':
    args = argument_parser()
    input_file = open(args.input, 'r')
    # output_file = open('http_scored.json', 'w')

    country = list()
    for line in input_file:
        json_line = json.loads(line)

        if args.http:
            country.append(http(json_line))

    print avg(country)
