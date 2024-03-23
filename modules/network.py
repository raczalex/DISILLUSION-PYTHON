import subprocess
from utilities import regedit
from utilities import print

class Network():
    def __init__(self) -> None:
        pass

    def _setNetworkAutoTuningToNormal(self):
        command = r'netsh int tcp set global autotuninglevel=disabled'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)

    def _disableExplicitCongestionNotification(self):
        command = r'netsh int tcp set global ecncapability=disabled'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)

    def _enableNetworkDirectMemoryAccess(self):
        command = r'netsh int tcp set global netdma=enabled'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)

    def _disableReceiveSideCoalescing(self):
        command = r'netsh int tcp set global rsc=disabled'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)
    
    def _enableReceiveSideScaling(self):
        command = r'netsh int tcp set global rss=enabled'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Ndis\Parameters","RssBaseCpu",1)

    def _disableTCPTimestamps(self):
        command = r'netsh int tcp set global timestamps=disabled'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)

    def _setInitialRetransmissionTimerTo2MS(self):
        command = r'netsh int tcp set global initialRto=2000'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)

    def _setMTUSizeTo1500(self):
        command = r'netsh interface ipv4 set subinterface "Ethernet" mtu=1500 store=persistent'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)

    def _disableNonSackRTTResiliency(self):
        command = r'netsh int tcp set global nonsackrttresiliency=disabled'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)

    def _setMaxSynRetransmissionsTo2(self):
        command = r'netsh int tcp set global maxsynretransmissions=2'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)

    def _disableMemoryPressureProtection(self):
        command = r'netsh int tcp set security mpp=disabled'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)

    def _disableSecurityProfiles(self):
        command = r'netsh int tcp set security profiles=disabled'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)

    def _increaseARPCacheSizeTo4096(self):
        command = r'netsh int ip set global neighborcachelimit=4096'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)

    def _enableCongestionProvider(self):
        command = r'netsh int tcp set supplemental Internet congestionprovider=ctcp'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)

    def _disableIPv6(self):
        command = r'netsh int ipv6 set state disabled'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)

    def _disableISATAP(self):
        command = r'netsh int isatap set state disabled'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)

    def _disableTeredo(self):
        command = r'netsh int teredo set state disabled'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)

    def _setTimeToLiveTo64(self):
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","DefaultTTL",64)
    
    def _enableTCPWindowScaling(self):
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","Tcp1323Opts",1)

    def _disableTCPSelectiveAcks(self):
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","SackOpts",0)

    def _increaseMaximumPortNumber(self):
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","MaxUserPort",65534)

    def _decreaseTimeToWaitInTimeWaitState(self):
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","TcpTimedWaitDelay",30)

    def _disableAutoDisconnectForIdleConnections(self):
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\services\LanmanServer\Parameters","autodisconnect",4294967295)

    def _limitNumberOfSMSSessions(self):
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\services\LanmanServer\Parameters","Size",3)

    def _disableOplocks(self):
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\services\LanmanServer\Parameters","EnableOplocks",0)

    def _setIRPStackSize(self):
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\services\LanmanServer\Parameters","IRPStackSize",20)

    def _disableSharingViolations(self):
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\services\LanmanServer\Parameters","SharingViolationDelay",0)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\services\LanmanServer\Parameters","SharingViolationRetries",0)

    def _setNetworkThrottlingIndex(self):
        regedit._setHKLMdwordREG(r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile","NetworkThrottlingIndex",4294967295)

    def _disableNetbiosOverTCPIP(self):
        command_query = ['reg', 'query', r'HKLM\SYSTEM\CurrentControlSet\services\NetBT\Parameters\Interfaces', '/s', '/f', 'NetbiosOptions']
        command_add = ['Reg.exe', 'add', '"{key}"', '/v', 'NetbiosOptions', '/t', 'REG_DWORD', '/d', '2', '/f']

        result = subprocess.run(command_query, capture_output=True, text=True)

        registry_keys = [line.strip() for line in result.stdout.splitlines() if 'HKEY' in line]

        for key in registry_keys:
            print(key)
            add_command = [part.format(key=key) if part == '"{key}"' else part for part in command_add]
            subprocess.run(add_command,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            print._printg('NETWORK',add_command)

    def _enableDirectCacheAccess(self):
        command = r'netsh int tcp set global dca=enabled'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)

    def _enableMSIModeOnNetworkAdapter(self):
        command_get_pnp_device_id = ['wmic', 'path', 'win32_NetworkAdapter', 'get', 'PNPDeviceID']
        result = subprocess.run(command_get_pnp_device_id, capture_output=True, text=True)
        pnp_device_ids = [line.strip() for line in result.stdout.splitlines() if 'PNPDeviceID' in line]

        for pnp_device_id in pnp_device_ids:
            _, _, pnp_device_id_value = pnp_device_id.partition('=')
            pnp_device_id_value = pnp_device_id_value.strip()

            regedit._setHKLMdwordREG('NETWORK',f'System\\CurrentControlSet\\Enum\\{pnp_device_id_value}\\Device Parameters\\Interrupt Management\\Affinity Policy','DevicePriority',None)
            regedit._setHKLMdwordREG('NETWORK',f'System\\CurrentControlSet\\Enum\\{pnp_device_id_value}\\Device Parameters\\Interrupt Management\\MessageSignaledInterruptProperties','MSISupported',1)

    def _wifiOn(self):
        commands = [r'sc config LanmanWorkstation start= demand',
                    r'sc config WdiServiceHost start= demand',
                    r'sc config NcbService start= demand',
                    r'sc config ndu start= demand',
                    r'sc config Netman start= demand',
                    r'sc config netprofm start= demand',
                    r'sc config WwanSvc start= demand',
                    r'sc config Dhcp start= auto',
                    r'sc config DPS start= auto',
                    r'sc config lmhosts start= auto',
                    r'sc config NlaSvc start= auto',
                    r'sc config nsi start= auto',
                    r'sc config RmSvc start= auto',
                    r'sc config Wcmsvc start= auto',
                    r'sc config Winmgmt start= auto',
                    r'sc config WlanSvc start= auto',
                    r'schtasks /Change /TN "Microsoft\Windows\WlanSvc\CDSSync" /Enable',
                    r'schtasks /Change /TN "Microsoft\Windows\WCM\WiFiTask" /Enable',
                    r'schtasks /Change /TN "Microsoft\Windows\NlaSvc\WiFiTask" /Enable',
                    r'schtasks /Change /TN "Microsoft\Windows\DUSM\dusmtask" /Enable'
                    ]

        for cmd in commands:
                subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
                print._printg('NETWORK',cmd)

        regedit._setHKLMdwordREG('NETWORK',r"Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator","NoActiveProbe",0)
        regedit._setHKLMdwordREG('NETWORK',r"System\CurrentControlSet\Services\NlaSvc\Parameters\Internet","EnableActiveProbing",1)
        regedit._setHKLMdwordREG('NETWORK',r"System\CurrentControlSet\Services\BFE","Start",2)
        regedit._setHKLMdwordREG('NETWORK',r"System\CurrentControlSet\Services\Dnscache","Start",2)
        regedit._setHKLMdwordREG('NETWORK',r"System\CurrentControlSet\Services\WinHttpAutoProxySvc","Start",3)

        commands.clear()

        commands = [r'net start DPS',
                    r'net start nsi',
                    r'net start NlaSvc',
                    r'net start Dhcp',
                    r'net start Wcmsvc',
                    r'net start RmSvc',
                    r'wmic path win32_networkadapter where index=0 call disable',
                    r'wmic path win32_networkadapter where index=1 call disable',
                    r'wmic path win32_networkadapter where index=2 call disable',
                    r'wmic path win32_networkadapter where index=3 call disable',
                    r'wmic path win32_networkadapter where index=4 call disable',
                    r'wmic path win32_networkadapter where index=5 call disable',
                    r'wmic path win32_networkadapter where index=0 call enable',
                    r'wmic path win32_networkadapter where index=1 call enable',
                    r'wmic path win32_networkadapter where index=2 call enable',
                    r'wmic path win32_networkadapter where index=3 call enable',
                    r'wmic path win32_networkadapter where index=4 call enable',
                    r'wmic path win32_networkadapter where index=5 call enable',
                    r'arp -d *',
                    r'route -f',
                    r'nbtstat -R',
                    r'nbtstat -RR',
                    r'netcfg -d',
                    r'netsh winsock reset',
                    r'netsh int 6to4 reset all',
                    r'netsh int httpstunnel reset all',
                    r'netsh int ip reset',
                    r'netsh int isatap reset all',
                    r'netsh int portproxy reset all',
                    r'netsh int tcp reset all',
                    r'netsh int teredo reset all',
                    r'netsh branchcache reset',
                    r'ipconfig /release',
                    r'ipconfig /renew'
                    ]
        
        for cmd in commands:
                subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
                print._printg('NETWORK',cmd)

    def _wifiOff(self):
            commands = [r'sc config NlaSvc start= disabled',
                        r'sc config LanmanWorkstation start= disabled',
                        r'schtasks /Change /TN "Microsoft\Windows\WlanSvc\CDSSync" /Disable',
                        r'schtasks /Change /TN "Microsoft\Windows\WCM\WiFiTask" /Disable',
                        r'schtasks /Change /TN "Microsoft\Windows\NlaSvc\WiFiTask" /Disable',
                        r'schtasks /Change /TN "Microsoft\Windows\DUSM\dusmtask" /Disable'
                        ]
            for cmd in commands:
                subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
                print._printg('NETWORK',cmd)

            regedit._setHKLMdwordREG('NETWORK',r"Software\Policies\Microsoft\Windows\NetworkConnectivityStatusIndicator","NoActiveProbe",1)
            regedit._setHKLMdwordREG('NETWORK',r"System\CurrentControlSet\Services\NlaSvc\Parameters\Internet","EnableActiveProbing",0)

            commands.clear()

            commands = [r'sc config BFE start= demand',
                        r'sc config Dnscache start= demand',
                        r'sc config WinHttpAutoProxySvc start= demand',
                        r'sc config Dhcp start= auto',
                        r'sc config DPS start= auto',
                        r'net start RmSvc',
                        r'sc config lmhosts start= disabled',
                        r'sc config nsi start= auto',
                        r'sc config Wcmsvc start= disabled',
                        r'sc config Winmgmt start= auto',
                        r'sc config WlanSvc start= demand'
                        ]
            
            for cmd in commands:
                subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
                print._printg('NETWORK',cmd)

    def _setDNSPriority(self):
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider","LocalPriority",4)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider","HostsPriority",5)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider","DnsPriority",6)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\ServiceProvider","NetbtPriority",7)

    def _enableOnboardProcessor(self):
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces","DisableTaskOffload",0)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","DisableTaskOffload",0)
        command = r'netsh int ip set global taskoffload=disabled'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)

    def _disableNagilesAlgorithm(self):
        command_get_guid = ['wmic', 'path', 'win32_networkadapter', 'get', 'GUID']

        result = subprocess.run(command_get_guid, capture_output=True, text=True)
        guids = [line.strip() for line in result.stdout.splitlines() if '{' in line]

        for guid in guids:
            regedit._setHKLMdwordREG('NETWORK',f'SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{guid}','InterfaceMetric',0o55)

            regedit._setHKLMdwordREG('NETWORK',f'SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{guid}','TCPNoDelay',0o1)

            regedit._setHKLMdwordREG('NETWORK',f'SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{guid}','TcpAckFrequency',0o1)

            regedit._setHKLMdwordREG('NETWORK',f'SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\{guid}','TcpDelAckTicks',0000000)

        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces","TCPDelAckTicks",1)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","TCPDelAckTicks",1)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","TCPNoDelay",1)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces","TCPNoDelay",1)
        regedit._setHKLMdwordREG('NETWORK',r"SOFTWARE\Microsoft\MSMQ\Parameters","TCPNoDelay",1)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","TcpAckFrequency",1)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces","TcpAckFrequency",1)

    def _adapter(self):
        regedit._setHKLMdwordREG('NETWORK',r"SOFTWARE\Microsoft\Windows\CurrentVersion\DeliveryOptimization\Config","DODownloadMode",0)
        regedit._setHKLMdwordREG('NETWORK',r"SOFTWARE\Microsoft\Windows\CurrentVersion\DeliveryOptimization\Config","DownloadMode",0)
        regedit._setHKLMdwordREG('NETWORK',r"SOFTWARE\Microsoft\Windows\CurrentVersion\DeliveryOptimization\Settings","DownloadMode",0)

    def _resetAllInternetSettings(self):
        commands = [r'netsh int reset all',
                    r'netsh int ipv4 reset',
                    r'netsh int ipv6 reset',
                    r'netsh winsock reset',
                    r'netsh int ip reset',
                    r'ipconfig /release',
                    r'ipconfig /flushdns',
                    r'ipconfig /renew']
        for cmd in commands:
                subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
                print._printg('NETWORK',cmd)

    def _stopNetworkThrottling(self):
        command = r'netsh advfirewall firewall add rule name="StopThrottling" dir=in action=block remoteip=173.194.55.0/24,206.111.0.0/16 enable=yes'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)

    def _disableNetworkLimiting(self):
        command = r'netsh interface tcp set heuristics disabled'
        subprocess.Popen(command,text=True).wait()
        print._printg('NETWORK',command)

    def _disableNetworkPowerManagement(self):
        commands = [r'PowerShell Disable-NetAdapterLso -Name "*"',
                    r'powershell "ForEach($adapter In Get-NetAdapter){Disable-NetAdapterPowerManagement -Name $adapter.Name -ErrorAction SilentlyContinue}"',
                    r'powershell "ForEach($adapter In Get-NetAdapter){Disable-NetAdapterLso -Name $adapter.Name -ErrorAction SilentlyContinue}"',
                    r'POWERSHELL Disable-NetAdapterPowerManagement -Name "*" -ErrorAction SilentlyContinue']
        for cmd in commands:
                subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
                print._printg('NETWORK',cmd)
        
    def _disableHiddenPowerSavingsAndNIC(self):
        command_get_sub_id = ['Reg', 'query', r'HKLM\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002bE10318}', '/v', '*SpeedDuplex', '/s']

        result = subprocess.run(command_get_sub_id, capture_output=True, text=True)
        sub_ids = []
        sub_ids = [line.strip() for line in result.stdout.splitlines() if 'HKEY' in line]

        features_to_disable = [
                "AutoPowerSaveModeEnabled",
                "AutoDisableGigabit",
                "AdvancedEEE",
                "DisableDelayedPowerUp",
                "*EEE",
                "EEE",
                "EnablePME",
                "EEELinkAdvertisement",
                "EnableGreenEthernet",
                "EnableSavePowerNow",
                "EnablePowerManagement",
                "EnableDynamicPowerGating",
                "EnableConnectedPowerGating",
                "EnableWakeOnLan",
                "GigaLite",
                "NicAutoPowerSaver",
                "PowerDownPll",
                "PowerSavingMode",
                "ReduceSpeedOnPowerDown",
                "S5NicKeepOverrideMacAddrV2",
                "S5WakeOnLan",
                "ULPMode",
                "WakeOnDisconnect",
                "*WakeOnMagicPacket",
                "*WakeOnPattern",
                "WakeOnLink",
                "WolShutdownLinkSpeed"
            ]

        for sub_id in sub_ids:
            for feature in features_to_disable:
                subprocess.run(['Reg.exe', 'add', sub_id, '/v', feature, '/t', 'REG_SZ', '/d', '0', '/f'],text=True)
                print._printg('NETWORK',feature)
        return sub_ids


    def _disableJumboFrame(self,sub_id):
        subprocess.run(['Reg.exe', 'add', sub_id, '/v', 'JumboPacket', '/t', 'REG_SZ', '/d', '1514', '/f'],text=True)
        print._printg('NETWORK','JumboPacket 1514')

    def _configureBufferSizes(self,sub_id):
        subprocess.run(['Reg.exe', 'add', sub_id, '/v', 'TransmitBuffers', '/t', 'REG_SZ', '/d', '4096', '/f'],text=True)
        print._printg('NETWORK','TransmitBuffers 4096')
        subprocess.run(['Reg.exe', 'add', sub_id, '/v', 'ReceiveBuffers', '/t', 'REG_SZ', '/d', '512', '/f'],text=True)
        print._printg('NETWORK','ReceiveBuffers 512')

    def _configureOffloads(self,sub_id):
        offloads_to_configure = [
            "IPChecksumOffloadIPv4", "LsoV1IPv4", "LsoV2IPv4", "LsoV2IPv6",
            "PMARPOffload", "PMNSOffload", "TCPChecksumOffloadIPv4",
            "TCPChecksumOffloadIPv6", "UDPChecksumOffloadIPv6",
            "UDPChecksumOffloadIPv4"
        ]

        for offload in offloads_to_configure:
            subprocess.run(['Reg.exe', 'add', sub_id, '/v', offload, '/t', 'REG_SZ', '/d', '0', '/f'],text=True)
            print._printg('NETWORK',offload)

    def _enableRSS(self,sub_id):
        subprocess.run(['Reg.exe', 'add', sub_id, '/v', 'RSS', '/t', 'REG_SZ', '/d', '1', '/f'],text=True)
        print._printg('NETWORK','RSS 1')
        subprocess.run(['Reg.exe', 'add', sub_id, '/v', '*NumRssQueues', '/t', 'REG_SZ', '/d', '2', '/f'],text=True)
        print._printg('NETWORK','*NumRssQueues 2')
        subprocess.run(['Reg.exe', 'add', sub_id, '/v', 'RSSProfile', '/t', 'REG_SZ', '/d', '3', '/f'],text=True)
        print._printg('NETWORK','RSSProfile 3')
        

    def _disableFlowControl(self,sub_id):
        subprocess.run(['Reg.exe', 'add', sub_id, '/v', '*FlowControl', '/t', 'REG_SZ', '/d', '0', '/f'],text=True)
        print._printg('NETWORK','*FlowControl 0')
        subprocess.run(['Reg.exe', 'add', sub_id, '/v', 'FlowControlCap', '/t', 'REG_SZ', '/d', '0', '/f'],text=True)
        print._printg('NETWORK','FlowControlCap 0')

    def _removeInterruptDelays(self,sub_id):
        interrupt_delays_to_remove = ["RxAbsIntDelay", "TxIntDelay", "TxAbsIntDelay"]

        for delay in interrupt_delays_to_remove:
            subprocess.run(['Reg.exe', 'add', sub_id, '/v', delay, '/t', 'REG_SZ', '/d', '0', '/f'],text=True)
            print._printg('NETWORK',f'{delay} 0')

    def _removeAdapterNotification(self,sub_id):
        subprocess.run(['Reg.exe', 'add', sub_id, '/v', 'FatChannelIntolerant', '/t', 'REG_SZ', '/d', '0', '/f'],text=True)
        print._printg('NETWORK','FatChannelIntolerant 0')

    def _optimizeNetworkAdapter(self):
        sub_ids = self._disableHiddenPowerSavingsAndNIC()
        for sub_id in sub_ids:
            self._disableJumboFrame(sub_id)
            self._configureBufferSizes(sub_id)
            self._configureOffloads(sub_id)
            self._enableRSS(sub_id)
            self._disableFlowControl(sub_id)
            self._removeInterruptDelays(sub_id)
            self._removeAdapterNotification(sub_id)

    def _tcpCongestionControlAvoidenceAlgorithm(self):
        regedit._setHKLMbinaryREG('NETWORK',r"System\CurrentControlSet\Control\Nsi\{eb004a03-9b1a-11d4-9123-0050047759bc}\0","0200",b"0000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000ff000000000000000000000000000000000000000000ff000000000000000000000000000000")
        regedit._setHKLMbinaryREG('NETWORK',r"System\CurrentControlSet\Control\Nsi\{eb004a03-9b1a-11d4-9123-0050047759bc}\0","1700",b"0000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000ff000000000000000000000000000000000000000000ff000000000000000000000000000000")
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Winsock","MinSockAddrLength",16)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Winsock","MaxSockAddrLength",16)

    def _afdRegTweaks(self):
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\AFD\Parameters","DefaultReceiveWindow",16384)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\AFD\Parameters","DefaultSendWindow",16384)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\AFD\Parameters","FastCopyReceiveThreshold",16384)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\AFD\Parameters","FastSendDatagramThreshold",16384)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\AFD\Parameters","DynamicSendBufferDisable",0)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\AFD\Parameters","IgnorePushBitOnReceives",1)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\AFD\Parameters","NonBlockingSendSpecialBuffering",1)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\AFD\Parameters","DisableRawSecurity",1)
        
    def _reinforceNetworkProperties(self):
        regedit._setHKLMdwordREG('NETWORK',r"SOFTWARE\Policies\Microsoft\Windows\Psched","NonBestEffortLimit",0)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Psched","NonBestEffortLimit",0)
    
    def _tweakingTCPIPRegistrySettings(self):
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","DisableIPSourceRouting",2)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","EnableICMPRedirect",1)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","EnablePMTUDiscovery",1)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","Tcp1323Opts",0)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","TcpMaxDupAcks",2)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","TcpTimedWaitDelay",32)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","GlobalMaxTcpWindowSize",8760)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","TcpWindowSize",8760)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","MaxConnectionsPerServer",0)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","MaxUserPort",65534)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","SackOpts",0)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","DefaultTTL",64)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","DelayedAckFrequency",1)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","DelayedAckTicks",1)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","CongestionAlgorithm",1)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","MultihopSets",15)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","FastCopyReceiveThreshold",16384)
        regedit._setHKLMdwordREG('NETWORK',r"SYSTEM\CurrentControlSet\Services\Tcpip\Parameters","FastSendDatagramThreshold",16384)

    def _networkAdapterPriority(self):
        result = subprocess.run(['wmic', 'path', 'win32_networkadapter', 'get', 'PNPDeviceID'], capture_output=True, text=True)
        adapter_list = [line.strip() for line in result.stdout.splitlines() if 'VEN_' in line]
        for adapter in adapter_list:
            regedit._setHKLMbinaryREG('NETWORK',f'SYSTEM\\ControlSet001\\Enum\\{adapter}\\Device Parameters\\Interrupt Management','AssignmentSetOverride',b'04')
            regedit._setHKLMdwordREG('NETWORK',f'SYSTEM\\ControlSet001\\Enum\\{adapter}\\Device Parameters\\Interrupt Management','DevicePolicy',4)
            regedit._setHKLMdwordREG('NETWORK',f'SYSTEM\\ControlSet001\\Enum\\{adapter}\\Device Parameters\\Interrupt Management','MessageSignaledInterruptProperties',256)

    def _doAll(self):
        self._setNetworkAutoTuningToNormal()    
        self._disableExplicitCongestionNotification()
        self._enableNetworkDirectMemoryAccess()
        self._disableReceiveSideCoalescing()
        self._enableReceiveSideScaling()
        self._disableTCPTimestamps()
        self._setInitialRetransmissionTimerTo2MS()
        self._setMTUSizeTo1500()
        self._disableNonSackRTTResiliency()
        self._setMaxSynRetransmissionsTo2()
        self._disableMemoryPressureProtection()
        self._disableSecurityProfiles()
        self._increaseARPCacheSizeTo4096()
        self._enableCongestionProvider()
        self._disableIPv6()
        self._disableISATAP()
        self._disableTeredo()
        self._setTimeToLiveTo64()
        self._enableTCPWindowScaling()
        self._disableTCPSelectiveAcks()
        self._increaseMaximumPortNumber()
        self._decreaseTimeToWaitInTimeWaitState()
        self._disableAutoDisconnectForIdleConnections()
        self._limitNumberOfSMSSessions()
        self._disableOplocks()
        self._setIRPStackSize()
        self._disableSharingViolations()
        self._setNetworkThrottlingIndex()
        self._disableNetbiosOverTCPIP()
        self._enableDirectCacheAccess()
        self._enableMSIModeOnNetworkAdapter()
        self._setDNSPriority()
        self._enableOnboardProcessor()
        self._disableNagilesAlgorithm()
        self._adapter()
        self._stopNetworkThrottling()
        self._disableNetworkLimiting()
        self._disableNetworkPowerManagement()
        self._disableHiddenPowerSavingsAndNIC()
        self._optimizeNetworkAdapter()
        self._tcpCongestionControlAvoidenceAlgorithm()
        self._afdRegTweaks()
        self._reinforceNetworkProperties()
        self._tweakingTCPIPRegistrySettings()
        self._networkAdapterPriority()