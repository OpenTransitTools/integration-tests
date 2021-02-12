import os
import sys

browsers = [
  {'name': 'iPhone_7', 'browser': 'x', 'browserVersion': '', 'os': '', 'osVersion': '', 'res': '1024x768'},
  {'name': 'iPhone_12', 'browser': 'x', 'browserVersion': '', 'os': '', 'osVersion': '', 'res': '1024x768'}
]

bs_key = "your browserstack '<uname>:<key>' here" if len(sys.argv) < 2 else sys.argv[1]

template = """ capabilities:
     browserName: "{browser}"
     browser_version: '{browserVersion}'
     os: "{os}"
     os_version: '{osVersion}'
     resolution: '{res}'
     name: 'Selenium IDE automate test'
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
