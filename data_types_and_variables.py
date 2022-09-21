from string import whitespace


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
def movie_rental(rentals):
    """takes a list of tuples (movie, daysRented)and prints their sum"""
    total_sum = 0
    for r in rentals:
        total_sum += 3 * r[1]
        print(f"{r[0]}: {3* r[1]}")
    print(f"total: {total_sum}\n\n")
movie_rental([("The Little Mermaid",3),
("Brother Bear", 5),
("Hercules",1)])

#q2
#totalPay takes a list of tuples ($/hr,hrs) and returns the total pay
def total_pay(time_card):
    '''totalPay takes a list of tuples ($/hr,hrs) and returns the total pay'''
    sum_total = 0
    for t in time_card:
        sum_total += t[0] * t[1]
    return sum_total
print(f"Total Pay: ${total_pay([(400,6),(380,4),(350,10)])}.00")

#q3
# curriculum contains all the courses and how many seats are left (capacity)
curriculum = {
'How Algebra Will Save Your Eye':{'start_time':8.0,'end_time':10.0,'capacity':10},
'Simlish':{'start_time':10.0,'end_time':12.0,'capacity':5},
'Interpretive Astrology':{ 'start_time':9.0,'end_time':11.0,'capacity':100},
'Aerobic Antiquing':{'start_time':7.0,'end_time':9,'capacity':3},
'Corporate Shilling':{'start_time':14.0,'end_time':18.0,'capacity':0}
}
# mySchedule is a dictionary with the class name as a key 
# and a tuple of the start and end times represented as float values
# 0.0-24.0
my_schedule = {'How Algebra Will Save Your Eye':(8.0,10.0)}
# Schedule class
def schedule_class(class_name, schedule):
    """Schedule class takes a class name and the student's current schedule.
    If they are able to take the class, it returns their new schedule
    and decriments the class' capacity in 'curriculum.' Otherwise
    it prints an error"""
    try:
        class_info = curriculum[class_name]
    except KeyError:
        print(f'class {class_name} doesn\'t exist!')
        return schedule
    if class_info['capacity'] <= 0:
        print("Unable to join! class full!")
        return schedule
    for s in schedule:
        if s == class_name:
            print(f'Already scheduled in class {s}')
            return schedule
        elif schedule[s][0] >= class_info['start_time'] and schedule[s][0] < class_info['end_time']:
            print(f'scheduling conflict! class {s} starts before {class_name} ends!')
            return schedule
        elif schedule[s][1] > class_info['start_time'] and schedule[s][1] <= class_info['end_time']:
            print(f'scheduling conflict! class {class_name} starts before {s} ends!')
            return schedule
    schedule[class_name] = (class_info['start_time'],class_info['end_time'])
    curriculum[class_name]['capacity'] -= 1
    return schedule
print(f"{my_schedule}\n\n")
my_schedule = schedule_class('Simlish',my_schedule)
print(f"{my_schedule}\n\n")
my_schedule = schedule_class('Interpretive Astrology',my_schedule)
print(f"{my_schedule}\n\n")
my_schedule = schedule_class('Aerobic Antiquing',my_schedule)
print(f"{my_schedule}\n\n")
my_schedule = schedule_class('Corporate Shilling', my_schedule)
print(f"{my_schedule}\n\n")
my_schedule = schedule_class('Data Science', my_schedule)
print(f"{my_schedule}\n\n")
my_schedule = schedule_class('Simlish',my_schedule)
print(f"{my_schedule}\n\n")
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
def check_for_discount(customer):
    if customer['isPremium']:
        return True
    cart_count = len(customer['cart'])
    if cart_count > 1:
        return True
    elif cart_count > 0 and customer['cart'][0][1] > 1:
        return True
    else:
        return False

for c in customers:
    ret_str = c['name']
    if check_for_discount(c):
        ret_str += ' gets a discount!'
    else:
        ret_str += ' does not get a discount :('
    print(ret_str)

username = 'codeup'
password = 'notastrongpassword'
#checks if PW is 5 or more characters
PW_IS_FIVE_OR_MORE_CHARS = len(password) > 4
#checks if username is less than 20 characters
USR_LESS_THAN_TWENTY_CHARS = len(username) < 21
#checks username is not equal to password
#  & vice versa
PW_IS_NOT_USR = username != password
def no_ws_first_or_last(string_to_check):
    '''function to check if first and last are not white space'''
    if string_to_check[0] != whitespace and \
        string_to_check[len(string_to_check)-1] != whitespace:
        return True
    else:
        return False
FIRST_AND_LAST_NOT_WS = no_ws_first_or_last(username) \
    and no_ws_first_or_last(password)
print(f"password is >= 5 chars: {PW_IS_FIVE_OR_MORE_CHARS}")
print(f"username is <= 20 chars: {USR_LESS_THAN_TWENTY_CHARS}")
print(f"Password is not username: {PW_IS_NOT_USR}")
print(f"First and last of username and password != whitespace: {FIRST_AND_LAST_NOT_WS}")
