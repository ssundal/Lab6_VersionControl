"""
Lab 6
Authors: Shan Sundal and Arin Sareddy
Class: COP3502C
Section: 22282
Description:
"""


# THIS IS WHERE SHAN WRITE THE ENCODE FUNCTION

def encoder(password):
    user_password = str(password)
    res = []
    for i in user_password:
        new_number = str(int(i) + 3)
        res.append(new_number)
    return "".join(res)


def decode(password):
    pass


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

        if user_input == 1:
            get_password = input("Please enter your password to encode: ")
            encoded_password = encoder(get_password)
            print("Your password has been encoded and stored!")
            print()

        if user_input == 2:
            print(f"The encoded password is {encoder(get_password)}, and the original password is {decode(encoded_password)}.")
            print()

        if user_input == 3:
            continue_program = False


if __name__ == "__main__":
    main()
