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
import sys
from datetime import datetime

import devices.iphone_new
import devices.iphone_old
import devices.android_new
import devices.android_old


# vars
browsers = []
bs_key = None
landscape = desktops = tablets = older = smoke = False
phones = True
cmd_line_opts = "-l [add landscape tests], -m [phones (on by default)], -d [desktops], -t [tablets], -o [older devices], -s [generate 1 device per OS (smoke tests)]"
build = "gen ran {:%Y.%m.%d_%H.%M}".format(datetime.now())
caps_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'caps')


def usage():
    """
    cmd line usage (note - hoping to make this .py portable and zero dependencies)
    """
    if bs_key is None:
        print("\n ERROR:\tyou need to provide the uname:password 'ACCESS KEY' from BrowserStack's automate (see README.md)")
    print('\n usage:\tpython gen.py uname:password [optional parameters]')
    print('\tprovide a valid uname:password as a cmdline param here, else your tests will not run on browserstack')
    print('\tnote: optional dashed cmd-line params may be added after the first uname:password param')
    print('\t  {}\n'.format(cmd_line_opts))


def write_cap_file(rec):
    """
    .format() template to generate a .cap file for browserstack automate
    NOTE: selenium is very sensitive to this format ... an extra space will make the test runner fail
          so if things don't run or are behaving correctly, the template below could easily be the problem
    """
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


def append_device_array(recs, is_smoke=False):
    """
    add element(s) to our device array
    """
    if len(recs) > 0:
        if is_smoke:
            browsers.append(recs[0])
        else:
            browsers.extend(recs)


# process the cmd-line
if len(sys.argv) > 1:
    bs_key = sys.argv[1]
    if ":" not in bs_key:
        bs_key = None
    else:
        landscape = True if "-l" in sys.argv else False
        older = True if "-o" in sys.argv else False
        smoke = True if "-s" in sys.argv else False
        desktops = True if "-d" in sys.argv else False
        tablets = True if "-t" in sys.argv else False
        if desktops or tablets:
            phones = True if "-p" in sys.argv else False

# populate the browsers array
if phones:
    append_device_array(devices.android_new.phones, smoke)
    append_device_array(devices.iphone_new.phones, smoke)
    if older:
        append_device_array(devices.android_old.phones, smoke)
        append_device_array(devices.iphone_old.phones, smoke)

if tablets:
    append_device_array(devices.android_new.tablets, smoke)
    append_device_array(devices.iphone_new.tablets, smoke)
    if older:
        append_device_array(devices.android_old.tablets, smoke)
        append_device_array(devices.iphone_old.tablets, smoke)

if desktops:
    if older:
        pass

# process
if bs_key is None or len(browsers) < 1:
    usage()
else:
    # gen caps/*.cap capability files
    for rec in browsers:
        write_cap_file(rec)
        if landscape:
            write_cap_file(make_landscape(rec))

    # inform how one can remove these tests, etc...
    print('SUCCESS...')
    print("list all the device targets via `ls {}`".format(caps_dir))
    print('\nNOTE: to bulk delete old tests from BS, use this 2-step process (get BS build ids, then DELETE them):')
    print(' curl -u "{}" https://api.browserstack.com/automate/builds.json'.format(sys.argv[1]))
    print(' curl -u "{}" -X DELETE https://api.browserstack.com/automate/builds/<hashed_id>.json'.format(sys.argv[1]))
    print()