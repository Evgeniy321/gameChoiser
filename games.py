from random import randint
from time import sleep
from collections import defaultdict
import os

def writeGames(games):
    file = open('list.txt', 'w')
    file.writelines([i+'\n' for i in games])
    file.close()

def choiceGame(games, pause):
    length = len(games)
    print(f"\n\nThere are {length} games:\n\n---------------------------------\n\n")
    while length > 1:
        game = games[randint(0, length-1)]
        sleep(pause)
        print(f"games left {length} drops out{' ' if length < 10 else ''}: {game}")
        games.remove(game)
        length = len(games)

    print(f"\n---------------------------\n\nwinner is: {games[0]}\n\n")
    return games[0]

def selectGames():
    listOfFolders = list(filter(lambda x: x != '',[i if i.find('.') == -1 else '' for i in os.listdir('.')]))
    games = []
    for folder in listOfFolders:
        listOfFiles = list(filter(lambda x: x != '',[i[:i.find('.')] if i.find('Настройки') == -1 else '' for i in os.listdir(f'{folder}/.')]))
        games += listOfFiles

    games.remove('Steam')
    games.remove('Arc')
    return games


def main():
    games = selectGames()
    winners = defaultdict(lambda:0,{})
    delay = float(input("Enter delay from delete: "))
    while input("tab Enter to continue or repeat: ") == '':
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
        print(f"{(maxStr+7)*'-'}\n|{key} {' '*(maxStr - len(key))}: {val}|")
        total+= val
    print(f"{(maxStr+7)*'-'}\n|total {' '*(maxStr - 5)}: {total}|\n{(maxStr+7)*'-'}\n")
        

if __name__ == '__main__':
    main()