handout.pdf: handout.md
	pandoc handout.md -o handout.pdf \
	--template eisvogel -V lang=en-GB \
	--listings --highlight-style espresso
