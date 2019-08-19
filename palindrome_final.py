#Problem #4 Palindrome

def reverse_sentence(sentence):
    print ("Sentence: " ,sentence)
    sentence = remove_whitespace(sentence)
    return sentence[::-1]

def remove_whitespace(sentence):
    strip = sentence.strip()
    remove_space = strip.replace(" ", "")
    sentence = remove_space
    return sentence

#function used for testing
def palindrome(sentence):
    reversed_sentence = reverse_sentence(sentence)
    sentence = remove_whitespace(sentence)

    if (sentence.lower() == reversed_sentence.lower()):
        print("Reversed: ", reverse_sentence(sentence), " \n " , "is a palindrome")
    else:
        print("Reversed after if: ", reverse_sentence(sentence))
        print("is not a palindrome")

def return_bool_if_palindrome(sentence):
    reversed_sentence = reverse_sentence(sentence)
    sentence = remove_whitespace(sentence)

    if (sentence.lower() == reversed_sentence.lower()):
        return True
    else:
        return False


#testing

sentence = "Step on no pets"
sentence2 = "put it up"
sentence3 = "not a palimdrome"
word1 = "word"
word_with_numbers = "W1991w"

print(return_bool_if_palindrome(sentence))
print(return_bool_if_palindrome(sentence2))
print(return_bool_if_palindrome(sentence3))
print(return_bool_if_palindrome(word1))
print(return_bool_if_palindrome(word_with_numbers))

#palindrome("step on no pets") 
#palindrome("put it up")
#palindrome("this is not a palindrome")
#palindrome("Step on no pets")
