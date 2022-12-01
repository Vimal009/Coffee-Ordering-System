print("Coffee Ordering System") 
#making the lists
available_coffee = ['Flat White', 'Long Black', 'Cappuccino', 'Espresso', 'Latte']
coffee_prices = {'Flat White': 100, 'Long Black': 120, 'Cappuccino': 150, 'Espresso': 200, 'Latte': 250}
sub_total = []
final_order = {}
customer_adress = {}


#ordering a coffee
print("Hi, Welcome to our text based Coffee Ordering")
order_coffee = True
while order_coffee:    
    print("Please choose a coffee: ")
    print()
    for coffee in available_coffee:
        print(coffee)
        print()
    while True:
        coffee = input("Which coffee would you like to order?")
        if coffee in available_coffee:
            print(f"You have ordered a {coffee}.")
            sub_total.append(coffee_prices[coffee])
            break
        if coffee not in available_coffee:
            print(f"I am sorry, we currently do not have {coffee}.")
    extra_coffee = input("Would you like to order another coffee?")
    if extra_coffee == "no":
        for key, value in final_order.items():
            print(f"\nYou have order a {key} coffee with {value}")
        check_order = True
        while check_order:
            print()
            order_correct = input("Is this correct? yes/no ")
            if order_correct == "yes":
                check_order = False
                order_coffee = False
            if order_correct == "no":
                print(final_order)
                
#finalizing the order
print(f"\nYour total order price is: ₹{sum(sub_total)}")

print("Please provide us with your Name, Address and phonenumber")
customer_adress['Name'] = input("Name:")
customer_adress['Room No'] = input("Room No & Building Name:")
customer_adress['Locality'] = input("Locality:")
customer_adress['City Name'] = input("Cityname:")
customer_adress['Pin Code'] = input("PIN CODE:")
customer_adress['Phone No'] = input("Phone Number:")
print()
print(f"Thank you for your order {customer_adress['Name']}.")
print()
print("We will deliver your order to this address")
print()
print(customer_adress['Room No'])
print(customer_adress['Locality'])
print(customer_adress['City Name'])
print(customer_adress['Pin Code'])
print()
print(f"we will contact you on {customer_adress['Phone No']} if anything comes up.")
print("Thank You")