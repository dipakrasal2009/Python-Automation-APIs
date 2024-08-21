from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

def set_volume(level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        ISimpleAudioVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(ISimpleAudioVolume)
    volume.SetMasterVolume(level, None)
