import random

import unit

if __name__ == '__main__':
    u1 = unit.Unit(100, 20)
    u2 = unit.Unit(100, 20)
    while True:
        if random.random() >= 0.5:
            u1.attack(u2)
            print("Unit 1 attacked unit 2")
        else:
            u2.attack(u1)
            print("Unit 2 attacked unit 1")
        if u1.is_dead():
            print("Unit 1 dead")
            break
        if u2.is_dead():
            print("Unit 2 dead")
            break
