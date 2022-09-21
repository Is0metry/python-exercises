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
totalUsers = len(data)
activeUsers = 0
inactiveUsers = 0
for d in data:
    if d['isActive']:
        activeUsers+=1
    else:
        inactiveUsers+=1
grandTotal = 0
maxBalance = 0
minBalance = 0
for d in data:
    balance = handle_commas(d['balance'][1:])
    if balance > maxBalance:
        maxBalance = balance
    if balance < minBalance:
        minBalance = balance
    grandTotal += balance
avgBalance = grandTotal / totalUsers

favoriteFruits = {}
for d in data:
    if d.get('favoriteFruit') not in favoriteFruits.keys():
        favoriteFruits[d['favoriteFruit']] = 1
    else:
        favoriteFruits[d['favoriteFruit']] += 1
mostFavoriteFruit = max(favoriteFruits, key=favoriteFruits.get)
leastFavoriteFruit = min(favoriteFruits, key=favoriteFruits.get)

unreadMessages = {}
for d in data:
  name = d['name']
  unread = re.search(r'\d+',d['greeting'])
  if unread is not None:
    unreadMessages[name] = int(unread.group())
for u in unreadMessages.keys():
    print(f'User {u} has {unreadMessages[u]} unread messages')