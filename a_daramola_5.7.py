#Akinola Daramola Jr
#Programming Exercise 5.7
#Due Date: 07/17/2022

"""
Stadium Seating

There are three seating categories at a stadium.
Class A seats cost $20, Class B seats cost $15, and Class C seats cost $10.
Write a program that asks how many tickets for each class of seats were sold,
then displays the amount of income generated from ticket sales.
"""

#Define mainline function
def main():
    #Calling function with cost per seat of each class as arguments
    seats(20,15,10)

    
    #classA_seats(20)
    #classB_seats(15)
    #classC_seats(10)
    

#Define function with cost per seat of each class as parameters
def seats(classA_seat_cost, classB_seat_cost, classC_seat_cost):

    #Declared the quantity seats for each class dynamically
    classA_seats = int(input("How many tickets were sold in Class A? "))
    classB_seats = int(input("How many tickets were sold in Class B? "))
    classC_seats = int(input("How many tickets were sold in Class C? "))


    #Calculating ticket sales for eacch class
    classA_ticket_sales = classA_seats * classA_seat_cost
    classB_ticket_sales = classB_seats * classB_seat_cost
    classC_ticket_sales = classC_seats * classC_seat_cost


    #Displaying total income generated from each class
    print(f"Class A Ticket Sales: ${classA_ticket_sales:,.2f}")
    print(f"Class B Ticket Sales: ${classB_ticket_sales:,.2f}")
    print(f"Class C Ticket Sales: ${classC_ticket_sales:,.2f}")

    #Display total income generated from ticket sales
    total_ticket_sales = classA_ticket_sales + classB_ticket_sales + classC_ticket_sales
    print(f"Total Ticket Sales: ${total_ticket_sales:,.2f}")




  
"""
#Defining Class A function with 
def classA_seats(cost_per_ticket):
    #Declaring value of ticket quantity
    classA_ticket_quantity = int(input("How many tickets were sold in Class A? "))
    #Calculating ticket sales for Class A
    classA_ticket_sales = classA_ticket_quantity * cost_per_ticket
    #Displaying total income generated from Class A ticket sales
    print(f"Class A Ticket Sales: ${classA_ticket_sales:,.2f}")

#Defining Class B function
def classB_seats(cost_per_ticket):
    #Declaring value of tickt quantity
    classB_ticket_quantity = int(input("How many tickets were sold in Class B? "))
    #Calculating ticket sales for Class B
    classB_ticket_sales = classB_ticket_quantity * cost_per_ticket
    #Displaying total income generated from Class B ticket sales
    print(f"Class B Ticket Sales: ${classB_ticket_sales:,.2f}")

#Defining Class C function
def classC_seats(cost_per_ticket):
    #Declaring value of tickt quantity
    classC_ticket_quantity = int(input("How many tickets were sold in Class C? "))
    #Calculating ticket sales for Class C
    classC_ticket_sales = classC_ticket_quantity * cost_per_ticket
    #Displaying total income generated from Class C ticket sales
    print(f"Class C Ticket Sales: ${classC_ticket_sales:,.2f}")

"""

#Calling mainline function
main()



