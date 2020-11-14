import random

def unreadable():
    upper_char=['A','B','C','D','E'];
    lower_char=['a','b','c','d','e'];
    special_char=['@','#','!','^','&'];
    return (random.choice(upper_char)+random.choice(lower_char)+str(random.randint(0,9))+random.choice(special_char)+random.choice(lower_char)+random.choice(upper_char)+random.choice(special_char)+str(random.randint(0,9)))

