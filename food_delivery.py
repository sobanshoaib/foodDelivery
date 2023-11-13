'''
Soban Shoaib
Food Delivery
'''



'''
food delivery, that sells the restaurants MacScams, Burger Prince, and Mary White
whichever location they select, the menu would be displayed and the cost

be displayed again. option to checkout will also appear
each menu would have the items with numbers. the person will click on a food, then it will say quantity how much. once it is done, the menu will

cost provided, along with calculations showing taxes

'''

def display_restaurants(symbol):
    '''
    Main menu that displayes restaurants
    '''
    print(symbol*50)
    print('Welcome to the Eat2Go Cashier. \nWhich restaurant would you like to order from?')
    print(symbol*50)
    print('1. MacRichie\n2. Burger Prince\n3. Mary White')
    limit = [1,2,3]
    
    isValid = False
    while not isValid:
        choose_restaurant = int(input('>'))
        if choose_restaurant in limit: # check if user input is one of 1,2,3
            isValid = True
        else:
            print('Please select number 1, 2, or 3') # keep asking until correctly put

    return choose_restaurant


def read_files():
    '''
    Read files from another file
    '''

    with open('macrichie.txt', 'r') as file:
        contents_mac = file.readlines()
    with open('burgerprince.txt', 'r') as file:
        contents_prince = file.readlines()
    with open('marywhite.txt', 'r') as file:
        contents_mary = file.readlines()

    return contents_mac, contents_prince, contents_mary


def option_one(file):
    '''
    Display the menu for restaurant 1 and select choice
    '''
    
    print('Menu for MacRichie:')
    print()
 
    for line in file:
        new = line.strip().split(',') # cut into pieces
        food = new[0]
        cost = new[1]
        print(f'{food:<15} = ${cost:^5}') # proper formatting

    food_choice = input('Select number you would like to order, or press q to quit: ')

    return food_choice

def option_one_subsection(choice, file):
    
    cost = [] # where all the costs will go

    for line in file:
        cut = line.strip().split('.', 1) # split the line
        if choice == cut[0]: # if the user choice matches the number of the menu item
            cut_two = cut[1].strip().split(',')
            money = float(cut_two[1])
            cost.append(money)

    return cost

def option_one_decision(first, options, file_one):
    
    isValid = False
    while not isValid:
            if first.lower() == 'q': # q to exit the program
                print('Goodbye!')
                isValid = True
            elif first in options:
                get = option_one_subsection(first, file_one) # the list which contains the corresponding price of the menu item
                print(get)
                isValid = True
            elif first not in options:
                first = input('please try again: ') # keep re-trying until appropriate option selected


def option_two(file):

    print('Menu for Burger Prince:')
    print()
 
    for line in file:
        new = line.strip().split(',')
        food = new[0]
        cost = new[1]
        print(f'{food:<17} = ${cost:^5}')

    food_choice = input('Select number you would like to order, or press q to quit: ')

    return food_choice

def option_two_subsection(choice, file):
    
    cost = [] # where all the costs will go

    for line in file:
        cut = line.strip().split('.', 1) # split the line
        if choice == cut[0]: # if the user choice matches the number of the menu item
            cut_two = cut[1].strip().split(',')
            money = float(cut_two[1])
            cost.append(money)

    return cost

def option_two_decision(second, options, file_two):

    isValidTwo = False
    while not isValidTwo:
        if second.lower() == 'q': # q to exit the program
            print('Peace out!')
            isValidTwo = True
        elif second in options:
            get_two = option_two_subsection(second, file_two) # the list which contains the corresponding price of the menu item
            print(get_two)
            isValidTwo = True
        elif second not in options:
            second = input('please try again: ') # keep re-trying until appropriate option selected

def option_three(file):
    
    print('Menu for Mary White:')
    print()
 
    for line in file:
        new = line.strip().split(',')
        food = new[0]
        cost = new[1]
        print(f'{food:<16} = ${cost:^5}')

    food_choice = input('Select number you would like to order, or press q to quit: ')

    return food_choice

def option_three_subsection(choice, file):
    
    cost = [] # where all the costs will go

    for line in file:
        cut = line.strip().split('.', 1) # split the line
        if choice == cut[0]: # if the user choice matches the number of the menu item
            cut_two = cut[1].strip().split(',')
            money = float(cut_two[1])
            cost.append(money)

    return cost

def option_three_decision(third, options, file_three):

    isValidThree = False
    while not isValidThree:
        if third.lower() == 'q': # q to exit the program
            print('See you next time!')
            isValidThree = True
        elif third in options:
            get_three = option_three_subsection(third, file_three) # the list which contains the corresponding price of the menu item
            print(get_three)
            isValidThree = True
        elif third not in options:
            third = input('please try again: ') # keep re-trying until appropriate option selected




def main():
    
    symbol = '*'
    restaurant_choice = display_restaurants(symbol)   
    files = read_files()
    options = ['1','2','3', '4', '5', 'q']

    if restaurant_choice == 1: # if the user select restaurant 1
        first = option_one(files[0])
        option_one_decision(first, options, files[0])

    elif restaurant_choice == 2:
        second = option_two(files[1])
        option_two_decision(second, options, files[1])

    elif restaurant_choice == 3:
        third = option_three(files[2])
        option_three_decision(third, options, files[2])


if __name__ == '__main__':
    main()