# Q1 is_two() function takes an Any-type argument and returns True if it is equal to the integer 2
# or the string '2'
is_two = lambda numb: numb == 2 or numb == '2'
if __name__ == '__main__':
    print('is_two tests:')
    print(is_two(2))
    print(is_two(2))
    print(is_two('2'))
    print(is_two('1'))
    print(is_two(1))
    print('')

#Q2 is_vowel function takes a string of a single character
# converts it to lower case, and returns True if the character is a vowel. #
# Otherwise, it returns False
is_vowel = lambda string: string.lower() in ('a','e','i','o','u')
if __name__ == '__main__':
    print('is_vowel tests:')
    print(f'input: "A", output: {is_vowel("A")}')
    print(f'input: "e", output: {is_vowel("e")}')
    print(f'input: "I", output: {is_vowel("I")}')
    print(f'input: "T", output: {is_vowel("T")}')
    print('')

#Q3 is_consonant function takes a string of a single character and returns the inverse of is_vowel
# i.e. if the string is a consonant, it returns True, otherwise it returns False
is_consonant = lambda con: not is_vowel(con)
if __name__ == '__main__':
    print('is_consonant tests:')
    print(is_consonant('s'))
    print(is_consonant('T'))
    print(is_consonant('I'))
    print(is_consonant('rt'))
    print('')

#Q5 cap_if_consonant takes a string that is a word and returns a string
# if the first letter of the word is a consonant, it capitalizes it
def cap_if_consonant(word):
    if is_consonant(word[0]):
        word = word[0].upper() + word[1:]
    return word
if __name__ == '__main__':
    print('cap_if_consonant testing')
    print(f"word: tentative, result: {cap_if_consonant('tentative')}")
    print(f'word: opossum, result: {cap_if_consonant("opossum")}')

#Q5 Calculate tip function takes a bill amount and a tip percentage (between 0 and 1)
# and returns the total bill with tip included
def calculate_tip(bill,tip):
    return round((1+tip) * bill,2)
if __name__ == '__main__':
    print('calculate_tip testing')
    print(f'input: (100,.25), output: {calculate_tip(100,.25):1.2f}')
    print('')
#Q6 apply_discount function takes the subtotal of a transaction and the discount to be applied
#(between 0  and 1) and returns the total minus the discount.
def apply_discount(total, discount):
    return total - (total * discount)
if __name__ == '__main__':
    print('apply_discount testing')
    print(f'input: (100,.25) output:{apply_discount(100,.25):1.2f}')

#Q7 handle_commas takes a string of numbers with commas and returns the number as a float
#if there is a decimal place, or as an integer if there is not

def handle_commas(commaNum):
    # the string that will be converted to the output
    retStr = ""
    # the flag that tracks the decimal place
    decPointFlag = False
    for c in commaNum:
        #check if c is a decimal place and that one has not already appeared in the string
        if c == '.' and not decPointFlag:
            #set the flag to true to indicate a decimal place has been added
            decPointFlag = True
            #adds the character to the string
            retStr += c
        #checks if the character is a digit and, if it is, adds it to the string
        elif c.isdigit():
            retStr += c
        # if the character is a comma, skip over it
        elif c == ',':
            continue
        else:
            #throws an error if the number isn't valid
            raise ValueError("Not a valid number")
    # if the number contains a decimal point, returns it as a float
    if decPointFlag:
        return float(retStr)
    # otherwise returns it as an int
    else:
        return int(retStr)
if __name__ == '__main__':
    print("handle_commas testing:")
    print(f'input: 100,000,000 , output: {handle_commas("100,000,000")}')
    print(f'input: 100,000,000.02575 , output: {handle_commas("100,000,000.02575")}')
#doing this here for clarity
    test3 = 0
    try:
        test3 = handle_commas('100,000,k00')
    except ValueError:
        test3 = "Error"
    print(f'input: 100,000,k00 , output: {test3}')

#Q8 get_letter_grade takes a score and returns the appropriate letter grade
def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >=80:
        return 'B'
    elif score >=70:
        return 'C'
    elif score >=60:
        return 'D'
    else:
        return 'F'
if __name__ == '__main__':
    print("get_letter_grade testing")
    print(f"input: 90, output: {get_letter_grade(90)}")
    print(f"input: 85, output: {get_letter_grade(85)}")
    print(f"input: 72, output: {get_letter_grade(72)}")
    print(f"input: 60, output: {get_letter_grade(60)}")
    print(f"input: 40, output: {get_letter_grade(40)}")

#Q9 remove_vowels takes in a string and returns that string without the vowels
def remove_vowels(sentence):
    #initializes return string
    retStr = ''
    #iterates over the string
    for s in sentence:
        # if the string is a consonant, adds it to the return_string
        if is_consonant(s):
            retStr += s
    return retStr
if __name__ == '__main__':
    print("remove_vowel testing")
    print(f'input: Thanks for the memories, output: {remove_vowels("Thanks for the Memories")}')
    print(f'input: aeiou, output: {remove_vowels("aeiou")}')
    print(f'input: abcdefghijklmnopqrstuvwxyz, output: {remove_vowels("abcdefghijklmnopqrstuvwxyz")}')
#Q10 normalize_name takes in an arbitrary string and returns a snake_case/normalized
#version of that string
def normalize_name(name):
    #initialize return string
    retStr = ""
    #checks that the name has started in order to check for whitespace
    nameStart = False
    #strips any white space off the beginning and end
    name = name.strip()
    for n in name:
        #if n is a space AND there has been at least one alphanumeric
        #character has been noted before this character, it adds
        # an underscore in place of the space
        if n == ' ' and nameStart:
            retStr += '_'
        # if n is a digit or an underscore, adds it to the return string
        elif n.isdigit() or n == '_':
            retStr += n
        # if n is an alpha character, adds its lower-case version to the string
        elif n.isalpha():
            retStr += n.lower()
    return retStr
if __name__ == '__main__':
    print('testing for normalize_name')
    print(f'input: Normalize Name, output:{normalize_name("Normalize Name")}')
    print(f'input: Woody is the best!, output:{normalize_name("Woody is the best!")}')
    print(f'input: Ive been dreaming of colours, output:{normalize_name("Ive been dreaming of colors")}')
    print(f'input: % completed, output:{normalize_name("% completed")}\n\n')

#Q11 cumulative_sum takes a list and returns the cumulative sum at each number of the array
def cumulative_sum(arr):
    #initializes return value
    cumSum = 0
    for a in range(0,len(arr)):
        #adds a to the cumulative sum
        cumSum += arr[a]
        #place3s the cumulative sum in arr[a]
        arr[a] = cumSum
    return arr
if __name__ == '__main__':
    print('testing for cumulative_sum')
    print(f'input: [1,1,1], output:{cumulative_sum([1,1,1])}')
    print(f'input: [1,2,3,4], output:{cumulative_sum([1,2,3,4])}')
    print(f'input: [10,-9,8,-7,6,6,6], output:{cumulative_sum([10,-9,8,-7,6,6,6])}')
#Bonus 1
def twelveTo24(time):
    time = time.strip()
    timeOfDay = 0 if time[time.index('m')-1] == 'a' else 12
    indexOfColon = time.index(':')
    hours = int(time[:indexOfColon])
    minutes = time[indexOfColon+1:indexOfColon+3]
    return str(timeOfDay + hours)+ ':' + minutes
if __name__ == '__main__':
    print('testing for twelveTo24')
    print(f'input: 10:54am, output: {twelveTo24("10:54am")}')
    print(f'input: 4:00pm, output: {twelveTo24("4:00pm")}')
    print(f'input: 8:48pm, output: {twelveTo24("8:00pm")}')
# Bonus 2
def col_index(column):
    if len(column) == 1:
        return ord(column[0]) - 64
    else:
        return 26 ** (len(column)-1) * (ord(column[0]) - 64) + col_index(column[1:])
if __name__ == '__main__':
    print('basic testing for excel_col_no')
    print(f'input: A, output:{col_index("A")}')
    print(f'input: AA, output:{col_index("AA")}')
    print(f'input: ZZ, output:{col_index("ZZ")}')
    print(f'input: AAA, output:{col_index("AAA")}')
    print(f'input: ABA, output:{col_index("ABA")}')
    print(f'input: ZZZ, output:{col_index("ZZZ")}')
    comp_test_flag = False # set to True to view output of comprehensive testing
    if comp_test_flag:
        print('comprehensive testing for excel_col_no')
        for i in range(0,26):
            print(f'input: {chr(i+65)}, output:{col_index(chr(i+65))}')
        for i in range(0,26):
            for j in range(0,26):
                print(f'input: {chr(i+65)+chr(j+65)}, output:{col_index(chr(i+65)+chr(j+65))}')
        for i in range(0,26):
            for j in range(0,26):
                for k in range(0,26):
                    print(f'input: {chr(i+65) + chr(j+65) + chr(k+65)}, output:{col_index(chr(i+65) + chr(j+65) + chr(k+65))}')
