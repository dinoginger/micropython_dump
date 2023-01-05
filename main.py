from machine import ADC, Pin
import time

DEFAULT_ENTRY_PIN = 13
DEFAULT_ADC_PIN = 12


class Lab1_controller:

    _info_pin = None
    _entry_pin = None

    def __init__(self, adc, entr): #
        Pin(adc).value(1)
        self._info_pin = ADC(Pin(adc))

        self._info_pin.atten(ADC.ATTN_11DB) # volt [0.0 - 3.6v]

        
        self._entry_pin = Pin(entr, Pin.OUT)
        self._entry_pin.value(1)

    def reciever(self):
        print((self._info_pin.read()/4095)*100) # values are from 0 to 4095 so we get percentages
        time.sleep(0.1)
        #test version
        

    def something(self):
        pass

    def LED_on(self):
        self._entry_pin.value(1)

    def LED_off(self):
        self._entry_pin.value(0)


Pin(DEFAULT_ENTRY_PIN, Pin.OUT).value(0)
print("script is running")
lab_machine = Lab1_controller(DEFAULT_ADC_PIN, DEFAULT_ENTRY_PIN)
input("Press anything to launch\n")

while True:
    lab_machine.reciever()

# TODO :  proper logging of the results for long lab (separate class ig)
# TODO : improve main class