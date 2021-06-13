import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**kwargs):
    #contents contain k multiple times
    self.contents=[k for k,v in kwargs.items() for i in range(v)]


  def draw(self, ball):
    if (ball>len(self.contents)):
      drawOut=self.contents
      return drawOut
    balls_drawn = random.sample(self.contents, k=ball)

    for b in balls_drawn:
      self.contents.remove(b)

    return balls_drawn


def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
  expected_balls = [k for k, v in expected_balls.items() for i in range(v)]
  if (num_balls_drawn<len(expected_balls)):
    return 0
  suceed=0
  
  for i in range (num_experiments):
    hatcop=copy.deepcopy(hat)
    balls_drawn=hatcop.draw(num_balls_drawn)
    
    
    balls=[]
    
    for ball in expected_balls:
      if ball in balls_drawn:
        balls_drawn.remove(ball)
        balls.append(ball)
    
    if sorted(expected_balls) == sorted(balls):
      suceed+=1
      

    
  return float(suceed)/num_experiments
