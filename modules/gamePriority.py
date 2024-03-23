from utilities import regedit
from utilities import print

class GamePriority():
    def __init__(self) -> None:
        pass

    def _configureQosForGame(self,exe_name):
        try:
            reg_key_path = f'Software\\Policies\\Microsoft\\Windows\\QoS\\{exe_name}.exe'
            qos_settings = [
                ('Application Name', f'{exe_name}.exe'),
                ('Version', '1.0'),
                ('Protocol', '*'),
                ('Local Port', '*'),
                ('Local IP', '*'),
                ('Local IP Prefix Length', '*'),
                ('Remote Port', '*'),
                ('Remote IP', '*'),
                ('Remote IP Prefix Length', '*'),
                ('DSCP Value', '46'),
                ('Throttle Rate', '-1'),
            ]

            for key, value in qos_settings:
                regedit._setHKLMregszREG('GAME PRIORITY',reg_key_path,key,value)

            print._printg('SUCCESS', f'Configured QoS for {exe_name}.exe')

        except Exception as e:
            print._printr('ERROR', f'Configuring QoS for {exe_name}.exe')

    def _tweakGame(self,exe_name):
        self._configureQosForGame(exe_name)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","CpuPriorityClass",8)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuPriorityClass",8)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","CpuPriority",42)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuPriority",42)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","IoPriority",8)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","Clock Rate",65536)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","Affinity",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","CpuThreadPriority",8)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","CpuPriorityControl",1)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","CpuThreadCount",8)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","PowerThrottlingOff",1)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","CpuPrioritySeperation",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","RMHdcpKeyGlobZero",1)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","PowerLimitEnabled",1)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","Priority",6)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","SystemResponsiveness",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GPU Priority",8)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","IOPriorityClass",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","MaximumPerformanceEnabled",1)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","MaxPerformance",256)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","LowestPerformance",256)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","MinimumPerformanceEnabled",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","Io Priority",8)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","HBFlagsSwitch",1)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","HiberbootEnabled",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","PowerSettingProfile",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","SleepStudyDeviceAccountingLevel",4)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","WatchdogResumeTimeout",120)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","WatchdogSleepTimeout",300)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","POSTTime",8323)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","BootmgrUserInputTime",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","FwPOSTTime",8323)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","CoalescingTimerInterval",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuSpeed",256)
        regedit._setHKLMregszREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","e","True")
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","CpuCoresAlways",18)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","CpuUtilization",256)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","LatencyPerformance",256)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuPerformance",256)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","RenderingSpread",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","RenderingPerformance",256)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","LatencySpread",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","RenderingPriority",8)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","LatencyPriority",8)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","CpuSpread",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuRenderingPriority",8)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","SpreadPriority",1)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuMax",256)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","MinPerformance",256)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","PerformancePriority",8)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","PerformanceSpread",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuMaxPerformance",256)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","CpuMaxPerformance",256)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuAccelerating",256)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","DisableHWAcceleration",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","MaxMultisampleSize",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","HwSchMode",2)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuThrottling",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuStutter",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","FadeIo",24)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuClockSwitchLatency",1)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","UseReferenceRasterizer",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","EnableHWAcceleration",1)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","SmoothBrightnessDefaultEnable",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","SmoothBrightnessDefaultDisable",1)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","EnableRenderingSlowDown",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","EnableRenderingCache",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","EnableRenderingPowerSlowDown",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","EnablePowerSlowDown",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","EnablePowerControlSlowDown",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","DisableRenderingContextPreemption",1)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","DisableRenderingPreemption",1)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","DisableFGBoostDecay",1)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","IsLowPriority",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","IsRenderingLowPriority",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","RenderingBasePriority",130)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","RenderingOverTargetPriority",80)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","RenderThrottlingOff",1)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","EnableMidRenderingPreemption",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","RenderingPowerSteeringEnable",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","PowerSavingVsyncOn",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","HwSchedMode",2)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","UnlimitedPerformance",1)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","SmoothStutterEnabled",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","EnableGpuTempData",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","EnableGpuCashing",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","EnableGpuSlowDown",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","PPMEnabled",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","EnableGpuPowerControl",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","EnableGpuPreemption",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuIdleLatencyEnabled",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuIdleEnabled",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuPreemptionEnabled",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuBackgoundTaskPriority",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuRenderingPriority",3)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuBackgoundTaskLimit",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","PowerSavingBackgoundTaskEnabled",1)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","RenderingSmoothStutterEnabled",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","RenderingStutterEnabled",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuRenderingLatencyEnabled",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuRenderingPriorityForBackgoundTask",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","PowerSavingRenderingEnabled",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuClockSpeed",65536)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuRenderingClockSpeed",65536)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","UseBestResolution",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","SmoothResolutionEnabled",1)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","TVSupportEnabled",0)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","GpuThrottleRate",65536)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","SwapEffectUpgradeCache",1)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","CpuPriorityClass",3)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe\\PerfOptions","IoPriority",3)
        regedit._setHKLMdwordREG('GAME PRIORITY',f"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\{exe_name}.exe","UseLargePages",1)

    def _configureQosAndTweakGTA5(self):
        self._tweakGame('GTA5')

    def _configureQosAndTweakFiveM(self):
        self._tweakGame('fivem')

    def _configureQosAndTweakCS2(self):
        self._tweakGame('cs2')

    def _configureQosAndTweakApex(self):
        self._tweakGame('r5apex')
    
    def _configureQosAndTweakFortnite(self):
        self._tweakGame('FortniteClient-Win64')

    def _configureQosAndTweakValorant(self):
        self._tweakGame('ValorantClient-Win64-Shipping')

    def _doAll(self):
        self._configureQosAndTweakGTA5()
        self._configureQosAndTweakFiveM()
        self._configureQosAndTweakCS2()
        self._configureQosAndTweakApex()
        self._configureQosAndTweakFortnite()
        self._configureQosAndTweakValorant()