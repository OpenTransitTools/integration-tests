DIR=`dirname $0`

TEST_URL=${TEST_URL:="https://labs.trimet.org"}
BROWSERS=${BROWSERS:="firefox chrome safari edge"}
SIDES_DIR=${SIDES_DIR:="./sides"}

cd $DIR/../

for b in $BROWSERS; do
  sel="selenium-side-runner --base-url $TEST_URL -c \"browserName=$b\" $SIDES_DIR/*"
  echo $sel
  eval $sel
done

cd -
