# DOCUMENTATION

Software used for creating figures, diagrams, and documents for the documentation.

## Flowchart

Created with the following software:

- `Dia` - Install via AUR with `yay -S dia-git`
- `Inkscape` - Installation with Arch `pacman -S inkscape`

## Document

The PDF documentation was typesetted in LaTeX. Converting to other extension might
require the use of `pandoc`.

### LaTeX Setup Neovim

1. Install all `texlive` packages via the package manager
2. Install `neovim` for text editing and `zathura` for preview
3. Setup [Nvole](https://github.com/steguiosaur/nvole) in `$CONFIG` - a Neovim
distribution for editing LaTeX files
