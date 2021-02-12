import os
import sys

# https://www.browserstack.com/automate/capabilities
# https://www.browserstack.com/list-of-browsers-and-platforms/js_testing
# https://www.browserstack.com/docs/automate/selenium/selenium-ide
# 

browsers = [
  {'name': 'iPhone_8+Chrome', 'device': 'iPhone 8 Plus', 'browser': 'Chrome', 'browserVersion': 'latest', 'os': 'iOS', 'osVersion': '12', 'orientation': 'portrait'},
  {'name': 'iPhone_8+Safari', 'device': 'iPhone 8 Plus', 'browser': 'Safari', 'browserVersion': 'latest', 'os': 'iOS', 'osVersion': '12', 'orientation': 'landscape'},
]

bs_key = "your browserstack '<uname>:<key>' here" if len(sys.argv) < 2 else sys.argv[1]

template = """ capabilities:
     device: "{device}"
     orientation: "{orientation}"
     os: "{os}"
     os_version: '{osVersion}'
     browserName: "{browser}"
     browser_version: '{browserVersion}'
     name: 'Selenium IDE automate test'
     real_mobile: true
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
