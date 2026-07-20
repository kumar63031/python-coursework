
'''

#flipkart
class Flipkart:
    discount = 10
    products = ['laptop','phone','mouse','charger']

    @classmethod
    def showProducts(cls):
        print(cls.products)

    def login(self,username,password):
        self.username = username
        self.password = password
        print(f'welcome to the flipkart {self.username}')

    @staticmethod
    def banner():
        print("10% discount is going on flipkart ,shop now!")


pranathi = Flipkart()
pranathi.login('pranathi','pranathi@123',)
pranathi.banner()
pranathi.showProducts()



vamsi = Flipkart()
dinesh = Flipkart()


'''

class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self.followers = []

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password = newpassword


vamsi = Instagram('vamsi','vamsi@123')

print("Before username:",vamsi.username)
vamsi.username = 'praneeth'
print("After username:",vamsi.username)

print("Before password:",vamsi.getpassword())
vamsi.setpassword('praneeth@123')
print("After password:",vamsi.getpassword())





































