def account():
    """
    -asks the users to create an account or login,if the account is already created

    Returns: a message indicating the result of the account

    """
    global username # using global variable so that a particular username can be used throughout the program

    while True:
        choice = input('Press 1 for the creation of an account and 2 for logging in to an account: ')

        with open('datas.txt', 'a+') as f:
            f.seek(0)
            x = f.readlines()

        if choice == '1':
            f_name = input('Enter your first name: ')
            l_name = input('Enter your last name: ')
            while True:
                try:
                    username = input('Enter your username: ')
                    # Strip newlines from lines and check if username exists
                    if any(username == line.split(',')[0] for line in x):
                        print('Username already exists!')
                    elif username == '':
                        print('please enter username')
                    else:
                      while True:
                        password = input('Enter your password: ')
                        if len(password) != 8:
                            print("Password must be exactly 8 characters.")
                        else:
                            with open('datas.txt', 'a') as f:
                                f.write(username + ',' + password + '\n')
                            print('Account creation successful.')
                            break
                      return
                except Exception as e:
                    print(type(e), ':', e)


        elif choice == '2':
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            if any(username == line.split(',')[0] and password == line.split(',')[1].strip() for line in x):
                print('You are successfully logged into your account.')
                return  # Exit after successful login
            else:
                print('Invalid username or password, please try again.')
        else:
            print('Invalid choice, please try again.')


with open('onlineshopping.txt', 'w+') as f:
    f.write('WELCOME TO THE GLAMOUR!!')  # writing in a file "online shopping "
    f.write('\n@The globally ensured skin care line')
    f.write('\nManage your skin care routine with us')
    f.write('\nWe have come up with a great deal of ensured products to make your skin care easier!!')
    f.write('\n\nOUR MAIN DEAL ITEMS')
    f.write('\nCleanser\tRs 650\nMoisturizer\tRs 450\nEye cream\tRs 350\nSerum\tRs 500\nToner\tRs 795\nSunscreen\tRs '
            '900\nMakeup remover\tRs 660\nAcne treatment\tRs 440\nLotion\tRs 630')
    f.seek(0)
    x = f.read()  # reads the whole file "online shopping"
    y=x.lower()
    print(x)  # prints the whole file on the console

products_list=[{'product':'cleanser','price':650},
                 {'product':'moisturizer','price':450},
                 {'product':'eye cream','price':350},
                 {'product':'serum','price':500},
                 {'product':'toner','price':795},
                 {'product':'sunscreen','price':900},
                 {'product':'makeup remover','price':660},
                 {'product':'acne treatment','price':440},
                 {'product':'lotion','price':630}]  # dictionaries enclosed in list so as to access easily

shopping_cart = {}  # creating it to add the products in it.


def add_to_cart():
    """ asks the users to add product in the cart from the given product list

    Input: string.

    Returns : adds products in the cart."""
    while True:
      try:
        product = input("\nEnter a product (or type 'done') to finish):")# make sure to write the first letter of the product 'small' otherwise it will display 'product not found' message.
        if product.lower() == 'done':
            break
        with open('onlineshopping.txt', 'w+') as f:
            if product in y:  # checking if the user-entered product is in the product list or not.
               quantity=int(input('How many?'))
               shopping_cart[product]=quantity  # adding it in the empty dictionary,keeping the product as value and quantity as key
            else:
               print(f'\n{product} NOT IN OUT PRODUCT LIST :(')
      except ValueError:
          print('Enter numbers only')
      except Exception as e:
          print(type(e),';',e)
    print('PRODUCTS HAVE BEEN ADDED TO THE CART.')


def remove_from_Cart():
    """asks the users if they want to remove any product from the cart or not.

    Input: string.

    Returns: shopping cart with the products user wants to be in .
    """
    while True:
        product = input(
            "\nEnter the product you want to remove('or type 'no' to finish)")  # make sure to write the first letter of the product 'capital'
        if product == 'no':
            break
        if product in shopping_cart:  # finding the product in the cart
            del shopping_cart[product]  # deleting the product from the shopping cart
        else:
            print(f"\n{product} NOT FOUND IN THE CART")
    print('PRODUCTS HAVE BEEN REMOVED FROM THE CART ')

def view_shopping_cart():
    """ asks the user if they want to view the cart

    Input: string

    Returns: shopping cart with the products and quantity
    after the purchase is made, it gives the total bill too

    if the purchase is cancelled, it keeps the items in the cart

    """
    global total_amount     # using global variable so as to use it in other functions too.
    total_amount = 0        # initializing a counter to calculate the total bill.
    for product, quantity in shopping_cart.items():  # fetching the product and quantity from shopping cart
        for i in products_list:                      # finding the product in the main product list
            if i['product'] == product:               # check if the product in the main product list matches the product in the cart
                total_amount += i['price'] * quantity  # fetching the price of the product from the main product list
                break                                 # stop searching for this product once found
    while True:
      view = input(
         '\nDO YOU WANT TO VIEW YOUR CART?(yes/no)')  # ask the user if he wants to check his shopping cart or not
      if view.lower() == 'yes':
          print(shopping_cart)
          print('\nYOUR TOTAL BILL IS RS:', total_amount)
          break
      elif view.lower() == 'no':
          print('\nENJOY SHOPPING')
          break
      else:
          print('\nPLEASE ENTER YES OR NO')

def checkout():
    while True:
      confirmation = input('\nDO YOU WANT TO CONFIRM YOUR PURCHASE?(yes/no)')
      if confirmation == 'yes':
           print("\nTHANKYOU FOR YOUR PURCHASE!")
           print("\nWE LOOK FORWARD TO SEEING YOU AGAIN SOON!!")
           break
      elif  confirmation == 'no':
           print('\nPURCHASE CANCELLED')
           break
      else:
           print('\nPLEASE ENTER YES OR NO')


def get_date():
    """
       Get the current date.

       Returns:
       - datetime.date: The current date.
       """
    from datetime import date
    return date.today()  # getting date for shopping history


def shopping_history():
    """
    displays the shopping history of the particular user.

    Returns: purchase history of the user along with the date and total bill.

    if the user has no history, it prints an appropriate message.

    """
    check = 0
    with open('shopping_history.txt', 'a+') as file:  # opening shopping history text file
        file.seek(0)
        lines = file.readlines()
        for line in lines:
            sp = line.split("'")  # splitting each item of the 'line'
            if username == sp[0]:  # it will help to access the user's history with the help of username
                print(line, '\n')
                check = 1  # counter becomes 1 from 0
        if check == 0:  # if username not found
            print(f"\n{username} HAS NO SHOPPING HISTORY.")
            return False


def save_history():
    """
    saves the purchase history of the user in the file.

    Returns:nothing unless called by another function.

    saves user's purchase history along with username and date.

    for example: Sarah's shopping history on 2024-01-12 Product: Serum,Quantity: 3   TOTAL BILL IS RS. XXXX

    where X represents the total bill
    """
    global total_amount  # using global variable to use the same variable in this function.

    with open('shopping_history.txt', 'a+') as file:  # opening 'shopping history' file to save history
        file.write(f"\n{username}'s Shopping History on {get_date()}")  # saving username along with the date
        for keys, values in shopping_cart.items():  # fetching the products and quantity from the shopping cart
            file.write(f"\tProduct: {keys}, Quantity: {values}")  # saving history in this form
        file.write(f'\tTOTAL BILL IS  RS:{str(total_amount)}')


def exit_app():
    """
    asks the user if he wants to exit the application or not.

    Returns:gracefully exits the application.

    allows the user to keep exploring if they want to exit the application.
    """
    while True:
       bye = input('\nARE YOU SURE YOU WANT TO EXIT THE APPLICATION? (yes/no)').lower()
       if bye == 'yes':
          print('\nWE LOOK FORWARD TO SEEING YOU AGAIN SOON!')
          exit()
       elif bye == 'no':
          print('\nENJOY SHOPPING!!')
          break
       else:
          print("\nPLEASE ENTER 'yes' OR 'no' ")


print("\n1- Create account \n2- login")
account()  # asking the user to create or login into their account.

while True:  # ask the user what they want their next step to be.
    print('1.Add items')
    print('2.Remove items')
    print('3.View Shopping cart')
    print('4.Checkout')
    print('5.View shopping History')
    print('6.exit')
    choice = input('Enter your choice number:')
    # when user enters a number,corresponding functions will be called to execute specific tasks.
    if choice == '1':
        add_to_cart()
    elif choice == '2':
       remove_from_Cart()
    elif choice == '3':
       view_shopping_cart()
       save_history()
    elif choice == '4':
       checkout()
    elif choice=='5':
       shopping_history()
    elif choice == '6':
       exit_app()
    else:
        print('Invalid Choice.Please try again.')
