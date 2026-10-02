# class Tamagotchi:
#     def __init__(self, name):
#         self.name = name
#         self.hunger = 50
#         self.happiness = 50
#         self.is_alive = True

#     def _check_alive(self):
#         if self.hunger >= 100 or self.happiness <= 0:
#             self.is_alive = False
#         if not self.is_alive:
#             print(f"{self.name} больше не с нами... 😢")
#         return self.is_alive

#     def feed(self):
#         if not self._check_alive():
#             return
#         self.hunger = max(0, self.hunger - 20)
#         self.happiness = max(0, self.happiness - 5)
#         print(f"{self.name} поел 🍖")

#     def play(self):
#         if not self._check_alive():
#             return
#         self.happiness = min(100, self.happiness + 20)
#         self.hunger = min(100, self.hunger + 15)
#         print(f"{self.name} поиграл 🎾")
#         self._check_alive()

#     def tick(self):
#         if not self._check_alive():
#             return
#         self.hunger = min(100, self.hunger + 10)
#         self.happiness = max(0, self.happiness - 10)
#         self._check_alive()

#     def status(self):
#         if not self._check_alive():
#             return
#         print(f"{self.name}: голод {self.hunger}, счастье {self.happiness}")


# # --- Играем! ---
# pet = Tamagotchi("Пиксель")




# while True:
#     n = int(input("1) Status \n2)Play\n3)Feed\n4)Tick\n0)Kill pet\nChouse one: "))
#     match n:

#         case 1:
#             pet.status()
#         case 2:
#             pet.play()
#         case 3:
#             pet.feed()
#         case 4:
#             pet. tick()
#         case 0:
#             print ("You kill own pet!")
#             break
#         case _:
#             print("Invalid input")









# import random


# class Hero:
#     def __init__(self, name):
#         self.name = name
#         self.health = 100
#         self.power = 10

#     def attack(self, other):
#         other.health -= self.power

#     def is_alive(self):
#         return self.health > 0


# class Warrior(Hero):
#     def __init__(self, name):
#         super().__init__(name)
#         self.power = 15


# class Mage(Hero):
#     def __init__(self, name):
#         super().__init__(name)
#         self.power = 20

#     def attack(self, other):
#         if random.random() < 0.5:
#             print(f"{self.name} промахнулся! ✨")
#         else:
#             super().attack(other)


# class Healer(Hero):
#     def __init__(self, name):
#         super().__init__(name)
#         self.power = 5

#     def heal(self):
#         self.health = min(100, self.health + 15)
#         print(f"{self.name} лечится 💚 (+15 HP)")


# def battle(hero1, hero2):
#     round_num = 1

#     while hero1.is_alive() and hero2.is_alive():
#         print(f"--- Раунд {round_num} ---")
#         hero1.attack(hero2)

#         if hero2.is_alive():
#             hero2.attack(hero1)

#         round_num += 1

#     if hero1.is_alive():
#         print(f"🏆 Победил {hero1.name}!")
#     else:
#         print(f"🏆 Победил {hero2.name}!")

# while True:
#     a = int(input("""
# 1) Battle
# 2) Exit
# Choose one: """))

#     if a == 1:
#         print("Mage\nHero\nHealer\nWarrior")
#         a = input("Введите своего воина: ")

#         if a != "Mage" and a != "Hero" and a != "Healer" and a != "Warrior":
#             print("Такого воина нет!")
#             continue

#         print("Mage\nHero\nHealer\nWarrior")
#         b = input("Введите второго воина: ")

#         if b != "Mage" and b != "Hero" and b != "Healer" and b != "Warrior":
#             print("Такого воина нет!")
#             continue

#         if a == "Mage":
#             a = Mage("Mage1")
#         elif a == "Hero":
#                 a = Hero("Hero1")
#         elif a == "Healer":
#              a = Healer("Healer1")
#         elif a == "Warrior":
#              a = Warrior("Warrior1")

#         if b == "Mage":
#               b = Mage("Mage1")
#         elif b == "Hero":
#              b = Hero("Hero1")
#         elif b == "Healer":
#                b = Healer("Healer1")
#         elif b == "Warrior":
#              b = Warrior("Warrior1")

#         battle(a, b)

#     elif a == 2:
#         break

#     else:
#         print("Invalid input!!!!")







# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"{self.name} — {self.price} руб."


# class Cart:
#     def __init__(self):
#         self.items = []

#     def add(self, product, quantity=1):
#         for _ in range(quantity):
#             self.items.append(product)

#     def total(self):
#         result = 0
#         for item in self.items:
#             result += item.price
#         return result

#     def remove(self, name):
#         for item in self.items:
#             if item.name == name:
#                 self.items.remove(item)
#                 return
#         print(f"Товара «{name}» нет в корзине")

#     def checkout(self):
#         print("===== ЧЕК =====")
#         for item in self.items:
#             print(item)
#         print("---------------")
#         print(f"ИТОГО: {self.total()} руб.")


# a = Cart()






# while True:
#     n = int(input("""
# 1)Add_tovar
# 2)checout"""))
#     if n==1:
#         a1 = input("Введите имя товара: ")
#         b = int(input("Введите цену тавара: "))
#         c = int(input("Введите количество етого товара: "))
#         a.add(Product(a1, b), quantity=c)
#     elif n==2:
#         a.checkout()
#         break
#     else:
#         print("Erro input!!")

























# class BankAccount:
#     def __init__(self, owner):
#         self.owner = owner
#         self.balance = 0
#         self.history = []

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             self.history.append(f"+{amount} руб.")

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Сумма снятия должна быть больше нуля!")
#         elif amount > self.balance:
#             self.history.append(f"ОТКАЗ: попытка снять {amount} руб.")
#             print("Недостаточно средств!")
#         else:
#             self.balance -= amount
#             self.history.append(f"-{amount} руб.")




#     def show_history(self):
#         print(f"История счёта {self.owner}:")
#         for i, op in enumerate(self.history, 1):
#             print(f"{i}. {op}")



# class SavingsAccount(BankAccount):
#     def __init__(self, owner, rate=0.05):
#         super().__init__(owner)
#         self.rate = rate

#     def add_interest(self):
#         interest = self.balance * self.rate
#         self.balance += interest
#         self.history.append(f"Проценты: +{interest:.0f} руб.")

#     def withdraw(self, amount):
#         if amount > self.balance / 2:
#             self.history.append(
#                 f"ОТКАЗ: лимит снятия (запрошено {amount})"
#             )
#             print("Нельзя снять больше половины баланса!")
#         else:
#             super().withdraw(amount)


# acc = SavingsAccount("Ehson")




# while True:
#     a=int(input("""
# 1)deposit
# 2)withdraw
# 3)add_intrest
# 4)show_history
# """))
#     if a==1:
#         a = int(input("Ввелите сумму пополнение: "))
#         acc.deposit(a)
#     elif a==2:
#         a = int(input("Ввелите сколко хоитите снят! "))
#         acc.withdraw(a)
#     elif a==3:
#         acc.add_interest()
#     elif a==4:
#         acc.show_history()
#     else:
#         print("Eror input!!!")







# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_available = True


# class Reader:
#     def __init__(self, name):
#         self.name = name
#         self.books = []


# class Library:
#     def __init__(self):
#         self.catalog = []

#     def add_book(self, book):
#         self.catalog.append(book)

#     def _find(self, title):
#         for book in self.catalog:
#             if book.title == title:
#                 return book
#         return None

#     def lend(self, book_title, reader):
#         book = self._find(book_title)

#         if book is None:
#             print("Такой книги нет")
#         elif not book.is_available:
#             print("Книга занята")
#         elif len(reader.books) >= 3:
#             print("Верните сначала что-нибудь")
#         else:
#             book.is_available = False
#             reader.books.append(book)
#             print(f"{reader.name} взял «{book.title}»")

#     def take_back(self, book_title, reader):
#         for book in reader.books:
#             if book.title == book_title:
#                 book.is_available = True
#                 reader.books.remove(book)
#                 print(f"{reader.name} вернул «{book.title}»")
#                 return
#         print(f"У {reader.name} нет этой книги")

#     def show_available(self):
#         print("Свободные книги:")
#         for book in self.catalog:
#             if book.is_available:
#                 print(f"  {book.title} — {book.author}")






# lib = Library()




# while True:
#     a = int(input("""
# 1)add_book
# 2)find_book
# 3)lend
# 4)take_back
# 5)show_availibl"""))
#     if a==1:
#         a = input("Введите имя книги: ")
#         lib.add_book(a)
#     elif a==2:
#         a1 = input("Введите имя книги: ")
#         lib._find(a1)
#     elif a==3:
#         a2 = input("Введите имя книги: ")
#         a3 = input("Введите имя читателя: ")
#         lib.lend(a2, a3)
#     elif a==4:
#         a2 = input("Введите имя книги: ")
#         a3 = input("Введите имя читателя: ")
#         lib.take_back(a2,a3)

#     elif a==5:
#         lib.show_available()
#     else:
#         print("Invlid input!!!")














