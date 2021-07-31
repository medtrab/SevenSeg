from machine import Pin
# this class is for single 7 segment display
class Seg(machine):
    def __init__(self, common, a, b, c, d, e, f, g, dp):
        self.common = common
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.dp = dp

    def init(self):
        if common.lower() == "k":
            a=Pin(a, Pin.OUT)
            b=Pin(b, Pin.OUT)
            c=Pin(c, Pin.OUT)
            d=Pin(d, Pin.OUT)
            e=Pin(e, Pin.OUT)
            f=Pin(f, Pin.OUT)
            g=Pin(g, Pin.OUT)
            dp=Pin(dp, Pin.OUT)
            action = 1
        elif common.lower() == "a":
            a=Pin(a, Pin.OUT)
            b=Pin(b, Pin.OUT)
            c=Pin(c, Pin.OUT)
            d=Pin(d, Pin.OUT)
            e=Pin(e, Pin.OUT)
            f=Pin(f, Pin.OUT)
            g=Pin(g, Pin.OUT)
            dp=Pin(dp, Pin.OUT)
            action = 0

    def count(self,x):
        if x==0:
            zero = {a.value(action),b.value(action),c.value(action),d.value(action),e.value(action),f.value(action),g.value(0),dp.value(0)}
        elif x==action:
            one = {a.value(0),b.value(action),c.value(action),d.value(0),e.value(0),f.value(0),g.value(0),dp.value(0)}
        elif x==2:
            two = {a.value(action),b.value(action),c.value(0),d.value(action),e.value(action),f.value(0),g.value(action),dp.value(0)}
        elif x==3:
            three = {a.value(action),b.value(action),c.value(action),d.value(action),e.value(0),f.value(0),g.value(action),dp.value(0)}
        elif x==4:
            four = {a.value(0),b.value(action),c.value(action),d.value(0),e.value(0),f.value(action),g.value(action),dp.value(0)}
        elif x==5:
            five = {a.value(action),b.value(0),c.value(action),d.value(action),e.value(0),f.value(action),g.value(action),dp.value(0)}
        elif x==6:
            six = {a.value(action),b.value(0),c.value(action),d.value(action),e.value(action),f.value(action),g.value(action),dp.value(0)}
        elif x==7:
            seven = {a.value(action),b.value(action),c.value(action),d.value(0),e.value(0),f.value(0),g.value(0),dp.value(0)}
        elif x==8:
            eight = {a.value(action),b.value(action),c.value(action),d.value(action),e.value(action),f.value(action),g.value(action),dp.value(0)}
        elif x==9:
            nine = {a.value(action),b.value(action),c.value(action),d.value(action),e.value(0),f.value(action),g.value(action),dp.value(0)}
