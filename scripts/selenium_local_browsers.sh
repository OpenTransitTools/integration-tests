#
# run tests (see ./sides/ for list of selenium tests) on local browsers
#
DIR=`dirname $0`
. $DIR/base.sh

for b in $BROWSERS; do
  sel="selenium-side-runner --base-url $TEST_URL -c \"browserName=$b\" $SIDES_DIR/*.side"
  echo $sel
  eval $sel
done
