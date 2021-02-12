import os
import sys

# https://www.browserstack.com/automate/capabilities
# https://www.browserstack.com/list-of-browsers-and-platforms/js_testing
# https://www.browserstack.com/docs/automate/selenium/selenium-ide

browsers = [
  {'name': 'iPhone_8+ChromePort', 'device': 'iPhone 8 Plus', 'browser': 'Chrome', 'browserVersion': 'latest', 'os': 'iOS', 'osVersion': '12', 'orientation': 'portrait'},
  {'name': 'iPhone_8+ChromeLand', 'device': 'iPhone 8 Plus', 'browser': 'Chrome', 'browserVersion': 'latest', 'os': 'iOS', 'osVersion': '12', 'orientation': 'landscape'},

  {'name': 'iPhone_12+Safari', 'device': 'iPhone 12 Pro', 'browser': 'Safari', 'browserVersion': 'latest', 'os': 'iOS', 'osVersion': '14', 'orientation': 'portrait'},
  {'name': 'iPhone_12+Chrome', 'device': 'iPhone 12', 'browser': 'Chrome', 'browserVersion': 'latest', 'os': 'iOS', 'osVersion': '14', 'orientation': 'portrait'},  

  {'name': 'androidGalaxy8Chrome', 'device': 'Samsung Galaxy S8', 'browser': 'Chrome', 'browserVersion': 'latest', 'os': 'android', 'osVersion': '7', 'orientation': 'portrait'},
  {'name': 'androidPixel4Chrome', 'device': 'Google Pixel 4', 'browser': 'Chrome', 'browserVersion': 'latest', 'os': 'android', 'osVersion': '10', 'orientation': 'portrait'},
  {'name': 'androidMotoChrome', 'device': 'Motorola Moto G7 Play', 'browser': 'Chrome', 'browserVersion': 'latest', 'os': 'android', 'osVersion': '9', 'orientation': 'portrait'},
  
  {'name': 'iPad+SafariPort', 'device': 'iPad Pro 11 2018', 'browser': 'Safari', 'browserVersion': 'latest', 'os': 'iOS', 'osVersion': '12', 'orientation': 'portrait'},
  {'name': 'iPad+SafariLand', 'device': 'iPad Mini 2019', 'browser': 'Safari', 'browserVersion': 'latest', 'os': 'iOS', 'osVersion': '12', 'orientation': 'landscape'},  

  {'name': 'androidGalaxyPadChromePort', 'device': 'Samsung Galaxy Tab S6', 'browser': 'Chrome', 'browserVersion': 'latest', 'os': 'android', 'osVersion': '9', 'orientation': 'portrait'},
  {'name': 'androidGalaxyPadChromeLand', 'device': 'Samsung Galaxy Tab S4', 'browser': 'Chrome', 'browserVersion': 'latest', 'os': 'android', 'osVersion': '8.1', 'orientation': 'landscape'},

]

bs_key = "your browserstack '<uname>:<key>' here" if len(sys.argv) < 2 else sys.argv[1]

template = """ capabilities:
     device: "{device}"
     orientation: "{orientation}"
     os: "{os}"
     os_version: '{osVersion}'
     browserName: "{browser}"
     browser_version: '{browserVersion}'
     real_mobile: true
     name: 'Selenium IDE tests'
     build: "blah"
     browserstack.debug: true
     browserstack.console: "verbose"
     browserstack.networkLogs: true
 server: "https://{key}@hub-cloud.browserstack.com/wd/hub"
"""

root = os.path.dirname(os.path.abspath(__file__))

for n in browsers:
  filename = os.path.join(root, n['name'] + ".cap")
  with open(filename, 'w') as f:
    f.write(template.format(key=bs_key, **n))

#
# deleting tests:
#   curl -u "<uname:pass>" https://api.browserstack.com/automate/builds.json (then take 'hashed_id' from that output for below)
#   curl -u "<uname:pass>" -X DELETE https://api.browserstack.com/automate/builds/<hashed_id>.json
#
if len(sys.argv) < 2:
  print('ERROR: provide a valid uname:password as a cmdline param here, else your tests will not run on browserstack')
else:
  print('NOTE: to bulk delete old tests from BS, use the following 2 commands:')
  print('curl -u "{}" https://api.browserstack.com/automate/builds.json'.format(sys.argv[1]))
  print('curl -u "{}" -X DELETE https://api.browserstack.com/automate/builds/<hashed_id>.json'.format(sys.argv[1]))
