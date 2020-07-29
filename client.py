import socket
c = socket.socket()
c.connect(('localhost', 9999))
while True:
    print("\n")
    print("DATABASE MENU.")
    print("1. Find Customer")
    print("2. Add Customer")
    print("3. Delete Customer")
    print("4. Update Customer Age")
    print("5. Update Customer Address")
    print("6. Update Customer Phone")
    print("7. Print Report")
    print("8. Exit")

    choice = input("Select: ")
    choice = choice.strip()

    if choice is "1":
        nameToFind = input("Enter the name to find: ")
        if nameToFind.strip() is "" or nameToFind.strip() == "":
            print("Please enter a non-empty name.")
            continue
        c.send(bytes(str(choice), "utf-8"))
        c.send(bytes(nameToFind.strip(), "utf-8"))
        record = c.recv(10000).decode("utf-8")
        print(nameToFind.upper() + ": " + record.upper())
        continue

    elif choice is "2":
        print("Enter the details for the new customer: ")
        nameToAdd = input("NAME: ")
        if nameToAdd.strip() is "" or nameToAdd.strip() == "":
            print("Please enter a non-empty name.")
            continue
        ageToAdd = input("AGE(In Numeric Format Only): ")
        addressToAdd = input("ADDRESS: ")
        mobileToAdd = input("PHONE: ")
        if ageToAdd.strip() == "" or ageToAdd.strip() is "":
            ageToAdd += "-"
            ageToAdd = ageToAdd.strip()
        if addressToAdd.strip() == "" or addressToAdd.strip() is "":
            addressToAdd += "-"
            addressToAdd = addressToAdd.strip()
        if mobileToAdd.strip() == "" or mobileToAdd.strip() is "":
            mobileToAdd += "-"
            mobileToAdd = mobileToAdd.strip()
        c.send(bytes(str(choice), "utf-8"))
        c.send(bytes(nameToAdd.strip().lower(), "utf-8"))
        c.send(bytes(ageToAdd.strip(), "utf-8"))
        c.send(bytes(addressToAdd.strip(), "utf-8"))
        c.send(bytes(mobileToAdd.strip(), "utf-8"))
        record = c.recv(10000).decode("utf-8")
        print(record.upper())
        continue

    elif choice is "3":
        nameToDelete = input("Enter the name of customer to be deleted from the Database: ")
        if nameToDelete.strip() is "" or nameToDelete.strip() == "":
            print("Please enter a non-empty name.")
            continue
        c.send(bytes(str(choice), "utf-8"))
        c.send(bytes(nameToDelete.strip().lower(), "utf-8"))
        record = c.recv(10000).decode("utf-8")
        print(record.upper())
        continue

    elif choice is "4":
        nameToUpdate = input("Enter the name: ")
        if nameToUpdate.strip() is "" or nameToUpdate.strip() == "":
            print("Please enter a non-empty name.")
            continue
        c.send(bytes(str(choice), "utf-8"))
        ageToUpdate = input("Enter the new Age in NUMERIC FORMAT only: ")
        if ageToUpdate.strip() == "" or ageToUpdate.strip() is "":
            ageToUpdate += "-"
            ageToUpdate = ageToUpdate.strip()
        c.send(bytes(nameToUpdate.strip().lower(), "utf-8"))
        c.send(bytes(ageToUpdate.strip(), "utf-8"))
        record = c.recv(10000).decode("utf-8")
        print(record.upper())
        continue

    elif choice is "5":
        nameToUpdate = input("Enter the name: ")
        if nameToUpdate.strip() is "" or nameToUpdate.strip() == "":
            print("Please enter a non-empty name.")
            continue
        c.send(bytes(str(choice), "utf-8"))
        addressToUpdate = input("Enter the new Address: ")
        if addressToUpdate.strip() == "" or addressToUpdate.strip() is "":
            addressToUpdate += "-"
            addressToUpdate = addressToUpdate.strip()
        c.send(bytes(nameToUpdate.strip().lower(), "utf-8"))
        c.send(bytes(addressToUpdate.strip(), "utf-8"))
        record = c.recv(10000).decode("utf-8")
        print(record.upper())
        continue

    elif choice is "6":
        nameToUpdate = input("Enter the name: ")
        if nameToUpdate.strip() is "" or nameToUpdate.strip() == "":
            print("Please enter a non-empty name.")
            continue
        c.send(bytes(str(choice), "utf-8"))
        mobileToUpdate = input("Enter the new Phone: ")
        if mobileToUpdate.strip() == "" or mobileToUpdate.strip() is "":
            mobileToUpdate += "-"
            mobileToUpdate = mobileToUpdate.strip()
        c.send(bytes(nameToUpdate.strip().lower(), "utf-8"))
        c.send(bytes(mobileToUpdate.strip(), "utf-8"))
        record = c.recv(10000).decode("utf-8")
        print(record.upper())
        continue

    elif choice is "7":
        c.send(bytes(str(choice), "utf-8"))
        flag = c.recv(10000).decode("utf-8")
        if flag == "empty" or flag is "empty":
            print("No data found in the database!")
            continue
        result = c.recv(100000).decode("utf-8")
        customers = result.split("|")
        for customer in customers:
            print(customer)
            continue

    elif choice is "8":
        c.send(bytes(str(choice), "utf-8"))
        byeMsg = c.recv(10000).decode("utf-8")
        print(byeMsg)
        print("Good Bye")
        break

    else:
        c.send(bytes(str(choice), "utf-8"))
        print("Enter a valid option(1-8): ")
        continue