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
        chinaip.py <countries> <record_types>
    Example:
        chinaip.py CN ipv4
        chinaip.py CN,HK,TW ipv4,ipv6
    """
    assert len(args) == 2
    countries = set(map(str.upper, filter(lambda s: s, args[0].split(","))))
    record_types = set(map(str.upper, filter(lambda s: s, args[1].split(","))))

    with codecs.open("delegated-apnic-extended-latest", "r", "utf-8") as fp:
        lines = fp.readlines()

    for line in lines:
        # Ignore comments
        if line.startswith("#"):
            continue

        # Example:
        #   apnic|AU|ipv4|1.0.0.0|256|20110811|assigned|A91872ED
        # Parts:
        #       0| 1|   2|      3|  4|       5|       6|       7
        parts = line.split("|")
        if len(parts) < 8:
            continue

        country = parts[1].upper()
        record_type = parts[2].upper()
        if (country not in countries) or (record_type not in record_types):
            continue

        start = parts[3]
        value = int(parts[4])
        date = parts[5]
        status = parts[6]
        if record_type == "IPV4":
            # apnic|AU|ipv4|1.0.0.0|256|20110811|assigned|A91872ED
            print("%s/%d" % (start, length_to_cidr[value]))
        elif record_type == "IPV6":
            # apnic|CN|ipv6|2001:250::|35|20000426|allocated|A9235F14
            print("%s/%d" % (start, value))


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))
    main(sys.argv[1:])
