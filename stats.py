def word_count(text):
    return len(text.split())

def appearance_count(text):
    appearance_dict = {}

    for char in text:
        char_lower = char.lower()

        if appearance_dict.get(char_lower) == None:
            appearance_dict[char_lower] = 1
        else:
            appearance_dict[char_lower] += 1
    
    return appearance_dict

def sorted_lst(char_dict):
    lst = []

    for key, value in char_dict.items():
        lst.append({"name": key, "num": value}) 

    lst.sort(key=char_value, reverse=True)

    return lst


def char_value(char_dict):
    return char_dict["num"]