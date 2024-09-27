def main():
    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
    print("--- Begin book-report ---")
    print(f"{word_count(file_contents)} words found in the document")
    #char_count(file_contents)
    #print("The", char_count["Character"], char_count["Count"])
    for dict in char_count(file_contents):
        print("The", dict["Character"],"character was found",dict["Count"],"times")
    print("--- End report ---")

def word_count(f):
    book_list = [f]
    counter = 0
    for text in book_list:
        splitted_list = text.split()
        for word in splitted_list:
            counter += 1   
    return counter

def char_count(f):
    character_dict = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,
                      "j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,
                      "s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0,}
    character_list = []
    lowered_string = f.lower()
    for character in lowered_string:
        if character in character_dict:
                character_dict[character] += 1
    for character in character_dict:
        dict_for_list = {}
        count = character_dict[character]
        dict_for_list["Character"] = character
        dict_for_list["Count"] = count
        character_list.append(dict_for_list)
    character_list.sort(reverse=True, key=sort_on)
    #print(character_list)
    #for i in range(0, len(character_dict)):
        #print(f"The {character_dict[i]} is found {character_dict[i]}times")
    return character_list

def sort_on(dict):
    return dict["Count"]

main()