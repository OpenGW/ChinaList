#!/usr/bin/env bash

cd "$(dirname "$(realpath "$0")")"

function download() {
    local FILE_URL="$1"
    local OUTPUT_FILE_NAME="${2:-"$(basename "$FILE_URL")"}"

    if [ -f "$OUTPUT_FILE_NAME" ]; then
        rm "$OUTPUT_FILE_NAME"
    fi

    wget "$FILE_URL" -O "$OUTPUT_FILE_NAME" --quiet
}


download "http://www.ipdeny.com/ipblocks/data/countries/cn.zone" "cn_ipv4.zone"
download "http://www.ipdeny.com/ipblocks/data/countries/hk.zone" "hk_ipv4.zone"
download "http://www.ipdeny.com/ipblocks/data/countries/tw.zone" "tw_ipv4.zone"

cat "cn_ipv4.zone" >  "@china_ipv4.txt"
cat "hk_ipv4.zone" >> "@china_ipv4.txt"
cat "tw_ipv4.zone" >> "@china_ipv4.txt"


download "http://www.ipdeny.com/ipv6/ipaddresses/blocks/cn.zone" "cn_ipv6.zone"
download "http://www.ipdeny.com/ipv6/ipaddresses/blocks/hk.zone" "hk_ipv6.zone"
download "http://www.ipdeny.com/ipv6/ipaddresses/blocks/tw.zone" "tw_ipv6.zone"

cat "cn_ipv6.zone" >  "@china_ipv6.txt"
cat "hk_ipv6.zone" >> "@china_ipv6.txt"
cat "tw_ipv6.zone" >> "@china_ipv6.txt"
