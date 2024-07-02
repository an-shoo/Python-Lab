def find_longest_and_shortest_words(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
        longest_word = max(words, key=len)
        shortest_word = min(words, key=len)
    return longest_word, shortest_word, len(longest_word), len(shortest_word)

filename = 'textfile.txt'
with open(filename, 'w') as file:
    for _ in range(5):
        line = input("Enter a line of text: ")
        file.write(line + '\n')

longest_word, shortest_word, longest_len, shortest_len = find_longest_and_shortest_words(filename)
print(f"Longest word: {longest_word} (Length: {longest_len})")
print(f"Shortest word: {shortest_word} (Length: {shortest_len})")
