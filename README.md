Source files for *Beginning mapping* course materials

# Build

- Download the Tufte [`handout.tex` template](https://github.com/wcaleb/pandoc-templates/blob/master/handout.tex)
- Install the `tufte` template in your pandoc `templates/` directory (`~/.pandoc/templates/` on linux; you may have to create it)
- Replace the `.tex` file extension with `.latex` (i.e. rename it `handout.latex`)
- If you have GNU Make available just run `make`
- If not, run `pandoc handout.md -o handout.pdf --template tufte` in terminal
