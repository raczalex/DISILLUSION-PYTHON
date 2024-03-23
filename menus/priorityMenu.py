
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.priority import Priority

class PriorityMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [PRIORITY]')

    def _displayMenu(self):
        
        options = [
            "Do All",
            "Advanced Priority Tweaks",
            "Win32 Priority Separation"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [PRIORITY]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                    Priority()._doAll()
                    sleep(2)
                elif choice == 2:
                    print('')
                    Priority()._advancedPriorityTweaks()  
                    sleep(2)  
                elif choice == 3:
                    print('')
                    Priority()._win32PrioritySeparation()  
                    sleep(2)
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   