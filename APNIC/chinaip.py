#!/usr/bin/env python

from __future__ import print_function
from __future__ import with_statement
import os
import sys
import codecs


length_to_cidr = {}
for exp in range(0, 32):
    length_to_cidr[pow(2, exp)] = 32 - exp


def main(args):
    # type: (list[str]) -> None
    """
    Command:
        chinaip.py <apnic_file_path> <countries> <rectypes>
    Example:
        chinaip.py <apnic_file_path> CN ipv4
        chinaip.py <apnic_file_path> CN,HK,TW ipv4,ipv6
    """
    assert len(args) == 3
    apnic_file_path = args[0]
    countries = set(map(str.upper, filter(lambda s: s, args[1].split(","))))
    rectypes = set(map(str.upper, filter(lambda s: s, args[2].split(","))))

    with codecs.open(apnic_file_path, "r", "utf-8") as fp:
        lines = fp.readlines()

    for line in lines:
        # Ignore comments
        if line.startswith("#"):
            continue

        # delegated-apnic-latest example:
        #   apnic|AU|ipv4|1.0.0.0|256|20110811|assigned
        # delegated-apnic-extended-latest example:
        #   apnic|AU|ipv4|1.0.0.0|256|20110811|assigned|A91872ED
        # Parts:
        #       0| 1|   2|      3|  4|       5|       6|
        parts = line.split("|")
        if len(parts) < 7:
            continue

        country = parts[1].upper()
        rectype = parts[2].upper()
        if (country not in countries) or (rectype not in rectypes):
            continue

        start = parts[3]
        value = int(parts[4])
        date = parts[5]
        status = parts[6]
        if rectype == "IPV4":
            # apnic|AU|ipv4|1.0.0.0|256|20110811|assigned|A91872ED
            print("%s/%d" % (start, length_to_cidr[value]))
        elif rectype == "IPV6":
            # apnic|CN|ipv6|2001:250::|35|20000426|allocated|A9235F14
            print("%s/%d" % (start, value))


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))
    main(sys.argv[1:])
