import subprocess
from utilities import regedit
from winreg import HKEY_LOCAL_MACHINE,REG_DWORD,KEY_SET_VALUE,OpenKey,SetValueEx
from utilities import print

class CPU():
    def __init__(self) -> None:
        pass

    def _intelCpuTweaks(self):
        commands = [r'bcdedit /set allowedinmemorysettings 0x0',
                    r'bcdedit /set isolatedcontext No']
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('INTEL',cmd)


        regedit._setHKLMdwordREG('INTEL',r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel","DistributeTimers",1)
        regedit._setHKLMdwordREG('INTEL',r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel","DisableTsx",0)
        regedit._setHKLMdwordREG('INTEL',r"SYSTEM\CurrentControlSet\Control\Power\PowerThrottling","PowerThrottlingOff",1)
        regedit._setHKLMdwordREG('INTEL',r"SYSTEM\CurrentControlSet\Control\Session Manager\Power","CoalescingTimerInterval",0)
        regedit._setHKLMdwordREG('INTEL',r"SYSTEM\CurrentControlSet\Control\Power","EnergyEstimationEnabled",0)
        regedit._setHKLMdwordREG('INTEL',r"SYSTEM\CurrentControlSet\Control\Power","EventProcessorEnabled",0)

    def _amdCpuTweaks(self):
        values_to_modify = ["WakeEnabled", "WdkSelectiveSuspendEnable"]

        for value in values_to_modify:
            reg_query_command = f'reg query "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class" /s /f "{value}"'
            reg_query_process = subprocess.Popen(reg_query_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            reg_query_output, _ = reg_query_process.communicate()

            hkey_paths = [line.split()[0] for line in reg_query_output.decode().splitlines() if line.startswith("HKEY")]

            for hkey_path in hkey_paths:
                with OpenKey(HKEY_LOCAL_MACHINE, hkey_path, 0, KEY_SET_VALUE) as key:
                    SetValueEx(key, value, 0, REG_DWORD, 0)
                    print._printg('AMD',f'{key} {value}')
                    

    def _disableAwayMode(self):
        commands = [r'powercfg -setacvalueindex scheme_current SUB_SLEEP AWAYMODE 0',
                    r'powercfg -setacvalueindex scheme_current SUB_SLEEP ALLOWSTANDBY 0',
                    r'powercfg -setacvalueindex scheme_current SUB_SLEEP HYBRIDSLEEP 0',
                    r'powercfg -setacvalueindex scheme_current sub_processor PROCTHROTTLEMIN 100',
                    r'powercfg /setactive SCHEME_CURRENT']
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('CPU',cmd)
        

    def _enableAllLogicalProcessors(self):
        command = r'bcdedit /set {current} numproc %NUMBER_OF_PROCESSORS%'
        subprocess.Popen(command,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
        print._printg('CPU',command)


    def _cpuCoolingTweaks(self):
        commands = [r'powercfg /setACvalueindex scheme_current SUB_PROCESSOR SYSCOOLPOL 1',
                    r'powercfg /setDCvalueindex scheme_current SUB_PROCESSOR SYSCOOLPOL 1',
                    r'powercfg /setactive SCHEME_CURRENT']
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('CPU',cmd)

    def _optimizeDCValues(self):
        commands = [r'Powercfg -setdcvalueindex scheme_current sub_processor PROCTHROTTLEMAX 100',
                    r'Powercfg -setactive scheme_current',
                    r'Powercfg -setdcvalueindex scheme_current sub_processor PROCTHROTTLEMIN 50',
                    r'Powercfg -setactive scheme_current']
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('CPU',cmd)

    def _optimizeACValues(self):
        commands = [r'Powercfg -setacvalueindex scheme_current sub_processor PROCTHROTTLEMAX 100',
                    r'Powercfg -setactive scheme_current',
                    r'Powercfg -setacvalueindex scheme_current sub_processor PROCTHROTTLEMIN 100',
                    r'Powercfg -setactive scheme_current']
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('CPU',cmd)

    def _disableCoreParking(self):
        commands = [r'powercfg -setacvalueindex scheme_current sub_processor CPMINCORES 100',
                    r'powercfg /setactive SCHEME_CURRENT']
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('CPU',cmd)

    def _fixIntelCPUStockSpeed(self):
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Services\IntelPPM","Start",3)

    def _fixAMDCPUStockSpeed(self):
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Services\AmdPPM","Start",3)

    def _disableThrottleStates(self):
        commands = [r'powercfg -setacvalueindex scheme_current sub_processor THROTTLING 0',
                    r'powercfg /setactive SCHEME_CURRENT']
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('CPU',cmd)

    def _setDeviceIdlePolicyToPerformance(self):
        commands = [r'powercfg -setacvalueindex scheme_current sub_none DEVICEIDLE 0',
                    r'powercfg /setactive SCHEME_CURRENT']
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('CPU',cmd)

    def _configureCStates(self):
        commands = [r'powercfg -setacvalueindex scheme_current sub_processor IDLEPROMOTE 98',
                    r'powercfg -setacvalueindex scheme_current sub_processor IDLEDEMOTE 98',
                    r'powercfg -setacvalueindex scheme_current sub_processor IDLECHECK 20000',
                    r'powercfg /setactive SCHEME_CURRENT']
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('CPU',cmd)

    def _useHigherPStatesOnLowerCStatesVisaVersa(self):
        commands = [r'powercfg -setacvalueindex scheme_current sub_processor IDLESCALING 1',
                    r'powercfg /setactive SCHEME_CURRENT']
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('CPU',cmd)

    def _dontRestrictCoreBoost(self):
        commands = [r'powercfg -setacvalueindex scheme_current sub_processor PERFEPP 0',
                    r'powercfg /setactive SCHEME_CURRENT']
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('CPU',cmd)

    def _enableTurboBoost(self):
        commands = [r'powercfg -setacvalueindex scheme_current sub_processor PERFBOOSTMODE 1',
                    r'powercfg -setacvalueindex scheme_current sub_processor PERFBOOSTPOL 100',
                    r'powercfg /setactive SCHEME_CURRENT']
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('CPU',cmd)

    def _disableCStates(self):
        commands = [r'powercfg -setacvalueindex 95533644-e700-4a79-a56c-a89e8cb109d9 238c9fa8-0aad-41ed-83f4-97be242c8f20 25dfa149-5dd1-4736-b5ab-e8a37b5b8187 0',
                    r'Powercfg -setactive scheme_current',
                    r'powercfg -setdcvalueindex 95533644-e700-4a79-a56c-a89e8cb109d9 238c9fa8-0aad-41ed-83f4-97be242c8f20 25dfa149-5dd1-4736-b5ab-e8a37b5b8187 0',
                    r'Powercfg -setactive scheme_current']
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('CPU',cmd)

    def _advancedCPURegistryTweaks(self):
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\943c8cb6-6f93-4227-ad87-e9a3feec08d1","Attributes",2)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\2a737441-1930-4402-8d77-b2bebba308a3\d4e98f31-5ffe-4ce1-be31-1b38b384c009\DefaultPowerSchemeValues\381b4222-f694-41f0-9685-ff5bb260df2e","ACSettingIndex",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\2a737441-1930-4402-8d77-b2bebba308a3\d4e98f31-5ffe-4ce1-be31-1b38b384c009\DefaultPowerSchemeValues\381b4222-f694-41f0-9685-ff5bb260df2e","DCSettingIndex",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\2a737441-1930-4402-8d77-b2bebba308a3\d4e98f31-5ffe-4ce1-be31-1b38b384c009\DefaultPowerSchemeValues\8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c","ACSettingIndex",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\3b04d4fd-1cc7-4f23-ab1c-d1337819c4bb\DefaultPowerSchemeValues\381b4222-f694-41f0-9685-ff5bb260df2e","ACSettingIndex",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\3b04d4fd-1cc7-4f23-ab1c-d1337819c4bb\DefaultPowerSchemeValues\381b4222-f694-41f0-9685-ff5bb260df2e","DCSettingIndex",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251-82be-4824-96c1-47b60b740d00\3b04d4fd-1cc7-4f23-ab1c-d1337819c4bb\DefaultPowerSchemeValues\8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c","ACSettingIndex",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Processor","AllowPepPerfStates",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Processor","Cstates",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Processor","Capabilities",516198)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power","HighPerformance",1)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power","HighestPerformance",1)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power","MinimumThrottlePercent",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power","MaximumThrottlePercent",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power","MaximumPerformancePercent",100)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power","Class1InitialUnparkCount",100)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power","InitialUnparkCount",100)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power","MaximumPerformancePercent",100)
        regedit._setHKLMdwordREG('CPU',r"SOFTWARE\Policies\Microsoft\Windows\WcmSvc\GroupPolicy","fDisablePowerManagement",1)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\PDC\Activators\Default\VetoPolicy","EA:EnergySaverEngaged",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\PDC\Activators\28\VetoPolicy","EA:PowerStateDischarging",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Misc","DeviceIdlePolicy",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor","PerfEnergyPreference",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor","PerfEnergyPreference",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor","CPMinCores",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor","CPMaxCores",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor","CPMinCores1",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor","CPMaxCores1",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor","CpLatencyHintUnpark1",100)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor","CPDistribution",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor","CpLatencyHintUnpark",100)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor","MaxPerformance1",100)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor","MaxPerformance",100)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor","CPDistribution1",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor","CPHEADROOM",0)
        binary_string = b'01000000020000000100000000000000020000000000000000000000000000002c0100003232030304000000040000000000000000000000840300002c01000000000000840300000001646464640000'
        regedit._setHKCUbinaryREG('CPU',r"Control Panel\PowerCfg\GlobalPowerPolicy","Policies",binary_string)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Processor","Cstates",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Processor","Capabilities",516198)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power","HighPerformance",1)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power","HighestPerformance",1)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power","MinimumThrottlePercent",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power","MaximumThrottlePercent",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power","MaximumPerformancePercent",100)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power","Class1InitialUnparkCount",100)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power","InitialUnparkCount",100)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power","MaximumPerformancePercent",100)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\PowerThrottling","PowerThrottlingOff",1)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor","CPHEADROOM",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\CurrentControlSet\Control\Power\Policy\Settings\Processor","CPCONCURRENCY",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","ProccesorThrottlingEnabled",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleThreshold",1)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdle",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuLatencyTimer",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuSlowdown",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","DedicatedSegmentSize",1298)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","Threshold",1)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuDebuggingEnabled",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","ProccesorLatencyThrottlingEnabled",0)

    def _cpuIdlePowerManagementTweaks(self):
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubDelay",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubInterval",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubPower",18)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubThreshold",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubType",2)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValue",100)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueMaximum",100)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueMinimum",100)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueStep",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueDefault",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueCurrent",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValuePrevious",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueNext",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueLast",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueFirst",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueCount",100)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueIndex",42)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueName",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueDescription",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueEnabled",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueDisabled",1)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueVisible",1)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueHidden",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueReadOnly",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueReadnv11",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValuenv11Only",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueExecute",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueNoExecute",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueSystem",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueUser",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubPower",100)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueDisabled",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubPower",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueCustom",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueAuto",1)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueManual",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueAutomatic",1)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueDisabledByDefault",1)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueEnabledByDefault",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueDefaultEnabled",0)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueDefaultDisabled",1)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueDefaultAuto",1)
        regedit._setHKLMdwordREG('CPU',r"SYSTEM\ControlSet001\Control\Processor","CpuIdleScrubValueDefaultManual",0)
