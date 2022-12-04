all_gifts = ["Parfum", "Socks", "Sweather", "Cup",
                "Hat", "Tea", "Coffee", "Clock", "Bag",
                "Book", "Wallet", "Cream", "Earrings"]


def ascii_encoder(letter):
    return ord(letter)


def binary_encoder(ascii_code):
    return bin(ascii_code)


def santa_encoder(word):
    code = []
    for letter in word:
        ascii_code = ascii_encoder(letter)
        binary_all = binary_encoder(ascii_code)
        binary = binary_all.split(sep="b")[1]
        code.append(binary)
    return code

if __name__ == '__main__':
    for word in all_gifts:
        print(f"Gift '{word}' is: {santa_encoder(word)}")

