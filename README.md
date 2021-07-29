about:
------
This suite of tests uses the Selenium side runner (https://www.selenium.dev/selenium-ide/docs/en/introduction/command-line-runner)
cmd-line system to execute automated integration tests for the "trimet.org" project.  These tests can either run against
locally installed browsers and/or browsers hosted on browserstack.com

pre-req:
--------
1. have Git, bash (cygwin on Windows), Node, Yarn and Python (2.7 or 3.x) installed on your machine
1. git clone https://github.com/OpenTransitTools/integration-tests.git
1. cd integration-tests/
1. yarn install
1. test browsers:
   * local install of Chrome, Firefox, Safari and/or Edge installed on the local machine
   * -- OR --
   * *BrowserStack* account that has the capability to run https://automate.browserstack.com/ 

drivers:
  EDGE: https://msedgewebdriverstorage.z22.web.core.windows.net/?prefix=90.0.789.1/

run tests locally:
-----------------
1. scripts/smoke.sh CHROME
1. (see scripts/base.sh and export BROWSERS to fit what browsers you'd like to target)
1. scripts/selenium_local_browsers.sh

run tests using BrowserStack: 
----------------------------
1. log into https://automate.browserstack.com/
1. copy uname and key from BrowserStack into a long string with a colon separating the two elements, ala \<your uname\>:\<your key\> <br>![BrowserStack Uname & Key img](docs/images/BrowserStack_uname_key.png?raw=true)
1. cd scripts/browserstack
1. python gen.py <your uname>:<your key> -t smoke
1. ls *.cap  # the python app should have generated some number of browser targets for your tests 
1. cd ../../
1. scripts/ 

NOTES:
1. https://www.browserstack.com/list-of-browsers-and-platforms/js_testing
1. https://www.browserstack.com/automate/capabilities?tag=selenium-4
1. <https://www.browserstack.com/guide/selenium-grid-tutorial#:~:text=What%20is%20Selenium%20Grid%3F,to%20multiple%20registered%20Grid%20nodes.>

creating new tests:
-------------------
1. less ./sides/*.side
1. these are the selenium tests
1. to start, I created initial .side files using Selenium IDE on Firefox, capturing some events using the app
1. I saved the test from Selenium IDE as a .side file, and then hand edited the resulting .json
1. my goal in editing is to remove hard-coded element IDs (which are often sequential, and change based on even the most
   minor changes to the app), since these ids make the tests very fragile to app changes
1. xx