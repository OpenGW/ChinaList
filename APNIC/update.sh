#!/usr/bin/env bash

cd "$(dirname "$(realpath "$0")")"

OUTPUT_FILE_NAME="delegated-apnic-extended-latest"


if [ -f "$OUTPUT_FILE_NAME" ]; then
    rm "$OUTPUT_FILE_NAME"
fi

wget "https://ftp.apnic.net/stats/apnic/delegated-apnic-extended-latest" -O "$OUTPUT_FILE_NAME" --quiet

./chinaip.py CN,HK,TW ipv4 > "@china_ipv4.txt"
./chinaip.py CN,HK,TW ipv6 > "@china_ipv6.txt"
