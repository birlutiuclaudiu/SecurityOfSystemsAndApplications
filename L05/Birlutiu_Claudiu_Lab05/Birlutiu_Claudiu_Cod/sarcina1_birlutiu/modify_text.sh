#!/bin/bash

tr [:upper:] [:lower:] < article.txt > lowercase.txt &&
tr -cd ’[a-z][\n][:space:]’ < lowercase.txt > plaintext.txt;
