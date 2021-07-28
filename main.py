#!/bin/python3
import random

# Code your Robot class here:
class Robot:
  def __init__(self, a_name = "Rob",a_mass = 25,a_year="1985"):
    self.distance = 0
    self.name = a_name
    self.mass = a_mass
    self.year = a_year
    
  def move(self):
    steps = random.randint(1000,3000)
    self.distance += steps
    return steps
  
  def __str__(self):
    output = f"""
    Robot Information:
      Name: {self.name}
      Mass: {self.mass}
      Year Made: {self.year}
      Distance Traveled: {self.distance}
    """
    return output.strip()

# Code your oldest_robot function here:
# def oldest_robot(robot_list):
#   for 

#   oldest_year = 0
#   oldest_year == min(robot_list).year
#   return oldest_year
rob1 = Robot("R2D2", 40, 1977)
rob2= Robot("skynet", 30,1984)
rob3= Robot()
rob4= Robot("Pris", 35, 1982)
robots=[rob1,rob2,rob3,rob4]
# oldest_robot(robots)
  






# Code your robot_race function here:


def main():
  rob1 = Robot("R2D2", 40, 1977)
  rob2= Robot("skynet", 30,1984)
  rob3= Robot()
  rob4= Robot("Pris", 35, 1982)

  robots=[rob1,rob2,rob3,rob4]
  for robot in robots:
    robot
    robot.move()
    print(robot)
 


    
 

if __name__ == "__main__":
  main()