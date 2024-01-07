'''
Soban Shoaib
Food Delivery
'''





from money_adding import Money



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

def cost_care_one(choice, file):
    '''
    Whatver a menu item a person would select, here the cost will be taken care of, and then be displayed later
    '''
    
    cost = '' # where all the costs will go

    for line in file:
        cut = line.strip().split('.', 1) # split the line
        if choice == cut[0]: # if the user choice matches the number of the menu item
            cut_two = cut[1].strip().split(',')
            money = float(cut_two[1])
            cost += str(money)

    return float(cost)

def option_one_decision(first, options, file_one, cart):
    '''
    Corresponding result to selected option from menu item
    '''
    
    isValid = False
    while not isValid:
        if first.lower() == 'q': # q to exit the program
            print('Goodbye!')
            isValid = True
        elif first in options:
            cost_of_item_first = cost_care_one(first, file_one) # the list which contains the corresponding price of the menu item
            isValid = True
        elif first not in options:
            first = input('please try again: ') # keep re-trying until appropriate option selected

    quantity = int(input('Enter the amount of this item you would like: '))
    cost_after_amount = cost_of_item_first * quantity
    print()
    print(f'This equates to ${cost_after_amount:0.2f}. Please select one of the following options.')
    cart.adding(cost_after_amount)


    choices= [1, 'c', 'q'] 
    print('To continue ordering please select 1 to go to the list of retaurants. To finish ordering and go to checkout please select c. To quit altogether please select q')
    
    isValid = False
    while not isValid:
        select = input('>')        
        if select == '1':
            isValid = True
            return 'retry'
        elif select == 'c': #goes to checkout
            #print(cart)
            shopping_cart(cart)
            isValid = True
        elif select.lower() == choices[2]:
            print('Goodbye')
            isValid = True
        else:
            print('Please try again and select the appropriate choice')

    return cost_after_amount


def option_two(file):
    '''
    Display the menu for restaurant 2 and select choice
    '''

    print('Menu for Burger Prince:')
    print()
 
    for line in file:
        new = line.strip().split(',') # cut into pieces
        food = new[0]
        cost = new[1]
        print(f'{food:<17} = ${cost:^5}') # proper formatting

    food_choice = input('Select number you would like to order, or press q to quit: ')

    return food_choice

def cost_care_two(choice, file):
    '''
    Whatver a menu item a person would select, here the cost will be taken care of, and then be displayed later
    '''
    
    cost = '' # where all the costs will go

    for line in file:
        cut = line.strip().split('.', 1) # split the line
        if choice == cut[0]: # if the user choice matches the number of the menu item
            cut_two = cut[1].strip().split(',')
            money = float(cut_two[1])
            cost += str(money)

    return float(cost)

def option_two_decision(second, options, file_two, cart):
    '''
    Corresponding result to selected option from menu item
    '''

    isValidTwo = False
    while not isValidTwo:
        if second.lower() == 'q': # q to exit the program
            print('Peace out!')
            isValidTwo = True
        elif second in options:
            cost_of_item_second = cost_care_two(second, file_two) # the list which contains the corresponding price of the menu item

            isValidTwo = True
        elif second not in options:
            second = input('please try again: ') # keep re-trying until appropriate option selected

    quantity = int(input('Enter the amount of this item you would like: '))
    cost_after_amount = cost_of_item_second * quantity
    print()
    print(f'This equates to ${cost_after_amount:.2f}. Please select one of the following options.')
    cart.adding(cost_after_amount)

    choices= [1, 'c', 'q'] 
    print('To continue ordering please select 1 to go to the list of retaurants. To finish ordering and go to checkout please select c. To quit altogether please select q')
    
    isValid = False
    while not isValid:
        select = input('>')      
        if select == '1': #back to main menu           
            isValid = True
            return 'retry'
        elif select == 'c':
            #print(cart)
            shopping_cart(cart)
            isValid = True
        elif select.lower() == choices[2]:
            print('Goodbye')
            isValid = True
        else:
            print('Please try again and select the appropriate choice')

    return cost_after_amount



def option_three(file):
    '''
    Display the menu for restuarant 3 and select choice
    '''
    
    print('Menu for Mary White:')
    print()
 
    for line in file:
        new = line.strip().split(',') # cut into pieces
        food = new[0]
        cost = new[1]
        print(f'{food:<16} = ${cost:^5}') # proper formatting

    food_choice = input('Select number you would like to order, or press q to quit: ')

    return food_choice

def cost_care_three(choice, file):
    '''
    Whatver a menu item a person would select, here the cost will be taken care of, and then be displayed later
    '''
    cost = '' # where all the costs will go

    for line in file:
        cut = line.strip().split('.', 1) # split the line
        if choice == cut[0]: # if the user choice matches the number of the menu item
            cut_two = cut[1].strip().split(',')
            money = float(cut_two[1])
            cost += str(money)

    return float(cost)

def option_three_decision(third, options, file_three, cart):
    '''
    Corresponding result to selected option from menu item
    '''

    isValidThree = False
    while not isValidThree:
        if third.lower() == 'q': # q to exit the program
            print('See you next time!')
            isValidThree = True
        elif third in options:
            cost_of_item = cost_care_three(third, file_three) # the list which contains the corresponding price of the menu item            
            isValidThree = True
        elif third not in options:
            third = input('please try again: ') # keep re-trying until appropriate option selected
    quantity = int(input('Enter the amount of this item you would like: '))
    cost_after_amount = cost_of_item * quantity
    print()
    print(f'This equates to ${cost_after_amount}. Please select one of the following options.')
    cart.adding(cost_after_amount)
    
    choices= [1, 'c', 'q'] 
    print('To continue ordering please select 1 to go to the list of retaurants. To finish ordering and go to checkout please select c. To quit altogether please select q')
    
    isValid = False
    while not isValid:
        select = input('>')
        if select == '1':
            isValid = True
            return 'retry'
        elif select == 'c':
            #print(cart)
            shopping_cart(cart)
            isValid = True
        elif select.lower() == choices[2]:
            print('Goodbye')
            isValid = True
        else:
            print('Please try again and select the appropriate choice')


    return cost_after_amount


def shopping_cart(cart):
    
    gst = 0.05
    total = (cart.cost * gst) + cart.cost


    print(f'Your subtotal comes out to {cart}.')
    print(f'After GST, your final total is {total:.2f}')
    print("Thank you for ordering with Eat2Go! We hope to see you again soon!")


def main():
    
    cart = Money()
    valid = False
    symbol = '*'
    restaurant_choice = display_restaurants(symbol) 

    while not valid:  
        files = read_files()
        options = ['1','2','3', '4', '5', 'q']
        cost_first = cost_second = cost_third = None

        if restaurant_choice == 1: # if the user select restaurant 1
            first = option_one(files[0])
            if first == 'q':
                break
            cost_first = option_one_decision(first, options, files[0], cart)
            valid = True


        elif restaurant_choice == 2: # if the user selects restaurant 2
            second = option_two(files[1])
            if second == 'q':
                break
            cost_second = option_two_decision(second, options, files[1], cart)
            valid = True


        elif restaurant_choice == 3: # if the user selects restuarant 3
            third = option_three(files[2])
            if third == 'q':
                break
            cost_third = option_three_decision(third, options, files[2], cart)
            valid = True

        if cost_first == 'retry' or cost_second == 'retry' or cost_third == 'retry':
            valid = False

    
if __name__ == '__main__':
    main()




