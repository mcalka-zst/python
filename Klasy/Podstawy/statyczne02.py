import os
os.system("cls")

class Person:
    __nr = 0  # pole statyczne

    def __init__(self):
        Person.__nr += 1

    def __del__(self):
        Person.__nr -= 1
        print("Niszczymy osobę %s %s, zostało jeszcze %d" % (self.__firstName, self.__lastName, Person.count()))

    def read(self):
        self.__firstName = input("Podaj imię: ")
        self.__lastName = input("Podaj nazwisko: ")

    def write(self):
        print("%s %s ma nr %d" % (self.__firstName, self.__lastName, Person.count()))

    #metoda statyczna
    def count():
        return Person.__nr

# -----------------------


person1 = Person()
person1.read()
person1.write()
person2 = Person()
person2.read()
person2.write()
person3 = Person()
person3.read()
person3.write()
print("Utworzyłem %d osób" % Person.count())
# print("Utworzyłem %d osób" % Person.__nr) tu będzie błąd
