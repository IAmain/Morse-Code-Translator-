encoding = {}
decoding = {}
f = open("morse.txt", 'r')


def menu():
    print("This program will allow you to translate text to morse code or translate morse code to text.")
    print("Pick one of the options below")
    print("*** Enter 't' for encoding the text")
    print("*** Enter 'm' for decoding the morse code")
    print("*** Enter 'e' to exit the program")



def morse(encoding, decoding):
    for line in f:
        key, value = line.split()  # splitting the line in the file into 2 for encoding and decoding
        encoding[key] = value  # in dict the key is the English letter and the value is the cipher code
        decoding[value] = key

def encrypt(userInput, encoding):
    encoding = encoding
    encryption = ""
    for char in userInput:
        encryption = encryption + encoding[char.upper()]
    return encryption


def decrypt(userInput, decoding):
    decoding = decoding
    decryption = ""
    for char in userInput:
        decryption = decryption + decoding[char] + ' '
    return decryption


def main():
    morse(encoding, decoding)
    menu()
    option = input("My input is: ")
    while option != 't' or option != 'm' or option != 'e':
        if option == 't':
            userInput = input("Enter text to translate ").replace(" ","")
            print(encrypt(userInput,encoding))
            menu()
            option = input("My input is: ")

        elif option == 'm':
            userInput = input("Enter text to translate ").split()
            print(decrypt(userInput, decoding))
            menu()
            option = input("My input is: ")

        elif option == 'e':  # if option is e, then exit the program
            print("Thank you for using the program")
            break

        elif option != 't' or option != 'm' or option != 'e':
            print("**invalid option")
            menu()
            option = input("My input is: ")

main()
f.close()
