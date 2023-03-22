class coche:
    puertas = 0
    
    def incr_doors(self):
        self.puertas += 1

auto = coche()

auto.incr_doors()

print(auto.puertas)