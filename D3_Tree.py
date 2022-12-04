
def get_heights(tree_height):

    trunk_height = tree_height // 4
    body_height = tree_height - trunk_height

    return trunk_height, body_height

def print_tree(tree_height, trunk_height ,body_height ,sign):

    width = tree_height + len(sign)
    for branch in range(1 ,body_height +1):
        spaces_number = int((width - (branch * len(sign) ) /2))

        if branch == 1:
            print(spaces_number * " ", end = "")
            print(branch * " *", end = "")
            print(spaces_number * " ")
        else:

            print(spaces_number * " ", end = "")
            print(branch * sign, end = "")
            print(spaces_number * " ")

    for unit in range(trunk_height):
        trunk_width = 3
        spaces_number = int((width *2 - trunk_width ) /2)
        print(spaces_number * " ", end = "")
        print(trunk_width * "|")

def main():

    tree_height = 15
    trunk_height, body_height = get_heights(tree_height)
    sign = "*x*"
    print_tree(tree_height,trunk_height ,body_height ,sign)

if __name__ == '__main__':
    main()