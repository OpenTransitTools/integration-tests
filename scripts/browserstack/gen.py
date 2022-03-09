"""
simple utility that generate a bunch of .cap files for use in automate.browserstack.com

:see:
  https://www.browserstack.com/automate/capabilities
  https://www.browserstack.com/list-of-browsers-and-platforms/js_testing
  https://www.browserstack.com/docs/automate/selenium/selenium-ide

:note - to deleting tests from BS via the command line:
  curl -u "<uname:pass>" https://api.browserstack.com/automate/builds.json (then take 'hashed_id' from that output for below)
  curl -u "<uname:pass>" -X DELETE https://api.browserstack.com/automate/builds/<hashed_id>.json
"""
import os
from datetime import datetime

import cmd_line
import device_reader


def write_cap_file(rec):
    """
    .format() template to generate a .cap file for browserstack automate
    NOTE: selenium is very sensitive to this format ... an extra space will make the test runner fail
          so if things don't run or are behaving correctly, the template below could easily be the problem
    """
    build = "gen ran {:%Y.%m.%d_%H.%M}".format(datetime.now())
    template = """ capabilities:
     device: "{device}"
     orientation: "{orientation}"
     os: "{os}"
     os_version: '{osVersion}'
     browserName: "{browser}"
     browser_version: '{browserVersion}'
     real_mobile: true
     name: '{name}'
     build: '{build}'
     browserstack.debug: true
     browserstack.console: "verbose"
     browserstack.networkLogs: true
 server: "https://{key}@hub-cloud.browserstack.com/wd/hub"
 """
    filename = os.path.join(caps_dir, rec['name'] + ".cap")
    with open(filename, 'w') as f:
        f.write(template.format(key=bs_key, build=build, **rec))


def make_landscape(rec, orientation='landscape'):
    """
    set landscape in record (and name / file name)
    NOTE: this breaks the records loaded in ... might need to deep copy
    """
    ret_val = rec
    ret_val['orientation'] = orientation
    ret_val['name'] = "{}{}".format(rec['name'], orientation.capitalize())
    return ret_val


def x():
    for rec in browsers:
        write_cap_file(rec)
        if landscape:
            write_cap_file(make_landscape(rec))


def append_device_array(recs, is_smoke=False):
    """
    add element(s) to our device array
    """
    if len(recs) > 0:
        if is_smoke:
            browsers.append(recs[0])
        else:
            browsers.extend(recs)


def main():
    args = cmd_line.make_parser()
    recs = device_reader.parse_csv(args.devices_csv)
    print(recs)


if __name__ == "__main__":
    main()

