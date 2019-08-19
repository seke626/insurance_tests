#incomplete

def split_characters(word):
    character_list = []
    n = len(word)
    for character in word:
        character_list.insert(n, character)
        n+=1
    return (character_list)

ow = split_characters("wo")

def swap_words(word):
    first = 0
    second = 1
    
    i = len(word)
    print("i", i % 2)
    if (i % 2 == 0 or i == 1):
        word[first], word[second] = word[second], word[first]
        
    else:
        return ("if not working", word)
    
    return ("Something not working", word)
    ###########################
    #aList[] = split_characters(word)
    i = int(len(word))
    first = 0
    second = 1
    
    if (i % 2 == 0 or i == 1):
        word[first], word[second] = word[second], word[first]
    return word
    
    
def swap(aList):
    temp = char1
    char1 = char2
    char2 = temp
    aList.append(char1)
    aList.append(char2)
    return (aList)

def swapping(aList):
    
    return aList

def swap_characters(word):
    word = split_characters(word)

    
    new_list.append(a)

swap_characters("word")
    

def test_words(word):
    aList = []
    aList = split_characters(word)
    counter = 0
    first = 0
    second = 1
    
    #print(aList[0])

    length_of_word = (len(aList))
    
    while counter < length_of_word:
        if length_of_word % 2 == 0:    
            
            print (aList)
        else:
            
            print ("No")
        counter+=1
        
#print(swap("H", "I"))

#print(test_words("HI"))

#TODO: 
    
    

#print(ow[0])
#print(swap_words(ow))

#print(test_words("wow"))

#print(ow)
#print(split_characters("word"))
    
    
