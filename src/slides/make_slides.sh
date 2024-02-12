#!/bin/bash
#
# bash ../make_slides.sh slides_nickname.do.txt
#
# But this script is normally run from make.sh to make both
# chapter and slides.

dofile=$1
if [[ -z "$dofile" ]]; then
  for i in *.do.txt; do
    dofile=$i
  done
fi
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
mv ${filename}.pdf ${filename}-beamer.pdf

# Handouts
doconce format pdflatex tmp_preprocess__$filename --latex_title_layout=beamer --latex_table_format=footnotesize --latex_admon_title_no_period --latex_code_style=pyg 
doconce slides_beamer tmp_preprocess__$filename --beamer_slide_theme=red_shadow --handout
pdflatex -shell-escape tmp_preprocess__$filename.tex
pdfjam tmp_preprocess__${filename}.pdf --no-landscape --frame true --nup 2x3 --suffix 6up
mv tmp_preprocess__${filename}-6up.pdf ${filename}-6up.pdf
rm tmp* 
./clean.sh
