
"""
Identify data types:
99.9 float
"False" string
False boolean
'0' string
0 int
True bool
'True' string
[{}] list
{'a': []} dict

"""
"""
What data type would best represent:

A term or phrase typed into a search box? string
If a user is logged in? bool
A discount amount to apply to a user's shopping cart? float
Whether or not a coupon code is valid? true
An email address typed into a registration form? string
The price of a product? integer (in cents, floats are weird)
A Matrix? a list of lists
The email addresses collected from a registration form? list of strings
Information about applicants to Codeup's data science program? dictionary
"""
"""
'1' + 2: ERROR, can't add an int to a string

6%4: 2 (6/4 = 1 remainder 2)

type(6%4): int

type(type(6%4)): type

'3 + 4 is ' + 3 + 4: Error, can't add int to a string

0 < 0: False

'False' == False: False

True == 'True': False (string 'True' not the same as True)

5 >= -5: True

True or "42": True (True or anything is always true)

6 % 5: 1 (6/5 = 1 remainder 1)

5 < 4 and 1 == 1: False

'codeup' == 'codeup' and 'codeup' == 'Codeup': False 
(capital C not same as lowercase c)

4 >= 0 and 1 !== 1: Error if you type it like that
(should be !=) but False if you fix the syntax

6%3 == 0: True

5%2 != 0: True

[1] + 2: Error, can't add a nonlist to a list
with concat operation

[1] + [2]: [1,2]

[1] * 2: [1,1] (Can't add, but you can multiply!)

[1] * [2]: Error (Inverse of above, can add, can't
multiply lists)

[] + [] == []: True, concat of two empty lists
still an empty list (0+0=0)

{} + {}: Error, can't add dictionaries

"""
#q1
#takes a list of tuples (movie, daysRented)
#and prints their sum
def movieRental(rentals):
    sum = 0
    for r in rentals:
        sum += 3 * r[1]
        print(f"{r[0]}: {3* r[1]}")
    print(f"total: {sum}\n\n")
movieRental([("The Little Mermaid",3),
("Brother Bear", 5),
("Hercules",1)])

#q2
#totalPay takes a list of tuples ($/hr,hrs) and returns the total pay
def totalPay(timeCard):
    sumTotal = 0
    for t in timeCard:
        sumTotal += t[0] * t[1]
    return sumTotal
print(f"Total Pay: ${totalPay([(400,6),(380,4),(350,10)])}.00")

#q3
# curriculum contains all the courses and how many seats are left (capacity)
curriculum = {
'How Algebra Will Save Your Eye':{'startTime':8.0,'endTime':10.0,'capacity':10},
'Simlish':{'startTime':10.0,'endTime':12.0,'capacity':5},
'Interpretive Astrology':{ 'startTime':9.0,'endTime':11.0,'capacity':100},
'Aerobic Antiquing':{'startTime':7.0,'endTime':9,'capacity':3},
'Corporate Shilling':{'startTime':14.0,'endTime':18.0,'capacity':0}
}
# mySchedule is a dictionary with the class name as a key and a tuple of the start and end times represented as float values
# 0.0-24.0
mySchedule = {'How Algebra Will Save Your Eye':(8.0,10.0)}
# Schedule class
def scheduleClass(className, schedule):
    try:
        classInfo = curriculum[className]
    except KeyError:
        print(f'class {className} doesn\'t exist!')
        return schedule
    if classInfo['capacity'] <= 0:
        print("Unable to join! class full!")
        return schedule
    for s in schedule:
        if s == className:
            print(f'Already scheduled in class {s}')
            return schedule
        elif schedule[s][0] >= classInfo['startTime'] and schedule[s][0] < classInfo['endTime']:
            print(f'scheduling conflict! class {s} starts before {className} ends!')
            return schedule
        elif schedule[s][1] > classInfo['startTime'] and schedule[s][1] <= classInfo['endTime']:
            print(f'scheduling conflict! class {className} starts before {s} ends!')
            return schedule
    schedule[className] = (classInfo['startTime'],classInfo['endTime'])
    curriculum[className]['capacity'] -= 1
    return schedule
print(f"{mySchedule}\n\n")
mySchedule = scheduleClass('Simlish',mySchedule)
print(f"{mySchedule}\n\n")
mySchedule = scheduleClass('Interpretive Astrology',mySchedule)
print(f"{mySchedule}\n\n")
mySchedule = scheduleClass('Aerobic Antiquing',mySchedule)
print(f"{mySchedule}\n\n")
mySchedule = scheduleClass('Corporate Shilling', mySchedule)
print(f"{mySchedule}\n\n")
mySchedule = scheduleClass('Data Science', mySchedule)
print(f"{mySchedule}\n\n")
mySchedule = scheduleClass('Simlish',mySchedule)
print(f"{mySchedule}\n\n")
print(f"{curriculum}\n\n")

#q4
#Catalog of all the items in the store
#I didn't HAVE to make this but I WANTED to make this.
catalog = [
{'name':'Susan Sontag Camping Kit','price':105000},
{'name':'Saran Susan Sarandon Wrap','price':2350},
{'name':'BEANS','price':10},
{'name':'Scoopy Banoopy','price':10000000000},
{'name':'Anvil Brand Anvil','price':50000},
{'name':'Bachelor of Science in Computer Science for Woody Sims','price':1},
]
# list of dicts containing customers and their carts
# carts as represented as a list of tuples containing a reference 
# to the item and the quantity of items
customers = [
{'name':'Mark','cart':[(catalog[0],1),(catalog[2],1)], 'isPremium':False},
{'name':'Yuvia','cart':[(catalog[1],3)], 'isPremium':False},
{'name':'Rae','cart':[(catalog[3],1)], 'isPremium':True},
{'name':'Chris','cart':[(catalog[5],1)],'isPremium':False}
]
# check for customer takes a customer dictionary
# and returns True if they qualify for a discount
# otherwise it returns false
def checkForDiscount(customer):
    if customer['isPremium']:
        return True
    cartCount = len(customer['cart'])
    if cartCount > 1:
        return True
    elif cartCount > 0 and customer['cart'][0][1] > 1:
        return True
    else:
        return False

for c in customers:
    retStr = c['name']
    if checkForDiscount(c):
        retStr += ' gets a discount!'
    else:
        retStr += ' does not get a discount :('
    print(retStr)

username = 'codeup'
password = 'notastrongpassword'
#checks if PW is 5 or more characters
pwIsFiveOrMoreChars = len(password) > 4
#checks if username is less than 20 characters
usrLessThanTwentyChars = len(username) < 21
#checks username is not equal to password
#  & vice versa
pwIsNotUsr = username != password
import string
# function to check if first and last are not white space
def noWSFirstOrLast(str):
    if str[0] != string.whitespace and str[len(str)-1] != string.whitespace:
        return True
    else:
        return False
firstAndLastNotWS = noWSFirstOrLast(username) and noWSFirstOrLast(password)
print(f"password is >= 5 chars: {pwIsFiveOrMoreChars}")
print(f"username is <= 20 chars: {usrLessThanTwentyChars}")
print(f"Password is not username: {pwIsNotUsr}")
print(f"First and last of username and password != whitespace: {firstAndLastNotWS}")