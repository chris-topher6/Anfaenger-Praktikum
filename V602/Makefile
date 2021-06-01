all: build/main.pdf

# hier Python-Skripte:
build/plot.pdf: $(wildcard skript/*.py) matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python skript/auswertung.py

#build/plot.pdf: $(wildcard skript/*.py) matplotlibrc header-matplotlib.tex | build
#	TEXINPUTS=$$(pwd): python skript/0_messwerte.py 
#	TEXINPUTS=$$(pwd): python skript/1_bragg.py 
#	TEXINPUTS=$$(pwd): python skript/2_emissionsspektrum.py 
#	TEXINPUTS=$$(pwd): python skript/3_absorbtionsspektrum.py 

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
