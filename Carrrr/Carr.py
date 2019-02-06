from graphics import *

from Carrrr.wheel import Wheel

class Car():
    def __init__(self, position, width, height):
        point = Point(position.x + width, position.y + height)
        self.body = Rectangle(position, point)
        self.wheel1 = Wheel(point, 0.6*radius, radius)
        point = Point(position.x,position.y+height)
        self.wheel2 = Wheel(point, 0.6*radius, radius)
    def draw(self, win):
        self.win = win
    def move(self, dx, dy):
        self.wheel2.move(dx, dy)
        self.wheel1.move(dx, dy)
        self.body.move(dx, dy)

    def animate(self):
        self.win.after(250, self.animate)
        self.move(5, 0)

def main():
    main_win = GraphWin("A Car", 500, 300)

    body = Rectangle( Point(10,10), Point(200,100))
    body.setFill('blue')
    body.draw(main_win)

    wheel1 = Wheel(Point(10, 100), 30, 50)
    wheel2 = Wheel(Point(200, 100), 30, 50)
    wheel1.set_color('red')
    wheel2.set_color('red')
    wheel1.draw(main_win)
    wheel2.draw(main_win)

    Car.animate()
    main_win.mainloop()
if __name__ == "__main__":
    main()