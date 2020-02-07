#!/usr/bin/env python
# Usage: ./csv2tab.sh < data.csv > data.tsv && head data.tsv 
# From: https://unix.stackexchange.com/questions/359832/converting-csv-to-tsv
import csv, sys
csv.writer(sys.stdout, dialect='excel-tab').writerows(csv.reader(sys.stdin))
