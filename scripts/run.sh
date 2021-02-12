DIR=`dirname $0`

BROWSERS=${BROWSERS:="firefox chrome safari edge"}
SIDES_DIR=${SIDES_DIR:="./sides"}

cd $DIR/../

for b in $BROWSERS; do
  sel="selenium-side-runner -c \"browserName=$b\" $SIDES_DIR/*"
  echo $sel
  eval $sel
done

cd -
