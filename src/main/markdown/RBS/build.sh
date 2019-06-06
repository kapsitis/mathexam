#!/bin/bash

pandoc -s -o $1.docx $1.md --mathjax="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
    
