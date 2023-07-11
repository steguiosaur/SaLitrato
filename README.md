# SaLitrato

## Features

- Include all files to be indexed for search
- Run Boyer-Moore Algorithm on included files
- Display all instances of pattern in a list
- Preview occurence of selected pattern when selected on list

## Plan

### Graphical Interface

Includes `main menu`, `folder menu`, and `search menu`

1. `Main Menu` - shows `Create Folder` button for creating segregated instance
of files where Boyer-Moore Algorithm will run.

    - [ ] `Create Folder` button creates an object of the folder displaying the name
    and one of its file as image. Opening leads to its files like what file manager
    do.

2. `File Menu` - shows all files included and `Add File` which the Boyer-Moore
Algorithm will detect the pattern.

3. `Search Menu` - menu where previewer is displayed. Also includes the search
entry and lists of where th pattern appeared.

## Setup

1. Install dependencies

    ```sh
    pip install -r requirements.txt
    ```

2. Run the program by executing `src/main.py` in the `$SOURCES` folder

    ```sh
    python main.py
    ```
