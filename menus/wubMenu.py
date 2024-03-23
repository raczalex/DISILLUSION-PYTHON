
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.wub import WUB

class WUBMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [WUB]')

    def _displayMenu(self):
        
        options = [
            "Enable WUB (x64)",
            "Enable WUB (x86)",
            "Disable WUB (x64)",
            "Disable WUB & Protect Services (x64)",
            "Disable WUB (x86)",
            "Disable WUB & Protect Services (x86)"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [WUB]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                    WUB()._enableWUBx64()
                    sleep(2)    
                elif choice == 2:
                    print('')
                    WUB()._enableWUBx86()
                    sleep(2)  
                elif choice == 3:
                    print('')
                    WUB()._disableWUBx64()
                    sleep(2)  
                elif choice == 4:
                    print('')
                    WUB()._disableWUBx64Protect()
                    sleep(2)  
                elif choice == 5:
                    print('')
                    WUB()._disableWUBx86()
                    sleep(2)  
                elif choice == 6:
                    print('')
                    WUB()._disableWUBx86Protect()
                    sleep(2)  
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   