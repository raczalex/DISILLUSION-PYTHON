
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.gpu import GPU

class GPUMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [GPU]')

    def _displayMenu(self):
        
        options = [
            "Do All (General)",
            "Do All (Nvidia)",
            "Do All (Amd)",
            "MMCSS GPU Tweaks (General)",
            "Graphics Card Scheduler Tweaks (General)",
            "Disable Preemption (General)",
            "Disable Disable GPU Energy Drv (General)",
            "Latency Tolerance (General)",
            "VRAM (General)",
            "Set Driver Acceleration (Nvidia)",
            "Force Contigous Memory Allocation (Nvidia)",
            "DPCS For Each Core (Nvidia)",
            "Disable Write Combining (Nvidia)",
            "Disable TDR (Nvidia)",
            "Optimize Power Mizer (Nvidia)",
            "Advanced Driver Debloat (Nvidia)",
            "Remove Telemetry (Nvidia)",
            'Disable Hidden Power Saving Features (Nvidia)',
            'Advanced Tweaks (Nvidia)',
            'Latency Tolerance (Nvidia)',
            'Disable All Preemptions (Nvidia)',
            "Disable Override Refresh Rate (Amd)",
            "Disable Snapshot (Amd)",
            "Disable Anti Aliasing (Amd)",
            "Disable Allow Subscription (Amd)",
            "Disable Anisotropic Filtering (Amd)",
            "Disable RS Overlay (Amd)",
            "Enable Adaptive De-Interlacing (Amd)",
            "Disable Allow Skins (Amd)",
            "Disable Auto Color Depth Reduction (Amd)",
            "Disable Power Gating (Amd)",
            "Disable Disable Clock Gating (Amd)",
            "Disable ASPM (Amd)",
            "Disable Ultra Low Power States (Amd)",
            "Enable De-Lag (Amd)",
            "Disable Frame Rate Target (Amd)",
            "Disable DMA (Amd)",
            "Enable Block Write (Amd)",
            "Disable Stutter Mode (Amd)",
            "Disable GPU Mem Clock Sleep State (Amd)",
            "Disable Thermal Throttling (Amd)",
            "Disable Preemption (Amd)",
            "Setting Main 3D (Amd)",
            "Setting Flip Queue Size (Amd)",
            "Setting Shader Cache (Amd)",
            "Configuring TFQ (Amd)",
            "Disable HDCP (Amd)",
            "Disable GPU Power Down (Amd)",
            "Disable Logging (Amd)",
            "More Tweaks (Amd)",
            "More Tweaks 2 (Amd)",
            "GPU Tweaks (Intel)"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [GPU]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                    GPU()._generalGPUTweaks()
                    sleep(2)
                elif choice == 2:
                    print('')
                    GPU()._nvidiaGpuTweaks()
                    sleep(2)    
                elif choice == 3:
                    print('')
                    GPU()._amdGPUTweaks()
                    sleep(2)
                elif choice == 4:
                    print('')
                    GPU()._mmcssGpuTweaks()
                    sleep(2)  
                elif choice == 5:
                    print('')
                    GPU()._graphicsCardSchedulerTweaks()
                    sleep(2)  
                elif choice == 6:
                    print('')
                    GPU()._disablePreemptionGeneral()
                    sleep(2)  
                elif choice == 7:
                    print('')
                    GPU()._disableGpuEnergyDrv()
                    sleep(2)  
                elif choice == 8:
                    print('')
                    GPU()._latencyTolerance()
                    sleep(2)  
                elif choice == 9:
                    print('')
                    GPU()._vram()
                    sleep(2)  
                elif choice == 10:
                    print('')
                    GPU()._setDriverAcceleration()
                    sleep(2)  
                elif choice == 11:
                    print('')
                    GPU()._forceContigousMemoryAllocation()
                    sleep(2)  
                elif choice == 12:
                    print('')
                    GPU()._dpcsForEachCore()
                    sleep(2)  
                elif choice == 13:
                    print('')
                    GPU()._disableWriteCombining()
                    sleep(2)  
                elif choice == 14:
                    print('')
                    GPU()._disableTDR()
                    sleep(2)  
                elif choice == 15:
                    print('')
                    GPU()._optimizePowerMizer()
                    sleep(2)  
                elif choice == 16:
                    print('')
                    GPU()._advancedDriverDebloat()
                    sleep(2)  
                elif choice == 17:
                    print('')
                    GPU()._removeNvidiaTelemetry()
                    sleep(2)  
                elif choice == 18:
                    print('')
                    GPU()._disableHiddenPowerSavingFeatures()
                    sleep(2)  
                elif choice == 19:
                    print('')
                    GPU()._advancedTweaks()
                    sleep(2)
                elif choice == 20:
                    print('')
                    GPU()._latencyTolerance2()
                    sleep(2)
                elif choice == 21:
                    print('')
                    GPU()._disableAllPreemptions()
                    sleep(2)
                elif choice == 22:
                    print('')
                    GPU()._disableOverrideRefreshRate()
                    sleep(2)
                elif choice == 23:
                    print('')
                    GPU()._disableSnapshot()
                    sleep(2)
                elif choice == 24:
                    print('')
                    GPU()._disableAntiAliasing()
                    sleep(2)
                elif choice == 25:
                    print('')
                    GPU()._disableAllowSubscription()
                    sleep(2)
                elif choice == 26:
                    print('')
                    GPU()._disableAnisotropicFiltering()
                    sleep(2)
                elif choice == 27:
                    print('')
                    GPU()._disableRSOverlay()
                    sleep(2)
                elif choice == 28:
                    print('')
                    GPU()._enableAdaptiveDeInterlacing()
                    sleep(2)
                elif choice == 29:
                    print('')
                    GPU()._disableAllowSkins()
                    sleep(2)
                elif choice == 30:
                    print('')
                    GPU()._disableAutoColorDepthReduction()
                    sleep(2)
                elif choice == 31:
                    print('')
                    GPU()._disablePowerGating()
                    sleep(2)
                elif choice == 32:
                    print('')
                    GPU()._disableClockGating()
                    sleep(2)
                elif choice == 33:
                    print('')
                    GPU()._disableASPM()
                    sleep(2)
                elif choice == 34:
                    print('')
                    GPU()._disableULPS()
                    sleep(2)
                elif choice == 35:
                    print('')
                    GPU()._enableDeLag()
                    sleep(2)
                elif choice == 36:
                    print('')
                    GPU()._disableFRT()
                    sleep(2)
                elif choice == 37:
                    print('')
                    GPU()._disableDMA()
                    sleep(2)
                elif choice == 38:
                    print('')
                    GPU()._enableBlockWrite()
                    sleep(2)
                elif choice == 39:
                    print('')
                    GPU()._disableStutterMode()
                    sleep(2)
                elif choice == 40:
                    print('')
                    GPU()._disableGPUMemClockSleepState()
                    sleep(2)
                elif choice == 41:
                    print('')
                    GPU()._disableThermalThrottling()
                    sleep(2)
                elif choice == 42:
                    print('')
                    GPU()._disablePreemptionAMD()
                    sleep(2)
                elif choice == 43:
                    print('')
                    GPU()._settingMain3D()
                    sleep(2)
                elif choice == 44:
                    print('')
                    GPU()._settingFlipQueueSize()
                    sleep(2)
                elif choice == 45:
                    print('')
                    GPU()._settingShaderCache()
                    sleep(2)
                elif choice == 46:
                    print('')
                    GPU()._configuringTFQ()
                    sleep(2)
                elif choice == 47:
                    print('')
                    GPU()._disableHDCP()
                    sleep(2)
                elif choice == 48:
                    print('')
                    GPU()._disableGPUPowerDown()
                    sleep(2)
                elif choice == 49:
                    print('')
                    GPU()._disableAMDLogging()
                    sleep(2)
                elif choice == 50:
                    print('')
                    GPU()._moreAMDTweaks()
                    sleep(2)
                elif choice == 51:
                    print('')
                    GPU()._moreAMDTweaks2()
                    sleep(2)
                elif choice == 52:
                    print('')
                    GPU()._intelGpuTweaks()
                    sleep(2)
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   