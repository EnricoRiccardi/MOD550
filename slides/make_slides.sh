#!/bin/bash
#
# bash ../make_slides.sh slides_nickname.do.txt
#
# But this script is normally run from make.sh to make both
# chapter and slides.

dofile=$1
if [ ! -f $dofile ]; then
  echo "No such file: $dofile"
  exit 1
fi

filename=`echo $dofile | sed 's/\.do\.txt//'`

# LaTeX PDF for printing
# (Smart to make this first to detect latex errors - HTML/MathJax
# gives far less errors and warnings)

# LaTeX Beamer
preprocess -DFORMAT=pdflatex ../newcommands.p.tex > newcommands_keep.tex
doconce format pdflatex $filename --latex_title_layout=beamer --latex_table_format=footnotesize --latex_admon_title_no_period --latex_code_style=pyg 
doconce slides_beamer $filename --beamer_slide_theme=red_shadow
pdflatex -shell-escape $filename
pdflatex -shell-escape $filename
pdflatex -shell-escape $filename
cp ${filename}.pdf ${filename}-beamer.pdf
rm -f ${filename}.pdf
cp ${filename}.tex ${filename}-beamer.tex  # sometimes nice to look at

# Handouts
# doconce format pdflatex $filename --latex_title_layout=beamer --latex_table_format=footnotesize --latex_admon_title_no_period --latex_code_style=pyg
# doconce slides_beamer $filename --beamer_slide_theme=red_shadow --handout
# pdflatex -shell-escape $filename
# pdflatex -shell-escape $filename
# pdflatex -shell-escape $filename
# pdfnup --nup 2x3 --frame true --delta "1cm 1cm" --scale 0.9 --outfile ${filename}-beamer-handouts2x3.pdf ${filename}.pdf
# rm -f ${filename}.pdf
