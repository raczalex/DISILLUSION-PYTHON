import subprocess
from utilities import regedit
from utilities import print

class Power():
    def __init__(self) -> None:
        pass

    def _disableStoragePowerSavings(self):
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\Storage\SD\IdleState\1","IdleExitEnergyMicroJoules",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\Storage\SD\IdleState\1","IdleExitLatencyMs",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\Storage\SD\IdleState\1","IdlePowerMw",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\Storage\SD\IdleState\1","IdleTimeLengthMs",4294967295)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\Storage\SSD\IdleState\1","IdleExitEnergyMicroJoules",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\Storage\SSD\IdleState\1","IdleExitLatencyMs",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\Storage\SSD\IdleState\1","IdlePowerMw",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\Storage\SSD\IdleState\1","IdleTimeLengthMs",4294967295)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\Storage\SSD\IdleState\2","IdleExitEnergyMicroJoules",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\Storage\SSD\IdleState\2","IdleExitLatencyMs",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\Storage\SSD\IdleState\2","IdlePowerMw",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\Storage\SSD\IdleState\2","IdleTimeLengthMs",4294967295)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\Storage\SSD\IdleState\3","IdleExitEnergyMicroJoules",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\Storage\SSD\IdleState\3","IdleExitLatencyMs",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\Storage\SSD\IdleState\3","IdlePowerMw",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\Storage\SSD\IdleState\3","IdleTimeLengthMs",4294967295)

    def _disableTimerCoalescing(self):
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Session Manager","CoalescingTimerInterval",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Session Manager\Power","CoalescingTimerInterval",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","CoalescingTimerInterval",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel","CoalescingTimerInterval",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Session Manager\Executive","CoalescingTimerInterval",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\ModernSleep","CoalescingTimerInterval",0)

    def _deleteDefaultPowerPlans(self):
        commands = [r'powercfg -delete 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c',
                    r'powercfg -delete 381b4222-f694-41f0-9685-ff5bb260df2e',
                    r'powercfg -delete a1841308-3541-4fab-bc81-f71556f20b4a']
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('POWER',cmd)

    def _disablePowerSavingOnDevices(self):
        command = r'POWERSHELL "$devices = Get-WmiObject Win32_PnPEntity; $powerMgmt = Get-WmiObject MSPower_DeviceEnable -Namespace root\wmi; foreach ($p in $powerMgmt){$IN = $p.InstanceName.ToUpper(); foreach ($h in $devices){$PNPDI = $h.PNPDeviceID; if ($IN -like \"*$PNPDI*\"){$p.enable = $False; $p.psbase.put()}}}"'
        subprocess.Popen(command,text=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
        print._printg('POWER',command)

    def _disableGpuEnergyDriver(self):
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Services\GpuEnergyDrv","Start",4)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Services\GpuEnergyDr","Start",4)

    def _disableStoragePowerManagement(self):
        result = subprocess.run(['reg', 'query', r'HKLM\SYSTEM\CurrentControlSet\Enum', '/s', '/f', 'StorPort'], capture_output=True, text=True)
        storport_entries = [line.strip() for line in result.stdout.splitlines() if 'StorPort' in line]

        for entry in storport_entries:
            subprocess.run(['Reg.exe', 'add', entry, '/v', 'EnableIdlePowerManagement', '/t', 'REG_DWORD', '/d', '0', '/f'],text=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
            print._printg('POWER','EnableIdlePowerManagement 0')

        power_management_services = ['EnableHIPM', 'EnableDIPM', 'EnableHDDParking']
        for service in power_management_services:
            result = subprocess.run(['reg', 'query', r'HKLM\SYSTEM\CurrentControlSet\Services', '/s', '/f', service], capture_output=True, text=True)
            
            service_entries = [line.strip() for line in result.stdout.splitlines() if 'HKEY' in line]

            for entry in service_entries:
                subprocess.run(['Reg', 'add', entry, '/v', service, '/t', 'REG_DWORD', '/d', '0', '/f'],text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
                print._printg('POWER',f'{service} 0')
                
        smartctl_result = subprocess.run(['resources\\smartctl.exe', '--scan'], capture_output=True, text=True)
        smartctl_devices = [line.split()[0] for line in smartctl_result.stdout.splitlines()]

        for device in smartctl_devices:
            subprocess.run(['resources\\smartctl.exe', '-s','apm,off',device],text=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
            print._printg('POWER',f'resources\\smartctl.exe -s apm,off {device}')
            subprocess.run(['resources\\smartctl.exe', '-s','aam,off',device],text=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
            print._printg('POWER',f'resources\\smartctl.exe -s aam,off {device}')

        regedit._setHKLMdwordREG('POWER',r'SYSTEM\CurrentControlSet\Control\Storage','StorageD3InModernStandby',0)

    def _disableIdlePowerManagement(self):
        result = subprocess.run(['Reg', 'query', r'HKLM\SYSTEM\CurrentControlSet\Enum', '/s', '/f', 'StorPort'], capture_output=True, text=True)
        storport_entries = [line.strip() for line in result.stdout.splitlines() if 'StorPort' in line]

        for entry in storport_entries:
            subprocess.run(['Reg.exe', 'add', entry, '/v', 'EnableIdlePowerManagement', '/t', 'REG_DWORD', '/d', '0', '/f'],text=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL)
            print._printg('POWER','EnableIdlePowerManagement 0')

    def _disableLinkPowerManagement(self):
        result = subprocess.run(['reg', 'query', r'HKLM\SYSTEM\CurrentControlSet\Services', '/s', '/f', 'EnableHIPM'], capture_output=True, text=True)
            
        hipm_entries = [line.strip() for line in result.stdout.splitlines() if 'HKEY' in line]

        for entry in hipm_entries:
            subprocess.run(['Reg', 'add', entry, '/v', 'EnableHIPM', '/t', 'REG_DWORD', '/d', '0', '/f'],text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            print._printg('POWER',f'EnableHIPM 0')

    def _importDisillusionPowerPlans(self):
        commands = ['powercfg -import "resources\DISILLUSION_Optimal_PowerPlan.pow"',
                    'powercfg -import "resources\DISILLUSION_PowerPlan.pow"',
                    'powercfg.cpl']
        for cmd in commands:
            subprocess.Popen(cmd,text=True).wait()
            print._printg('POWER',cmd) 


    def _additionalPowerTweaks(self):
        regedit._setHKLMdwordREG('POWER',r'SYSTEM\CurrentControlSet\Control\Power','Class2InitialUnparkCount',100)
        regedit._setHKLMdwordREG('POWER',r'SYSTEM\CurrentControlSet\Control\Power','EnergyEstimationDisabled',1)
        regedit._setHKLMdwordREG('POWER',r'SYSTEM\CurrentControlSet\Control\Power','PerfBoostAtGuaranteed',1)
        regedit._setHKLMdwordREG('POWER',r'SYSTEM\CurrentControlSet\Control\Power','PpmMfBufferingThreshold',0)
        regedit._setHKLMdwordREG('POWER',r'SYSTEM\CurrentControlSet\Control\Power','MfOverridesDisabled',1)
        regedit._setHKLMdwordREG('POWER',r'SYSTEM\CurrentControlSet\Control\Power','PpmMfOverridesDisabled',1)
        regedit._setHKLMdwordREG('POWER',r'SYSTEM\CurrentControlSet\Control\Power','UserBatteryDischargeEstimator',1)
        regedit._setHKLMdwordREG('POWER',r'SYSTEM\CurrentControlSet\Control\Power','PowerThrottlingOff',1)
        regedit._setHKLMdwordREG('POWER',r'SYSTEM\CurrentControlSet\Control\Power\PowerThrottling','PowerThrottlingOff',1)

    def _tweakWindowsPowerSettings(self):
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","AwayModeEnabled",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","Class1InitialUnparkCount",100)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","CsEnabled",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","CustomizeDuringSetup",1)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","EnergyEstimationEnabled",1)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","HiberFileSizePercent",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","HibernateEnabled",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","MfBufferingThreshold",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","PerfCalculateActualUtilization",1)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","TimerRebaseThresholdOnDripsExit",30)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","EventProcessorEnabled",1)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","HiberFileType",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","Class2InitialUnparkCount",100)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","EnergyEstimationDisabled",1)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","PerfBoostAtGuaranteed",1)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","PpmMfBufferingThreshold",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","MfOverridesDisabled",1)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","PpmMfOverridesDisabled",1)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","UserBatteryDischargeEstimator",1)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","PowerThrottlingOff",1)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerThrottling","PowerThrottlingOff",1)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Session Manager\Power","HiberbootEnabled",0)

    def _enableKBoost(self):
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","PerfLevelSrc",2222)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","PowerMizerEnable",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","PowerMizerLevel",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}\0000","PowerMizerLevelAC",0)

    def _enableHardwarePStates(self):
        commands = [r'powercfg -setacvalueindex scheme_current sub_processor PERFAUTONOMOUS 1',
                    r'powercfg -setacvalueindex scheme_current sub_processor PERFAUTONOMOUSWINDOW 20000',
                    r'powercfg -setacvalueindex scheme_current sub_processor PERFCHECK 20']
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('POWER',cmd)

    def _disablePowerThrottling(self):
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","CoalescingTimerInterval",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","PlatformAoAcOverride",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","EnergyEstimationEnabled",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","EventProcessorEnabled",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","CsEnabled",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerThrottling","PowerThrottlingOff",1)

    def _coalescingTimerInterval(self):
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Session Manager\Power","CoalescingTimerInterval",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","CoalescingTimerInterval",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Session Manager\Kernel","CoalescingTimerInterval",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Session Manager\Executive","CoalescingTimerInterval",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Session Manager","CoalescingTimerInterval",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\ModernSleep","CoalescingTimerInterval",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","CoalescingTimerInterval",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control","CoalescingTimerInterval",0)

    def _MMCSSPowerTweaks(self):
        regedit._setHKLMregszREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251_82be_4824_96c1_47b60b740d00\943c8cb6_6f93_4227_ad87_e9a3feec08d1","Attributes","2")
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251_82be_4824_96c1_47b60b740d00\75b0ae3f_bce0_45a7_8c89_c9611c25e100","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251_82be_4824_96c1_47b60b740d00\75b0ae3f_bce0_45a7_8c89_c9611c25e100","Affinity",0)
        regedit._setHKLMregszREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251_82be_4824_96c1_47b60b740d00\75b0ae3f_bce0_45a7_8c89_c9611c25e100","Background Only","False")
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251_82be_4824_96c1_47b60b740d00\75b0ae3f_bce0_45a7_8c89_c9611c25e100","Clock Rate",10000)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251_82be_4824_96c1_47b60b740d00\75b0ae3f_bce0_45a7_8c89_c9611c25e100","GPU Priority",8)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251_82be_4824_96c1_47b60b740d00\75b0ae3f_bce0_45a7_8c89_c9611c25e100","Priority",6)
        regedit._setHKLMregszREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251_82be_4824_96c1_47b60b740d00\75b0ae3f_bce0_45a7_8c89_c9611c25e100","Scheduling Category","High")
        regedit._setHKLMregszREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251_82be_4824_96c1_47b60b740d00\75b0ae3f_bce0_45a7_8c89_c9611c25e100","SFIO Priority","High")
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251_82be_4824_96c1_47b60b740d00\75b0ae3f_bce0_45a7_8c89_c9611c25e100","BackgroundPriority",0)
        regedit._setHKLMregszREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251_82be_4824_96c1_47b60b740d00\75b0ae3f_bce0_45a7_8c89_c9611c25e100","Latency Sensitive","True")

    def _disablePowerEstimationAndTelemetry(self):
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\TaggedEnergy","DisableTaggedEnergyLogging",1)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\TaggedEnergy","TelemetryMaxApplication",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\TaggedEnergy","TelemetryMaxTagPerApplication",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\EnergyEstimation\TaggedEnergy","EnergyEstimationEnabled",0)

    def _disableHibernation(self):
        command = r'powercfg /h off'
        subprocess.Popen(command,text=True).wait()
        print._printg('POWER',command)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","HibernateEnabled",0)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power","SleepReliabilityDetailedDiagnostics",0)

    def _disableSleepStudy(self):
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Session Manager\Power","SleepStudyDisabled",1)

    def _disableFastStartup(self):
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Session Manager\Power","HiberbootEnabled",0)

    def _unhidingHiddenPowerPlanSettings(self):
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\19cbb8fa_5279_450e_9fac_8a3d5fedd0c1\12bbebe6_58d6_4636_95bb_3217ef867c1a","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\245d8541_3943_4422_b025_13a784f679b7","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\2a737441_1930_4402_8d77_b2bebba308a3\0853a681_27c8_4100_a2fd_82013e970683","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\2a737441_1930_4402_8d77_b2bebba308a3\48e6b7a6_50f5_4782_a5d4_53bb8f07e226","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\2a737441_1930_4402_8d77_b2bebba308a3\d4e98f31_5ffe_4ce1_be31_1b38b384c009","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\44f3beca_a7c0_460e_9df2_bb8b99e0cba6\3619c3f2_afb2_4afc_b0e9_e7fef372de36","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\4faab71a_92e5_4726_b531_224559672d19","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\501a4d13_42af_4429_9fd1_a8218c268e20\ee12f906_d277_404b_b6da_e5fa1a576df5","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\5FB4938D_1EE8_4b0f_9A3C_5036B0AB995C\DD848B2A_8A5D_4451_9AE2_39CD41658F6C","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\68AFB2D9_EE95_47A8_8F50_4115088073B1","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\F15576E8_98B7_4186_B944_EAFA664402D9","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\8619B916_E004_4dd8_9B66_DAE86F806698\468FE7E5_1158_46EC_88BC_5B96C9E44FD0","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\8619B916_E004_4dd8_9B66_DAE86F806698\49CB11A5_56E2_4AFB_9D38_3DF47872E21B","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\8619B916_E004_4dd8_9B66_DAE86F806698\60C07FE1_0556_45CF_9903_D56E32210242","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\8619B916_E004_4dd8_9B66_DAE86F806698\82011705_FB95_4D46_8D35_4042B1D20DEF","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\8619B916_E004_4dd8_9B66_DAE86F806698\9FE527BE_1B70_48DA_930D_7BCF17B44990","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\8619B916_E004_4dd8_9B66_DAE86F806698\C763EE92_71E8_4127_84EB_F6ED043A3E3D","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\9596FB26_9850_41fd_AC3E_F7C3C00AFD4B\03680956_93BC_4294_BBA6_4E0F09BB717F","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\9596FB26_9850_41fd_AC3E_F7C3C00AFD4B\10778347_1370_4ee0_8bbd_33bdacaade49","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\9596FB26_9850_41fd_AC3E_F7C3C00AFD4B\34C7B99F_9A6D_4b3c_8DC7_B6693B78CEF4","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\DE830923_A562_41AF_A086_E3A2C6BAD2DA\13D09884_F74E_474A_A852_B6BDE8AD03A8","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\DE830923_A562_41AF_A086_E3A2C6BAD2DA\5C5BB349_AD29_4ee2_9D0B_2B25270F7A81","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\DE830923_A562_41AF_A086_E3A2C6BAD2DA\E69653CA_CF7F_4F05_AA73_CB833FA90AD4","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251_82be_4824_96c1_47b60b740d00\75b0ae3f_bce0_45a7_8c89_c9611c25e100","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251_82be_4824_96c1_47b60b740d00\893dee8e_2bef_41e0_89c6_b55d0929964c","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251_82be_4824_96c1_47b60b740d00\94D3A615_A899_4AC5_AE2B_E4D8F634367F","Attributes",2)
        regedit._setHKLMdwordREG('POWER',r"SYSTEM\CurrentControlSet\Control\Power\PowerSettings\54533251_82be_4824_96c1_47b60b740d00\bc5038f7_23e0_4960_96da_33abaf5935ec","Attributes",2)

    def _doAll(self):
        self._disableStoragePowerSavings()    
        self._disableTimerCoalescing()
        self._disablePowerSavingOnDevices()
        self._disableGpuEnergyDriver()
        self._disableStoragePowerManagement()
        self._disableIdlePowerManagement()
        self._disableLinkPowerManagement()
        self._importDisillusionPowerPlans()
        self._additionalPowerTweaks()
        self._tweakWindowsPowerSettings()
        self._enableKBoost()
        self._enableHardwarePStates()
        self._disablePowerThrottling()
        self._coalescingTimerInterval()
        self._MMCSSPowerTweaks()
        self._disablePowerEstimationAndTelemetry()
        self._disableHibernation()
        self._disableSleepStudy()
        self._disableFastStartup()
        self._unhidingHiddenPowerPlanSettings()
