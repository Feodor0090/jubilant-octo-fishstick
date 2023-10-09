import random

import unit

if __name__ == '__main__':
    u1 = unit.Unit(100, 20)
    u2 = unit.Unit(100, 20)
    while True:
        if random.random() >= 0.5:
            u1.attack(u2)
            print(f"Unit 1 attacked unit 2 ({u2.health()} left)")
        else:
            u2.attack(u1)
            print(f"Unit 2 attacked unit 1 ({u1.health()} left)")
        if u1.is_dead():
            print("Unit 1 dead")
            break
        if u2.is_dead():
            print("Unit 2 dead")
            break
