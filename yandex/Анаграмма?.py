first_word = input()
second_word = input()
first_word_counts = {}
second_word_counts = {}
for char in first_word:
    if char in first_word_counts:
        first_word_counts[char] += 1
    else:
        first_word_counts[char] = 1
for char in second_word:
    if char in second_word_counts:
        second_word_counts[char] += 1
    else:
        second_word_counts[char] = 1
if first_word_counts == second_word_counts:
    print('YES')
else:
    print('NO')