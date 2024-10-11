def main():
    text_path = "books/frankenstein.txt"
    file_text = get_file_text(text_path)
    num_words = count_words(file_text)
    num_chars_dict = count_chars(file_text)
    sorted_chars_list = sort_dict_to_list(num_chars_dict)

    print(f"--- Begin report of {text_path} ---")
    print(f"{num_words} found in the document")
    print("")
    
    for char in sorted_chars_list:
        if char['char'].isalpha():
            print(f"The {char['char']} character was found {char['val']} times")
    
    print("--- End report ---")


def get_file_text(file_path):
    with open(file_path) as f:
        return f.read()


def count_words(file_text):
    num_words = len(file_text.split())
    return num_words


def count_chars(file_text):
    chars = {}
    file_text = file_text.lower()
    for char in file_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def sort_value(dict):
    return dict["val"]


def sort_dict_to_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "val": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_value)
    return sorted_list


main()