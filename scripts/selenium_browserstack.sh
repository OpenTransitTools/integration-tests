#
# run selenium side runner
#
DIR=`dirname $0`
. $DIR/base.sh

for t in $DIR/browserstack/*cap; do
    sel="$SELENIUM_CMD --base-url $TEST_URL --config-file $t $SIDES_DIR/*"
    echo $sel
    #eval $sel
done
