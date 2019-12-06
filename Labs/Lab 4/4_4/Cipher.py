#Brandon Kim
#4-4 Cipher


e_dict = {}  # Global Variable; Encryption dictionary
d_dict = {}  # Global Variable; Decryption dictionary


def load_cipher_file(file_name):

    file = open(file_name, "r")

    for name in file:
        name = name.split()
        letter = name[0]
        letter2 = name[1]
        e_dict[letter] = letter2
        d_dict[letter2] = letter


def encrypt_or_decrypt_message(dictionary, msg):
    finalMSG = ""

    for letter in msg.upper():
        if letter in dictionary:
            finalMSG += dictionary[letter]
        else:
            finalMSG += letter
    return finalMSG


def main():
    #open the file
    file_name = input("Enter the filename of the cipher to use.")
    load_cipher_file(file_name)

    user = 1234567654323454345

    while user != "Q":
        user = input("\tE - Encrypt a Message \n\tD - Decrypt a Message \n\tL - Load new chipher key \n\tQ - Quit")
        user = user.upper()

        if user == "E":
            msg = input("Enter your message to be encrypted.")
            a = encrypt_or_decrypt_message(e_dict,msg)
            print(a)

        elif user == "D":
            msg = input("Enter your message to be decrypted.")
            a = encrypt_or_decrypt_message(d_dict,msg)
            print(a)

        elif user == "L":
            file_name = input("Enter the filename of the cipher to use.")
            load_cipher_file(file_name)
            continue

        if user == "Q":
            break

        else:
            print("Pick another answer?")
            continue



    print("\t\t\tGoodbye! Goodbye!")





main()
