.PHONY: all

all: \
	handout.pdf crib.pdf

handout.pdf: handout.md
	pandoc handout.md -o handout.pdf \
	--template ~/.pandoc/templates/Eisvogel-3.1.0/eisvogel.latex -V lang=en-GB \
	--listings --highlight-style espresso

crib.pdf: crib.md
	pandoc crib.md -o crib.pdf \
	--template ~/.pandoc/templates/Eisvogel-3.1.0/eisvogel.latex -V lang=en-GB \
	--listings --highlight-style espresso
