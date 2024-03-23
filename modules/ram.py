import subprocess
from utilities import regedit
from utilities import print

class RAM():
    def __init__(self) -> None:
        pass

    def _disableMemoryCompression(self):
        command = r'PowerShell -Command "Disable-MMAgent -MemoryCompression"'
        subprocess.Popen(command,text=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL).wait()
        print._printg('RAM',command)
        

    def _disablePageCombining(self):
        command = r'PowerShell -Command "Disable-MMAgent -PageCombining"'
        subprocess.Popen(command,text=True,stderr=subprocess.DEVNULL,stdout=subprocess.DEVNULL).wait()
        print._printg('RAM',command)
    
    def _setSvcSplitHost(self):
        wmic_command = 'wmic os get TotalVisibleMemorySize'
        wmic_process = subprocess.Popen(wmic_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        wmic_output, _ = wmic_process.communicate()

        total_memory_value = wmic_output.decode().split('\n')[1]
        total_memory_str = ''.join(total_memory_value)

        if total_memory_str:
            total_memory = int(total_memory_str)
            svchost_value = total_memory + 1024000

            regedit._setHKLMdwordREG('RAM',r'SYSTEM\CurrentControlSet\Control','SvcHostSplitThresholdInKB',svchost_value)
        else:
            print._printr('RAM','Error retrieving TotalVisibleMemorySize')

    def _disableSuperfetch(self):
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\memory management\prefetchparameters","EnableSuperfetch",0)

    def _disablePrefetch(self):
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters","EnablePrefetcher",0)

    def _ramTweaks(self):
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","LargeSystemCache",1)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","ClearPageFileAtShutdown",0)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","DisablePagingExecutive",1)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","LargeSystemCache",0)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","NonPagedPoolQuota",0)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","NonPagedPoolSize",0)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","PagedPoolQuota",0)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","PagedPoolSize",192)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","SecondLevelDataCache",1024)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","SessionPoolSize",192)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","SessionViewSize",192)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","SystemPages",4294967295)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","PhysicalAddressExtension",1)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","ClearPageFileAtShutdown",0)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","DisablePagingExecutive",1)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","LargeSystemCache",0)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","NonPagedPoolQuota",0)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","NonPagedPoolSize",0)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","PagedPoolQuota",0)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","PagedPoolSize",192)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","SecondLevelDataCache",1024)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","SessionPoolSize",192)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","SessionViewSize",192)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","SystemPages",4294967295)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","PhysicalAddressExtension",1)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","FeatureSettings",1)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","FeatureSettingsOverride",3)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","FeatureSettingsOverrideMask",3)
        regedit._setHKLMdwordREG('RAM',r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management","PoolUsageMaximum",96)


    def _doAll(self):
        self._disableMemoryCompression()
        self._disablePageCombining()
        self._setSvcSplitHost()
        self._disableSuperfetch()
        self._disablePrefetch()
        self._ramTweaks()