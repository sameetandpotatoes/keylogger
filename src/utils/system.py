import platform

OS_MAPPINGS = {
    'mac': 'Darwin',
    'linux': 'Linux',
    'windows': 'Windows'
}

def get_os():
    return platform.system()
