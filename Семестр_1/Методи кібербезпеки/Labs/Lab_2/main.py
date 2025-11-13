import math

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


class Main:
    def __init__(self, value="",key=""):
        self.__value = str(value)
        self.__key = str(key)

    def get_value(self):
        return str(self.__value)

    def get_key(self):
        return str(self.__key)


    def set_value(self, value):
        self.__value = str(value)

    def set_key(self, value):
        self.__key = str(value)

    def __str__(self):
        return f"The text:\"{self.__value}\".\nThe key:\"{self.__key}\"."


def input_text(value):
    temp = input("Enter the text: ")
    value.set_value(temp)

def input_key(value):
    temp = input("Enter the key: ")
    value.set_key(temp)

def encrypt(value):
    temp = str(input("Use Caesar cipher or XOR? (c/x):")).lower().replace(' ', '')
    if temp == 'c':
        in_caesar(value)
    elif temp == "x":
        in_xor(value)
    else:
        print("\nYour choice is wrong!")

def decrypt(value):
    temp = str(input("Use Caesar cipher or XOR? (c/x):")).lower().replace(' ', '')
    if temp == 'c':
        out_caesar(value)
    elif temp == "x":
        out_xor(value)
    else:
        print("\nYour choice is wrong!")

def menu(value):

    while True:
        print("\n\nMenu:\n")
        print("1.Enter the text.")
        print("2.Enter the key.")
        print("3.Encrypt.")
        print("4.Decrypt.")
        print("5.Show the text and the key.")
        print("6.Exit")

        try:
            choice = int(input("\nYour choice: "))
        except Exception:
            print("\nInvalid choice.")
            continue


        if choice == 1:
            input_text(value)
        if choice == 2:
            input_key(value)
        if choice == 3:
            encrypt(value)
        if choice == 4:
            decrypt(value)
        if choice == 5:
            print(f"\n{value}")
        if choice == 6:
            print("\n\nExit...\n\n")
            break

def in_caesar(value):

    try:
        value.set_key(int(str(value.get_key()).lower().replace(' ','')))
    except Exception:
        print("\nThe key is invalid. The key must be an integer.")
        value.set_key(0)

    if int(value.get_key()) == 0:
        print(value)
        return

    new_text = ""
    for temp in value.get_value():

        if temp in numbers:
            for i, char in enumerate(numbers):
                if char == temp:
                    new_text += f"{numbers[(i + int(value.get_key())) % len(numbers)]}"


        elif temp.upper() in alphabet:
                if temp.isupper():

                    for i, char in enumerate(alphabet):
                        if char == temp:
                            new_text += f"{alphabet[(i + int(value.get_key())) % len(alphabet)]}"

                else:

                    temp = temp.upper()

                    for i, char in enumerate(alphabet):
                        if char == temp:
                            new_text += f"{str(alphabet[(i + int(value.get_key())) % len(alphabet)]).lower()}"

        else: new_text += temp


    value.set_value(new_text)
    print(value)


def in_xor(value):
    text = value.get_value()
    key = value.get_key()

    result = ""

    i=0
    for char in text:
        if i == len(key):
            i = 0

        result += f"{chr(ord(char)^ord(key[i]))}"
        i+=1


    value.set_value(result)
    print(value)

def out_caesar(value):
    try:
        value.set_key(int(str(value.get_key()).lower().replace(' ', '')))
    except Exception:
        print("\nThe key is invalid. The key must be an integer.")
        value.set_key(0)

    if int(value.get_key()) == 0:
        print(value)
        return

    value.set_key(-int(value.get_key()))

    new_text = ""
    for temp in value.get_value():
        if temp in numbers:
            for i, char in enumerate(numbers):
                if char == temp:
                    new_text += f"{numbers[(i + int(value.get_key())) % len(numbers)]}"


        elif temp.upper() in alphabet:
            if temp.isupper():

                for i, char in enumerate(alphabet):
                    if char == temp:
                        new_text += f"{alphabet[(i + int(value.get_key())) % len(alphabet)]}"

            else:

                temp = temp.upper()

                for i, char in enumerate(alphabet):
                    if char == temp:
                        new_text += f"{str(alphabet[(i + int(value.get_key())) % len(alphabet)]).lower()}"

        else:
            new_text += temp

    value.set_key(-int(value.get_key()))
    value.set_value(new_text)
    print(value)

def out_xor(value):
    in_xor(value)

if __name__ == "__main__":
    for i in range(50):
        print(f"sqrt({i}) = {math.sqrt(i)}")
    '''
    main = Main()
    menu(main)
   
    for i in range(1000):
        print(f"{i}.\t({chr(i)})")
    '''

