class Person:
    count=0
    def __init__(self):
        pass

    def read(self):
        self.__firstName = input("Podaj imię: ")
        self.__lastName = input("Podaj nazwisko: ")

    def write(self):
        print("%s %s" % (self.__firstName, self.__lastName))
# -----------------------


person = Person()
person.read()
person.write()
#print(person.__firstName) będzie błąd