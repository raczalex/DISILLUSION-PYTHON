
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.mouse import Mouse

class MouseMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [MOUSE]')

    def _displayMenu(self):
        
        options = [
            "Do All Except Data Queue Size",
            "Disable Mouse Keys",
            "Optimize Mouse HID",
            "Enable 1:1 Pixel Movements",
            "Disable Mouse Smoothing",
            "Optimize Mouse Thread Priority",
            "Set CRSS To Real Time",
            "Set CSRSS To Real Time",
            "Optimize Mouse Settings",
            "Set Mouse Data Queue Size To (19)",
            "Set Mouse Data Queue Size To (21)",
            "Set Mouse Data Queue Size To (23)",
            "Set Mouse Data Queue Size To (32)",
            "Set Mouse Data Queue Size To (37)",
            "Set Mouse Data Queue Size To (48)",
            "Set Mouse Data Queue Size To (Default)",
            "Set Mouse Data Queue Size To (Custom)"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [MOUSE]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                    Mouse()._doAll()
                    sleep(2)
                elif choice == 2:
                    print('')
                    Mouse()._disableMouseKeys()
                    sleep(2)
                elif choice == 3:
                    print('')
                    Mouse()._mouseHIDOptimize()
                    sleep(2)  
                elif choice == 4:
                    print('')
                    Mouse()._enable1on1PixelMovements()
                    sleep(2)  
                elif choice == 5:
                    print('')
                    Mouse()._disableMouseSmoothing()
                    sleep(2)  
                elif choice == 6:
                    print('')
                    Mouse()._optimizeMouseThreadPriority()
                    sleep(2)  
                elif choice == 7:
                    print('')
                    Mouse()._setCRSSToRealtime()  
                    sleep(2)
                elif choice == 8:
                    print('')
                    Mouse()._setCSRSSToRealTime()
                    sleep(2)  
                elif choice == 9:
                    print('')
                    Mouse()._optimizeMouseSettingsControlPanel()
                    sleep(2)  
                elif choice == 10:
                    print('')
                    Mouse()._setMouseDataQueueSizeTo19()
                    sleep(2)  
                elif choice == 11:
                    print('')
                    Mouse()._setMouseDataQueueSizeTo21()
                    sleep(2)
                elif choice == 12:
                    print('')
                    Mouse()._setMouseDataQueueSizeTo23()
                    sleep(2)
                elif choice == 13:
                    print('')
                    Mouse()._setMouseDataQueueSizeTo32()
                    sleep(2)
                elif choice == 14:
                    print('')
                    Mouse()._setMouseDataQueueSizeTo37()
                    sleep(2)
                elif choice == 15:
                    print('')
                    Mouse()._setMouseDataQueueSizeTo48()
                    sleep(2)
                elif choice == 16:
                    print('')
                    Mouse()._setMouseDataQueueSizeToDefault()
                    sleep(2)
                elif choice == 17:
                    print('')
                    queue_size = int(input(f"   {Colors.white}[MOUSE]{Colors.light_green} Enter the Data Queue Size (default = 80):{Colors.white} "))
                    Mouse()._setMouseDataQueuSize(queue_size)
                    sleep(2)  
                elif choice == 18:
                    ''  
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   