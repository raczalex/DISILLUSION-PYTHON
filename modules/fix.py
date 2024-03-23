import subprocess
from utilities import print

class Fix():
    def __init__(self) -> None:
        pass

    def _scanNow(self):
        command = r'sfc /scannow'
        subprocess.Popen(command,text=True).wait()
        print._printg('FIX',command)

    def _dismRestoreHealth(self):
        command = r'dism /online /cleanup-image /restorehealth'
        subprocess.Popen(command,text=True).wait()
        print._printg('FIX',command)

    def _doAll(self):
        self._scanNow()
        self._dismRestoreHealth()