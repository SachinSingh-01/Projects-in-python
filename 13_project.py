'''A basic login/register system.
Register username and password
Save credentials to file
Login verification
Limit login attempts to 3
Concepts strengthened
file handling
conditions
loops
string comparison
functions'''
import time
def save_file(username, password):
    with open("login.txt", "w") as file:
        file.write(f"usename={username}\n")
        file.write(f"password={password}\n")
def register():
    user_Id="Sachinsingh"
    passkey="SachinBillu921"
    attempt=0
    lockeout=5
    while True:
        username=input("Enter you user_ID:")
        password=input("Enter you password:")
        if username==user_Id and password==passkey:
            print("Login successfull")
            break
        else:
            attempt+=1
            if (attempt<=3):
                print("Wrong username or password")
                save_file(username,password)
            else:
                time.sleep(lockeout)
                print("You can try now again")
register()
