from robot import Robot

def start():
    robot = Robot()
    robot.greeting()
    robot.recommend_restaurant()
    robot.which_restaurant()
    robot.last_bow()
    robot.save()
    start()

start()