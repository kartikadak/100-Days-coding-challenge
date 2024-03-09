#!/usr/bin/python2
#Display menu
def display_menu():
        print("\n Expense tracker")
        print("1. Add expense")
        print("2. view expense")
        print("3. Exit")
        print("4. total")
#Add expense
def add_exp(a):
        item = raw_input("Enter the name of the item: ")
        cost = float(raw_input("Enter the expense: "))
        a.append({"Items":item , "Expense":cost})
        print("Data added successfully")
#View expense
def view_exp(a):
        for i, cost in enumerate(a,1):
                print("{} {} {}".format(i,cost["Items"],cost["Expense"]))
#Total expense
def total_exp(a):
        x = 0
        for i, cost in enumerate(a, 1):
                price = int(cost["Expense"])
                x += price
                print("Item {}: {}".format(i, price))

        print("Total Expense: {}".format(x))

#Main function
def main():
        book = []
        while True:
                display_menu()
                choice = raw_input("What do you want to do from 1-3: ")
                if choice == "1":
                        add_exp(book)
                elif choice == "2":
                        view_exp(book)
                elif choice == "3":
                        print("Quiting! Exit")
                        break
                elif choice == "4":
                        total_exp(book)
                else:
                        print("Invalid Input")

if __name__ == "__main__":
    main()
