#!/bin/bash
##################################################
# A Simple BASH Script to create Validation Data #
##################################################
# Author : Abe Hoffman #
# Date   : Apr 2017    #
########################

main() {
  echo "Ensure 'train.csv' and 'test.csv' are in your current path"
  tail -n 10000 train.csv > validate.csv
  head -n 50000 train.csv > train0.csv
  mv train0.csv train.csv
  echo
  wc -l train.csv;wc -l validate.csv;wc -l test.csv
  echo
}

main

