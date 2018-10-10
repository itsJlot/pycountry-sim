#!/usr/bin/env python
from random import *

def chance(perc):
    if perc/100.0 < random():
        return True
    return False
def multiplier():
    return choice([0.25,0.5,0.75,1,1.25,1.5,1.75,2,3])
namelist = {"Male" : ["Skullcape" , "Hieronymus" , "Karsten" , "Cenk" , "Bréanainn" , "Yavor" , "Chavaqquq" , "Delaiah" , "Ramaz" , "Gernot" , "Lasse" , "Wigmar" , "Emeka" , "Flavio" , "Rainer" , "Roshan"],
                    "Female" : ["Imelda", "Helena" , "Niobe" , "Mia", "Marley", "Serpil", "Liat" , "Putu" , "Willy" , "Loretta" , "Oksana" , "Chisomo" , "Mathilde" , "Siiri" , "Antonija" , "Anica", "Kylie"],
                    "Other" : ["Lior", "Ale" , "Vanja" , "Yanick" , "Kasey" , "Blair" , "Tendai" , "Abimbola" , "Gabi" , "Brett" , "Lashawn" , "Tiyamike" , "Udo" , "Guanting" , "Toby" , "Sasha" , "Ji-Young" , "Shun" , "Oghenekaro" , "Chioma"],
                    "Sur" : ["Van Rossem" , "Teel" , "Garner" , "Katranjiev" , "Biondo" , "Madsen" , "Popov" , "Yamashita" , "Bryan" , "Wolf" , "Santana" , "Zino" , "Horn" , "Lewerenz" , "Armbruster" , "Herriot" , "Gardyner" , "Ikin" , "Mayes" , "Campo" , "Oliver" , "Bergström"],
                   }
def rbool():
    return choice([True,False])

def avg(v,v2,rfact):
    val = (v + v2)/2
    val += rfact * val * (random() - 0.5)
class Company():
    workers = []
    sector = None
    money = 0
    def __init__(self,owner):
        sector = choice(Country.sectors)
    def pay(self,other,amount):
        self.money -= amount
        other.money += amount
    def year(self, country):
        self.pay(country,self.money * country.vat)

class Sector():
    name = "Steel"
class Country(Company):
    # Sector syntax: (Sector name, base mat, ratio of buyers (0 consumer, 1 companies), price of 1 unit)
    sectors = [("Raw",None,0.98,50),("Industry","Raw",0.7,2000),("Tech","Industry",0.4,3000),("Food","Raw",0.1,100)]
    companies = []
    people = []
    workers = []
    banks = []
    ownedcompanies = []
    #vat: tax rate
    def __init__(self,hcount = 1000, money = 1000000,vat = 0.02):
        self.money = money
        self.companies.append(self)
        self.vat = vat
        self.banks = [Bank()]
        for x in range(hcount):
            p = Person()
            self.pay(p,500)
            self.people.append(p)
        while len(self.people) != 0:
            self.cyear()
    def cyear(self):
        for company in self.companies[1:]:
            company.year(self)

        print(self.people[0].name, self.people[0].money)
        self.people[0].year(self)
        for person in self.people[1:]:
            person.year(self)
    def get_bank(self):
        return choice(self.banks)
    def get_company(self):
        return choice(self.companies)
    def get_citizen(self):
        return choice(self.people)
    @staticmethod
    def get_name(t):
        return choice(namelist[t])

class Person:
    parent1 = None
    parent2 = None
    spouse = None
    money = 0
    age = 0
    attra = 0
    polal = 500
    bank = None

    def __init__(self,min = 15, max = 50, mmin = 0.5, mmax = 3, minage = 14,maxage = 99,lifeexp = 80,parent1 = None, parent2 = None):
        self.new = {}
        gauss(lifeexp,20)
        self.lifeexp = lifeexp
        hasParents = (parent1 != None) and not parent2
        self.gender = rbool()
        self.children = []
        if self.gender:
            self.name = Country.get_name("Male")
        else:
            self.name = Country.get_name("Female")
        if hasParents:
            self.attra = parent1.attra()
            self.polal = avg(parent1.polal,parent2.polal)
            self.sur = choice([parent1.sur,parent2.sur])
        else:
            self.age = randint(minage, maxage)
            self.polal = randint(0,1000)
            self.sur = Country.get_name("Sur")
    def year(self,country):
        self.age += 1
        if not self.pay(country,self.money * country.vat):
            self.bank = country.get_bank()
        if self.age > self.lifeexp:
            self.die(country)
    def pay(self,other,amount):
        if self.bank:
            self.bank.do_transaction(self,other,amount)
            return True
        return False
    def die(self,country):
        if len(self.children) == 0:
            country.money += self.money
            self.money = 0
        country.people.remove(self)

class Bank(Company):
    cut = 0.001
    intb = 0.01
    intg = 0.1
    money = 0
    customers = []
    def __init__(self,cut = 0.1):
        self.cut = cut
    def do_transaction(self,sender,rec,amount):
        sender.money -= amount
        self.money += amount * self.cut
        amount *= (1 - self.cut)
        rec.money += amount
    def year(self, country):
        pass
#print(Country.get_name("Male"))
Country()
print()
input("press enter key to exit")