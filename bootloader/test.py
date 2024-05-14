import time

import cflib.crtp
from cflib.crtp.crtpstack import CRTPPacket
from cflib.crtp.radiodriver import RadioManager
from utils.power_switch import PowerSwitch

power_switch = PowerSwitch('radio://0/80/2M/1217E7E7E7')
power_switch.reboot_to_bootloader()
