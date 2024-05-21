#!/usr/bin/env sh

# Loop to find and run Python tests
for test_file in $(find . -name "*_test.py"); do
    test_dir=$(dirname $test_file)
    cd $test_dir
    python -m unittest *_test.py
    cd -
done

# Loop to find and run C tests
for test_file in $(find . -path '*Unity*' -prune -o -name "test_*.c" -print); do
    test_dir=$(dirname $test_file)
    cd "$(dirname $test_dir)"

    if [ -f Makefile ]; then
        make clean
        make
        make run_tests

        test_status=$?
        if [ $test_status -ne 0 ]; then
            echo "Test failed with exit status $test_status"
            exit $test_status
        fi
    fi

    cd - > /dev/null
done
