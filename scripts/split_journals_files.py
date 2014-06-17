#!/usr/bin/python

import os
import csv
import codecs

journals = {}

def close_files():
  for journal in journals:
    journals[journal].close()

def write_journal(journal, row):
  data = row[0] + ", " + row[1] + ", " + row[2] + "\n"
  journal.write(data)

#TODO Delete jorunal directories
def split_files():
  with open('journals/dblp_journals.csv', 'rb') as f:
      reader = csv.reader(f)
      for row in reader:
        journal = row[2].replace(" ", '_').replace(".", '').lower()
        if journal in journals:
          write_journal(journals[journal], row)
        else:
          os.makedirs('journals/' + journal)
          journals[journal] = codecs.open("journals/" + journal + "/journal_data.csv", "w", "iso-8859-1")
          write_journal(journals[journal], row)

if ( __name__ == "__main__"):
  split_files()
  close_files()
