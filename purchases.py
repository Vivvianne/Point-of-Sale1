import os
import point, product

PRODUCTS = []
CUSTOMERS = []
PURCHASES = []

def display_purchase_menu():
    

    # creating purchase options  
    while True:
        print("""
        Purchases Menu
        1. List all purchases
        2. Make a Purchase
        3. Find a purchase
        0. Quit
        """)  
        option6 = int(input("Select Purchase option:"))  

        # choice 1
        if option6 == 1:
            print()
            list_purchase()
            
        elif option6 == 2:
            print()
            make_purchases()
        elif option6 == 3:
            print()
            find_purchase()
        elif option6 == 0:
            print()
            break
        else:
            print()
            print('Incorrect choice. Please try again! ')

class Purchase:

    def __init__(self,customer_name, product_id, purchase_item, price_purchased):
        assert purchase_item >=0, f'{purchase_item} is not greater or equal to zero!'

        self.customer_name = customer_name
        self.product_id = product_id
        self.purchase_item = purchase_item
        self.price_purchased = price_purchased

        def __repr__(self):
            return f"('{self. customer.name}', '{self.product_id}','{self.purchase_item}', '{self.price_purchased}')"





    





def list_purchase():
    purchases = []
    purchase_list = []
    with open('purchase.txt', 'r') as reader:
        for line in reader.readlines():
            purchases.append(line)

    for p in purchases:
        list = p.replace('\n','')
        purchase_list.append(list)
    print(purchase_list)



# function to make a purchse

def make_purchases():
    point.show_customers()
    product.show_products()
   
    customer_exists = False
    product_exists = False
    cus_id = input("Enter customer id to purchase: ")
    # check if the customer id exists
    for cus in point.customers:
        if cus_id == cus.id:
            customer_exists = True
            cus_name = cus.name
            print("Customer name is:  " , cus_name)
            break
           

    
    # check if product exists
    pro_id = input("Enter product id to purchase: ") 
    for prod in product.PRODUCTS:
        if pro_id ==prod.id:
            product_exists = True
           
      
    if customer_exists and product_exists:

        # make purchase
        purchase_q = int(input("Enter quantity of product to purchase: "))

        # checking if amount is available
        for i in range(len(product.PRODUCTS)):
            if pro_id == product.PRODUCTS[i].id:
                name = product.PRODUCTS[i].name
                quantity = int(product.PRODUCTS[i].quantity)
                if quantity >= purchase_q:
                    # update product amount
                    balance = quantity - purchase_q
                    # print("Product available")
                    price = float(product.PRODUCTS[i].price)
                    price_purchased = price * purchase_q
                    output = Purchase(cus_name,pro_id,purchase_q,price_purchased)
                    PURCHASES.append(output)
                    print("Purchase successfull!!!")
                    print()
                    print(PURCHASES)
                    # update_products()
                    while True:
                        print ("""
                        Choose purchase option:
                        1. Make another purchase
                        2. Checkout
                        3.Exit
                        """)
                        choice7 = int(input("Choose a purchase option: "))
                        if choice7 ==1:
                            make_purchases()
                        elif choice7 ==2:
                            checkout()
                            break
                        elif choice7 ==3:
                            print()
                            break

                        else:
                            print("Invalid option!!!")
                        
                else:
                    print("Quantity in stock is below " +str(purchase_q) + ' : ' +"quantity available:"+str(quantity) )
                    make_purchases()
                    break
  
    else:
        print("Invalid details!!!")






def checkout():
    total_purchase = 0
    for pur in PURCHASES:
        cost = float(pur.price_purchased)
        total_purchase += cost
        print()
        print("Total: "+ str(total_purchase))
        print("purchase is complete.")
        update_products()
        handle_file()

 


def update_products():
    for pur in PURCHASES:
        product_id = pur.product_id
        pur_quantity = int(pur.purchase_item)
        file = open('product.txt', 'r')
        temp = open('temp.txt', 'w')
        s = ' '
        while(s):
            s = file.readline()
            L = s.split(',')
            if len(s)> 0:
                if (L[0]) == product_id:
                    name = L[1]
                    quantity = int(L[2])
                    price = L[3]
                    updated_quantity = quantity - pur_quantity
                    temp.write(str(product_id) + ',' + name + ',' + str(updated_quantity) + ',' + str(price))
                    
                else:
                    temp.write(s)
        temp.close()
        file.close()
        os.remove('product.txt')
        os.rename('temp.txt', 'product.txt')
        print("Inventory is updated.")
        print("Stock remaining for " + name + ' : ' + str(updated_quantity))

def handle_file():
    with open('purchase.txt', 'a') as fo:
        for pur in PURCHASES:
            print(pur.customer_name + ',' + pur.product_id + ',' +str(pur.purchase_item) + ',' + str(pur.price_purchased), file=fo)

  

def find_purchase():
    total = 0
    items_bought = 0

    # menu for find option

    while True:
        print("""
        Find Options:
        1.Find by Customer name
        2. Find by Product Id
        0.Exit
        """)

        option8 = int(input("Select search option: "))
        if option8 ==1:
            fo = open('purchase.txt', 'r')
            customer_name = input("Please enter the customer name to search: ").lower()
            s = ' '

            while(s):
                s = fo.readline()
                L = s.split(',')
                if len(s)>0:
                    if(L[0]) == customer_name:
                        product_id = L[1]
                        quantity = L[2]
                        price = float(L[3])
                        print( )
                        # calculating total spent by the customer
                        total += price
                        print("Customer name: ", customer_name)
                        print("Product id: ", product_id)
                        print("Quantity purchase: ", quantity)
                        print("Price: ", price)

            print('*************')
            print("Total spent by " + customer_name + ' : ' + str(total))
            break

        elif option8 == 2:
            fo = open('purchase.txt', 'r')
            id = input("Please enter a product_id to find: ")

            s = ' '
            while(s):
                s = fo.readline()
                L =s.split(',')
                if len(s)>0:
                    if(L[1]) == id:
                        customer_name = L[0]
                        quantity = int(L[2])
                        price = float(L[3])
                        print( )
                        # calculate the total spent on a product

                        total += price
                        items_bought += quantity
                        print("Customer name: ", customer_name)
                        print(" Quantity purchased: ", quantity)
                        print("Price: ", price)

            print('**************')
            print("Total spent: " + str(total))
            print()
            print("No of products purchased: " + str(items_bought))
        
        elif option8 == 0:
            print()
            break

        else:
            print()
            print("Sorry! Incorrect option. Please try again.")


    
    if __name__ == "__main__":
        display_purchase_menu() 









