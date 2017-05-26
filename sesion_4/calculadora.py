class Calculadora:
    def __init__(self):
        self.ans = 0
        self.screen = "0"

    def btn_1(self):
        if self.screen == "0":
            self.screen = ""
        self.screen += "1"
        self.show()
    
    def btn_2(self):
        if self.screen == "0":
            self.screen = ""
        self.screen += "2"
        self.show()
    
    def btn_3(self):
        if self.screen == "0":
            self.screen = ""
        self.screen += "3"
        self.show()

    def btn_sum(self):
        self.ans += int(self.screen)
        self.screen = "0"
        self.show()

    def show(self):
        print "[%10s] (%d)" % (self.screen, self.ans)

c = Calculadora()

c.show()
c.btn_1()
c.btn_3()
c.btn_sum()
c.btn_2()
c.btn_1()
c.btn_sum()