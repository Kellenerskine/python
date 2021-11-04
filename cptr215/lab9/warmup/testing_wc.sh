#!/bin/bash
cd /Users/kellen/Desktop/CS/python/cptr215/lab9/warmup || return
python wc.py 04fg.txt Fzn.txt test2.txt test.txt
/bin/echo -n "------"
printf "\n"
python wc.py
/bin/echo -n "------"
printf "\n"
python wc.py test.txt
/bin/echo -n "------"
printf "\n"
python wc.py testy.html
