#
# run selenium side runner with Browserstack
# https://www.selenium.dev/selenium-ide/docs/en/introduction/command-line-runner
# https://www.browserstack.com/guide/selenium-side-runner
# https://www.seleniumhq.org/selenium-ide/docs/en/introduction/command-line-runner/#additional-params
#
DIR=`dirname $0`
. $DIR/base.sh

CAPS_FILES="$DIR/browserstack/caps/*cap"
PARALLEL_PROCESSES=5

for t in $CAPS_FILES; do
    echo $t
    # --filter smoke or --filter <regex>
    sel="$SELENIUM_CMD --timeout 30000 -w $PARALLEL_PROCESSES --base-url $TEST_URL --config-file $t $SIDES_DIR/*.side"
    echo $sel
    eval $sel
done
