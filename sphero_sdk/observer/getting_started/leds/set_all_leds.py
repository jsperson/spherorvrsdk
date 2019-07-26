import sys
sys.path.append('/home/pi/raspberry-pi-python')

from sphero_sdk import ObserverSpheroRvr
from sphero_sdk import Colors
from sphero_sdk import RvrLedGroups

rvr = ObserverSpheroRvr()

def main():
    rvr.wake()

    # Set power buttons to blue
    led_group_bitmask = RvrLedGroups.all_lights.value # 0x3fffffff

    rvr.set_all_leds_with_32_bit_mask(
        led_group_bitmask, [color for i in range(10) for color in [255, 0, 0]]
    )


main()
