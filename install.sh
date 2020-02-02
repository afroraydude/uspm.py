#!/bin/sh

# mv all files to appropriate dir
mkdir -p /usr/local/share/uspm
mv ./* /usr/local/share/uspm

# link executable
rm -rf /usr/local/bin/uspm
ln -s /usr/local/share/uspm/uspm.py /usr/local/bin/uspm

# create other folders
mkdir -p /var/uspm/storage
