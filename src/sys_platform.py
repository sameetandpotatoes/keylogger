import platform

class SysPlatform:
    def __init__(self):
        self.processor = platform.processor()
        self.os = platform.system()
        self.x86 = platform.machine()

def get_platform():
    return SysPlatform().__dict__
