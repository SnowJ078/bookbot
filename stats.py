def get_word_count(string_to_count):

    word_count = 0

    for word in string_to_count.split():
        word_count += 1

    return word_count

def get_character_count(string_to_count):
    
    character_count = {

    }

    for char in string_to_count:
        if char.lower() not in character_count:
            character_count[char.lower()] = 1
        else: 
            character_count[char.lower()] = character_count[char.lower()] + 1

    return character_count

def sort_on(dict):
    return dict["num"]

def sort_dictionary(dictionary):

    char_list = []
    
    for key in dictionary:
        new_dict = {}

        new_dict["char"] = key
        new_dict["num"] = dictionary[key]

        char_list.append(new_dict)

    char_list.sort(reverse=True, key=sort_on)

    return char_list
