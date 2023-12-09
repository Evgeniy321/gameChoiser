import os

def selectGames() -> dict:
    listOfFolders = list(filter(lambda x: x != '',[i if i.find('.') == -1 else '' for i in os.listdir('.')]))
    games = {}
    for folder in listOfFolders:
        if folder != 'launchers':
            listOfFiles = list(filter(lambda x: x != '',[i[:i.find('.')] if i.find('Настройки') == -1 else '' for i in os.listdir(f'{folder}/.')]))
            games[folder] = listOfFiles

    return games

games = selectGames()
gamelist = [f'{key} : {i}' for key,glf in games.items() for i in glf]
print(gamelist)