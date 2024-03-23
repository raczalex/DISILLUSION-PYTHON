from utilities import regedit

class Keyboard():
    def __init__(self) -> None:
        pass

    def _disableFilterKeys(self):
        regedit._setHKCUregszREG('KEYBOARD',r"Control Panel\Accessibility\Keyboard Response","Flags","122")

    def _disableToggleKeys(self):
        regedit._setHKCUregszREG('KEYBOARD',r"Control Panel\Accessibility\ToggleKeys","Flags","58")

    def _disableStickyKeys(self):
        regedit._setHKCUregszREG('KEYBOARD',r"Control Panel\Accessibility\StickyKeys","Flags","506")

    def _optimizeKeyboardThreadPriority(self):
        regedit._setHKLMdwordREG('KEYBOARD',r"SYSTEM\CurrentControlSet\Services\kbdclass\Parameters","ThreadPriority",31)

    def _reduceKeyboardRepeatDelay(self):
        regedit._setHKCUregszREG('KEYBOARD',r"Control Panel\Keyboard","KeyboardDelay","0")

    def _increaseKeyboardRepeatRate(self):
        regedit._setHKCUregszREG('KEYBOARD',r"Control Panel\Keyboard","KeyboardSpeed","31")

    def _setKeyboardDataQueueSize(self,value:int=80):
        regedit._setHKLMdwordREG('KEYBOARD',r"SYSTEM\CurrentControlSet\Services\kbdclass\Parameters","KeyboardDataQueueSize",value)

    def _setKeyboardDataQueueSizeTo19(self):
        self._setKeyboardDataQueueSize(19)

    def _setKeyboardDataQueueSizeTo21(self): 
        self._setKeyboardDataQueueSize(21)

    def _setKeyboardDataQueueSizeTo23(self): 
        self._setKeyboardDataQueueSize(23)

    def _setKeyboardDataQueueSizeTo32(self): 
        self._setKeyboardDataQueueSize(32)

    def _setKeyboardDataQueueSizeTo37(self): 
        self._setKeyboardDataQueueSize(37)

    def _setKeyboardDataQueueSizeTo48(self): 
        self._setKeyboardDataQueueSize(48)
        
    def _setKeyboardDataQueueSizeToDefault(self): 
        self._setKeyboardDataQueueSize(80)

    def _enableNumLockOnStartup(self):
        regedit._setHKUregszREG('KEYBOARD',r".DEFAULT\Control Panel\Keyboard","InitialKeyboardIndicators","2")
        regedit._setHKCUregszREG('KEYBOARD',r"Control Panel\Keyboard","InitialKeyboardIndicators","2")

    def _doAll(self):
        self._disableFilterKeys()
        self._disableToggleKeys()
        self._disableStickyKeys()
        self._optimizeKeyboardThreadPriority()
        self._reduceKeyboardRepeatDelay()
        self._increaseKeyboardRepeatRate()