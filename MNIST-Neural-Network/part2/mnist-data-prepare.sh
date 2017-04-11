#!/bin/bash
#################################################
# A Simple BASH Script for Preparing MNIST Data #
#################################################
# Author : Abe Hoffman #
# Date   : Apr 2017    #
########################

## Define Functions ##
prompt_user() {
  echo
  echo "1. Create a folder called 'mnist'"
  echo "2. Download MNIST data files"
  echo "3. Uncompress them in the folder"
  echo
  while true; do
      read -p "Would you like to proceed? (Y/n) " yn
      case $yn in
          [Yy]* ) echo; main; break;;
          [Nn]* ) exit;;
          * ) echo "Please answer yes or no.";;
      esac
  done
}

create_folder() {
  rm -rf ./mnist
  echo -n "Creating 'mnist' folder: "
  mkdir mnist > /dev/null 2>&1
  cd mnist > /dev/null 2>&1
  echo "[DONE]"
}

download() {
  echo -n "Downloading MNIST Data: "
  wget http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz > /dev/null 2>&1
  wget http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz > /dev/null 2>&1
  wget http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz > /dev/null 2>&1
  wget http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz > /dev/null 2>&1
  echo "[DONE]"
}

unzip() {
  echo -n "Uncompressing the Data: "
  gzip -df *.gz > /dev/null 2>&1
  echo "[DONE]"
  echo
}

## Main Function ##
main() {
  create_folder
  download
  unzip
}

prompt_user

