
hoursWorked = 40
hourlyRate = 20.5 
weeklyPay = 0
if hoursWorked > 40:
    weeklyPay = 40 * hourlyRate + (hoursWorked - 40) * 1.5 * hourlyRate
else:
    weeklyPay = 40 * hourlyRate
print(f'Week\'s pay: {weeklyPay}\n\n')

#q2
i = 5
while i <=15:
    print(i)
    i += 1
i = 100
print('')
while i >= -10:
    print(i)
    i += -10
print('')
i = 2
while i < 1000000:
    print(i)
    i *= i
i = 100
print('')
i = 100
while i > 0:
    print(i)
    i -= 5
print('')

#q3
timeTableNumber = int(input("enter a number:\n"))
for i in range(1,11):
    print(f'{timeTableNumber} x {i} = {timeTableNumber * i}')
for i in range(1,10):
    print(str(i)*i)
#part c
#part i
positiveInteger = 0
while positiveInteger <= 1:
    inpt = input("enter a positive integer:\n")
    try:
        positiveInteger = int(inpt)
    except ValueError:
        positiveInteger = 0
        print('I said an integer you cappucino!!')
for i in range(positiveInteger,0,-1):
    print(positiveInteger)
    positiveInteger -= 1
# part ii
positiveInteger = 0
while positiveInteger <=1:
    inpt = input('Enter a positive integer')
    try:
        positiveInteger = int(inpt)
    except ValueError:
        print("What part of POSITIVE INTEGER isn't clicking squeeb?")
# part iii
positiveInteger = 0
while True:
    inpt = input("Number to skip: ")
    if inpt.isdigit():
        positiveInteger = int(inpt)
    if positiveInteger > 0 and positiveInteger < 50 and positiveInteger % 2 != 0:
        break
for i in range(1,50,2):
    if i == positiveInteger:
        continue
    print(f"Here's an odd number: {i}")
# Q3: Fizzbuzz
for i in range(1,101,1):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 ==0:
        output += "Buzz"
    if output == "":
        output = str(i)
    print(output)
# Q4 Power Table
posInt = 0
while posInt < 1:
    inpt = input("What number would you like to go up to? ")
    if inpt.isdigit():
        posInt = int(inpt)
print("Here's your table!\n")
print("{0:<3s} {1:^3s} {2:>3s}".format("number|","squared|","cubed"))
for i in range(1, posInt + 1):
    print("{0:<3d} {1:^3d} {2:>3d}".format(i, i * i, i * i * i))
# Q5 Letter Grade
score = -1
letterGrade = ""
while score < 0:
    inpt = input("enter score: ")
    if inpt.isdigit():
        score = int(inpt)
    else:
        continue
    if score > 87:
        letterGrade = 'A'
    elif score > 79:
        letterGrade = 'B'
    elif score > 66:
        letterGrade = 'C'
    elif score > 59:
        letterGrade = 'D'
    else:
        letterGrade = 'F'
    print(f"Letter Grade: {letterGrade}")
    inpt = input("Continue? y/[n]: ")
    if inpt.lower() == 'y':
        score = -1

# # Q5: books (I'm doing it with Youtube videos though since I've actually consumed a lot of those recently)


ytvids = [{'title': 'Eagles are turning people into horses', 'author': 'britannick', 'genre': 'Comedy'}, 
{'title': 'Escape From Tomorrow is a dumb exercise in misery','author': 'Jenny Nicholson', 'genre': 'Documentary'}, 
{'title': 'The last bronycon: a fandom autopsy','author': 'Jenny Nicholson', 'genre': 'Documentary'}, 
{'title': 'FizzBuzz: one simple interview question', 'author': 'Tom Scott', 'genre': 'Technology'}, 
{'title': 'Reptilia', 'author': 'The Strokes','genre': 'music'},
{'title': 'Tightrope walking cheat device', 'author': 'James Brunton', 'genre': 'Technology'},
{'title': 'UNHhhh ep 187 - Lying', 'author': 'WOWPresents', 'genre': 'Comedy'}, 
{'title': 'W.U.G', 'author': 'Chris Fleming', 'genre': 'Music'}, 
{'title': 'Welcome to the Internet', 'author': 'Bo Burnham', 'genre': 'Comedy'}]
# Quick tool to make generating the dictionary easier
# flag  = True
# while flag:
#     title = input("enter a title: ")
#     author = input("enter the creator: ")
#     genre = input("enter the genre: ")
#     if title == "" or author == "" or genre == "":
#         continue
#     ytvids.append({'title':title,'author':author,'genre':genre})
#     if input('continue? ') == 'n':
#         print(ytvids)
#         flag = False
for vid in ytvids:
    print(f"Title: {vid['title']}")
    print(f"Creator: {vid['author']}")
    print(f"Genre: {vid['genre']}\n\n")
inpt = input("enter a genre: ")
for vid in ytvids:
    if vid['genre'].lower() == inpt.lower():
        print("\nVideo:")
        print(f"Title: {vid['title']}")
        print(f"Creator: {vid['author']}")
        print(f"Genre: {vid['genre']}\n\n")