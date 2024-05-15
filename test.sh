#!/usr/bin/env sh

for test_file in $(find . -name "*_test.py"); do
    test_dir=$(dirname $test_file)
    cd $test_dir
    python -m unittest *_test.py
    cd -
done