from utilities import regedit

class Mouse():
    def __init__(self) -> None:
        pass

    def _disableMouseKeys(self):
        regedit._setHKCUregszREG('MOUSE',r"Control Panel\Accessibility\MouseKeys","Flags","0")

    def _disableMouseAcceleration(self):
        regedit._setHKCUregszREG('MOUSE',r"Control Panel\Mouse","MouseSpeed","0")
        regedit._setHKCUregszREG('MOUSE',r"Control Panel\Mouse","MouseThreshold1","0")
        regedit._setHKCUregszREG('MOUSE',r"Control Panel\Mouse","MouseThreshold2","0")

    def _mouseHIDOptimize(self):
        regedit._setHKLMdwordREG('MOUSE',r"SYSTEM\CurrentControlSet\Services\mouhid\Parameters","TreatAbsolutePointerAsAbsolute",1)
        regedit._setHKLMdwordREG('MOUSE',r"SYSTEM\CurrentControlSet\Services\mouhid\Parameters","TreatAbsoluteAsRelative",0)

    def _enable1on1PixelMovements(self):
        regedit._setHKCUregszREG('MOUSE',r"Control Panel\Mouse","MouseSensitivity","10")

    def _disableMouseSmoothing(self):
        regedit._setHKCUbinaryREG('MOUSE',r"Control Panel\Mouse","SmoothMouseXCurve",b'00000000000000000000000000000000000000000000000000000000000000000000000000000000')
        regedit._setHKCUbinaryREG('MOUSE',r"Control Panel\Mouse","SmoothMouseYCurve",b'00000000000000000000000000000000000000000000000000000000000000000000000000000000')

    def _optimizeMouseThreadPriority(self):
        regedit._setHKLMdwordREG('MOUSE',r"SYSTEM\CurrentControlSet\Services\mouclass\Parameters","ThreadPriority",31)

    def _setCRSSToRealtime(self):
        regedit._setHKLMdwordREG('MOUSE',r"SYSTEM\CurrentControlSet\Control\Session Manager\kernel","DebugPollInterval",1000)

    def _setCSRSSToRealTime(self):
        regedit._setHKLMdwordREG('MOUSE',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\csrss.exe\PerfOptions","CpuPriorityClass",4)
        regedit._setHKLMdwordREG('MOUSE',r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\csrss.exe\PerfOptions","IoPriority",3)

    def _optimizeMouseSettingsControlPanel(self):
        regedit._setHKUdwordREG('MOUSE',r".DEFAULT\Control Panel\Desktop","ForegroundLockTimeout",0)
        regedit._setHKUregszREG('MOUSE',r".DEFAULT\Control Panel\Desktop","MenuShowDelay","0")
        regedit._setHKUdwordREG('MOUSE',r".DEFAULT\Control Panel\Desktop","MouseWheelRouting",0)
        regedit._setHKUregszREG('MOUSE',r".DEFAULT\Control Panel\Mouse","Beep","No")
        regedit._setHKUregszREG('MOUSE',r".DEFAULT\Control Panel\Mouse","ExtendedSounds","No")
        regedit._setHKUregszREG('MOUSE',r".DEFAULT\Control Panel\Sound","Beep","No")
        regedit._setHKUregszREG('MOUSE',r".DEFAULT\Control Panel\Sound","ExtendedSounds","No")
        regedit._setHKCUdwordREG('MOUSE',r"Control Panel\Mouse","ActiveWindowTracking",0)
        regedit._setHKCUregszREG('MOUSE',r"Control Panel\Mouse","Beep","No")
        regedit._setHKCUregszREG('MOUSE',r"Control Panel\Mouse","DoubleClickHeight","No")
        regedit._setHKCUregszREG('MOUSE',r"Control Panel\Mouse","DoubleClickSpeed","No")
        regedit._setHKCUregszREG('MOUSE',r"Control Panel\Mouse","DoubleClickWidth","No")
        regedit._setHKCUregszREG('MOUSE',r"Control Panel\Mouse","ExtendedSounds","No")
        regedit._setHKCUregszREG('MOUSE',r"Control Panel\Mouse","MouseHoverHeight","No")
        regedit._setHKCUregszREG('MOUSE',r"Control Panel\Mouse","MouseHoverWidth","No")
        regedit._setHKCUregszREG('MOUSE',r"Control Panel\Mouse","MouseTrails","No")
        regedit._setHKCUregszREG('MOUSE',r"Control Panel\Mouse","SnapToDefaultButton","No")
        regedit._setHKCUregszREG('MOUSE',r"Control Panel\Mouse","SwapMouseButtons","No")
        regedit._setHKCUregszREG('MOUSE',r"Control Panel\Mouse","MouseHoverTime","No")

    def _setMouseDataQueuSize(self,value:int):
        regedit._setHKLMdwordREG('MOUSE',r"SYSTEM\CurrentControlSet\Services\mouclass\Parameters","MouseDataQueueSize",value)

    def _setMouseDataQueueSizeTo19(self):
        self._setMouseDataQueuSize(19)

    def _setMouseDataQueueSizeTo21(self): 
        self._setMouseDataQueuSize(21)

    def _setMouseDataQueueSizeTo23(self): 
        self._setMouseDataQueuSize(23)

    def _setMouseDataQueueSizeTo32(self): 
        self._setMouseDataQueuSize(32)

    def _setMouseDataQueueSizeTo37(self): 
        self._setMouseDataQueuSize(37)

    def _setMouseDataQueueSizeTo48(self): 
        self._setMouseDataQueuSize(48)
        
    def _setMouseDataQueueSizeToDefault(self): 
        self._setMouseDataQueuSize(80)

    def _doAll(self):
        self._disableMouseKeys()
        self._disableMouseAcceleration()
        self._mouseHIDOptimize()
        self._enable1on1PixelMovements()
        self._disableMouseSmoothing()
        self._optimizeMouseThreadPriority()
        self._setCRSSToRealtime()
        self._setCSRSSToRealTime()
        self._optimizeMouseSettingsControlPanel()

