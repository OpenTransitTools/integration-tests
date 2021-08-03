#
# run selenium side runner
#
DIR=`dirname $0`
. $DIR/base.sh

CAPS_FILES="$DIR/browserstack/caps/*cap"

for t in $CAPS_FILES; do
    echo $t
    sel="$SELENIUM_CMD --base-url $TEST_URL --config-file $t $SIDES_DIR/*"
    echo $sel
    eval $sel
done
