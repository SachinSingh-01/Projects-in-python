'''Daily Habit Tracker
What to build
Add habits
Mark habits as done
View progress
Concepts used
List for habits
Dictionary for habit → status
if-else for completed or not
Loop for daily usage
Functions for operations'''
dic={}
lst=[]
def add_habit():
    habit=input("Enter habit to add:")
    lst.append(habit)
    dic[habit]="Not Done"
def habit_done():
    done=input("Enter habit which is done:")
    if done in lst:
        dic[done]="Done"
    else:
        print("Habit not present")
def view_progress():
    if not dic:
        print("No habits added yet")
    else:
        for habit, status in dic.items():
            print(habit, ":", status)
while True:
    print("\n1.To add habit")
    print("2.To check done or not")
    print("3.To view progress")
    print("4.Exit")
    choice=int(input("Enter number from (1-4):"))
    match choice:
        case 1:
            add_habit()
        case 2:
            habit_done()
        case 3:
            view_progress()
        case 4:
            print("\nYou exit")
            break
        case _:
            print("Invalid number")