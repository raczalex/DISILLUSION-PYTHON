
from utilities.console import _initTitle,_clear,_printThreeColumnsWithNumbersColored
from pystyle import Colors
from time import sleep
from modules.network import Network

class NetworkMenu():
    def __init__(self) -> None:
        _initTitle('DISILLUSION - [NETWORK]')

    def _displayMenu(self):
        
        options = [
            "Do All Except Reset",
            "Set Auto Tuning To Normal",
            "Disable Explicit Congestion Notification",
            "Enable Direct Memory Access",
            "Disable Receive Side Coalescing",
            "Enable Receive Side Scaling",
            "Disable TCP Timestamps",
            "Set Initial Retransmission Timer To 2",
            "Set MTU Size To 1500",
            "Disable Non Sack RTT Resiliency",
            "Set Max Syn Retransmissions To 2",
            "Disable Memory Pressure Protection",
            "Disable Security Profiles",
            "Increase ARP Cache Size To 4096",
            "Enable Congestion Provider",
            'Disable IPv6',
            'Disable ISatap',
            'Disable Teredo',
            "Set Time To Live 64",
            "Enable TCP Window Scaling",
            "Disable TCP Selective Acks",
            "Increase Maximum Port Number",
            "Decrease Time Wait In TimeWaitState",
            "Disable Auto Disconnect For Idle Connections",
            "Limit Number Of SMS Sessions",
            "Disable Oplocks",
            "Set IRP Stack Size",
            "Disable Sharing Violations",
            "Set Network Throttling Index",
            "Disable NetBios Over TCP/IP",
            "Enable Direct Cache Access",
            "Enable MSI Mode On Network Adapter",
            "Turn WiFi On",
            "Turn WiFi Off",
            "Set DNS Priority",
            "Enable On Board Processor",
            "Disable Nagiles Algorithm",
            "Adapter",
            "Stop Network Throttling",
            "Disable Network Limiting",
            "Disable Network Power Management",
            "Disable Hidden Power Savings And NIC",
            "Optimize Network Adapter",
            "TCP Congestion Control Avoidence Algorithm",
            "AFD Reg Tweaks",
            "Reinforce Network Properties",
            "TCP/IP Settings Tweaks",
            "Network Adapter Priority",
            "Reset All Internet Settings"
        ]

        while True:
            _clear()
            _initTitle('DISILLUSION - [NETWORK]')
            _printThreeColumnsWithNumbersColored(options)
            try:
                choice = int(input(f"\n\n   {Colors.white}[MENU]{Colors.light_green} Enter the number of your choice (0 to exit):{Colors.white} "))
                if choice == 1:
                    print('')
                    Network()._doAll()
                    sleep(2)
                elif choice == 2:
                    print('')
                    Network()._setNetworkAutoTuningToNormal()
                    sleep(2)    
                elif choice == 3:
                    print('')
                    Network()._disableExplicitCongestionNotification()
                    sleep(2) 
                elif choice == 4:
                    print('')
                    Network()._enableNetworkDirectMemoryAccess()
                    sleep(2) 
                elif choice == 5:
                    print('')
                    Network()._disableReceiveSideCoalescing()
                    sleep(2) 
                elif choice == 6:
                    print('')
                    Network()._enableReceiveSideScaling()
                    sleep(2) 
                elif choice == 7:
                    print('')
                    Network()._disableTCPTimestamps()
                    sleep(2) 
                elif choice == 8:
                    print('')
                    Network()._setInitialRetransmissionTimerTo2MS()
                    sleep(2) 
                elif choice == 9:
                    print('')
                    Network()._setMTUSizeTo1500()
                    sleep(2) 
                elif choice == 10:
                    print('')
                    Network()._disableNonSackRTTResiliency()
                    sleep(2) 
                elif choice == 11:
                    print('')
                    Network()._setMaxSynRetransmissionsTo2()
                    sleep(2) 
                elif choice == 12:
                    print('')
                    Network()._disableMemoryPressureProtection()
                    sleep(2) 
                elif choice == 13:
                    print('')
                    Network()._disableSecurityProfiles()
                    sleep(2) 
                elif choice == 14:
                    print('')
                    Network()._increaseARPCacheSizeTo4096()
                    sleep(2) 
                elif choice == 15:
                    print('')
                    Network()._enableCongestionProvider()
                    sleep(2) 
                elif choice == 16:
                    print('')
                    Network()._disableIPv6()
                    sleep(2) 
                elif choice == 17:
                    print('')
                    Network()._disableISATAP()
                    sleep(2) 
                elif choice == 18:
                    print('')
                    Network()._disableTeredo()
                    sleep(2)
                elif choice == 19:
                    print('')
                    Network()._setTimeToLiveTo64()
                    sleep(2) 
                elif choice == 20:
                    print('')
                    Network()._enableTCPWindowScaling()
                    sleep(2) 
                elif choice == 21:
                    print('')
                    Network()._disableTCPSelectiveAcks()
                    sleep(2) 
                elif choice == 22:
                    print('')
                    Network()._increaseMaximumPortNumber()
                    sleep(2) 
                elif choice == 23:
                    print('')
                    Network()._decreaseTimeToWaitInTimeWaitState()
                    sleep(2) 
                elif choice == 24:
                    print('')
                    Network()._disableAutoDisconnectForIdleConnections()
                    sleep(2) 
                elif choice == 25:
                    print('')
                    Network()._limitNumberOfSMSSessions()
                    sleep(2) 
                elif choice == 26:
                    print('')
                    Network()._disableOplocks()
                    sleep(2) 
                elif choice == 27:
                    print('')
                    Network()._setIRPStackSize()
                    sleep(2) 
                elif choice == 28:
                    print('')
                    Network()._disableSharingViolations()
                    sleep(2) 
                elif choice == 29:
                    print('')
                    Network()._setNetworkThrottlingIndex()
                    sleep(2) 
                elif choice == 30:
                    print('')
                    Network()._disableNetbiosOverTCPIP()
                    sleep(2) 
                elif choice == 31:
                    print('')
                    Network()._enableDirectCacheAccess()
                    sleep(2) 
                elif choice == 32:
                    print('')
                    Network()._enableMSIModeOnNetworkAdapter()
                    sleep(2)
                elif choice == 33:
                    print('')
                    Network()._wifiOn()
                    sleep(2) 
                elif choice == 34:
                    print('')
                    Network()._wifiOff()
                    sleep(2) 
                elif choice == 35:
                    print('')
                    Network()._setDNSPriority()
                    sleep(2) 
                elif choice == 36:
                    print('')
                    Network()._enableOnboardProcessor()
                    sleep(2) 
                elif choice == 37:
                    print('')
                    Network()._disableNagilesAlgorithm()
                    sleep(2) 
                elif choice == 38:
                    print('')
                    Network()._adapter()
                    sleep(2) 
                elif choice == 39:
                    print('')
                    Network()._stopNetworkThrottling()
                    sleep(2) 
                elif choice == 40:
                    print('')
                    Network()._disableNetworkLimiting()
                    sleep(2) 
                elif choice == 41:
                    print('')
                    Network()._disableNetworkPowerManagement()
                    sleep(2) 
                elif choice == 42:
                    print('')
                    Network()._disableHiddenPowerSavingsAndNIC()
                    sleep(2) 
                elif choice == 43:
                    print('')
                    Network()._optimizeNetworkAdapter()
                    sleep(2) 
                elif choice == 44:
                    print('')
                    Network()._tcpCongestionControlAvoidenceAlgorithm()
                    sleep(2)
                elif choice == 45:
                    print('')
                    Network()._afdRegTweaks()
                    sleep(2)
                elif choice == 46:
                    print('')
                    Network()._reinforceNetworkProperties()
                    sleep(2)
                elif choice == 47:
                    print('')
                    Network()._tweakingTCPIPRegistrySettings()
                    sleep(2)
                elif choice == 48:
                    print('')
                    Network()._networkAdapterPriority()
                    sleep(2)
                elif choice == 49:
                    print('')
                    Network()._resetAllInternetSettings()
                    sleep(2)   
                elif choice == 0:
                    print(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Exiting the menu.")
                    sleep(1)
                    break
                else:
                    input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Press Enter to continue.")
            except ValueError:
                input(f"\n   {Colors.white}[MENU] {Colors.white}{Colors.light_red}Invalid input. Press Enter to continue.")
   