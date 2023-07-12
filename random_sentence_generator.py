import random


def get_random_word(words):
    return random.choice(words)


def what_to_add():
    global names, places, verbs, nouns, adverbs, details
    mapping = {
        1: names,
        2: places,
        3: verbs,
        4: nouns,
        5: adverbs,
        6: details
    }
    display = {
        1: "names",
        2: "places",
        3: "verbs",
        4: "nouns",
        5: "adverbs",
        6: "details"
    }
    print("This is the adding function,choose what to add or use [Q] to quit")
    while True:

        entry_string = input("Write [1] to add name, [2] to add place, [3] to add verb, [4] to add noun, "
                             "[5] to add adverb, [6] to add details or Q to quit,"
                             " or [L][number] if u want to add a list of items,separated by spaces " )

        if entry_string.upper() == "Q":
            break
        if "L" in entry_string or "l" in entry_string:
            number = int(entry_string[-1])
            lst = input(f"Enter the list of {display[number]}: ").split()
            mapping[number].extend(lst)
        else:
            number = int(entry_string)
            mapping[number].append(input(f"Enter {display[number]}:"))

names = ["Peter", "Michell", "Jane", "Steve"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park"]
print("Click [Enter] to generate a new one.Or click '!' to add more words.Or 'h' for help")
while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)
    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}")
    a = input()
    if a == "":
        continue
    elif a.upper() == "H":
        print("Click [Enter] to generate a new one.Or click '!' to add more words.Or 'h' for help")
    else:
        what_to_add()
