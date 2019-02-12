Source files for *Beginning mapping* course materials

# Build

- Download the [Eisvogel pandoc template](https://github.com/Wandmalfarbe/pandoc-latex-template)
- Install it in your pandoc `templates/` directory (`~/.pandoc/templates/` on linux; you may have to create it)
- Replace the `.tex` file extension with `.latex` (i.e. rename it `handout.latex`)
- If you have GNU Make available just run `make`
- If not, run `pandoc handout.md -o handout.pdf` in terminal
