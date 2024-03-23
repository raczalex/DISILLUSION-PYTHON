
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.cpu import CPU

class CPUMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [CPU]')

    def _displayMenu(self):
        
        options = [
            "Intel Tweaks (Intel)",
            "Amd Tweaks (Amd)",
            "Disable Away Mode (General)",
            "Enable All Logical Processors (General)",
            "Cooling Tweaks (General)",
            "Optimize DC Values (General)",
            "Optimize AC Values (General)",
            "Disable Core Parking (General)",
            "Fix CPU Stock Speed (Intel)",
            "Fix CPU Stock Speed (Amd)",
            "Disable Throttle States (General)",
            "Set Device Idle Policy To Performance (General)",
            "Configure C-States (General)",
            "Use Higher P-States On Lower C-States (General)",
            "Do Not Restrict Core Boost (General)",
            'Enable Turbo Boost (General)',
            'Disable C-States (General)',
            'Advanced Registry Tweaks (General)',
            "CPU Idle Power Management Tweaks (General)"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [CPU]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                    CPU()._intelCpuTweaks()
                    sleep(2)
                elif choice == 2:
                    print('')
                    CPU()._amdCpuTweaks()
                    sleep(2)    
                elif choice == 3:
                    print('')
                    CPU()._disableAwayMode()
                    sleep(2) 
                elif choice == 4:
                    print('')
                    CPU()._enableAllLogicalProcessors()
                    sleep(2)  
                elif choice == 5:
                    print('')
                    CPU()._cpuCoolingTweaks()
                    sleep(2)  
                elif choice == 6:
                    print('')
                    CPU()._optimizeDCValues()
                    sleep(2)  
                elif choice == 7:
                    print('')
                    CPU()._optimizeACValues()
                    sleep(2)  
                elif choice == 8:
                    print('')
                    CPU()._disableCoreParking()
                    sleep(2)  
                elif choice == 9:
                    print('')
                    CPU()._fixIntelCPUStockSpeed()
                    sleep(2)  
                elif choice == 10:
                    print('')
                    CPU()._fixAMDCPUStockSpeed()
                    sleep(2)  
                elif choice == 11:
                    print('')
                    CPU()._disableThrottleStates()
                    sleep(2) 
                elif choice == 12:
                    print('')
                    CPU()._setDeviceIdlePolicyToPerformance()
                    sleep(2)  
                elif choice == 13:
                    print('')
                    CPU()._configureCStates()
                    sleep(2)  
                elif choice == 14:
                    print('')
                    CPU()._useHigherPStatesOnLowerCStatesVisaVersa()
                    sleep(2)  
                elif choice == 15:
                    print('')
                    CPU()._dontRestrictCoreBoost()
                    sleep(2)  
                elif choice == 16:
                    print('')
                    CPU()._enableTurboBoost()
                    sleep(2)  
                elif choice == 17:
                    print('')
                    CPU()._disableCStates()
                    sleep(2)  
                elif choice == 18:
                    print('')
                    CPU()._advancedCPURegistryTweaks()
                    sleep(2)
                elif choice == 19:
                    print('')
                    CPU()._cpuIdlePowerManagementTweaks()
                    sleep(2)
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   