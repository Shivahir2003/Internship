import random


def check_word(word,word_guess):
    green_char=[]
    yellow_char=[]
    grey_char=[]
    for x in range(len(word)):
        if word[x] == word_guess[x]:
            # print(f" {word_guess[x]}  green")
            green_char.append(word[x])
        if word[x] in word_guess:
            if word_guess[x] in green_char :
                # print(f"grey in duplicate {word_guess[x]}")
                grey_char.append(word_guess[x])
            yellow_char.append(word[x])
        if word_guess[x] not in word:
            grey_char.count(x)
            # print(f" {word_guess[x]}  grey")
            grey_char.append(word_guess[x])
            # ssdf,asdf,hell,hill,hisf
        [yellow_char.remove(char)for char in green_char if char in yellow_char]
    return green_char,yellow_char,grey_char

def generate_random_word():
    words_list = ["apple", "beach", "chair", "dance", "eleph", "flask", "glide", "happy", "igloo", "jumpy"]
    
    word= random.choice(words_list)
    return word

def check_contition(word,word_guess):
    if word_guess == 'show':
        return word
    if not word_guess.isalpha():
        return "only characters are allowed"
    if len(word_guess)!=5:
        return "word must be 5 characters long"
    1


def main():
    word= generate_random_word()
    # word="shiv"
    for tries in range(0,6):
        word_guess=input("enter word to guess   ")
        condition =check_contition(word,word_guess)
        if condition is not None:
            print(condition)
            continue
        green_char,yellow_char,grey_char=check_word(word,word_guess)
        
        
        if len(green_char) ==5:
            
            print("you guessed correct word in ",tries+1,"attempt")
            # print(f"word is {word}")  jww
            break   
        else:
            print(f"letter at right place {green_char}")
            print(f"letter is in world but wrong position {yellow_char}")
            print(f"letter does not exists in word {grey_char}")
            
    else:
        print(" you are out of tries ")
        print(f"word is `{word}`")
    
if __name__=="__main__":
    main()