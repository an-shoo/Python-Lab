passwd = {'rahul': 'genius', 'kumar': 'smart', 'ankita': 'intelligent'}

# a) Print all the items in the dictionary
print("All items:")
for user, pwd in passwd.items():
    print(f"{user}: {pwd}")

# b) Print all the keys in the dictionary
print("\nAll keys:")
for user in passwd.keys():
    print(user)

# c) Print all the values in the dictionary
print("\nAll values:")
for pwd in passwd.values():
    print(pwd)

# d) Get the passwords of users
print("\nPasswords of users:")
for user in passwd:
    print(f"{user}'s password is {passwd[user]}")

# e) Change the password of a particular user
print("\nChanging ankita's password")
passwd['ankita'] = 'brilliant'
print(f"ankita's new password is {passwd['ankita']}")
