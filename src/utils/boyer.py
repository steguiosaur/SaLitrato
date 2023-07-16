def set_badchar_array(pattern):
    table = {}
    for i in range(len(pattern)):
        table[pattern[i]] = i
    return table

def boyer_moore(text, pattern, bc_table):
    pattern = pattern.lower()
    text = text.lower()
    m = len(pattern)
    n = len(text)
    if m == 0 or n == 0 or n < m:
        return []

    positions = []
    shift = 0

    while shift <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1
        if j < 0:
            positions.append(shift)
            shift += 1
        else:
            bc_shift = j - bc_table.get(text[shift + j], -1)
            shift += max(1, bc_shift)

    return positions
