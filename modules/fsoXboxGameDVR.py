from utilities import regedit

class FsoXboxGameDVR():
    def __init__(self) -> None:
        pass

    def _disable(self):
        regedit._setHKLMdwordREG('FSO & XBOX GAMEDVR',r"SOFTWARE\Microsoft\PolicyManager\default\ApplicationManagement\AllowGameDVR","value",0)
        regedit._setHKCUdwordREG('FSO & XBOX GAMEDVR',r"System\GameConfigStore","GameDVR_Enabled",0)
        regedit._setHKCUdwordREG('FSO & XBOX GAMEDVR',r"System\GameConfigStore","GameDVR_FSEBehaviorMode",0)
        regedit._setHKCUdwordREG('FSO & XBOX GAMEDVR',r"System\GameConfigStore","GameDVR_HonorUserFSEBehaviorMode",0)
        regedit._setHKCUdwordREG('FSO & XBOX GAMEDVR',r"System\GameConfigStore","GameDVR_DXGIHonorFSEWindowsCompatible",0)
        regedit._setHKCUdwordREG('FSO & XBOX GAMEDVR',r"System\GameConfigStore","GameDVR_EFSEFeatureFlags",0)
        regedit._setHKLMdwordREG('FSO & XBOX GAMEDVR',r"SOFTWARE\Policies\Microsoft\Windows\GameDVR","AllowGameDVR",0)
        regedit._setHKCUdwordREG('FSO & XBOX GAMEDVR',r"Software\Microsoft\GameBar","UseNexusForGameBarEnabled",0)
        regedit._setHKCUdwordREG('FSO & XBOX GAMEDVR',r"Software\Microsoft\Windows\CurrentVersion\GameDVR","AppCaptureEnabled",0)

    def _revert(self):
        regedit._setHKLMdwordREG('FSO & XBOX GAMEDVR',r"SOFTWARE\Microsoft\PolicyManager\default\ApplicationManagement\AllowGameDVR","value",1)
        regedit._setHKCUdwordREG('FSO & XBOX GAMEDVR',r"System\GameConfigStore","GameDVR_Enabled",1)
        regedit._setHKCUdwordREG('FSO & XBOX GAMEDVR',r"System\GameConfigStore","GameDVR_FSEBehaviorMode",1)
        regedit._setHKCUdwordREG('FSO & XBOX GAMEDVR',r"System\GameConfigStore","GameDVR_HonorUserFSEBehaviorMode",1)
        regedit._setHKCUdwordREG('FSO & XBOX GAMEDVR',r"System\GameConfigStore","GameDVR_DXGIHonorFSEWindowsCompatible",0)
        regedit._setHKCUdwordREG('FSO & XBOX GAMEDVR',r"System\GameConfigStore","GameDVR_EFSEFeatureFlags",0)
        regedit._setHKLMdwordREG('FSO & XBOX GAMEDVR',r"SOFTWARE\Policies\Microsoft\Windows\GameDVR","AllowGameDVR",1)
        regedit._setHKCUdwordREG('FSO & XBOX GAMEDVR',r"Software\Microsoft\GameBar","UseNexusForGameBarEnabled",0)
        regedit._setHKCUdwordREG('FSO & XBOX GAMEDVR',r"Software\Microsoft\Windows\CurrentVersion\GameDVR","AppCaptureEnabled",1)