
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.gamePriority import GamePriority

class GamePriorityMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [GAME PRIORITY]')

    def _displayMenu(self):
        
        options = [
            "Do All Games From Here",
            "Configure QoS and Tweak GTA5",
            "Configure QoS and Tweak FiveM",
            "Configure QoS and Tweak CS2",
            "Configure QoS and Tweak Apex Legends",
            "Configure QoS and Tweak Fortnite",
            "Configure QoS and Tweak Valorant",
            "Configure QoS For Custom Game (.exe)",
            "Tweak Custom Game (.exe)"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [GAME PRIORITY]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                    GamePriority()._doAll()
                    sleep(2)
                elif choice == 2:
                    print('')
                    GamePriority()._configureQosAndTweakGTA5()
                    sleep(2)    
                elif choice == 3:
                    print('')
                    GamePriority()._configureQosAndTweakFiveM()
                    sleep(2)  
                elif choice == 4:
                    print('')
                    GamePriority()._configureQosAndTweakCS2()  
                elif choice == 5:
                    print('')
                    GamePriority()._configureQosAndTweakApex()
                    sleep(2)  
                elif choice == 6:
                    print('')
                    GamePriority()._configureQosAndTweakFortnite()
                    sleep(2)  
                elif choice == 7:
                    print('')
                    GamePriority()._configureQosAndTweakValorant()  
                elif choice == 8:
                    print('')
                    exe = str(input(f"   {Colors.white}[GAME PRIORITY]{Colors.light_green} Enter the exe name (without .exe):{Colors.white} "))
                    GamePriority()._configureQosForGame(exe)
                    sleep(2)  
                elif choice == 9:
                    print('')
                    exe = str(input(f"   {Colors.white}[GAME PRIORITY]{Colors.light_green} Enter the exe name (without .exe):{Colors.white} "))
                    GamePriority()._tweakGame(exe)
                    sleep(2)  
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   