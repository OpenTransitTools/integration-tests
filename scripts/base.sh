DIR=`dirname $0`
SEP=${SEP:=":"}
EXE=${EXE:=""}

# set path to node_mod's install of drivers and selenium
P=".$SEP$DIR$SEP$PWD/node_modules/.bin$SEP$DIR/../node_modules/.bin"
for d in chromedriver geckodriver edgedriver msedgedriver; do
    DR="$PWD/node_modules/$d/bin"
    if [ ! -f $DR/$d$EXE ]; then
        echo "$P/$d$EXE doesn't exist"
        cp $DR/$d $DR/$d$EXE
    fi
    P="$P$SEP$DR$SEP$DIR/../node_modules/$d/bin"
done
export PATH="./scripts$SEP$P$SEP$PATH"
echo "export PATH=\"$PATH\""

# set selenium-side-runner default params
TEST_URL=${TEST_URL:="https://labs.trimet.org"}   # note: export TEST_URL="http://localhost:8000" for testing locally
SIDES_DIR=${SIDES_DIR:="./sides"}
SELENIUM_CMD=${SELENIUM_CMD:="selenium-side-runner"}
BROWSERS=${BROWSERS:="firefox chrome safari MicrosoftEdge"}

# process cmd line
