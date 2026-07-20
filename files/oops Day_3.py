
# polymorphism

# method overridding

'''
class Hotstar:
    def __init__(self,name):
        self.name = name
        print(f'{self.name}, Welcome to the hotstar')
    def login(self):
        print("You can login")
    def dashboard(self):
        print("You can see the dashboard items")
    def search(self):
        print("You can search")
    def languages(self):
        print("You select the languages")
    def playcontrollers(self):
        print("You can play and pause the video")
    def ads(self):
        print("Ads will run")
    def movies(self):
        print("You can have limited access on movies")
    def sports(self):
        print("Limited time you can watch sports")
    def quality(self):
        print("limited quality")

class PremiumHotstar(Hotstar):
    def __init__(self,name):
        self.name = name
        print(f'{self.name}, Welcome to the premium hotstar ')
    def ads(self):
        print("Ads won't run")
    def movies(self):
        print("You can have unlimited access on movies")
    def sports(self):
        print("you can watch sports")

subbu = Hotstar('subbu')

subbu.login()
subbu.dashboard()
subbu.languages()
subbu.search()
subbu.playcontrollers()
subbu.ads()
subbu.movies()
subbu.sports()
subbu.quality()
    
kumar = PremiumHotstar('kumar')

kumar.login()
kumar.dashboard()
kumar.languages()
kumar.search()
kumar.playcontrollers()
kumar.ads()
kumar.movies()
kumar.sports()
kumar.quality()


'''

class Number:
    def __init__(self,n):
        self.n = n
    def __add__(self,other):
        return self.n + other.n
    def __sub__(self,other):
        return self.n - other.n
    def __mul__(self,other):
        return self.n * other.n
    def __truediv__(self,other):
        return self.n / other.n
    def __eq__(self,other):
        return self.n == other.n
    def __lt__(self,other):
        return self.n < other.n
    def __gt__(self,other):
        return self.n > other.n
    def __str__(self):
        return str(self.n)

n1 = Number(10)
n2 = Number(20)

print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1==n2)
print(n1<n2)
print(n1>n2)
print(n1,n2)





































