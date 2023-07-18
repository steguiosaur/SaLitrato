def set_badchar_array(pattern):
    table = {}      # creates dictionary of pattern for bad char processing
    for index in range(len(pattern)):
        table[pattern[index]] = index
    return table    # {'p':0,'a':1,'t':2,'t':3,'e':4,'r':5,'n':6}

def boyer_moore(text, pattern, bc_table):
    len_pattern = len(pattern)
    len_text = len(text)

    if len_pattern == 0 or len_text == 0 or len_text < len_pattern:
        return []

    pattern = pattern.lower()
    text = text.lower()

    positions = []  # collect starting indexes of matched pat in txt
    shift = 0       # start at 0 index of text
    while shift <= len_text - len_pattern:
        cur_index = len_pattern - 1 # point index to the last char of pattern
        # loop breaks when all pattern matches or pattern[cur_index] doesnt match current text
        while cur_index >= 0 and pattern[cur_index] == text[shift + cur_index]:
            cur_index -= 1  # iterate backwards
        if cur_index < 0:   # pattern is matched if cur_index is negative
            positions.append(shift) # put index in positions list
            shift += len_pattern # entirely shift the pattern
        else:
            # bc_table.get() retrieves value associated with character using text[shift + cur_index]
            # as key, returning the rightmost occurrence of the character. Being reduced by
            # cur_index, it will calculate the distance of current index to that rightmost char
            shift += max(1, cur_index - bc_table.get(text[shift + cur_index], -1))

    return positions
