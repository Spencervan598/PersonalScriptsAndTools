#!/bin/bash
download="$1"
result="$2"
while [ ! "$x" ]; do
    if [ ! "$download" ]; then
        echo "If same directory insert filename, if not insert file path"
        read -r download
        echo "$download"
    fi
    if [ ! "$result" ]; then
        echo "Insert given sum"
        read -r result
        echo "$result"

    fi
    if [ "$(sha256sum "$download" | awk '{print $1}')" = "$result" ]; then
        echo "Match"
    else
        echo "No Match"
    fi
    printf "Press Enter to check another. Any other key to quit.\n"
    read -r -n 1 x
    result=""
    download=""
done
