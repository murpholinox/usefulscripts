#!/usr/bin/env python
## What it does: Converts csv data files to tsv.
## From: https://unix.stackexchange.com/questions/359832/converting-csv-to-tsv
## Usage: `./csv2tab.sh < data.csv > data.tsv`
## Output: tsv file
## Works with: python3


import csv, sys
csv.writer(sys.stdout, dialect='excel-tab').writerows(csv.reader(sys.stdin))
