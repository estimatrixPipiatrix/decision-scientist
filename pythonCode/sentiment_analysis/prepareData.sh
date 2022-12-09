#!/bin/bash

if test -f train.ft.txt.bz2; then echo 'train.ft.txt.bz2 already exists'; else unzip archive.zip; fi
bunzip2 train.ft.txt.bz2
bunzip2 test.ft.txt.bz2
grep -v ',' train.ft.txt > train_no_commas.txt
grep -v ',' test.ft.txt  > test_no_commas.txt
