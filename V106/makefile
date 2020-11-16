all: build/main.pdf

# hier Python-Skripte:
build/schwingungen.pdf: schwingungen.py | build
	python schwingungen.py

build/tabellen.txt: AuswertungV106.py | build
	python AuswertungV106.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:

build/main.pdf: main.tex build/schwingungen.pdf
	lualatex main.tex --output-directory=build main.tex 

build/main.bcf: main.tex
	biber main.bcf

build/main.pdf: main.tex build/schwingungen.pdf build/main.bcf
	lualatex main.tex --output-directory=build main.tex 
	

#build/main.pdf: FORCE | build
#	  TEXINPUTS=build: main.tex\
#	  BIBINPUTS=build: biber main.bcf\
#	  max_print_line=1048576 \
#	latexmk \
#	  --lualatex \
#	  --output-directory=build \
#	  --interaction=nonstopmode \
#	  --halt-on-error \
#	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean