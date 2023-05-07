import time

import ssd1306
from machine import I2C,Pin
import menu
import machine
i2c = I2C(0, scl=Pin(14), sda=Pin(12))  # 硬件I2C
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
oled.fill(0xff)
text=[['music','print("perform a music")'],['photo','m.initText(subtext)','print("Special click detacted")'],['game','a']]
subtext=[['back','m.initText(text)'],['see photo a','a']]
m=menu.menu(oled,0,0,128,64)
m.initText(text) # main menu
oled.show()

def myupfun(myp):
    pass
    global m
    print("myup,",myp)
    m.moveUp()
    oled.show()
def mydownfun(myp):
    pass
    global m
    print("mydown,", myp)
    m.moveDown()
    oled.show()

def myclickfun(myp):
    pass
    global m
    print("myclick,", myp)
    m.click()
    oled.show()



myled=Pin(22,Pin.OUT)

myup = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP)  # 引脚编号、引脚模式下降沿以及是否存在相关拉电阻
mydown = machine.Pin(25, machine.Pin.IN, machine.Pin.PULL_UP)
myclick = machine.Pin(33, machine.Pin.IN, machine.Pin.PULL_UP)

myup.irq(trigger=machine.Pin.IRQ_FALLING, handler=myupfun)  # 触发中断，回调模式
mydown.irq(trigger=machine.Pin.IRQ_FALLING, handler=mydownfun)
myclick.irq(trigger=machine.Pin.IRQ_FALLING, handler=myclickfun)

while True:

    myled.value(1-myled.value())
    time.sleep(1)