import os
from menus.mainMenu import MainMenu

if __name__ == '__main__':
    os.system("mode con cols=175 lines=40")
    main = MainMenu()
    main._displayMenu()