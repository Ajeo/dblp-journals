#!/usr/bin/python

import os
import csv
import json

if ( __name__ == "__main__"):
    root_dir = "./journals"
    journals = []
    all_subdirs = [ name for name in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, name)) ]

    for subdir in all_subdirs:
        terms = []
        path_subdir = root_dir + "/" + subdir
        lda_subdir = [ name for name in os.listdir(path_subdir) if os.path.isdir(os.path.join(path_subdir, name)) ][0]
        with open(path_subdir + "/" + lda_subdir + '/journal_data-top-terms.csv', 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[1] != "Top Terms" and not (row[1] in terms) :
                    terms.append(row[1])

        journals.append({"name": subdir, "topics": len(terms)})

    print journals
    with open('./scripts/assets/journal_topic_list.json', 'w') as outfile:
        json.dump(journals, outfile, indent=4)
