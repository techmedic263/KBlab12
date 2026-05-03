import math


class U:
    G = 6.674e-11


class Planet:
    def __init__(self, name, mass, size, x_vel, x_pos, y_pos, color):
        self.name = name
        self.mass = mass
        self.size = size
        self.x_vel = x_vel
        self.y_vel = 0
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color

    def move_to(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos

    def set_x_vel(self, v):
        self.x_vel = v

    def set_y_vel(self, v):
        self.y_vel = v

    def get_x_vel(self):
        return self.x_vel

    def get_y_vel(self):
        return self.y_vel


class Sun:
    def __init__(self, name, mass, x_pos, y_pos):
        self.name = name
        self.mass = mass
        self.x_pos = 0.0
        self.y_pos = 0.0

    def get_mass(self):
        return self.mass

    def get_x_pos(self):
        return self.x_pos

    def get_y_pos(self):
        return self.y_pos


class SolarSystem:
    def __init__(self):
        self.planets = []
        self.the_sun = None

    def add_sun(self, sun):
        self.the_sun = sun

    def add_planet(self, planet):
        self.planets.append(planet)

    def move_planets(self):
        dt = 0.001

        for planet in self.planets:

            planet.move_to(
                planet.get_x_pos() + dt * planet.get_x_vel(),
                planet.get_y_pos() + dt * planet.get_y_vel()
            )


            dist_x = self.the_sun.get_x_pos() - planet.get_x_pos()
            dist_y = self.the_sun.get_y_pos() - planet.get_y_pos()
            distance = math.sqrt(dist_x**2 + dist_y**2)


            acc_x = U.G * self.the_sun.get_mass() * dist_x / distance**3
            acc_y = U.G * self.the_sun.get_mass() * dist_y / distance**3


            planet.set_x_vel(planet.get_x_vel() + dt * acc_x)
            planet.set_y_vel(planet.get_y_vel() + dt * acc_y)

    def show_planets(self):
        for p in self.planets:
            print(f"{p.name}: ({p.x_pos:.2f}, {p.y_pos:.2f})")


class Simulation:
    def __init__(self, solar_system, width, height, steps):
        self.solar_system = solar_system
        self.width = width
        self.height = height
        self.steps = steps

    def run(self):
        for _ in range(self.steps):
            self.solar_system.move_planets()
            self.solar_system.show_planets()

# main program

if __name__ == '__main__':
    solar_system = SolarSystem()

    the_sun = Sun("SOL", 5000, 0.0, 0.0)
    solar_system.add_sun(the_sun)

    earth = Planet("EARTH", 47.5, 1, 25, 5.0, 200.0, "green")
    solar_system.add_planet(earth)

    mars = Planet("MARS", 40.5, 0.1, 62, 10.0, 125.0, "red")
    solar_system.add_planet(mars)

    simulation = Simulation(solar_system, 500, 500, 10)
    simulation.run()