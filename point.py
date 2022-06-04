import os
customers = []
class Customer:

    def __init__(self, id, name, address):
        

        # instance variables
        self.id = id
        self.name = name
        self.address = address

        
        

def show_customer_menu():
    customer_list = []

    while True:
        print("""
        Customer menu
        1. Customer List
        2. Create a customer
        3. Update a customer
        4. Delete a customer
        0. Quit
        """)

        option4 = int(input("Choose a customer option: "))

        if option4 == 1:
            print()
            list_customers()
        elif option4 ==2:
            print()
            customer_list.append(create_customer())
            print(customer_list)

        elif option4 ==3:
            print()
            update_customer()

        elif option4 == 4:
            print()
            delete_customer()

        elif option4 == 0:
            print()
            break

        else:
            print()
            print('Oops! Incorrect option. Please try again! ')

        




def list_customers():
    customers = []
    customers_list = []
    with open('customer.txt','r') as reader:
        for line in reader.readlines():
            customers.append(line)
   
    for c in customers:
        lists = c.replace('\n','')
        customers_list.append(lists)
    print(customers_list)




def create_customer():
    pt = open('customer.txt', 'a+', newline='')
    customer_id = input("Enter Customer id : ")
    with open("customer.txt",'r') as pt_r:
        for line in pt_r.readlines():
            if customer_id in line:
                print()
                print("The ID already exists!! Enter a a different ID !!")
                print()
                return create_customer()

    # user inputs
    customer_name = input("Enter Customer name:  ").lower()
    address = input("Enter customer address:   ")
    pt.write(customer_id + ',' +  customer_name  +  ','  +  address + "\n")
    pt.close()
    if(pt):
        print("Customer added successfully!!!")
    print()
    output = {"id": customer_id, "name": customer_name, "address": address}
    return output


def update_customer():
    file = open('customer.txt','r')
    temp = open('temp.txt','w')
    id = int(input("Enter customer id to change: "))
    st =" "
    while(st):
        st = file.readline()
        J = st.split(",")
        if len(st)>0:
            if int(J[0])==id:
                name = input("Enter customer name: ").lower()
                address = input("Enter customer address: ")
                temp.write(str(id) + ',' + name + ',' + address + "\n")
            else:
                temp.write(st)
    temp.close()
    file.close()
    os.remove('customer.txt')
    os.rename('temp.txt','customer.txt')
    print("Customer is updated successfully!")
    list_customers()


   





def delete_customer():
    customer = open("customer.txt", 'r')
    temp =open("temp.txt", 'w')
    id = int(input("Enter customer id to delete: "))
    st = ' '
    while(st):
        st = customer.readline()
        J = st.split(',')
        if len(st)>0:
            if int(J[0]) !=id:
                temp.write(st)

    customer.close()
    temp.close()
    os.remove('customer.txt')
    os.rename('temp.txt','customer.txt')
    print("Customer is deleted successfuly! ")
    list_customers()




def show_customers():
    file = open('customer.txt','r')
    for i in file:
        item = i.split(',')
        id = item[0]
        name = item[1]
        address = item[2]
        customer = Customer(id,name,address)
        customers.append(customer)
        







    if __name__ == "__main__":
        show_customer_menu()