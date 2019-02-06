from graphics import *


class Wheel():
    def __init__(self, center, wheel_radius, tire_radius):
        self.tire_circle = Circle(center, tire_radius)
        self.wheel_circle = Circle(center, wheel_radius)

    def draw(self, win):
        self.win = win
        self.tire_circle.draw(win)
        self.wheel_circle.draw(win)

    def undraw(self):
        self.tire_circle.undraw()
        self.wheel_circle.undraw()

    def set_color(self, wheel_color, tire_color='black'):
        self.tire_circle.setFill(tire_color)
        self.wheel_circle.setFill(wheel_color)

    def move(self, dx, dy):
        self.tire_circle.move(dx, dy)
        self.wheel_circle.move(dx, dy)

    def animate(self):
        self.win.after(250, self.animate)
        self.move(5,0)


def main():
    main_win = GraphWin('Wheel', 700, 500)

    wheel_center = Point(300,300)
    tire_radius = 100
    
    new_wheel = Wheel(wheel_center, 0.6*tire_radius, tire_radius)
    #tire_circle = Circle(wheel_center, tire_radius)
    #tire_circle.setFill('blue')
    #tire_circle.draw(main_win)

    new_wheel.set_color('grey')

    new_wheel.draw(main_win)
    new_wheel.animate()
    main_win.mainloop()



if __name__ == "__main__":
    main()