#!/usr/bin/env python
from random import *

"""
TODO: Stealing companies, starting companies
"""


def chance(perc):
    if perc / 100.0 < random():
        return True
    return False


namelist = {
    "Male": ["Skullcape", "Hieronymus", "Karsten", "Cenk", "Bréanainn", "Yavor", "Chavaqquq", "Delaiah", "Ramaz",
             "Gernot", "Lasse", "Wigmar", "Emeka", "Flavio", "Rainer", "Roshan"],
    "Female": ["Imelda", "Helena", "Niobe", "Mia", "Marley", "Serpil", "Liat", "Putu", "Willy", "Loretta", "Oksana",
               "Chisomo", "Mathilde", "Siiri", "Antonija", "Anica", "Kylie"],
    "Other": ["Lior", "Ale", "Vanja", "Yanick", "Kasey", "Blair", "Tendai", "Abimbola", "Gabi", "Brett", "Lashawn",
              "Tiyamike", "Udo", "Guanting", "Toby", "Sasha", "Ji-Young", "Shun", "Oghenekaro", "Chioma"],
    "Sur": ["Van Rossem", "Teel", "Garner", "Katranjiev", "Biondo", "Madsen", "Popov", "Yamashita", "Bryan", "Wolf",
            "Santana", "Zino", "Horn", "Lewerenz", "Armbruster", "Herriot", "Gardyner", "Ikin", "Mayes", "Campo",
            "Oliver", "Bergström"],
    "Company": ['Itgreen\n', 'Tresplanet\n', 'Dongsonace\n', 'Hay-holding\n', 'Lexistrip\n', 'Subelectronics\n', 'Ranfase\n',
                'Intechnology\n', 'Greenphase\n', 'Tranholding\n', 'Quotein\n', 'Unitam\n', 'Ranfax\n', 'Planetlane\n',
                'Blackzoom\n', 'Spancity\n', 'Groovedax\n', 'Villacane\n', 'Alphait\n', 'Hottrans\n', 'Zamelectronics\n',
                'coning\n', 'xx-core\n', 'Faxtechnology\n', 'Runbelane\n', 'Faserancan\n', 'Roundtechno\n', 'Inchtexon\n',
                'Betacone\n', 'Trantom\n', 'Zaamtaxon\n', 'Domtam\n', 'Nimfix\n', 'Hotplus\n', 'Donzap\n', 'Hothow\n',
                'Zencon\n', 'Trusttrax\n', 'Medbam\n', 'Qvotinflex\n', 'Rounddom\n', 'Drip-kix\n', 'Unisaoline\n',
                'Newfan\n', 'Zapcorporation\n', 'Flexcorporation\n', 'Ozercom\n', 'Kanremcity\n', 'X-ron\n', 'Linetech\n', 'Zimronis\n', 'Zaamunalab\n', 'inchla\n', 'Haycane\n', 'Xx-taxon\n', 'O-ron\n', 'Tinlane\n', 'Indigolex\n', 'Super-line\n', 'ope-lux\n', 'Zummahouse\n', 'Highdex\n', 'zimzim\n', 'Silverlex\n', 'Zimcon\n', 'Overzoom\n', 'domtech\n', 'Alphazone\n', 'Sonjayzim\n', 'Caretriplex\n', 'Joy-base\n', 'Zathcon\n', 'lacare\n', 'icetaxon\n', 'Strongfase\n', 'xx-can\n', 'Plexcity\n', 'Baming\n', 'fasetone\n', 'Dalttexon\n', 'konktex\n', 'Overcorporation\n', 'saolam\n', 'Indicom\n', 'Solelectronics\n', 'Sonhotcore\n', 'Sunqvolane\n', 'Conetrans\n', 'Zumplus\n', 'Freshlex\n', 'Acelane\n', 'Flexace\n', 'k-how\n', 'X-lane\n', 'Duocan\n', 'Zotstreet\n', 'Plus-code\n', 'Techmedia\n', 'Greenholding\n', 'Voltax\n', 'Intech\n', 'D-holding\n', 'Acestrip\n', 'Zoomelectronics\n', 'Voltelectronics\n', 'Hotzunhex\n', 'Sailis\n', 'Apelectrics\n', 'drip-how\n', 'Doncode\n',
                'Zunbiocare\n', 'Itla\n', 'Anzocity\n', 'Dontechno\n', 'Fasecone\n', 'Freshkix\n', 'Mathgreen\n', 'Tonfax\n', 'Canhotcore\n', 'Soldrill\n', 'Acetexon\n', 'Icemedla']
}


def rbool():
    return choice([True, False])


def avg(v, v2, rfact):
    val = (v + v2) / 2
    val += rfact * val * (random() - 0.5)
    return val


class Company():
    workers = []
    sector = None
    money = 0

    def __init__(self, owner):
        self.sector = choice(Country.sectors)
        #print(self.sector)
        self.product = 0
        self.base_materials = 0
        self.money = 0
        self.workers = [owner]
        self.owner = owner
        self.quality = 1
        if type(owner) == Country:
            #print(self.sector)
            self.name = "State owned company: " + self.sector[0] + " Sector"
        else:
            self.name = owner.sur
        #print("Company started: " + self.name)

    def pay(self, other, amount):
        self.money -= amount
        other.money += amount

    def produce(self):

        """Allows the company to produce their product, the number of workers they have times, but is limited by the available base material"""
        if self.sector[1]:
            self.product += min(len(self.workers), self.base_materials)
        else:
            self.product += len(self.workers) + 1
        #print(self.base_materials,self.product)

    def year(self, country):
        if type(self) != Country and type(self.owner) != Country:
            self.pay(self.owner, self.money * 0.05)
            for worker in self.workers:
                self.pay(worker, 100 * worker.age / 100)
        self.pay(country, self.money * country.vat)

        if self.sector[1] and self.base_materials <= len(self.workers):
            country.market.open_buy_offer(
                Offer(self.sector[1], len(self.workers)+1, self.sector[3] * self.quality, self))
        if self.sector[0] and self.product > 0:
            country.market.open_sell_offer(
                Offer(self.sector[0], self.product, self.sector[3], self))
        self.quality += 0.01
        self.produce()
    def __str__(self):
        return self.name + "," + " (Owned by: " + str(self.owner) + " budget: " + str(self.money)

    def request_job(self,person):
        extra_m = 1
        if not type(self.owner) == Country:
            if not type(self) == Country:
                if person.id in self.owner.attraction:
                    extra_m = self.owner.attraction[person.id]

        score = person.iq * (person.eq/2) * (100 - person.age) * person.mstate * extra_m/40000000

        if gauss(0.8,0.3) < score:
            #print(person, "got hired by: ", self," with score:", score)
            self.workers.append(person)
            person.employer = self

class Country(Company):
    # Sector syntax: (Sector name, base mat, ratio of buyers (0 consumer, 1 companies), price of 1 unit)
    sectors = [("Raw", None, 0, 50), ("Industry", "Raw", 20, 2000), ("Tech", "Industry", 20, 3000),
               ("Food", "Raw", 10, 100)]
    companies = []
    people = []
    workers = []
    banks = []
    ownedcompanies = []
    id = 0

    # vat: tax rate
    def __init__(self, hcount=1000, money=100000000, vat=0.02):
        Company.__init__(self, self)
        self.money = money
        self.companies.append(self)
        self.companies.append(Company(self))
        self.vat = vat
        self.banks = [Bank()]
        self.market = Market(self)
        self.sector = ("Raw", None, 0.98, 50)
        for x in range(hcount):
            p = Person(country=self)
            self.pay(p, 5000)
        year = 0
        while len(self.people) != 0:
            year += 1
            self.cyear()

    def cyear(self):
        for company in self.companies:
            company.year(self)
        if len(self.people) > 0:
            self.people[0].year(self)
            for company in self.companies:
                company.year(self)
            for person in self.people[1:]:
                person.year(self)
        self.market.serve()
    def get_bank(self):
        return choice(self.banks)

    def get_company(self):
        return choice(self.companies)

    def get_citizen(self):
        return choice(self.people)

    @staticmethod
    def get_name(t):
        return choice(namelist[t])

    def request_child_support(self, child):
        if child.age < 20:
            self.pay(child, 400)
        else:
            self.pay(child, 10)
    def __str__(self):
        return "Country"

class Offer():
    def __init__(self, material, count, price, company):
        self.material = material
        self.count = count
        self.price = price
        self.company = company

    def as_market_offer(self):
        return (self.material, self.count, self.price, self.company)
    def __str__(self):
        return str(self.as_market_offer())

class Market():
    def __init__(self, country):
        self.country = country
        self.sell_offers = []
        self.buy_offers = []

    # Offer format: (requested material, count, min_price, self)
    def open_sell_offer(self, offer):
        self.sell_offers.append(offer)

    # Offer format: (sold material, count, price, self)
    def open_buy_offer(self, offer):
        print("Buying: ",offer.material)
        self.buy_offers.append(offer)

    def request_market_price(self, product):
        offers = self.get_sell_offers(product, 1000000, 0)
        if len(offers) > 0:
            price_list = [x[3] for x in self.get_sell_offers(product, 1000000, 0)]
            average = sum(price_list) / len(price_list)
            return average
        return list(filter(lambda x: x[0] == product, self.country.sectors))[0][2]

    def get_buy_offers(self, mat_name, price, max_count):
        return list(filter(lambda x: x.material == mat_name and x.count <= max_count, self.buy_offers))

    def get_sell_offers(self, mat_name, price, max_count):
        if len(self.sell_offers):
            pass
        return list(filter(lambda x: x.material == mat_name and x.price >= price and x.count >= max_count, self.sell_offers))

    def serve(self):
        for orequest in self.sell_offers:
            request = orequest.as_market_offer()
            offers = self.get_buy_offers(request[0], request[2], request[1])
            offers.sort(key=lambda x: x.price)
            if len(offers) > 0:
                offer = offers[0]
                if orequest.price * orequest.count < orequest.company.money:
                    offer.company.pay(orequest.company, offer.price * offer.count)
                    offer.company.ressources += offer.count
                    request.company.ressources -= offer.count
                    self.buy_offers.remove(offer)
                    print(orequest.company, "sold", offer.count, "ressources to", offer.company)
        self.sell_offers = []
        self.buy_offers = []

class Person:
    parent1 = None
    parent2 = None
    spouse = None
    money = 0
    age = 0
    attra = 0
    polal = 500
    bank = None
    position = []

    def __init__(self, minage=14, maxage=99, lifeexp=80, country=None, parent1=None, parent2=None):
        self.new = {}
        self.mstate = 100
        self.lifeexp = gauss(lifeexp, 20)
        hasParents = parent1 and parent2
        self.gender = rbool()
        self.food = 0
        self.employer = None
        self.children = []
        self.companies = []
        self.attraction = {}
        self.oppinion = {}
        Country.id += 1
        self.id = Country.id
        self.country = country
        self.country.people.append(self)
        self.hunger = 0
        if self.gender:
            self.name = Country.get_name("Male")
        else:
            self.name = Country.get_name("Female")
        if hasParents:
            self.eq = avg(parent1.eq, parent2.eq, 0.1)
            self.iq = avg(parent1.iq, parent2.iq, 0.1)
            self.attra = avg(parent1.attra, parent2.attra, 0.1)
            self.polal = avg(parent1.polal, parent2.polal, 0.1)
            self.sur = choice([parent1.sur, parent2.sur])
            #print("Child born: ", self)
        else:
            self.eq = gauss(100, 20)
            self.iq = gauss(100, 20)
            self.age = randint(minage, maxage)
            self.polal = randint(0, 1000)
            self.sur = Country.get_name("Sur")

    def year(self, country):
        self.age += 1
        if self.hunger > 1000:
            if random() > 0.8:
                self.die(self.country)
                #print(self,"starved")
        self.hunger += randint(50, 100)
        if self.hunger > 500:
            if self.food > 0:
                self.hunger -= randint(250,500)
                self.food -= 1
            else:
                self.country.market.open_buy_offer(Offer("Food",4,100,self))
        if self.age > 18:
            if not self.pay(country, self.money * country.vat):
                self.bank = country.get_bank()
            if random() / 3 < 1 / (len(self.companies) + 1.2) and self.money > 100:
                # print("Company time",self.name,self.sur, self.money)
                #print(1 / (len(self.companies) + 0.1), "company starting chance with", len(self.companies), "companies")
                comp = Company(self)
                self.companies.append(comp)
                self.pay(comp, 100)
            if self.employer == None:
                self.country.get_company().request_job(self)
            for child in self.children:
                self.pay(child, self.money * 0.04)
                country.request_child_support(child)
            if len(country.people) == 0:
                return None
            for x in range(50):
                person = choice(country.people)
                if person != self:
                    if person.id in self.attraction:
                        self.attraction[person.id] += self.compatability(person)
                        person.attraction[self.id] += person.compatability(self)
                    else:
                        self.attraction[person.id] = self.compatability(person)
                        person.attraction[self.id] = person.compatability(self)
                    if self.spouse:
                        if self.attraction[self.spouse.id] * 10 < self.attraction[person.id]:
                            self.cheat(person)
                            break
                    else:
                        if self.attraction[person.id] > 2.5 + random() * 2.5:
                            if self.spouse == None and person.spouse == None:
                                self.marry(person)
            if self.spouse:
                self.couple()
            if self.age > self.lifeexp:
                self.die(country)

    def couple(self):
        if random() > 0.8:

            child_had, child = self.have_child(self.spouse)
            if child_had:
                pass#print(self, "Had a child: ", child)
        if random() > 0.95:
            self.attraction[self.spouse.id] -= random() * 2

    def compatability(self, other):
        comp = 0.5
        if self.sur == other.sur:
            comp -= 0.1
        comp -= (1 - (max(self.eq, other.eq) / min(self.eq, other.eq)))
        comp -= (1 - (max(self.eq, other.eq) / min(self.eq, other.eq)))
        comp -= abs(self.polal - other.polal) / 1000
        return comp

    def marry(self, other):
        if random() > 0.75:
            other.spouse = self
            self.spouse = other
            if self.id == 5:
                pass
                # print("Marriage happened: " + self.name + " " + self.sur, other.name + " " + other.sur + " love: " + str(self.attraction[other.id]))

    def divorce(self):
        if self.spouse:
            # print(self, "divorced", self.spouse)
            self.spouse.spouse = None
        self.spouse = None

    def cheat(self, other):
        if self.spouse:
            # print(self, "is cheating on", self.spouse)
            if random() > 0.7:
                child_had, child = self.have_child(other)

                if child_had:
                    if random() > self.spouse.mstate / 105:
                        if random() > 0.50:
                            self.spouse.murder(other)
                            self.spouse.murder(child)
                            print(self.spouse, "Went on a killing spree and then killed themselve")
                            self.spouse.murder(self.spouse)
                            self.die(self.country)

                        else:
                            other.murder(self.spouse)
                    else:
                        self.spouse.divorce()
            elif random() > self.spouse.mstate / 120:
                self.spouse.murder(other)
                if random() > 0.4:
                    self.divorce()
        elif random() > 0.90:
            self.divorce()
            self.marry(other)

    def have_child(self, other):
        if random() > 0.85:
            child = Person(minage=0, maxage=0, country=self.country, parent1=self, parent2=other)
            self.children.append(child)
            self.country.people.append(child)
            return True, child
        return False, None

    def murder(self, other):
        #print(str(self) + " murdered " + str(other))
        other.pay(self, other.money)
        other.die(other.country)
        self.mstate *= (random() + 4) / 5

    def pay(self, other, amount):
        if self.bank:
            self.bank.do_transaction(self, other, amount)
            return True
        return False

    def die(self, country):
        if len(self.children) == 0:
            country.money += self.money
            self.money = 0
        self.divorce()
        if self in country.people:
            country.people.remove(self)

    def __str__(self):
        return self.name + " " + self.sur


class House():
    def __init__(self, rent=5000, price=500000, slots=2, x=5, y=5):
        self.rent = rent
        self.slots = slots
        self.x = x
        self.y = y


class Bank(Company):
    cut = 0.001
    intb = 0.01
    intg = 0.1
    money = 0
    customers = []

    def __init__(self, cut=0.1):
        self.cut = cut

    def do_transaction(self, sender, rec, amount):
        sender.money -= amount
        self.money += amount * self.cut
        amount *= (1 - self.cut)
        rec.money += amount

    def year(self, country):
        pass


Country()
input("press enter key to exit")