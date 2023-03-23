# Gauri Nandihalli

def encoder(password):
    new_string = ""
    for digit in password:
        if int(digit) < 7:
            new_number = int(digit) + 3
            new_string += str(new_number)
        elif digit == '7':
            digit = '0'
            new_string += digit
        elif digit == '8':
            digit = '1'
            new_string += digit
        elif digit == '9':
            digit = '2'
            new_string += digit
    return new_string


if __name__ == "__main__":

    stored_password_encoded = None
    while True:
        print()
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        user_option = int(input("Please enter an option: "))

        if user_option == 1:
            user_password = input("Please enter your password to encode: ")
            print("Your password has been stored!")
            stored_password_encoded = encoder(user_password)

        elif user_option == 2:
            pass

        elif user_option == 3:
            break
