#
# run selenium side runner
#
DIR=`dirname $0`
. $DIR/base.sh

echo SELENIUM PATH: `which $SELENIUM_CMD`
echo 

sel="$SELENIUM_CMD --base-url $TEST_URL $*"
echo $sel
eval $sel
