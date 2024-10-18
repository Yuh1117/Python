myDict = dict()


def add_word(word, meaning):
    if word not in myDict.keys():
        myDict.setdefault(word, meaning)


def display():
    count = 0
    for key, value in myDict.items():
        print(f"{key} - {value}")
        count += 1
    print("So tu trong tu dien: ", count)


def word_search(word):
    if word.capitalize() in myDict.keys():
        print(f"{word.capitalize()} - {myDict[word.capitalize()]}")
    else:
        print("Khong tim thay")

def delete_word(word):
    del myDict[word.capitalize()]

if __name__ == '__main__':
    add_word("Car", "Xe oto")
    add_word("Computer", "May tinh")
    add_word(meaning="Mau xanh la", word="Green")
    display()
    print("-------")
    word_search("car")
    print("-------")
    delete_word("car")
    print(myDict)


