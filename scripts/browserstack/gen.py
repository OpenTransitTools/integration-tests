"""
simple utility that generate a bunch of .cap files for use in automate.browserstack.com

:see:
  # important tool - build caps file 
  https://www.browserstack.com/automate/capabilities

  # generic list of browsers that run
  https://www.browserstack.com/list-of-browsers-and-platforms/js_testing

  # instructions
  https://www.browserstack.com/docs/automate/selenium/selenium-ide

  # for when you mistakenly check in your key :-(
  https://www.browserstack.com/docs/automate/selenium/reset-access-key#using-command-prompt 

:note - to deleting tests from BS via the command line:
  curl -u "<uname:pass>" https://api.browserstack.com/automate/builds.json (then take 'hashed_id' from that output for below)
  curl -u "<uname:pass>" -X DELETE https://api.browserstack.com/automate/builds/<hashed_id>.json
"""
import os
import glob
from datetime import datetime

import cmd_line
import device_reader


build_time = "gen ran {:%Y.%m.%d_%H.%M}".format(datetime.now())


def is_desktop(rec):
    return rec['device'] in ["win", "mac"]


def gen_caps(rec, key, name, orientation):
    """
    .format() template to generate a .cap file for browserstack automate
    NOTE: selenium is very sensitive to this format ... an extra space will make the test runner fail
          so if things don't run or are behaving correctly, the template below could easily be the problem
    """
    temp_body = """
    os: '{os}'
    os_version: '{osVersion}'
    browserName: '{browser}'
    browser_version: '{browserVersion}'
    resolution: '{resolution}'
    real_mobile: true
    name: '{dname}'
    build: '{build_time}'
    browserstack.debug: true
    browserstack.console: 'verbose'
    browserstack.networkLogs: true
server: "https://{browserstack_key}@hub-cloud.browserstack.com/wd/hub"
"""
    if is_desktop(rec):
        resolution = '1280x1024'
        template = """capabilities: """ + temp_body
    else:
        resolution = '1134 x 750'
        template = """capabilities: 
    orientation: "{orientation}"
    device: "{device}" """ + temp_body
    # realMobile: 'true'

    ret_val = template.format(build_time=build_time, browserstack_key=key, dname=name, resolution=resolution, orientation=orientation, **rec)
    return ret_val


def write_cap_file(rec, key, name, path, orientation="vertical", do_info_file=True):
    caps = gen_caps(rec, key, name, orientation)
    filename = os.path.join(path, name + ".cap")
    with open(filename, 'w') as f:
        f.write(caps)
    if do_info_file:
        filename = os.path.join(path, name + ".txt")
        with open(filename, 'w') as f:
            f.write("  ")
            f.write(get_info(rec, orientation))
            f.write("\n\n  ")
            f.write(get_url(rec))
            f.write("\n")



def rm_files(dir):
    files = glob.glob(dir + '/*.???')
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))


def get_url(rec, url="https%3A%2F%2Ftrimet.org%2Fhome"):
    # https://live.browserstack.com/dashboard#os=android&os_version=10.0&device=Motorola+Moto+G9+Play&device_browser=firefox&zoom_to_fit=true&full_screen=true&url=https%3A%2F%2Flabs.trimet.org%2Fhome%2F&speed=1
    template = "https://live.browserstack.com/dashboard#os={os}&os_version={osVersion}&device={device}&device_browser={browser}&browser_version={browserVersion}&zoom_to_fit=true&full_screen=true&url={url}&speed=1"
    return template.format(url=url, **rec)


def get_info(rec, landscape=""):
    template = "{device} ({os} {osVersion}) using {browser} ({browserVersion} {landscape})"
    return template.format(landscape=landscape, **rec)


def print_url(rec):
    print(get_url(rec))


def process(recs, args):
    """
    add element(s) to our device array
    """
    path = args.caps_dir
    if args.rm_caps and path:
        rm_files(path)

    for i, r in enumerate(recs):
        if args.number < i: break
        if args.urls: 
            print_url(r)
        else:
            name = r['name']
            key = args.browserstack_key
            write_cap_file(r, key, name, path, do_info_file=not args.no_info_file)
            if not is_desktop(r) and args.landscape:
                name = "{}Land".format(name)
                write_cap_file(r, key, name, path, "landscape")


def main():
    args = cmd_line.make_parser()
    recs = device_reader.parse_csv_args(args)
    process(recs, args)


if __name__ == "__main__":
    main()
