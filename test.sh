#!/usr/bin/env bash

dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $dir

source ./environment-test.sh

py.test --cov application tests --cov-report term-missing
