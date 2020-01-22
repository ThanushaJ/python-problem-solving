#import ast
#Contacts = {"thanu": 9108041555, "Nani": 9499389282, "Mom": 7263825825}
f = open("contacts.txt",'r')
Contact = f.readline()
print(Contact)
Contacts = eval(Contact)
print(Contacts)
Need = "yes"
while Need == "yes":
    print("These contacts are available", Contacts.keys())
    Name = input("Select Name: ")
    if Name in Contacts:
        print(Contacts[Name])
    else:
        print("Contact Not available")
    Need = input("Do you need any contact information (yes/no)  ")
