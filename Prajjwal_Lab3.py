shoppingCart = {}
def myfunc():
  print("WELCOME TO THE AMANDO SHOPPING SITE\n1.Add product to the cart.\n2.Search the product.\n3.Delete the product from the cart.\n4.Quit.")
  while True:
    choice = int(input("\nEnter your choice: "))
    if choice in range(1,5):
      choicepicker = True
    else:
      choicepicker = False
    while choicepicker == True:
      if choice == 1:
        choice1 = int(input("Enter the number of items to be added in the stationary shop: "))
        if choice1 < 6:
          for x in range(1,choice1+1):
            product_name = input("Enter an item: ")
            brand = input("Enter the Brand name: ")
            shoppingCart[product_name] = brand
          print(f"\nYou added following items to the cart:")
          for key, value in shoppingCart.items():
            print(f'{key} : {value}')
            choicepicker = False
        else:
          print("Cart is full.\n")
          choicepicker = False

      elif choice == 2:
        choice3 = input("Enter the item to be searched: ")
        if choice3 in shoppingCart.keys():
          print(f'{choice3} : {value}\n')
          choicepicker = False
        else:
          print("No products exist with this name.\n")
          choicepicker = False
      
      elif choice == 3:
        if len(shoppingCart) == 0:
          print("Cart is empty, no item is found.\n")
          choicepicker = False 
        else: 
          choice4 = input("Enter the item to be removed: ")
          if choice4 in shoppingCart.keys():
            del shoppingCart[choice4]
            print(f"\nYou deleted following item from the cart:")
            print(f'{choice4} : {value}\n')
            choicepicker = False    
          else:
            print("Item not found.\n")
            choicepicker = False  

      elif choice == 4:
        print("You quit the program!")
        exit()
      
      else:
        print("Wrong Option Entered.")

myfunc()