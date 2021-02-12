DIR=`dirname $0`

P=".:$DIR:$PWD/node_modules/.bin:$DIR/../node_modules/.bin"
for d in "chromedriver geckodriver edgedriver msedgedriver"; do
    P="$P:$PWD/node_modules/$d/bin"
    P="$P:$DIR/../node_modules/$d/bin"
done
export PATH="$PATH:$P"


TEST_URL=${TEST_URL:="https://labs.trimet.org"}
BROWSERS=${BROWSERS:="firefox chrome safari MicrosoftEdge" }
SIDES_DIR=${SIDES_DIR:="./sides"}

cd $DIR/../

for b in $BROWSERS; do
  sel="selenium-side-runner --base-url $TEST_URL -c \"browserName=$b\" $SIDES_DIR/*"
  echo $sel
  eval $sel
done

cd -
