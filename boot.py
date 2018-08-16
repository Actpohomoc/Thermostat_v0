# Conexion del modulo NodeMCU a red wifi
#
import gc
#import webrepl
#webrepl.start()
gc.collect()

def do_connect():
    import network
    import settings
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(settings.WIFI_SSID, settings.WIFI_PW)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
