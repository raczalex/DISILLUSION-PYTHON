
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.keyboard import Keyboard

class KeyboardMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [KEYBOARD]')

    def _displayMenu(self):
        
        options = [
            "Do All Except Data Queue Size",
            "Disable Filter Keys",
            "Disable Toggle Keys",
            "Disable Sticky Keys",
            "Optimize Keyboard Thread Priority",
            "Reduce Keyboard Repeat Delay",
            "Increase Keyboard Repeat Rate",
            "Enable Num Lock On Start Up",
            "Set Keyboard Data Queue Size To (19)",
            "Set Keyboard Data Queue Size To (21)",
            "Set Keyboard Data Queue Size To (23)",
            "Set Keyboard Data Queue Size To (32)",
            "Set Keyboard Data Queue Size To (37)",
            "Set Keyboard Data Queue Size To (48)",
            "Set Keyboard Data Queue Size To (Default)",
            "Set Keyboard Data Queue Size To (Custom)"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [KEYBOARD]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                    Keyboard()._doAll()
                    sleep(2)
                elif choice == 2:
                    print('')
                    Keyboard()._disableFilterKeys()
                    sleep(2)   
                elif choice == 3:
                    print('')
                    Keyboard()._disableToggleKeys()
                    sleep(2)  
                elif choice == 4:
                    print('')
                    Keyboard()._disableStickyKeys()
                    sleep(2)  
                elif choice == 5:
                    print('')
                    Keyboard()._optimizeKeyboardThreadPriority()
                    sleep(2)  
                elif choice == 6:
                    print('')
                    Keyboard()._reduceKeyboardRepeatDelay()
                    sleep(2)  
                elif choice == 7:
                    print('')
                    Keyboard()._increaseKeyboardRepeatRate()
                    sleep(2)  
                elif choice == 8:
                    print('')
                    Keyboard()._enableNumLockOnStartup()
                    sleep(2)  
                elif choice == 9:
                    print('')
                    Keyboard()._setKeyboardDataQueueSizeTo19()
                    sleep(2)  
                elif choice == 10:
                    print('')
                    Keyboard()._setKeyboardDataQueueSizeTo21()
                    sleep(2)  
                elif choice == 11:
                    print('')
                    Keyboard()._setKeyboardDataQueueSizeTo23()
                    sleep(2)   
                elif choice == 12:
                    print('')
                    Keyboard()._setKeyboardDataQueueSizeTo32()
                    sleep(2)  
                elif choice == 13:
                    print('')
                    Keyboard()._setKeyboardDataQueueSizeTo37()
                    sleep(2)  
                elif choice == 14:
                    print('')
                    Keyboard()._setKeyboardDataQueueSizeTo48()
                    sleep(2)  
                elif choice == 15:
                    print('')
                    Keyboard()._setKeyboardDataQueueSizeToDefault()
                    sleep(2) 
                elif choice == 16:
                    print('')
                    queue_size = int(input(f"   {Colors.white}[KEYBOARD]{Colors.light_green} Enter the Data Queue Size (default = 80):{Colors.white} "))
                    Keyboard()._setKeyboardDataQueueSize(queue_size)
                    sleep(2)  
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   