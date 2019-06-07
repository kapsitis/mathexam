#!/bin/bash
if [ -z "$1" ]
then
  echo "Please specify path"
else
  export NEWPATH=`echo $1 | sed -e "s/\.md/.html/g"`
  pandoc -s -o $NEWPATH $1 --metadata pagetitle="Lapa" \
    --mathjax="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" \
    --css="../../style/default.css"
fi

