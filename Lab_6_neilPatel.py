# neil pate

def encode(passw):
    string = ""
    passw = list(passw)
    for y in range(len(passw)):
        if passw[y] == "7":
            passw[y] = "0"
            string += passw[y]
            continue
        if passw[y] == "8":
            passw[y] = "1"
            string += passw[y]
            continue
        if passw[y] == "9":
            passw[y] = "2"
            string += passw[y]
            continue
        if passw[y] == "0" or passw[y] == "1" or passw[y] == "2" or passw[y] == "3" or passw[y] == "4" or passw[y] == "5" or passw[y] == "6":
            fake = (int(passw[y]) + 3)
            string += str(fake)
    return string


if __name__ == "__main__":
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        option99 = int(input("Please enter an option: "))
        if option99 == 1:
            option_1 = input("Please enter your password to encode: ") # "12345678"
            encode_password = encode(option_1)
            print("Your password has been encoded and stored!\n")