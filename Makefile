# Latex Makefile ~ http://automata.cc ~ 2011

# usage:
# - copy me to dest-path/Makefile
# - set the latex_file to your latex filename without the .tex extension
# - $ make            ... to generate a pdf and dvi output
# - $ make dvi        ... to generate just a dvi output
# - $ make clean      ... to clean auxiliary files
# - $ make clean all  ... to clean everything generated

latex_file = paper

pdf:
	pdflatex $(latex_file)
	bibtex $(latex_file)
	pdflatex $(latex_file)
	pdflatex $(latex_file)

clean:
	rm -f *.aux *.bbl *.blg *.log

clean-all: clean
	rm -f *.pdf *.dvi
