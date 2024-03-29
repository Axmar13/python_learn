import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs) -> None:
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
        print(self.contents)
    
    def draw(self, balls):
        removed_balls = []
        if balls >= len(self.contents):
            removed_balls = self.contents
            self.contents.clear()
            return removed_balls
        else:
            for i in range(balls):
                removed_ball = self.contents.pop(int(random.choice(range(len(self.contents)))))
                removed_balls.append(removed_ball)
            return removed_balls
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        colors_gotten = hat_copy.draw(num_balls_drawn)

        for color in colors_gotten:
            if(color in expected_copy):
                expected_copy[color] -= 1
            
        if(all(x <= 0 for x in expected_copy.values())):
            count += 1

    return count / num_experiments


hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

print(hat1.draw(3))