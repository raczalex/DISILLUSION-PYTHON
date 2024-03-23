
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.usb import USB

class USBMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [USB]')

    def _displayMenu(self):
        
        options = [
            "Do All",
            "Disable Hidden USB Power Savings",
            "USB Controller Priority",
            "Enable MSI For Controller",
            "Disable USB Power Savings & Selective Suspend",
            "USB Thread Priority",
            "DirectX Tweaks"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [USB]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                    USB()._doAll()
                    sleep(2)
                elif choice == 2:
                    print('')
                    USB()._disableHiddenUsbPowerSavings()
                    sleep(2)    
                elif choice == 3:
                    print('')
                    USB()._usbControllerPriority()
                    sleep(2)  
                elif choice == 4:
                    print('')
                    USB()._enableMSIForController()
                    sleep(2)  
                elif choice == 5:
                    print('')
                    USB()._usbPowerSavingsDisableSelectiveSuspendAndMore()
                    sleep(2)  
                elif choice == 6:
                    print('')
                    USB()._usbThreadPriority()
                    sleep(2)  
                elif choice == 7:
                    print('')
                    USB()._directXTweak()
                    sleep(2)  
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   