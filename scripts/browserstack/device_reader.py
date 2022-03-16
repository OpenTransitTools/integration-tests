from csv import DictReader
import re


def parse_csv(csv_file, is_baseline, os_filter, browser_filter):
    ret_val = []

    has_os_filter = os_filter and len(os_filter) > 0
    has_browser_filter = browser_filter and len(browser_filter) > 0

    def filter(rec):
        ret_val = True

        os = rec['os']
        browser = rec['browser']
        baseline = rec['baseline']

        def find_in(search_list, ele):
            ret_val = False
            for s in search_list:
                if s in ele:
                    ret_val = True
                    break
            return ret_val

        if os and browser and baseline:
            if has_os_filter or has_browser_filter:
                # import pdb; pdb.set_trace()
                if has_os_filter and has_browser_filter:
                    if find_in(os_filter, os) and find_in(browser_filter, browser):
                        ret_val = False
                elif has_os_filter and find_in(os_filter, os):
                    ret_val = False
                elif has_browser_filter and find_in(browser_filter, browser):
                    ret_val = False
            else:
                ret_val = False  # no filters ... so don't filter

            if is_baseline and baseline.lower() != 'true':
                ret_val = True

        return ret_val

    def is_valid(rec):
        ret_val = False
        if rec and rec['device']:
            if filter(rec):
                ret_val = False
            else:
                ret_val = True
        return ret_val

    with open(csv_file, 'r') as f:
        recs = DictReader(f)
        for r in recs:
            if is_valid(r):
                ret_val.append(r)

    return ret_val


def parse_csv_args(args):
    return parse_csv(args.devices_csv, args.baseline, args.os_filter, args.browser_filter)
