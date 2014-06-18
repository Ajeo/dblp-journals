#!/usr/bin/python

import os
import csv
import json

output_path = "./output/journals"
sliced_usage_postfix = "-sliced-usage.csv"
top_terms_postfix = "-top-terms.csv"


def copy_and_move_file(terms_file, postfix_file):
    origin_path = path_lda_subdir + terms_file
    os.system("cp " + origin_path + " " + output_path)
    os.system("mv " + output_path + terms_file + " " + output_path + "/" + subdir + postfix_file)

def sliced_usage_to_json(subdir):
    with open(output_path + '/' + subdir + sliced_usage_postfix, 'rb') as f:
        output_json = []
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            find_topic = [x for x in output_json if x["key"] == row[0]]
            if len(find_topic) > 0:
                find_topic[0]["values"].append([row[1], row[2]])
            else:
                output_json.append({"key": row[0], "values": [[row[1], row[2]]]})

        with open(output_path + '/' + subdir + '-sliced-usage.json', 'w') as outfile:
            json.dump(output_json, outfile, indent=4)

    os.system("rm " + output_path + '/' + subdir + sliced_usage_postfix)

def fix_top_terms_format(subdir):
    tmp_file = open(output_path + "/tmp_file.csv", "w")
    with open(output_path + '/' + subdir + top_terms_postfix, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            terms = row[0] + ', '
            del row[0]
            terms += ' '.join(row)
            tmp_file.write(terms + '\n')
    tmp_file.close()

    os.system("mv " + output_path + "/tmp_file.csv" + " " + output_path + '/' + subdir + top_terms_postfix)

if ( __name__ == "__main__"):
    root_dir = "./journals"
    all_subdirs = [ name for name in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, name)) ]

    # reset
    os.system("rm " + output_path + "/*.csv")

    for subdir in all_subdirs:
        print subdir
        path_subdir = root_dir + "/" + subdir
        lda_subdir = [ name for name in os.listdir(path_subdir) if os.path.isdir(os.path.join(path_subdir, name)) ][0]
        path_lda_subdir = path_subdir + "/" + lda_subdir

        copy_and_move_file("/journal_data-sliced-usage.csv", sliced_usage_postfix)
        copy_and_move_file("/journal_data-top-terms.csv", top_terms_postfix)
        sliced_usage_to_json(subdir)
        fix_top_terms_format(subdir)
