import instaApi

name = input("Enter username or link: ")


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
    print(id)
except:
    print("enter valid name")

try:
    for i in instaApi.searchStory(id)['reel']['items']:
        if "video_versions" not in i:
            link = i["image_versions2"]["candidates"][0]["url"]
            print(f"image: {link}")
        else:
            link = i['video_versions'][0]["url"]
            print(f"video: {link}")
except:
    print("error processing data")