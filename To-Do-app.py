#!/usr/bin/python2
import os

#Create Display menu
def display_menu():
        print("\n TO-DO List")
        print("1. ADD Task")
        print("2. VIEW Task")
        print("3. Mark Task")
        print("4. Exit")

#Create adding function
def add_task(a):
        task = raw_input("Enter the task: ")
        a.append({"task_list": task , "completed": False})
        print("Added the task successfully")

#Create viewing function
def view_task(a):
        if not a:
                print("No tasks available")
        else:
                for i, task in enumerate(a,1):
                        if task["completed"] == False:
                                x = "not completed"
                        else:
                                x= "completed"
                        print("{} {} {}".format(i,task["task_list"],x))

#Create Mark as complete
def mark_task(a):
        view_task(a)
        list = int(raw_input("Enter the task to mark completed: "))
        if 1<=list<=len(a):
                a[list - 1]["completed"] = True
                print("Updated")
        else:
                print("Invalid Task Number.")

#Create Main function
def main():
        tasks = []

        while True:
                display_menu()
                choice = raw_input("Please enter your choice 1-4: ")
                if choice == "1":
                        add_task(tasks)
                elif choice == "2":
                        view_task(tasks)
                elif choice == "3":
                        mark_task(tasks)
                elif choice == "4":
                        print("Exit! Quitting")
                        break
                else:
                        print("Invalid Input")

if __name__ == "__main__":
    main()
           
