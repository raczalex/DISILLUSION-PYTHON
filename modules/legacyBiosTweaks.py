import subprocess
from utilities import regedit
from utilities import print

class LegacyBiosTweaks():
    def __init__(self) -> None:
        pass

    def _start(self):
        regedit._setHKLMdwordREG('LEGACY BIOS TWEAKS',r"System\CurrentControlSet\Services\VxD\BIOS","CPUPriority",1)
        regedit._setHKLMdwordREG('LEGACY BIOS TWEAKS',r"System\CurrentControlSet\Services\VxD\BIOS","FastDRAM",1)
        regedit._setHKLMdwordREG('LEGACY BIOS TWEAKS',r"System\CurrentControlSet\Services\VxD\BIOS","AGPConcur",1)
        regedit._setHKLMdwordREG('LEGACY BIOS TWEAKS',r"System\CurrentControlSet\Services\VxD\BIOS","PCIConcur",1)

        commands = [r'bcdedit /set tscsyncpolicy legacy',
                    r'bcdedit /set hypervisorlaunchtype off',
                    r'bcdedit /set linearaddress57 OptOut',
                    r'bcdedit /set increaseuserva 268435328',
                    r'bcdedit /set isolatedcontext No',
                    r'bcdedit /set allowedinmemorysettings 0x0',
                    r'bcdedit /set vsmlaunchtype Off',
                    r'bcdedit /set vm No']
        

        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('LEGACY BIOS TWEAKS',cmd)

        regedit._setHKLMdwordREG('LEGACY BIOS TWEAKS',r"Software\Policies\Microsoft\FVE","DisableExternalDMAUnderLock",0)
        regedit._setHKLMdwordREG('LEGACY BIOS TWEAKS',r"Software\Policies\Microsoft\Windows\DeviceGuard","EnableVirtualizationBasedSecurity",0)
        regedit._setHKLMdwordREG('LEGACY BIOS TWEAKS',r"Software\Policies\Microsoft\Windows\DeviceGuard","HVCIMATRequired",0)

        commands.clear()

        commands = [r'bcdedit /set x2apicpolicy Enable',
                    r'bcdedit /set uselegacyapicmode No',
                    r'bcdedit /set configaccesspolicy Default',
                    r'bcdedit /set MSI Default',
                    r'bcdedit /set usephysicaldestination No',
                    r'bcdedit /set usefirmwarepcisettings No"']
        
        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('LEGACY BIOS TWEAKS',cmd)