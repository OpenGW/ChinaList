#!/usr/bin/env bash

cd "$(dirname "$(realpath "$0")")"

OUTPUT_FILE_NAME="china_ip_list.txt"


if [ -f "$OUTPUT_FILE_NAME" ]; then
    rm "$OUTPUT_FILE_NAME"
fi

wget "https://raw.githubusercontent.com/17mon/china_ip_list/master/china_ip_list.txt" -O "$OUTPUT_FILE_NAME" --quiet

cp "$OUTPUT_FILE_NAME" "@china_ipv4.txt"
