def check_correct_position(word,word_guess):
    green_char={}
    for idx,char in enumerate(word_guess):
            if word[idx] == word_guess[idx]:
                green_char[idx]=char
    return green_char


def main():
    '''Not Worlde The Game'''
    word="plier"
    flag=False
    history=[]
    green_char={}
    yellow_char=[]
    grey_char=set()
    # undo=5
    tries=0
    while tries<6:
        print(f"tries={tries+1}")
        
        word_guess=input("enter word to guess   ")
        if word_guess == "0":
            break
        if word_guess =="show":
            print(f"valid letter at position = {green_char}")
            print(f"valid letter at wrong position = {yellow_char}")
            print(f" not valid number = {grey_char}")
            continue
        if word !=word_guess:
            # import pdb; pdb.set_trace()
            
            if tries!=0:
                green_letter = check_correct_position(word,word_guess)
                for idx,char in enumerate(word_guess):
                    if idx in green_char.keys() and (idx,char) not in green_char.items():
                        print(f"must use '{green_char[idx]}' as letter {idx+1}")
                        flag=True
                        # break  # print only one condition
                        continue # print all conditions
                    else:
                        green_char |= green_letter
            else:
                green_letter = check_correct_position(word,word_guess)
                green_char |= green_letter
                
            yellow_letter=[]
            for idx,char in enumerate(word_guess):
                if char in word and idx !=word.index(char):
                    yellow_letter.append(char)
                [yellow_letter.remove(char)for char in yellow_char if char in yellow_letter]
            else:       
                for yl in yellow_char:
                    if  yl not in word_guess :
                        print(f"letter {yl} must be used ")
                        flag=True
                        # break  # print only one condition
                        continue # print all conditions
                    else:
                        yellow_char.extend(yellow_letter)
                       
                
            grey_letter=[]
            for idx,char in enumerate(word_guess):
                if char not in word and char not in grey_char:
                    grey_letter.append(char)
                if tries ==0:
                    grey_char.update(grey_letter)
                    if char in grey_char:
                        print(f"letter '{char}' is eliminated")
                        continue
                elif char in grey_char:
                    print(f"you are already eliminated the letter '{char}'")
                    flag=True
                    # break  # print only one condition
                    continue # print all conditions    
                else:
                    grey_char.update(grey_letter)
            

        if word != word_guess and not flag:
            history.append(word_guess)
            tries+=1
            continue
        if word == word_guess:
            print("game Over")
            print(history)
            break
        
        
            
    else:
        print(" you are out of tries ")
        print("you have been survived")
        
    
if __name__=="__main__":
    main()
    