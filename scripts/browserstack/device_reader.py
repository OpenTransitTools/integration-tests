from csv import DictReader
import re


def parse_csv(csv_file):
    ret_val = []

    def is_valid(rec):
        ret_val = False
        if rec and rec['device']:
            ret_val = True
        return ret_val

    with open(csv_file, 'r') as f:
        recs = DictReader(f)
        for r in recs:
            if is_valid(r):
                ret_val.append(r)

    return ret_val