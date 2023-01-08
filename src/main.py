from machine import ADC, Pin, PWM
import time

# This is constants.
DEFAULT_ENTRY_PIN = 13
DEFAULT_ADC_PIN = 36
FILE_PATH  = "/test.txt"

class Lab1_controller:
    """
    The main class for our machine.

    Will include the main controller functions.    
    """
    _info_pin = None  # ADC pin (photosensor)
    _entry_pin = None # LED pin
    _pwm = None

    def __init__(self, adc, entr): # constructor

        
        self._entry_pin = Pin(entr)
        self._info_pin = ADC(Pin(adc))
        self._info_pin.atten(ADC.ATTN_11DB) # volt [0.0 - 3.6v]

        # 
        self._pwm = PWM(Pin(DEFAULT_ENTRY_PIN), 5000)

        self._entry_pin.value(1)  # Activating pins
 
        
        
    def reciever(self):
        info = self._info_pin.read()
        print(info) # values are from 0 to 4095 so we get percentages
        time.sleep(0.01)
        return info
        # TODO: finish it


    def change_light(self, value):
        self._pwm.duty(value)


    def LED_on(self):
        self._entry_pin.value(1)

    def LED_off(self):
        self._entry_pin.value(0)


print("script is running")
lab_machine = Lab1_controller(DEFAULT_ADC_PIN, DEFAULT_ENTRY_PIN)
input("Press anything to launch\n")

file = open(FILE_PATH, "w")

# bc thats the range for duty value.
for i in range(0,1024):
    lab_machine.change_light(i)
    info = lab_machine.reciever()
    print("writing {info}")
    file.write(str(info) + "\n")
file.close()
# TODO :  proper logging of the results for long lab (separate class ig)
# TODO : improve main class