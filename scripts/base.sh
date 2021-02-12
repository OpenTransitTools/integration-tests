DIR=`dirname $0`

# set path to node_mod's install of drivers and selenium
P=".:$DIR:$PWD/node_modules/.bin:$DIR/../node_modules/.bin"
for d in "chromedriver geckodriver edgedriver msedgedriver"; do
    P="$P:$PWD/node_modules/$d/bin"
    P="$P:$DIR/../node_modules/$d/bin"
done
export PATH="$PATH:$P"

# set selenium-side-runner default params
TEST_URL=${TEST_URL:="https://labs.trimet.org"}   # note: export TEST_URL="http://localhost:8000" for testing locally
BROWSERS=${BROWSERS:="firefox chrome safari MicrosoftEdge" }
SIDES_DIR=${SIDES_DIR:="./sides"}
SELENIUM_CMD=${SELENIUM_CMD:="selenium-side-runner"}
