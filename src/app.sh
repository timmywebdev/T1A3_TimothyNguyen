#!/bin/bash
if [[ -x "$(command -v python3)" ]]
then
    pyv="$(python3 -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        python3 src/main.py
    else
        echo "You've got the wrong version of python, please download Python3!" >&2
    fi 
else
    echo "You don't have python installed at all, please download Python3!" >&2
fi 