def get_number_of_words(text: str):
    list_of_words = text.split()
    return len(list_of_words)

def get_number_of_characters(text: str):
    characters = {}
    text = text.lower()
    for char in text:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return characters

def sort_on(dictionary: dict):
    return dictionary["num"]

def get_sorted_list_of_characters(characters: dict):
    sorted_list = []
    for char in characters.keys():
        sorted_list.append({"name": char, "num": characters[char]})
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
