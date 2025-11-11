name=input("Enter your name: ")
if name:
    name=name[0].upper()+name[1:].lower()
    print("Hello %s!"%name)
else:
    print("Hello Stranger!")