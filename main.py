import instaApi

name = input("Enter username of link: ")


# function that filter name
def validateName(name):
    if "https://" in name:
        temp = name[26:]
        for i in temp:
            if i == '/':
                name = temp[:temp.index(i)]
                return name
    else:
        return name


try:
    id = instaApi.searchUser(validateName(name))
except:
    print("enter valid name")
