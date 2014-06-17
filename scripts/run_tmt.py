#!/usr/bin/python

import os

from shutil import move
from os import remove, close
from tempfile import mkstemp

def replace(file_path, pattern, subst):
  fh, abs_path = mkstemp();
  new_file = open(abs_path, 'w')
  old_file = open(file_path)
  for line in old_file:
    new_file.write(line.replace(pattern, subst))
  new_file.close()
  close(fh)
  old_file.close()
  remove(file_path)
  move(abs_path, file_path)

def run_step1(path_subdir):
  os.system("cp src/scala/step1.scala " + path_subdir)
  replace(path_subdir + "/step1.scala", "journal_data.csv", path_subdir + "/journal_data.csv")
  os.system("java -jar tmt-0.4.0.jar " + path_subdir + "/step1.scala")

def run_step2(path_subdir):
  os.system("cp src/scala/step2.scala " + path_subdir)
  replace(path_subdir + "/step2.scala", "journal_data.csv", path_subdir + "/journal_data.csv")
  replace(path_subdir + "/step2.scala", "./lda-", path_subdir + "/lda-")
  os.system("java -jar tmt-0.4.0.jar " + path_subdir + "/step2.scala")

def run_step3(path_subdir, path_lda_subdir):
  os.system("cp src/scala/step3.scala " + path_subdir)
  replace(path_subdir + "/step3.scala", "journal_data.csv", path_subdir + "/journal_data.csv")
  replace(path_subdir + "/step3.scala", "lda-a017658d-30-0c74d394", path_lda_subdir)
  os.system("java -jar tmt-0.4.0.jar " + path_subdir + "/step3.scala")

def run_step4(path_subdir, path_lda_subdir):
  os.system("cp src/scala/step4.scala " + path_subdir)
  replace(path_subdir + "/step4.scala", "journal_data.csv", path_subdir + "/journal_data.csv")
  replace(path_subdir + "/step4.scala", "lda-a017658d-30-0c74d394", path_lda_subdir)
  os.system("java -jar tmt-0.4.0.jar " + path_subdir + "/step4.scala")

if ( __name__ == "__main__"):
  root_dir = "./journals"
  all_subdirs = [ name for name in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, name)) ]

  for subdir in all_subdirs:
    print subdir
    path_subdir = root_dir + "/" + subdir
    lda_subdir = [ name for name in os.listdir(path_subdir) if os.path.isdir(os.path.join(path_subdir, name)) ][0]
    # run_step1(path_subdir)
    # run_step2(path_subdir)
    run_step3(path_subdir, path_subdir + "/" + lda_subdir)
    run_step4(path_subdir, path_subdir + "/" + lda_subdir)

