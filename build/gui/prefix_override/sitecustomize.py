import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/roverj8/LUIS/ARGJ08/ARGOSJ8_IA_/install/gui'
