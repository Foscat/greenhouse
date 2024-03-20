#!/usr/bin/env python3

import time
import humidity_temp
import settings
import pincontrol
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)  # Board mode


plug1 = False  # Lights
plug2 = False  # Vent
plug3 = False  # Fan
plug4 = False  # Humidifier
plug5 = False  # De-Humidifier

mode = settings.veg


def main():
    print("Greenhouse control program has started")
    while True:
        result = humidity_temp.read_dht11_dat()
        global plug1
        global plug2
        global plug3
        global plug4
        global plug5
        if result:
            humidity, temperature = result
            temperature = (temperature * 1.8) + 32
            print("Humidity: %s %%,  Temperature: %s F`" %
                  (humidity, temperature))
            plugGroup = {"plug1": plug1, "plug2": plug2,
                         "plug3": plug3, "plug4": plug4, "plug5": plug5}
            plugSettings = settings.setSwitches(
                temperature, humidity, mode, plugGroup)
            print("What is on? Plug 1 (Lights): " + str(plugSettings["plug1"])+", Plug 2 (Vent): "+str(plugSettings["plug2"]) + ", Plug 3 (Fan): " +
                  str(plugSettings["plug3"])+", Plug 4 (Humidifier): "+str(plugSettings["plug4"]) + ", Plug 5 (De-Humidifier): "+str(plugSettings["plug5"]))
            plug1 = plugSettings["plug1"]
            plug2 = plugSettings["plug2"]
            plug3 = plugSettings["plug3"]
            plug4 = plugSettings["plug4"]
            plug5 = plugSettings["plug5"]
            pincontrol.setPlugPower(plug1, plug2, plug3, plug4, plug5)

    time.sleep(1)
    # print("Loop end")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        humidity_temp.destroy()
        pincontrol.destroy()
        print("Greenhouse control program has shut down.")
