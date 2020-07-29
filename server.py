import socket
########################################################
database = {}
with open(r'C:\\Users\\jenis\\Desktop\\data.txt', 'r') as customers:
    for data in customers:
        customer = data.split('|', 4)
        p = 0
        for item in customer:
            customer[p] = item.strip()
            p += 1
        name = customer[0]
        if name.strip() == "":
            continue
        database[name.lower().strip()] = customer[1:]


#########################################################
s = socket.socket()
s.bind(('localhost', 9999))
s.listen(20)
print("Waiting for connections")
client, addr = s.accept()
print("Connected with", addr)
while True:
    currentLength = len(database)
    choice = client.recv(10000).decode("utf-8")
    if choice is "1":
        nameToFind = client.recv(10000).decode("utf-8")
        if nameToFind in database:
            client.send((bytes(str(database[nameToFind]).strip('[]'), "utf-8")))
        else:
            client.send((bytes("Customer details not found.", "utf-8")))

    elif choice is "2":
        nameToAdd = client.recv(10000).decode("utf-8")
        nameToAdd = nameToAdd.strip()
        ageToAdd = client.recv(10000).decode("utf-8")
        addressToAdd = client.recv(10000).decode("utf-8")
        mobileToAdd = client.recv(10000).decode("utf-8")

        if nameToAdd in database:
            client.send(bytes("This user already exist in the database!", "utf-8"))
        else:
            database.update({nameToAdd.strip(): [ageToAdd, addressToAdd, mobileToAdd]})
            client.send(bytes("New User added Successfully.", "utf-8"))

    elif choice is "3":
        nameToDelete = client.recv(10000).decode("utf-8")
        if nameToDelete in database:
            del database[nameToDelete]
            client.send(bytes("The entry has been successfully deleted.", "utf-8"))
        else:
            client.send(bytes("No such user exist in the database.", "utf-8"))

    elif choice is "4":
        nameToUpdate = client.recv(10000).decode("utf-8")
        ageToUpdate = client.recv(10000).decode("utf-8")
        if nameToUpdate.lower() in database:
            database[nameToUpdate][0] = ageToUpdate.lower()
            client.send(bytes("The age has been updated successfully.", "utf-8"))
        else:
            client.send(bytes("No such user exist in the database", "utf-8"))

    elif choice is "5":
        nameToUpdate = client.recv(10000).decode("utf-8")
        addressToUpdate = client.recv(10000).decode("utf-8")
        if nameToUpdate.lower() in database:
            database[nameToUpdate][1] = addressToUpdate.lower()
            client.send(bytes("The address has been updated successfully.", "utf-8"))
        else:
            client.send(bytes("No such user exist in the database", "utf-8"))

    elif choice is "6":
        nameToUpdate = client.recv(10000).decode("utf-8")
        mobileToUpdate = client.recv(10000).decode("utf-8")
        if nameToUpdate.lower() in database:
            database[nameToUpdate][2] = mobileToUpdate.lower()
            client.send(bytes("The phone has been updated successfully.", "utf-8"))
        else:
            client.send(bytes("No such user exist in the database", "utf-8"))

    elif choice is "7":
        if len(database) == 0:
            client.send(bytes("empty", "utf-8"))
        else:
            client.send(bytes("non-empty", "utf-8"))
        result = ""
        for key in sorted(database):
            result += str("NAME: " + key + " AGE: " + database[key][0] + " ADDRESS: " + database[key][1] + " PHONE: " + database[key][2]) + "|"
        client.send(bytes(result, "utf-8"))

client.close()
##########################################################