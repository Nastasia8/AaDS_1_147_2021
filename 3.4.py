def main():
    txt()


def txt():
    text = ["Bass", "Pike", "Roach", "Catfish", "Trout", "Mackerel", "Salmon", "Zander", "Anchovy"]
    new_text = []

    for i in text:
        new_text.append(i[-1:])
    new_text.sort()
    new_text = new_text[::-1]

    print(new_text)

main()
