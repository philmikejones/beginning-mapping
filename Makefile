handout.pdf: handout.md
	pandoc handout.md -o handout.pdf -V geometry:landscape
