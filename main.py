import point
import product
import purchases


def menu():
    print("Options: ")
    print("[1] Customer")
    print("[2] Product")
    print("[3] Purchases")
    print("[0] Exit the program.")




menu()
print("****** Welcome to this POS program ****.")
option = int(input("Please enter your option: "))

while option !=0:
    if option ==1:
        point.show_customer_menu()
        pass

    elif option == 2:
        product.show_product_menu()
        print()
        pass

    elif option == 3:
        # option 3 stuff
        purchases.display_purchase_menu()
        pass

    else:
        print("Invalid option.")

    print()
    menu()
    option = int(input("Enter your option: "))

print("Thanks for using this program. Goodbye.")




if __name__ == "__main__":
    menu()
