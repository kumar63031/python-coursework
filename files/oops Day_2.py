
'''

#protected 

class Instagram:
    def __init__(self):
        self._post=[]
    @property
    def accesspost(self):
        return self._post

    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)

dinesh = Instagram()

print(dinesh.accesspost)
dinesh.accesspost = 'class and object'
print(dinesh.accesspost)


#  single inheritance


class whatsappv1:
    def message(self):
        print("You can send message to people")

class whatsappv2(whatsappv1):
    def calls(self):
        print("You can do video/audio calls")

dinesh = whatsappv1()
print("v1-Dinesh")
dinesh.message()

naresh = whatsappv2()
print("v2- Naresh")
naresh.message()
naresh.calls()



# multiple inheritance

class whatsappv1:
    def message(self):
        print("You can send message to people")

class whatsappv2:
    def calls(self):
        print("You can do video/audio calls")

class whatsappv3:
    def media(self):
        print("Yoc can share your photos/videos")

class whatsappv4(whatsappv1,whatsappv2,whatsappv3):
    def status(self):
        print("You can share status -[24 hours]")
    

dinesh = whatsappv4()
print("v4-Dinesh")
dinesh.message()
dinesh.calls()
dinesh.media()
dinesh.status()





# multi level inheritance

class whatsappv1:
    def message(self):
        print("You can send message to people")

class whatsappv2(whatsappv1):
    def calls(self):
        print("You can do video/audio calls")

class whatsappv3(whatsappv2):
    def media(self):
        print("Yoc can share your photos/videos")

class whatsappv4(whatsappv3):
    def status(self):
        print("You can share status -[24 hours]")
    

dinesh = whatsappv4()
print("v4-Dinesh")
dinesh.message()
dinesh.calls()
dinesh.media()
dinesh.status()





#hierarical in heritance


class whatsappv1:
    def message(self):
        print("You can send mesasges to people")

class whatsappv2(whatsappv1):
    def emojis(self):
        print("You can sen messages with emojis to people")

class whatsappv3(whatsappv1):
    def strickers(self):
        print("You can send messages with strickers to people")


dinesh = whatsappv2()
print("v2 - Dinesh")
dinesh.message()
dinesh.emojis()

dinesh = whatsappv3()
print("v3 - Dinesh")
dinesh.message()
dinesh.strickers()



#hybrid inheritance

class whatsappv1:
    def message(self):
        print("You can send mesasges to people")

class whatsappv2(whatsappv1):
    def emojis(self):
        print("You can sen messages with emojis to people")

class whatsappv3(whatsappv1):
    def strickers(self):
        print("You can send messages with strickers to people")

class whatsappv4(whatsappv2,whatsappv3):
    def gifs(self):
        print("You can send a messages with gifs,emojis,strickers to people")

dinesh = whatsappv4()
print("v4 - Dinesh")
dinesh.message()
dinesh.emojis()
dinesh.strickers()
dinesh.gifs()



#super method usage

class wpv1:
    def status(self):
        print("You can upload image/videos")

class wpv2(wpv1):
    def status(self):
        super().status()
        print("You can react and reply")

class wpv3(wpv2):
    def status(self):
        super().status()
        print("You can like and reshare")

dinesh = wpv3()
print("v3")
dinesh.status()

'''


class wpv1:
    def status(self):
        print("You can upload image/videos")

class wpv2:
    def status(self):
        print("You can react and reply")

class wpv3(wpv1,wpv2):
    def status(self):
        print("You can like and reshare")
        wpv1.status(self)
        wpv2.status(self)

kumar = wpv3()
print("kumar - v3")
kumar.status()
      







































