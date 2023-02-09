from machine import Pin, PWM

PWM_FREQ = 1000         # PWM Output Frequency
PWM_PIN = 3             # PWM Output Pin
SUB_DIV = 12            # Number of buttons/subdivisions
PULL_UP_BUTTONS = True  # Set to True if not using external pull up resistor


"""
Helper function to save on typing because my fingers were cold
n:  GPIO Pin No
io: 0 - Input (Button), 1 - Output (PWM, Enable Pin)

Yes, I know 0 and 1 are backwards but I was running on red bull fumes
"""
def make_pin(n, io):
    if io == 0:
        pup = Pin.PULL_UP if PULL_UP_BUTTONS else Pin.PULL_DOWN
        return Pin(n, Pin.IN, pup)
    if io == 1:
        return Pin(n, Pin.OUT, Pin.PULL_DOWN)

# Do this for each button/subdivision
a = make_pin(0, 0)
b = make_pin(1, 0)
c = make_pin(2, 0)
d = make_pin(4, 0)
e = make_pin(5, 0)
f = make_pin(6, 0)
g = make_pin(7, 0)
h = make_pin(8, 0)
i = make_pin(9, 0)
j = make_pin(10, 0)
k = make_pin(11, 0)
l = make_pin(12, 0)

pw_pin = make_pin(PWM_PIN, 1)
pwm = PWM(pw_pin)
pwm.freq(PWM_FREQ)

pwm.duty_u16(0) # Don't output PWM unless we want it to

en_pin = make_pin(16, 1) # This connects to 1,2EN on L293, set HIGH when outputting PWM.

def map_duty(n): return (65535//SUB_DIV) * n # Basically the Arduino Map function

while True:
    if not a.value():
        while not a.value():            # Keep running while pressed
            en_pin.on()                 # Enable pin on L293
            pwm.duty_u16(map_duty(1))   # Set PWM Output
    if not b.value():
        while not b.value():
            en_pin.on()
            pwm.duty_u16(map_duty(2))
    if not c.value():
        while not c.value():
            en_pin.on()
            pwm.duty_u16(map_duty(3))
    if not d.value():
        while not d.value():
            en_pin.on()
            pwm.duty_u16(map_duty(4))
    if not e.value():
        while not e.value():
            en_pin.on()
            pwm.duty_u16(map_duty(5))
    if not f.value():
        while not f.value():
            en_pin.on()
            pwm.duty_u16(map_duty(6))
    if not g.value():
        while not g.value():
            en_pin.on()
            pwm.duty_u16(map_duty(7))
    if not h.value():
        while not h.value():
            en_pin.on()
            pwm.duty_u16(map_duty(8))
    if not i.value():
        while not i.value():
            en_pin.on()
            pwm.duty_u16(map_duty(9))
    if not j.value():
        while not j.value():
            en_pin.on()
            pwm.duty_u16(map_duty(10))
    if not k.value():
        while not k.value():
            en_pin.on()
            pwm.duty_u16(map_duty(11))
    if not l.value():
        while not l.value():
            en_pin.on()
            pwm.duty_u16(map_duty(12))
    en_pin.off()        # Disable L293 when button let go
    pwm.duty_u16(0)     # Turn off PWM output when button let go

    
