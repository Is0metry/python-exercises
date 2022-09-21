from function_exercises import calculate_tip,handle_commas
import itertools,json, re

#q1
print(f'Bill: $123.85, tip %: 28.175, total: ${calculate_tip(123.85,28.175)}')
#q2 part A
iterations = []
for iterate in itertools.product('abc',[1,2,3]):
    iterations.append(iterate)
print(f'no. of combinations of digits: {len(iterations)}.')

#part b
iterations = []
for iterate in itertools.combinations('abcd',2):
    iterations.append(iterate)
print(f'No. of combinations: {len(iterations)}.')
#part C
iterations = []
for iterate in itertools.permutations('abcd',2):
    iterations.append(iterate)
print(f'No. of permutations: {len(iterations)}.')
# Q3
data = json.load(open('profiles.json','r',encoding='utf-8'))
total_users = len(data)
active_users = 0
inactive_users = 0
for d in data:
    if d['isActive']:
        active_users+=1
    else:
        inactive_users+=1
grand_total = 0
max_balance = (0,0)
min_balance = (0,10000000)
for d in enumerate(data):
    balance = handle_commas(d[1]['balance'][1:])
    if balance > max_balance[1]:
        max_balance = (d[0],balance)
    if balance < min_balance[1]:
        min_balance = (d[0],balance)
    grand_total += balance
print(f'Minimum Balance of {min_balance[1]} held by {data[min_balance[0]]["name"]}.')
print(f'Maximum Balance of {max_balance[1]} held by {data[max_balance[0]]["name"]}.')
avg_balance = grand_total / total_users

favorite_fruits = {}
for d in data:
    if d['favoriteFruit'] not in favorite_fruits.keys():
        favorite_fruits[d['favoriteFruit']] = 1
    else:
        favorite_fruits[d['favoriteFruit']] += 1
most_favorite_fruit = max(favorite_fruits, key=favorite_fruits.get)
least_favorite_fruit = min(favorite_fruits, key=favorite_fruits.get)

unread_messages = {}
for d in data:
    name = d['name']
    unread = re.search(r'\d+',d['greeting'])
    if unread is not None:
        unread_messages[name] = int(unread.group())
for u in unread_messages.keys():
    print(f'User {u} has {unread_messages[u]} unread messages')