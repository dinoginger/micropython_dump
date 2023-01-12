from machine import ADC, Pin, PWM
import machine
import time

# This is constants.
DEFAULT_ENTRY_PIN = 32
DEFAULT_ADC_PIN = 12
FILE_PATH = "data.txt"
MEASURING_PERIOD  = 60 # seconds
NUM_OF_HALF_MEASUREMENTS = 12 # insert explanation
DUTY_VALUE = 300

class Lab1_controller:

    """
    The main class for our machine.

    Will include the main controller functions.    
    """

    _info_pin = None  # ADC pin (photosensor)
    _entry_pin = None # LED pin
    _pwm = None

    def __init__(self, adc, entr):  # constructor

        
        self._entry_pin = Pin(entr)

        self._info_pin = ADC(Pin(adc))
        self._info_pin.atten(self._info_pin.ATTN_11DB) # volt [0.0 - 3.6v]

        
        self._pwm = PWM(Pin(DEFAULT_ENTRY_PIN), 148000)

        self._entry_pin.value(1)  # Activating pins
 
        
        
    def reciever(self):
        info = self._info_pin.read()
        print(info) # values are from 0 to 4095 so we get percentages
        time.sleep(MEASURING_PERIOD)
        return info
        # TODO: finish it 

    def average_reciever(self):
        
        info_container = []
        new_period = MEASURING_PERIOD/NUM_OF_HALF_MEASUREMENTS
        for i in range(NUM_OF_HALF_MEASUREMENTS):
            info_container.append(self._info_pin.read())
            time.sleep(new_period)
        info = round(sum(info_container)/len(info_container))
        print(info)
        return info
        
            



    def change_light(self, value):
        self._pwm.duty(value)


    def LED_on(self):
        self._entry_pin.value(1)

    def LED_off(self):
        self._entry_pin.value(0)

for i in range(3):
    machine.Pin(13, machine.Pin.OUT).value(1)
    time.sleep(0.2)
    machine.Pin(13, machine.Pin.OUT).value(0)
    time.sleep(0.2)


button = machine.Pin(33,machine.Pin.IN,machine.Pin.PULL_UP)
lab_machine = Lab1_controller(DEFAULT_ADC_PIN, DEFAULT_ENTRY_PIN)
lab_machine.change_light(DUTY_VALUE)
file = open(FILE_PATH, "a")
lll = []
print("entered main file")
#well have to calibrate brightness *(duty value)
# bc thats the range for duty value.
#for i in range(0,1024):
#print("await for the button")
while True:
    if button.value() == 1: 
        continue
    elif button.value() == 0:
        print("button pressed")
        for i in range(5):
            machine.Pin(13, machine.Pin.OUT).value(1)
            time.sleep(0.5)
            machine.Pin(13, machine.Pin.OUT).value(0)
            time.sleep(0.5)

        while True:

            #print(i)
            #lab_machine.change_light(i)
            machine.Pin(13, machine.Pin.OUT).value(1)
            time.sleep(0.1)
            machine.Pin(13, machine.Pin.OUT).value(0)



            info = lab_machine.average_reciever()
            #lll.append(info)

            print("writing {info}")
            file.write(str(info) + "\n")

            if button.value() == 0:
                for i in range(10):
                    machine.Pin(13, machine.Pin.OUT).value(1)
                    time.sleep(0.2)
                    machine.Pin(13, machine.Pin.OUT).value(0)
                    time.sleep(0.2)
                break        
    break
file.close()
# TODO :  proper logging of the results for long lab (separate class ig)
# TODO : improve main class
