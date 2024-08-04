def add_entry(dictionary, word, meaning):
    dictionary[word] = meaning

def search_word(dictionary, word):
    return dictionary.get(word, "Word not found")

def find_words_with_meaning(dictionary, meaning):
    answer= [word for word, mean in dictionary.items() if mean == meaning]
    if answer==[]:
        return ("Not found")
    else:
        return answer

def remove_entry(dictionary, word):
    if word in dictionary:
        del dictionary[word]

def display_all_words_sorted(dictionary):
    for word in sorted(dictionary):
        print(f"{word}: {dictionary[word]}")

dictionary = {
    "apple": "a fruit",
    "banana": "another fruit",
    "cherry": "yet another fruit"
}

add_entry(dictionary, "date", "a sweet fruit")
print(search_word(dictionary, "banana"))
print(find_words_with_meaning(dictionary, "a fruit"))
remove_entry(dictionary, "apple")
display_all_words_sorted(dictionary)
