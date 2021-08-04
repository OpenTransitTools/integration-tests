about:
------
This suite of tests uses the Selenium side runner (https://www.selenium.dev/selenium-ide/docs/en/introduction/command-line-runner)
cmd-line system to execute automated integration tests for the "trimet.org" project.  These tests can either run against
locally installed browsers and/or browsers hosted on browserstack.com

The browsers we'll be targeting as of August 2021 are:
![most important browsers to test](docs/images/important_browsers_2021.png?raw=true)

pre-req:
--------
1. have Git, bash (wsl or cygwin on Windows), Node, Yarn and Python (2.7 or 3.x) installed on your machine
1. git clone https://github.com/OpenTransitTools/integration-tests.git
1. cd integration-tests/
1. yarn install
1. test browsers:
   * local install of Chrome, Firefox, Safari and/or Edge installed on the local machine
   * -- OR --
   * *BrowserStack* account that has the capability to run https://automate.browserstack.com/ 

run tests locally:
-----------------
1. scripts/selenium_local_browsers.sh
1. you can control which browsers to test by setting the environment variable `export BROWSERS="firefox chrome safari MicrosoftEdge"`
1. NOTE: Edge testing doesn't run (as of August 2021) on Mac.  The selenium test runner keeps complaining that it can't find the MicrosoftWebDriver.exe.  I've tried to manually install that driver on Mac, and still no luck.  

run tests using BrowserStack: 
----------------------------
1. log into https://automate.browserstack.com/
1. copy uname and key from BrowserStack into a long string with a colon separating the two elements, ala \<your uname\>:\<your key\> <br>![BrowserStack Uname & Key img](docs/images/BrowserStack_uname_key.png?raw=true)
1. cd scripts/browserstack
1. python gen.py <your uname>:<your key>
1. ls caps/*.cap  # the python app should have generated some number of browser targets for your tests
1. NOTE: there are cmd-line params to limit (or increase) the list of devices, add .cap targets for testing portrait orientation, etc... ala the `-s == 'smoke'` cmd-line param  
1. cd ../../
1. scripts/selenium_browserstack.sh
1. go back to https://automate.browserstack.com/dashboard and you should see the tests running
![browser stack running tests](docs/images/bs_running.png?raw=true)
1. eventually selenium_browserstack.sh will finish and you'll see the test results there, and on https://automate.browserstack.com/dashboard there should be videos showing what the device looked like at it ran the test. 
![sbrowser stack playback app](docs/images/bs_playback.png?raw=true)

NOTES:
1. https://www.browserstack.com/list-of-browsers-and-platforms/js_testing
1. https://www.browserstack.com/automate/capabilities?tag=selenium-4
1. <https://www.browserstack.com/guide/selenium-grid-tutorial#:~:text=What%20is%20Selenium%20Grid%3F,to%20multiple%20registered%20Grid%20nodes.>

creating new tests:
------------------
1. less ./sides/*.side
1. these are the selenium tests
1. to start, I created initial .side files using Selenium IDE on Firefox, capturing some events using the app
1. I saved the test from Selenium IDE as a .side file, and then hand edited the resulting .json
1. my goal in editing is to remove hard-coded element IDs (which are often sequential, and change based on even the most
   minor changes to the app), since these ids make the tests very fragile to app changes
