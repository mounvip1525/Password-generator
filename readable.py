import random

def readable():
    word_list=[]
    special_char=['@','#','!','^','&'];

    with open("randomwords.txt") as file:
        words=file.readlines()
        for word in words:
            if len(word)>4:
                chars=word.split('\n')
                word_list.append(chars[0].capitalize())
         
    return(random.choice(word_list)+random.choice(special_char)+str(random.randint(10,999)))


    