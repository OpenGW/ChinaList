
# APNIC

All files are available at [https://ftp.apnic.net/stats/apnic/](https://ftp.apnic.net/stats/apnic/)


## delegated-apnic-latest

This file is available at
[https://ftp.apnic.net/stats/apnic/delegated-apnic-latest](https://ftp.apnic.net/stats/apnic/delegated-apnic-latest)

*This file is subset of `delegated-apnic-extended-latest`, so not used.*


## delegated-apnic-extended-latest

This file is available at
[https://ftp.apnic.net/stats/apnic/delegated-apnic-extended-latest](https://ftp.apnic.net/stats/apnic/delegated-apnic-extended-latest)

For the file format,
see [http://www.apnic.net/db/rir-stats-format.html](http://www.apnic.net/db/rir-stats-format.html)
or [http://ftp.apnic.net/apnic/stats/apnic/README-EXTENDED.TXT](http://ftp.apnic.net/apnic/stats/apnic/README-EXTENDED.TXT)
for details.

### Comments:
Line starting with `#`

### File header:
**version|registry|serial|records|startdate|enddate|UTCoffset**

*Example:* `2.3|apnic|20171018|100050||20171017|+1000`

### Summary line:
**registry|*|type|*|count|summary**

*Example:* `apnic|*|asn|*|8487|summary`

*Example:* `apnic|*|ipv4|*|39314|summary`

*Example:* `apnic|*|ipv6|*|52249|summary`

### Record format:

**registry|cc|type|start|value|date|status|opaque-id\[|extensions...]**

*Example:* `apnic|CN|ipv4|1.0.1.0|256|20110414|allocated|A92E1062`

*Example:* `apnic|CN|ipv6|2001:250::|35|20000426|allocated|A9235F14`

*Example:* `apnic|CN|asn|3460|1|20020801|allocated|A9162E3D`
