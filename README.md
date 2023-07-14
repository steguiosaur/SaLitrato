![Salitrato Logo](assets/salitrato_light.svg#gh-dark-mode-only)
![Salitrato Logo](assets/salitrato.svg#gh-light-mode-only)

## :globe_with_meridians: Description

Folder-wide image text search

## :abacus: Features

- Included image files are indexed for search
- Run Boyer-Moore Algorithm on included files
- Display all instances of pattern in a list
- Preview occurence of selected pattern when selected on list

## :clipboard: Setup Guide

### Prerequisites

- Python 3.11.x
- Tesseract (OCR engine)
- Install required dependencies

### Execution

1. Setup Python virtual environment
    > Skip this part if system packages does not break on `pip` installs.

    ```sh
    python -m venv venv
    source venv/bin/<enter_sh_executable>
    ```

2. Install dependencies

    ```sh
    pip install -r requirements.txt
    ```

3. Run the program by executing `src/main.py` in the `$SOURCES` folder

    ```sh
    python main.py
    ```
