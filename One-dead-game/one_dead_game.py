import random
import time


def count_dead(number,guess_num):
    dead =0
    injured=0
    # count dead, injured
    for i in range(len(number)):
        if number[i] == guess_num[i]:
            dead +=1
        if number[i] in guess_num:
            injured+=1
    return dead,injured-dead
    

def check_condition(guess_num,number):
    if guess_num == 'show':
        return number
    if guess_num.isalpha():
        return "only number are allowed"
            
    if len(guess_num)!=4:
        return "number must be 4 characters"
            
    if len(set(guess_num)) < len(guess_num):
        return "duplicate is not allowed"
    
def generate_number():
    while True:
    
        num = random.randrange(1000,9999)
        random_number =str(num)
    
        if len(set(random_number)) < len(random_number):
            
            continue
        else:
            break
    return random_number
# num = random.randrange(1000,9999)
#     random_number =str(num)
    
#     if len(set(random_number)) < len(random_number):
#           generate_number()
#     else:
#         return random_number
        
# def count_injured(number,guess_num):
#     injured=0
#     # for num in number:
#     #     for guess in guess_num:
#     #         if num == guess:
#     #             injured+=1
                
#     # second method
#     for num in number:
#         if num in guess_num:
#             injured+=1
#     return injured


def main():
    number =generate_number()
    history=[]
    # time_now=time.ctime(time.time())
    # start_time=time.strptime("%H:%M:%S",time_now)
    while True:
        # print(number)
        # print(start_time)
        guess_num=input("enter number  ")
        condition=check_condition(guess_num,number)
        if condition is not None:
            print(condition)
            continue
        dead,injured=count_dead(number,guess_num)
        history.append(guess_num)
        if dead == 4:
            print(f"you have completed game in {len(history)} attempts")
            print(history)
            break
        else:
            print(f"dead={dead}, injured={injured}")
    # end_time=time.time()-start_time
    # seconds=time.strftime("%H:%M:%S",end_time)
    # print(seconds)
    # print(end_time)
    # minute=end_time%60
    
    # print(f"00:{minute:02}:{end_time:02}")
    
    
            
if __name__=="__main__":
    main()