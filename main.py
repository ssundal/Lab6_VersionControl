"""
Lab 6
Authors: Shan Sundal and Arin Sareddy
Class: COP3502C
Section: 22282
Description: Github encode decode lab
"""


# THIS IS WHERE SHAN WRITE THE ENCODE FUNCTION

def encoder(password):
    user_password = str(password)
    res = []
    for i in user_password:
        new_number = str(int(i) + 3)
        res.append(new_number)
    return "".join(res)


# code written by arin
# iterates through string and subtracts 3 for every iteration
def decoder(encoded_password):
    encoded_password = str(encoded_password)
    string_result = ''
    for i in encoded_password:
        result = int(i) - 3
        string_result += str(result)
    return string_result


# displays menu and asks user what they want to do
def main():
    continue_program = True
    while continue_program:
        encoded_password = ""
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")

        user_input = int(input("Please enter an option: "))
        # encodes password and stores
        if user_input == 1:
            get_password = input("Please enter your password to encode: ")
            encoded_password = encoder(get_password)
            print("Your password has been encoded and stored!")
            print()
        # decodes password and prints both encoded password and decoded password
        if user_input == 2:
            print(f"The encoded password is {encoder(get_password)}, and the original password is {decoder(encoder(get_password))}.")
            print()
        # exits program
        if user_input == 3:
            continue_program = False


if __name__ == "__main__":
    main()
