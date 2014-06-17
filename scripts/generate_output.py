#!/usr/bin/python

import os

from shutil import move
from os import remove, close
from tempfile import mkstemp

if ( __name__ == "__main__"):
  root_dir = "./journals"
  output_path = "./output/journals"
  all_subdirs = [ name for name in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, name)) ]
  
  # reset
  os.system("rm " + output_path + "/*.csv")

  for subdir in all_subdirs:
    path_subdir = root_dir + "/" + subdir
    lda_subdir = [ name for name in os.listdir(path_subdir) if os.path.isdir(os.path.join(path_subdir, name)) ][0]
    path_lda_subdir = path_subdir + "/" + lda_subdir
    print path_lda_subdir

    sliced_usage_file = "/journal_data-sliced-usage.csv"
    sliced_usage_origin_path = path_lda_subdir + sliced_usage_file 
    os.system("cp " + sliced_usage_origin_path + " " + output_path)
    os.system("mv " + output_path + sliced_usage_file + " " + output_path + "/" + subdir + "-sliced-usage.csv")

    top_terms_file = "/journal_data-top-terms.csv"
    top_terms_origin_path = path_lda_subdir + top_terms_file 
    os.system("cp " + top_terms_origin_path + " " + output_path)
    os.system("mv " + output_path + top_terms_file + " " + output_path + "/" + subdir + "-top-terms.csv")

