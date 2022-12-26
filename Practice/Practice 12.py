class Television:
    def __init__(self, os, color, display):
        self.os = os
        self.color = color
        self.display = display

    def specs(self):
        print("Specification of this tv :", "OS:", self.os, "Color:", self.color, "Display:", self.display)


Sony = Television("Android", "Black", "Oled")
Samsung = Television("Tizen", "Black", "Dled")
LG = Television("Webos", "Grey", "Oled")

Sony.specs()
Samsung.specs()
LG.specs()

