import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = [color for color, amount in kwargs.items() for _ in range(amount)]

    def draw(self, num_balls_drawn):
        drawn_balls = []
        if num_balls_drawn >= len(self.contents): 
            drawn_balls = self.contents[:]
            self.contents.clear()
        else: 
            drawn_balls = random.sample(self.contents, num_balls_drawn)
            for ball in drawn_balls:
                self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    favorable_experiments = 0
    for _ in range(num_experiments): 
        experiment_hat = copy.deepcopy(hat)
        drawn_balls = experiment_hat.draw(num_balls_drawn)
        if all(drawn_balls.count(ball) >= amount for ball, amount in expected_balls.items()): 
            favorable_experiments += 1
    return favorable_experiments/num_experiments


hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)