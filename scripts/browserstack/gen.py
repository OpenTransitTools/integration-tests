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
from datetime import datetime

import cmd_line
import device_reader


def write_cap_file(rec, filename, bs_key):
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
    with open(filename, 'w') as f:
        f.write(template.format(key=bs_key, build=build, **rec))


def print_urls(rec, url="https%3A%2F%2Ftrimet.org%2Fhome"):
    #https://live.browserstack.com/dashboard#os=android&os_version=9.0&device=Samsung+Galaxy+A10&device_browser=chrome&zoom_to_fit=true&full_screen=true&url=https%3A%2F%2Ftrimet.org%2Fhome%2Fsearch&speed=1
    template = "https://live.browserstack.com/dashboard#device={device}&os={os}&os_version={osVersion}&browser={browser}&browser_version={browserVersion}&device_browser={browser}&url={url}&zoom_to_fit=true&full_screen=true&resolution=responsive-mode&speed=1"
    print(template.format(url=url, **rec))


def make_landscape(rec, orientation='landscape'):
    """
    set landscape in record (and name / file name)
    NOTE: this breaks the records loaded in ... might need to deep copy
    """
    ret_val = rec
    ret_val['orientation'] = orientation
    ret_val['name'] = "{}{}".format(rec['name'], orientation.capitalize())
    return ret_val


def process(recs, args):
    """
    add element(s) to our device array
    """
    for i, r in enumerate(recs):
        if args.number < i: break
        if args.urls: print_urls(r)


def main():
    args = cmd_line.make_parser()
    recs = device_reader.parse_csv(args.devices_csv)
    process(recs, args)


if __name__ == "__main__":
    main()

