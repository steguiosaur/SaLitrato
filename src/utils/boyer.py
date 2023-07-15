# Boyer-Moore String Matching Algorithm using bad character heuristics
# reference: https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/
#
# NOTE: `ord()` converts the character to its ASCII value.

NO_OF_CHARS = 256

# Preprocess bad character heuristics
def create_badchar_array(string, size):
    # allocate NO_OF_CHARS to array and put -1 as value to all
    bad_char_arr = [-1] * NO_OF_CHARS

    # replace -1 with the actual character in ASCII format
    for i in range(size):
        bad_char_arr[ord(string[i].lower())] = i

    return bad_char_arr


# Uses Boyer-Moore Algorithm to find all index positions of the pattern in the text
def get_matched_positions(text, pattern):
    matched_positions = []
    lp = len(pattern)
    lt = len(text)

    # set minimum length for pattern search
    if lp < 1:
        return matched_positions

    # convert both text and pattern to lowercase or uppercase
    text = text.lower()
    pattern = pattern.lower()

    # create bad character list
    bad_char = create_badchar_array(pattern, lp)

    shift = 0  # start character pointed to index 0 of text
    while shift <= lt - lp:
        j = lp - 1  # point index to the last character of pattern

        # loop stops when all indices are compared or pattern[j] does not match text[s+j]
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1  # point to the next character on the right

        if j < 0:  # all pattern matches the current text
            matched_positions.append(shift)
            # shift by the length of the pattern or shift only 1 if it exceeds the text length
            shift += (lp - bad_char[ord(text[shift + lp])] if shift + lp < lt else 1)
        else:
            # retrieve the last occurrence index of the character
            # at index shift + j in the pattern from the bad_char array and
            # shift the matching index pattern to the last occurrence of the text
            shift += max(1, j - bad_char[ord(text[shift + j].lower())])

    return matched_positions

