import subprocess
from utilities import print

class Bcdedit():
    def __init__(self) -> None:
        pass

    def _start(self):
        commands = [r'bcdedit /set configaccesspolicy default',
                    r'bcdedit /set MSI default',
                    r'bcdedit /set usephysicaldestination no',
                    r'bcdedit /set usefirmwarepcisettings no',
                    r'bcdedit /deletevalue useplatformtick >nul 2>&1',
                    r'bcdedit /deletevalue useplatformclockJ >nul 2>&1',
                    r'bcdedit /set disabledynamictick yes',
                    r'bcdedit /set tscsyncpolicy legacy',
                    r'bcdedit /set x2apicpolicy enable',
                    r'bcdedit /set ems no',
                    r'bcdedit /set bootems no',
                    r'bcdedit /set vm no',
                    r'bcdedit /set sos no',
                    r'bcdedit /set quietboot yes',
                    r'bcdedit /set integrityservices disable',
                    r'bcdedit /set bootux disabled',
                    r'bcdedit /set bootlog no',
                    r'bcdedit /set tpmbootentropy ForceDisable',
                    r'bcdedit /set disableelamdrivers yes',
                    r'bcdedit /set hypervisorlaunchtype off',
                    r'bcdedit /set isolatedcontext no',
                    r'bcdedit /set pae ForceDisable',
                    r'bcdedit /set vsmlaunchtype off']

        for cmd in commands:
            subprocess.Popen(cmd,text=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).wait()
            print._printg('BCDEDIT',cmd)