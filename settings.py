import time

maxTemp = 85
idealTemp = 77
minTemp = 70


veg = {
    "name": "Veg",
    "humidity": {
        "min": 40,
        "ideal": 50,
        "max": 60
    },
    "lights": {
        "on": 5,
        "off": 23
    },
    "ventOn": False
}

flower = {
    "name": "Flower",
    "humidity": {
        "min": 40,
        "ideal": 45,
        "max": 50
    },
    "lights": {
        "on": 7,
        "off": 19
    },
    "ventOn": True
}

final_flower = {
    "name": "Final Flower",
    "humidity": {
        "min": 40,
        "ideal": 45,
        "max": 50
    },
    "lights": {
        "on": 7,
        "off": 19
    },
    "ventOn": True
}


dry = {
    "name": "Dry",
    "humidity": {
        "min":  50,
        "ideal": 53,
        "max": 55
    }
    ,
    "lights": {
        "on": 0,
        "off": 0
    },
    "ventOn": False
}

def setSwitches(curTemp, curHumidity, mode, current_plugs):
    plug1 = current_plugs["plug1"]
    plug2 = current_plugs["plug2"]
    plug3 = current_plugs["plug3"]
    plug4 = current_plugs["plug4"]
    plug5 = current_plugs["plug5"]

    # Plug copy of values before function runs
    mutablePlugs = current_plugs 
    # gmt stores current gmtime
    gmt = time.gmtime()
    # Store current hour in military time
    milTimeHour = gmt[3]

    # Check time if lights should be on
    if milTimeHour > mode["lights"]["on"] and milTimeHour < mode["lights"]["off"]:
      print(milTimeHour > mode["lights"]["on"] and milTimeHour < mode["lights"]["off"], milTimeHour > mode["lights"]["on"], milTimeHour < mode["lights"]["off"])
      mutablePlugs["plug1"] = True
    else:
      mutablePlugs["plug1"] = False 

    # If temperature is too high for current mode
    if curTemp >= maxTemp:
     # If vent is not on turn on vent
      if not(plug2):
        mutablePlugs["plug2"] = True
      # If fan is not on then turn on fan
      if not(plug3):
        mutablePlugs["plug3"] = True
      # If the current humidity is below the max for the current mode turn on humidifier if not already on.
      if curHumidity < mode["humidity"]["max"] and not(plug4):
          mutablePlugs["plug4"] = True
      if curHumidity > mode["humidity"]["max"]:
        if plug4:
          mutablePlugs["plug4"] = False
        if not(plug5):
          mutablePlugs["plug5"] = True
    # If current temp is between the min and max or at ideal temp
    elif curTemp > minTemp and curTemp < maxTemp or curTemp == idealTemp:
      # If current humidity is too high for current mode
      if curHumidity > mode["humidity"]["max"]:
        # If humidifier is on turn it off
        if plug4:
          mutablePlugs["plug4"] = False
        # If dehumidifier is off turn it on
        if not(plug5):
          mutablePlugs["plug5"] = True
      # If current humidity is too low for current mode
      elif curHumidity < mode["humidity"]["min"]:
        # If humidifier is off turn it on
        if not(plug4):
          mutablePlugs["plug4"] = True
        # If dehumidifier is on turn it off
        if plug5:
          mutablePlugs["plug5"] = False
      # If current humidity is equal to the ideal for current mode
      elif curHumidity == mode["humidity"]["ideal"]:
        # If humidifier is on turn it off
        if plug4:
          mutablePlugs["plug4"] = False
        # If dehumidifier is on turn it off
        if plug5:
          mutablePlugs["plug5"] = False
    # If temp is lower than minimum allowed temp
    else:
      # If vent is on turn it off
      if plug2:
        mutablePlugs["plug2"] = False
      # If fan is on turn it off
      if plug3:
        mutablePlugs["plug3"] = False
      # If current humidity less than to the minimum for current mode
      if curHumidity < mode["humidity"]["min"]:
        # If humidifier is off turn it on
        if not(plug4):
          mutablePlugs["plug4"] = True
        # If dehumidifier is on turn it off
        if plug5:
          mutablePlugs["plug5"] = False
      else:
        # If humidifier is on turn it off
        if plug4:
          mutablePlugs["plug4"] = False
        # If dehumidifier is on turn it off
        if plug5:
          mutablePlugs["plug5"] = False
    return mutablePlugs

