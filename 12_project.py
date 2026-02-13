'''A simple notes application.
Requirements
Add a note
View all notes
Search notes by keyword
Delete a note
Save notes to file
Concepts strengthened
list
string searching
file handling
loops
functions'''
lst=[]
def add_note():
    note=input("Enter note to add:")
    lst.append(note)
def view_note():
    for note in lst:
        print(note)
def search_note():
    keyword=input("Enter the keyword to searcch note:")
    for note in lst:
        if keyword in note:
            print(note)
            found=True
    if not found:
        print("Note not present")
def delete_note():
    user_input=int(input("Enter index number to delete note:"))
    index=user_input-1
    if index < len(lst):
        lst.pop(index)
    else:
        print("Invalid index")
def save_file():
    with open("note.txt","w") as file:
        for note in lst:
            file.write(note + "\n")
        print("file save successfully")
while True:
    print("1.Add note")
    print("2.View note")
    print("3.Search note")
    print("4.Delete note")
    choice=int(input("Enter the number between (1-5):"))
    match choice:
        case 1:
            add_note()
        case 2:
            view_note()
        case 3:
            search_note()
        case 4:
            delete_note()
        case 5:
            save_file()
        case _:
            print("Invalid number")

