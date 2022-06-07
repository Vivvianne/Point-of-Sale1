# A simple Point Of Sale System

## Description

This system can be usefull to a merchant to monitor the number of customers in his system, the number of products in his inventory and the number and amount of 
purchases made. 
At the point of sale, the merchant calculates the amount owed by the customer, indicates that amount, may prepare an invoice for the customer. It also calculates the 
amount of products remaining in the inventory.
This project is implemented in Python and a text file to kep the data. It allows the administrator choose from a menu which has customer, products and pucharses 
choices. What the administrators needs to do first is to create a customer or create  and customer list and a products list, then this will allow for a purcase 
to happen.

## User Story

A user is presented with a menu that has options of; Customer, Products or purchases.

### Customer

If a user choses customer, the user should be able to create a customer, store the customer details in a txt file, get a list of customers and their details stored in 
the txt file, seach/find a customer, update customer details and delete a customer.

### Products

If a user chooses products, the user should also be able to create a product, store the products and it's details including the quantity and price in a text file, get 
the product list/inventory, 
search a product, update a produ and delete a product.

### Purchases

The user should finaly be able to make a purchase. The customer details especially the customer id is key in making purchases. Here the user has to key in the customer 
ID making the purchases, then key in the purchase ID to check whether these details exist. If they exist, the user then proceed to make a purchase by keying in the 
quantity of the products she/he would want to purchase. The user then makes a purchase and should get a message that purchase is successfull. Then the user either can 
choose to make another purchase or go to check out. If the user uses to checkout, the user will then be informed that the inventory is updated and informed the amount
of the purchase. When the product list is checked, the inventory should have been updated after purchase.
A user then can chose to exit purchases, the user will find themselves in the main menu, then a user can choose another otion or choose to exit the program.


## SetUp/Installations Requirements
### Prerequisite

Python3

## Running the Application

To run the application, you run it on your terminal:
"project location/project name/main.py"

## Technologies Used

Python3

## Licence


