#!/bin/bash
if [[ -x "$(command -v python3)" ]]
then
    pyv="$(python3 -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        python3 src/main.py
    else
        echo "You've got the wrong version of python, sort it out!" >&2
    fi 
else
    echo "You don't have python, go get it!" >&2
fi