from machine import ADC, Pin
import time

#just configuring and choosing pins
led = machine.Pin(32, machine.Pin.OUT)
resistor = machine.Pin(13, machine.Pin.OUT)
resistor.value(1)
led.value(1)

class Lab1_machine:

    _info_pin = None
    _entry_pin = None

    def __init__(adc: int, entry : int): #
        _info_pin = ADC(Pin(adc))
        _entry_pin = Pin(adc, Pin.OUT)

    def reciever():
        pass

    def something():
        pass



# while True:
#      led.value(1)
#      time.sleep(1)
#      led.value(0)
#      time.sleep(1)
#      pass

if __name__ == "__main__":
    lab_machine = Lab1_machine(adc=12, entry=13)
