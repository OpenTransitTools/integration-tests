import os
import sys

# https://www.browserstack.com/automate/capabilities
# https://www.browserstack.com/list-of-browsers-and-platforms/js_testing
# https://www.browserstack.com/docs/automate/selenium/selenium-ide

browsers = [
  {'name': 'iPhone_8+ChromePort', 'device': 'iPhone 8 Plus', 'browser': 'Chrome', 'browserVersion': 'latest', 'os': 'iOS', 'osVersion': '12', 'orientation': 'portrait'},
  {'name': 'iPhone_8+ChromeLand', 'device': 'iPhone 8 Plus', 'browser': 'Chrome', 'browserVersion': 'latest', 'os': 'iOS', 'osVersion': '12', 'orientation': 'landscape'},

  {'name': 'iPhoneXChromePort', 'device': 'iPhone X', 'browser': 'Chrome', 'browserVersion': 'latest', 'os': 'iOS', 'osVersion': '11', 'orientation': 'portrait'},
  {'name': 'iPhoneXSafariLand', 'device': 'iPhone X', 'browser': 'Safari', 'browserVersion': 'latest', 'os': 'iOS', 'osVersion': '11', 'orientation': 'landscape'},

  {'name': 'iPhone_11Chrome', 'device': 'iPhone 11 Pro Max', 'browser': 'Chrome', 'browserVersion': 'latest', 'os': 'iOS', 'osVersion': '13', 'orientation': 'portrait'},
  {'name': 'iPhone_11Chrome', 'device': 'iPhone 11 Pro', 'browser': 'Safari', 'browserVersion': 'latest', 'os': 'iOS', 'osVersion': '13', 'orientation': 'portrait'},
  
  {'name': 'iPhone_12+Safari', 'device': 'iPhone 12 Pro', 'browser': 'Safari', 'browserVersion': 'latest', 'os': 'iOS', 'osVersion': '14', 'orientation': 'portrait'},
  {'name': 'iPhone_12+Chrome', 'device': 'iPhone 12', 'browser': 'Chrome', 'browserVersion': 'latest', 'os': 'iOS', 'osVersion': '14', 'orientation': 'portrait'},  

  {'name': 'androidGalaxy8Chrome', 'device': 'Samsung Galaxy S8 Plus', 'browser': 'Chrome', 'browserVersion': 'latest', 'os': 'android', 'osVersion': '9.0', 'orientation': 'portrait'},
  {'name': 'androidPixel4Chrome', 'device': 'Google Pixel 4', 'browser': 'Chrome', 'browserVersion': 'latest', 'os': 'android', 'osVersion': '11.0', 'orientation': 'portrait'},
  {'name': 'androidPixel4XLChrome', 'device': 'Google Pixel 4 XL', 'browser': 'Chrome', 'browserVersion': 'latest', 'os': 'android', 'osVersion': '10.0', 'orientation': 'landscape'},  
  {'name': 'androidPixel5FF', 'device': 'Google Pixel 5', 'browser': 'Firefox', 'browserVersion': 'latest', 'os': 'android', 'osVersion': '11.0', 'orientation': 'portrait'},  
  {'name': 'androidMotoChrome', 'device': 'Motorola Moto G7 Play', 'browser': 'Chrome', 'browserVersion': 'latest', 'os': 'android', 'osVersion': '9.0', 'orientation': 'portrait'},
    
  {'name': 'iPad+SafariPort', 'device': 'iPad Pro 11 2018', 'browser': 'Safari', 'browserVersion': 'latest', 'os': 'iOS', 'osVersion': '12', 'orientation': 'portrait'},
  {'name': 'iPad+SafariLand', 'device': 'iPad Mini 2019', 'browser': 'Safari', 'browserVersion': 'latest', 'os': 'iOS', 'osVersion': '12', 'orientation': 'landscape'},  

  {'name': 'androidGalaxyTabChromePort', 'device': 'Samsung Galaxy Tab S6', 'browser': 'Chrome', 'browserVersion': 'latest', 'os': 'android', 'osVersion': '9.0', 'orientation': 'portrait'},
  {'name': 'androidGalaxyTabFFLand', 'device': 'Samsung Galaxy Tab S6', 'browser': 'Firefox', 'browserVersion': 'latest', 'os': 'android', 'osVersion': '9.0', 'orientation': 'landscape'},
  {'name': 'androidGalaxyTabUcPort', 'device': 'Samsung Galaxy Tab S6', 'browser': 'UC Browser', 'browserVersion': 'latest', 'os': 'android', 'osVersion': '9.0', 'orientation': 'portrait'},
  {'name': 'androidGalaxyTabSamLand', 'device': 'Samsung Galaxy Tab S6', 'browser': 'Samsung Internet', 'browserVersion': 'latest', 'os': 'android', 'osVersion': '9.0', 'orientation': 'landscape'},
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
     name: '{browser} + {orientation}'
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
