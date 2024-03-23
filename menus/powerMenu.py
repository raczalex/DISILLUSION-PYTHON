
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.power import Power

class PowerMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [POWER]')

    def _displayMenu(self):
        
        options = [
            "Do All Except Delete Default PP",
            "Disable Storage Power Savings",
            "Disable Timer Coalescing",
            "Delete Default Power Plans",
            "Disable Power Saving On Devices",
            "Disable Gpu Energy Driver",
            "Disable Storage Power Management",
            "Disable Idle Power Management",
            "Disable Link Power Management",
            "Import Disillusion Power Plans",
            "Additional Power Tweaks",
            "Windows Power Settings Tweaks",
            "Enable KBoost",
            "Enable Hardware P-States",
            "Disable Power Throttling",
            'Coalescing Timer Interval',
            'MMCSS Power Tweaks',
            'Disable Power Estimation And Telemetry',
            "Disable Hibernation",
            "Disable Sleep Study",
            "Disable Fast Startup",
            "Unhide Hidden Power Plan Settings"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [POWER]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                elif choice == 2:
                    print('')
                    Power()._disableStoragePowerSavings()
                    sleep(2)    
                elif choice == 3:
                    print('')
                    Power()._disableTimerCoalescing()
                    sleep(2)  
                elif choice == 4:
                    print('')
                    Power()._deleteDefaultPowerPlans()
                    sleep(2)  
                elif choice == 5:
                    print('')
                    Power()._disablePowerSavingOnDevices()
                    sleep(2) 
                elif choice == 6:
                    print('')
                    Power()._disableGpuEnergyDriver()
                    sleep(2) 
                elif choice == 7:
                    print('')
                    Power()._disableStoragePowerManagement()
                    sleep(2) 
                elif choice == 8:
                    print('')
                    Power()._disableIdlePowerManagement()
                    sleep(2) 
                elif choice == 9:
                    print('')
                    Power()._disableLinkPowerManagement()
                    sleep(2) 
                elif choice == 10:
                    print('')
                    Power()._importDisillusionPowerPlans()
                    sleep(2)  
                elif choice == 11:
                    print('')
                    Power()._additionalPowerTweaks()
                    sleep(2) 
                elif choice == 12:
                    print('')
                    Power()._tweakWindowsPowerSettings()
                    sleep(2) 
                elif choice == 13:
                    print('')
                    Power()._enableKBoost()
                    sleep(2) 
                elif choice == 14:
                    print('')
                    Power()._enableHardwarePStates()
                    sleep(2) 
                elif choice == 15:
                    print('')
                    Power()._disablePowerThrottling()
                    sleep(2) 
                elif choice == 16:
                    print('')
                    Power()._coalescingTimerInterval()
                    sleep(2) 
                elif choice == 17:
                    print('')
                    Power()._MMCSSPowerTweaks()
                    sleep(2)
                elif choice == 18:
                    print('')
                    Power()._disablePowerEstimationAndTelemetry()
                    sleep(2) 
                elif choice == 19:
                    print('')
                    Power()._disableHibernation()
                    sleep(2)  
                elif choice == 20:
                    print('')
                    Power()._disableSleepStudy()
                    sleep(2)
                elif choice == 21:
                    print('')
                    Power()._disableFastStartup()
                    sleep(2)
                elif choice == 22:
                    print('')
                    Power()._unhidingHiddenPowerPlanSettings()
                    sleep(2)      
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   