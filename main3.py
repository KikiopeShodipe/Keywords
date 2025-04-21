while True:
    age=input("Enter your age(Type 'exit' to quit):")
    if age.lower()=='exit':
        print("Exiting Program....")
        break
    if not age.isdigit():
        print("Invalid input")
        continue
    print("You entered age:",age)
    #print(f"You entered age:{age}")