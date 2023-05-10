def count_strings(strings):
    return len([string for string in strings if len(string) >= 2 and string[0] == string[-1]])

strings = ['abc', 'xyz', 'aba', '1221']
print(count_strings(strings)) # Output: 2
