

def split_characters(word):
    character_list = []
    n = len(word)
    for character in word:
        character_list.insert(n, character)
        n+=1
    return (character_list)

def swap_characters(*character_list):
    first = 0
    second = 1
    character_list[0, 1] = character_list[1, 0]

    return character_list
#try this in swap_characters
#map (lambda t: (t[1], t[0]), mylist)

word1 = "hi"
#print(split_characters(word1))
print(swap_characters(word1))
