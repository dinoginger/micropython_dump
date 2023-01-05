from machine import ADC, Pin
import time

# This is constants.
DEFAULT_ENTRY_PIN = 13
DEFAULT_ADC_PIN = 12


class Lab1_controller:
    """
    The main class for our machine.

    Will include the main controller functions.    
    """
    _info_pin = None  # ADC pin (photosensor)
    _entry_pin = None # LED pin

    def __init__(self, adc, entr): # constructor

        
        self._entry_pin = Pin(entr, Pin.OUT)
        self._info_pin = ADC(Pin(adc))

        self._entry_pin.value(1)  # Activating pins
        self.Pin(entr).value(1) # --  
    

        self._info_pin.atten(ADC.ATTN_11DB) # volt [0.0 - 3.6v]

        
        
    def reciever(self):
        print((self._info_pin.read()/4095)*100) # values are from 0 to 4095 so we get percentages
        time.sleep(0.1)
        # TODO: finish it
        

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