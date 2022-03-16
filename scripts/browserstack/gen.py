"""
simple utility that generate a bunch of .cap files for use in automate.browserstack.com

:see:
  https://www.browserstack.com/automate/capabilities
  https://www.browserstack.com/docs/automate/selenium/selenium-ide
  https://www.browserstack.com/list-of-browsers-and-platforms/js_testing

:note - to deleting tests from BS via the command line:
  curl -u "<uname:pass>" https://api.browserstack.com/automate/builds.json (then take 'hashed_id' from that output for below)
  curl -u "<uname:pass>" -X DELETE https://api.browserstack.com/automate/builds/<hashed_id>.json
"""
import os
import glob
from datetime import datetime

import cmd_line
import device_reader


def is_desktop(rec):
    return rec['device'] in ["win", "mac"]


def write_cap_file(rec, key, name, path, orientation="vertical"):
    """
    .format() template to generate a .cap file for browserstack automate
    NOTE: selenium is very sensitive to this format ... an extra space will make the test runner fail
          so if things don't run or are behaving correctly, the template below could easily be the problem
    """
    build = "gen ran {:%Y.%m.%d_%H.%M}".format(datetime.now())
    temp_body = """
    os: '{os}'
    os_version: '{osVersion}'
    browserName: '{browser}'
    browser_version: '{browserVersion}'
    resolution: '{resolution}'
    real_mobile: true
    name: '{dname}'
    build: '{build}'
    browserstack.debug: true
    browserstack.console: 'verbose'
    browserstack.networkLogs: true
server: "https://{browserstack_key}@hub-cloud.browserstack.com/wd/hub"
"""
    if is_desktop(rec):
        template = """capabilities: """ + temp_body
        resolution = '1280x1024'
    else:
        template = """capabilities: 
    orientation: "{orientation}"
    device: "{device}" """ + temp_body
        resolution = '1134 x 750'

    filename = os.path.join(path, name + ".cap")
    with open(filename, 'w') as f:
        f.write(template.format(build=build, browserstack_key=key, dname=name, resolution=resolution, orientation=orientation, **rec))


def rm_cap_files(dir):
    files = glob.glob(dir + '/*.cap')
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))


def print_urls(rec, url="https%3A%2F%2Ftrimet.org%2Fhome"):
    #https://live.browserstack.com/dashboard#os=android&os_version=9.0&device=Samsung+Galaxy+A10&device_browser=chrome&zoom_to_fit=true&full_screen=true&url=https%3A%2F%2Ftrimet.org%2Fhome%2Fsearch&speed=1
    template = "https://live.browserstack.com/dashboard#device={device}&os={os}&os_version={osVersion}&browser={browser}&browser_version={browserVersion}&device_browser={browser}&url={url}&zoom_to_fit=true&full_screen=true&resolution=responsive-mode&speed=1"
    print(template.format(url=url, **rec))


def process(recs, args):
    """
    add element(s) to our device array
    """
    path = args.caps_dir
    if args.rm_caps and path:
        rm_cap_files(path)

    for i, r in enumerate(recs):
        if args.number < i: break
        if args.urls: 
            print_urls(r)
        else:
            name = r['name']
            key = args.browserstack_key
            write_cap_file(r, key, name, path)
            if not is_desktop(r) and args.landscape:
                name = "{}Land".format(name)
                write_cap_file(r, key, name, path, "landscape")


def main():
    args = cmd_line.make_parser()
    recs = device_reader.parse_csv_args(args)
    process(recs, args)


if __name__ == "__main__":
    main()
