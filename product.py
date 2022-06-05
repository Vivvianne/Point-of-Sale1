import os
PRODUCTS = []

# product class
class Product:
    def __init__(self,id,name,quantity,price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price =price



def show_product_menu():
    product_list = []

    while True:
        print("""
        Product menu
        1. Product List
        2. Create a product
        3. Update a product
        4. Delete a product
        0. Quit
        """)

        option5 = int(input("Choose a product option: "))

        if option5 == 1:
            print()
            list_products()
        elif option5 ==2:
            print()
            product_list.append(create_product())
            print(product_list)

        elif option5 ==3:
            print()
            update_product()

        elif option5 == 4:
            print()
            delete_product()

        elif option5 == 0:
            print()
            break

        else:
            print()
            print('Oops! Incorrect option. Please try again! ')

def list_products():
    products = []
    products_list = []
    with open('product.txt','r') as reader:
        for line in reader.readlines():
            products.append(line)
   
    for c in products:
        lists = c.replace('\n','')
        products_list.append(lists)
    print(products_list)


def create_product():
    pt = open('product.txt', 'a+', newline='')

    product_id = input("Enter Product id : ")
    with open("product.txt",'r') as pt_r:
        for line in pt_r.readlines():
            if product_id in line:
                print()
                print("The ID already exists!! Enter a a different ID !!")
                print()
                return create_product()

    product_name = input("Enter the name of the Product:  ").lower()
    quantity = input("Enter the quantity of the product:   ")
    price = input("Enter the price of the product:   ")
    pt.write(product_id + ',' +  product_name  +  ','  +  quantity + ',' + price + "\n")
    pt.close()
    if(pt):
        print("Product added successfully!!!")
    print()
    output = {"id": product_id, "name": product_name, "quantity": quantity, "price": price}
    return output

def update_product():
    file = open('product.txt','r')
    temp = open('temp.txt','w')
    id = input("Enter Product id to change: ")
    st = ' '
    while(st):
        st = file.readline()
        J = st.split(',')
        if len(st)>0:
            if J[0] == id:
                name = input("Enter Product name: ")
                quantity = input("Enter product quantity : ")
                # assert quantity >=0, f"{quantity} is not greater or equal to zero!! "
                price = input("Enter the product price : ")
                # assert price >= 0, f"Price {price} is not greater or equal to zero!! "
                temp.write(str(id) + ',' +  name  +  ','  +  quantity + ',' + price + "\n")
            else:
                temp.write(st)
    temp.close()
    file.close()
    os.remove('product.txt')
    os.rename('temp.txt','product.txt')
    print("Product updated successfuly!!")
    list_products()




def delete_product():
    product= open("product.txt", 'r')
    temp =open("temp.txt", 'w')
    id = int(input("Enter product id to delete: "))
    st = ' '
    while(st):
        st = product.readline()
        J = st.split(',')
        if len(st)>0:
            if int(J[0]) !=id:
                temp.write(st)

    product.close()
    temp.close()
    os.remove('product.txt')
    os.rename('temp.txt','product.txt')
    print("Product is deleted successfuly! ")
    list_products()



def show_products():
    product = open("product.txt","r")
    for p in product:
        try:
            prod = p.split(',')
            id = prod[0]
            name = prod[1]
            quantity = int(prod[2])
            price = prod[3]
            output = Product(id,name,quantity,price)
            PRODUCTS.append(output)
        except:
            print()





    if __name__ == "__main__":
        show_product_menu() 