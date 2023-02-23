def choosing_characters(name, player):
    while len(player) < 5:
        choice = input(f"{name}, in what turns are your characters going to fight (warrior, mage, archer) ?: ")
        if choice == "warrior":
            player.append(warrior.copy())
        elif choice == "mage":
            player.append(mage.copy())
        elif choice == "archer":
            player.append(archer.copy())
    print(f"\n{name} team:")
    for i in player:
        print(f"{i['char']} -- {i['str']} STR and {i['hp']} HP")


def fight():
    c = 0
    while c == 0:
        player1[0]["hp"] = player1[0]["hp"] - player2[0]["str"]
        player2[0]["hp"] = player2[0]["hp"] - player1[0]["str"]
        print(player1[0], "\n", player2[0])
        # fight ends with
        if player1[0]["hp"] <= 0 and player2[0]["hp"] <= 0:
            c += 1
            player1.pop(0)
            player2.pop(0)
            print("We've lost both soldiers")
        elif player1[0]["hp"] <= 0:
            c += 1
            player1.pop(0)
            print(f"{name1}'s soldier is gone")
            if player2[0]["char"] == mage["char"]:
                player2[0]["hp"] = mage["hp"]
                player2[0]["str"] = mage["str"]
            elif player2[0]["char"] == warrior["char"]:
                player2[0]["hp"] = warrior["hp"]
                player2[0]["str"] = warrior["str"]
            elif player2[0]["char"] == archer["char"]:
                player2[0]["hp"] = archer["hp"]
                player2[0]["str"] = archer["str"]
        elif player2[0]["hp"] <= 0:
            c += 1
            player2.pop(0)
            print(f"{name2}'s soldier is gone")
            if player1[0]["char"] == mage["char"]:
                player1[0]["hp"] = mage["hp"]
                player1[0]["str"] = mage["str"]
            elif player1[0]["char"] == warrior["char"]:
                player1[0]["hp"] = warrior["hp"]
                player1[0]["str"] = warrior["str"]
            elif player1[0]["char"] == archer["char"]:
                player1[0]["hp"] = archer["hp"]
                player1[0]["str"] = archer["str"]


def rules_and_fight():
    while len(player1) > 0 and len(player2) > 0:
        if player1[0]["char"] == "warrior" and player2[0]["char"] == "mage":
            player1[0]["str"] = player1[0]["str"] * 1.5
        elif player1[0]["char"] == "archer" and player2[0]["char"] == "mage":
            player2[0]["str"] = player2[0]["str"] * 1.5
        elif player1[0]["char"] == "warrior" and player2[0]["char"] == "archer":
            player2[0]["str"] = player2[0]["str"] * 1.5
        elif player2[0]["char"] == "warrior" and player1[0]["char"] == "mage":
            player2[0]["str"] = player2[0]["str"] * 1.5
        elif player2[0]["char"] == "archer" and player1[0]["char"] == "mage":
            player1[0]["str"] = player1[0]["str"] * 1.5
        elif player2[0]["char"] == "warrior" and player1[0]["char"] == "archer":
            player1[0]["str"] = player1[0]["str"] * 1.5
        fight()


def result(one, two):
    if len(one) > len(two):
        print(f"{name1}'s team has won! Here are some leftovers: ")
        for i in one:
            print(f"{i['char']} -- {i['str']} STR and {i['hp']} HP")
    elif len(two) > len(one):
        print(f"{name2}'s team has won! Here are some leftovers: ")
        for i in two:
            print(f"{i['char']} -- {i['str']} STR and {i['hp']} HP")
    else:
        print("There are no winners! Everybody is dead!")


if __name__ == "__main__":
    warrior = {"char": "warrior", "str": 20, "hp": 100}
    mage = {"char": "mage", "str": 50, "hp": 50}
    archer = {"char": "archer", "str": 40, "hp": 70}

    player1 = []
    player2 = []

    name1 = input("Player one, what is your name? ")
    choosing_characters(name1, player1)

    name2 = input("\nPlayer two, what is your name? ")
    choosing_characters(name2, player2)

    rules_and_fight()
    result(player1, player2)
