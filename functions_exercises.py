#1.
def is_two(x):
    if x == 2 or x == '2':
        return True
    else:
        return False

#2.
def is_vowel(x):
    if x== 'a' or x== 'e' or x == 'i' or x== 'o' or x== 'u':
        return True
    else:
        return False

#3.
def is_consonant(x):
    if not x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        return True
    else:
        return False
        
#4.
def is_a_word(x):
    if not x == 'a%' or x == 'e%' or x == 'i%' or x == 'o%' or x == 'u%':
        return x.capitalize()
    else:
        return x
        
#5.
def calculate_tip(x, y):
    return x+(x * (y/100))
    
#6.
def apply_discount(x, y):
    return x-(x * (y/100))
    
#7.
def handle_commas(x):
     return x.replace(',','')
     
#8.
def get_letter_grade(x):
    if x < 60:
        print('your grade is an F')
    elif x >=60 and x <=69:
        print('your grade is a D')
    elif x >=70 and x <=79:
        print('your score is a C')
    elif x >=80 and x <=89:
        print('your score is a B')
    elif x >=90 and x<=100:
        print('your grade is an A')
    else:
        print('Error: you have not entered a number between 0 and 100.')
    return x
    
#9.
def remove_vowels(n):
    for i in "aeiouAEIOU":
        n = n.replace(i,"")
    return n
    
#10.
def normalize_name(n):
    for i in ' ':
        n = n.replace(i,'_')
        n = n.lower()
        n = n.strip()
    return n
    
#11.
def cumulative_sum(n):
    total = 0
    for x in n:
        total += x
        yield total