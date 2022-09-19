#1.a
Today = 'Tuesday'

if Today == 'Monday':
    print ('Today is monday')
else:
    print('today is not monday')
    
#1.b
Today = 'Saturday'

if Today == 'Saturday' or Today == 'Sunday':
    print ('Today is a weekend')
else:
    print('today is a weekday')
   
#1.c
hours_worked = 45
hourly_rate = 25

if hours_worked_week > 40:
    print(hourly_rate * (hours_worked +((hours_worked-40)*1.5)))
else:
    print(hourly_rate* hours_worked)
    
#2.a
i = 5
while i <= 15:
    print(i)
    i +=1
    
i = 0
while i <= 100:
    print(i)
    i += 2
    
i = 100
while i >= -10:
    print(i)
    i -= 5
    
i = 2
while i <= 1000000:
    print(i)
    i **= 2
    
i = 100
while i >= 1:
    print(i)
    i -= 5

#2.b.i.
n = int(input("input a number"))
for i in range(1,11):
    print(n,'x',i,'=',n*i)
    
#2.b.ii.
for i in range(10):
    print(str(i)*i)

#2.c.
def get_odd_number_between_1_and_50():
    while True:
        user_number = input("Please input a number between 1 and 50: \n")

        if user_number.isdigit():
            user_number = int(user_number)

            large_enough = user_number > 1
            small_enough = user_number < 50
            odd = user_number % 2 != 0

            if large_enough and small_enough and odd:
                break
            else:
                print("Your input must be less than 50 and odd and greater than: 1\n")
        else:
            print("Your input must be numerals.\n")

    return user_number

user_number = get_odd_number_between_1_and_50()

print(f"Number to skip is: {user_number}")
print() # prints an extra new line

for i in range(1, 50, 2):
    if i == user_number:
        print(f"Yikes! Skipping number: {i}")
        continue
    print(f"Here is an odd number: {i}")
    
#3
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    if number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
        
#4.
def square(i):
    return i*i
def cube(i):
    return i*i*i
  
def main():
    start = 1
    end=int(input("What number would you like to go up to? "))
    
    
    print("======\t\t=====\t\t=====")
    print("Number\t\tSquare\t\tCubed")
    print("======\t\t=====\t\t=====")
      
    for i in range(start,end+1):
        print(i,"\t\t",square(i),"\t\t",cube(i))
        
    while True:
        a = input("Do you want to continue? yes/no? ")
        if a=="yes":
            print("Okay, will continue!")
            continue
        elif a=="no":
            print("Okay, will stop!")
            break
        else:
            print("Enter either yes/no")
main()

        
#5.
print('enter a grade from 0 to 100')
number = input()
if int(number) >= 88:
     print('A')
elif int(number) >= 80 and int(number) <= 87:
    print('B')
elif int(number) >= 67 and int(number) <= 79:
    print('C')
elif int(number) >= 60 and int(number) <= 66:
    print('D')
else:
    print('F')
    
#6.
books = [
    {'title': 'Stormlight Archive', 'author': 'Brandon Sanderson','genre': 'Fantasy'},
    {'title': 'The Foundation', 'author': 'Isaac Asimov','genre': 'Sci-Fi'},
    {'title': '1632', 'author': 'Eric Flint','genre': 'Historical Fiction'}
]
book_genres = input('Enter a genre')
completed_books = [book for book in books if book['genre'] == book_genres]
for book in completed_books:
    print('---')
    print('title: ' + book['title'])
    print('author: ' + book['author'])
    print('genre: ' + book['genre'])