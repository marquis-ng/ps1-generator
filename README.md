# ps1-generator
A curses-based Bash prompt generator, written in Python.

## Introduction
Tired of generating a PS1 prompt for Bash? Use this.

## Installation
Just download the script and start making your prompt:
```bash
wget https://raw.githubusercontent.com/marquis-ng/ps1-generator/main/ps1gen.py
# curl https://raw.githubusercontent.com/marquis-ng/ps1-generator/main/ps1gen.py -o ps1gen.py
python3 ps1gen.py
```

## Keybindings:
| Key | Action |
| :-- | :-- |
| `Up` | Select above row |
| `Down` | Select below row |
| `Left` | Select previous item of row |
| `Right` | Select next item of row |
| `Home` | Select first item of row |
| `End` | Select last item of row |
| `Return` / `Space` | Add selected item to PS1 |
| `Backspace` | Remove selected item from PS1 |
