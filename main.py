''' ESP8266 NodeMCU
	PINOUT	 
 D0 > GPIO16 > User > Wake
 D1 > GPIO5 >>> SDA I2C (Using soft)
 D2 > GPIO4 >>> SCL I2C (Using soft)
 D3 > GPIO0 > Flash
 D4 > GPIO2 > TXD1
 D5 > GPIO14 > > HSCLK
 D6 > GPIO12 > > HMISO
 D7 > GPIO13 > RXD2 > HMOSI
 D8 > GPIO15 > TXD2 > HCS
 RX > GPIO3 > RXD0
 TX > GPIO1 > TXD0
 CLK > SCKL > SDCLK
 SDD > MISO > SDD0
 CMD > CS > SDCMD
 SD1 > MOSI > SDD1
 SD2 > GPIO9 > SDD2
 SD3 > GPIO10 > SDD3
 A0 > ADC0 > TOUT

'''
import cSensor
import cDisplay
import settings
from time import sleep_ms
from machine import Pin

RelayPin = Pin(settings.PIN_RELAY, Pin.OUT, value=0) #Relay Pin
target_temperature = 25
histeresis = 0.5

while True:    
    temperature, humidity = cSensor.get_data()
    cDisplay.display(settings.LOCATION, temperature, humidity)
        
    if temperature < (target_temperature - histeresis):
        RelayPin.on()
        #send_status("Relay ON")

    elif temperature > (target_temperature + histeresis):
        RelayPin.off()    
        #send_status("Relay OFF")

    sleep_ms(1000)


#print(temperature)
#print(humidity)
