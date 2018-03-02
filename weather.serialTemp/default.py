import os, sys, time
import xbmc, xbmcgui, xbmcaddon

from random import randint
import time

ADDON        = xbmcaddon.Addon()
ADDONNAME    = ADDON.getAddonInfo('name')
ADDONID      = ADDON.getAddonInfo('id')
ADDONVERSION = ADDON.getAddonInfo('version')

CWD          = ADDON.getAddonInfo('path').decode("utf-8")
RESOURCE     = xbmc.translatePath( os.path.join( CWD, 'resources', 'lib' ).encode("utf-8") ).decode("utf-8")
sys.path.append(RESOURCE)


WEATHER_WINDOW   = xbmcgui.Window(12600)


def set_property(name, value):
    WEATHER_WINDOW.setProperty(name, value)

def setTemp(data, number=0):
    if number == 0:
        set_property('Current.Location'          , data['Loc'])
        set_property('Current.Condition'         , data['Loc'])
        set_property('Current.Temperature'       , str(data['Temp']))
        set_property('Current.Wind'              , "na")
        set_property('Current.Humidity'          , "na")
        set_property('Current.OutlookIcon'       , getImg(data['Temp']))

def getImg(temp):
    if temp < 5:
        return "41.png"
    elif temp > 25:
        return "36.png"
    else:
        t = int(time.ctime()[11:13])
        if t < 8 or t > 20:
            return "33.png"
        else:
            return "34.png"

class MyMonitor(xbmc.Monitor):
    def __init__(self, *args, **kwargs):
        xbmc.Monitor.__init__(self)
MONITOR = MyMonitor()
set_property('WeatherProvider'    , ADDONNAME)
    
temp = randint(-20, 50)
data = {}
data['Loc'] = "Outside"
data['Temp'] = temp

setTemp(data)







