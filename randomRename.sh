#!/bin/sh

# Change this variable to alter the random string length
stringLength=10

# The first argument is the file to be randomly named. The second is the
# directory it is in
file=$1
directory=$2

extension=`python3 ~/git/random-rename/getExtension.py "$file"`
randomString=`python3 ~/git/random-rename/randomString.py $stringLength`

# Uncomment for testing purposes
#`konsole --hold -e echo $file $directory$randomString$extension`
`mv "$file" "$directory$randomString$extension"`
