#
# run selenium side runner
#
DIR=`dirname $0`
. $DIR/base.sh

CAPS_FILES="$DIR/browserstack/caps/*cap"

for t in $CAPS_FILES; do
    echo $t
    sel="$SELENIUM_CMD -w 5 \"$SIDES_DIR/*.side\" --parallel-runs --base-url $TEST_URL --config-file $t"
    echo $sel
    #eval $sel
done
