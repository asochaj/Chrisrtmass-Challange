import random

def gift_selector(all_gifts):

    specific_gifts = []

    while len(specific_gifts) < 3:
        gift = random.choice(all_gifts)

        if gift in specific_gifts:
            pass
        else:
            specific_gifts.append(gift)

    print(f"Gifts: {specific_gifts}")

if __name__ == '__main__':

    all_gifts = ["Perfume", "Socks", "Sweater", "Cup",
                    "Hat", "Tea", "Coffee", "Clock", "Bag",
                    "Book", "Wallet", "Cream", "Earrings"]
    gift_selector(all_gifts)
