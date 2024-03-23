
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.debloat import Debloat

class DebloatMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [DEBLOAT]')

    def _displayMenu(self):
        
        options = [
            "Do All",
            "Disable Unneccessary Bloatware",
            "Debloat Chrome",
            "Disable Useless Services (Task Scheduler)"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [DEBLOAT]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                    Debloat()._doAll()
                    sleep(2)
                elif choice == 2:
                    print('')
                    Debloat()._disableUnneccesaryBloatware()
                    sleep(2)    
                elif choice == 3:
                    print('')
                    Debloat()._debloatChrome()
                    sleep(2)  
                elif choice == 4:
                    print('')
                    Debloat()._disableUselessServicesFromTaskScheduler() 
                    sleep(2)
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   