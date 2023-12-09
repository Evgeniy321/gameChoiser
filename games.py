from random import randint
from time import sleep
from collections import defaultdict
import os

def writeGames(games: dict) -> None:
    file = open('list.txt', 'w')
    file.writelines([f'{i}({key})\n' for key,glf in games.items() for i in glf])
    file.close()

def choiceGame(games: dict, pause: float) -> str:
    gamelist = [f'{i}({key})' for key,glf in games.items() for i in glf]
    length = len(gamelist)
    print(f"\n\nThere are {length} games:\n\n---------------------------------\n\n")
    while length > 1:
        game = gamelist[randint(0, length-1)]
        sleep(pause)
        print(f"games left {length} drops out{' ' if length < 10 else ''}: {game}")
        gamelist.remove(game)
        length = len(gamelist)

    print(f"\n---------------------------\n\nwinner is: {gamelist[0]}\n\n")
    return gamelist[0]

def selectGames() -> dict:
    listOfFolders = list(filter(lambda x: x != '',[i if i.find('.') == -1 else '' for i in os.listdir('.')]))
    games = {}
    for folder in listOfFolders:
        if folder != 'launchers':
            listOfFiles = list(filter(lambda x: x != '',[i[:i.find('.')] if i.find('Настройки') == -1 else '' for i in os.listdir(f'{folder}/.')]))
            games[folder] = listOfFiles

    return games


def main() -> None:
    games = selectGames()
    winners = defaultdict(lambda:0,{})
    delay = float(input("Enter delay from delete: "))
    while input("tab Enter (other key to quit): ") == '':
        if len(games) > 1:
            writeGames(games)
        else:
            games = [i[:-1] for i in open('list.txt', 'r').readlines()]
        winner = choiceGame(games, delay)
        winners[winner]+=1

        
    print("liderboard")
    total = 0
    winners = dict(sorted(winners.items(), key=lambda x:x[1])[::-1])
    maxStr = max([len(i) for i in winners.keys()])
    for key, val in winners.items():
        print(f"{(maxStr+6)*'-'}\n|{key} {' '*(maxStr - len(key))}: {val}|")
        total+= val
    print(f"{(maxStr+6)*'-'}\n|total {' '*(maxStr - 5)}: {total}|\n{(maxStr+7)*'-'}\n")
        

if __name__ == '__main__':
    main()