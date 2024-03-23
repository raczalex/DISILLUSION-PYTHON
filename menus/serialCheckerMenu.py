
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.serialChecker import SerialChecker

class SerialCheckerMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [SERIAL CHECKER]')

    def _displayMenu(self):
        
        options = [
            "Start"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [SERIAL CHECKER]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                    SerialChecker()._start()
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   