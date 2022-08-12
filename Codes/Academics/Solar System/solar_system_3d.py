import matplotlib.pyplot as plt
from vectors import Vector
import math
import itertools


class SolarSystem:
    def __init__(self, size, projection_2d=False) -> None:
        self.size = size
        self.projection_2d = projection_2d
        self.bodies = []

        self.fig, self.ax = plt.subplots(
            1,
            1,
            figsize=(self.size / 50, self.size / 50),
            subplot_kw={"projection": "3d"},
        )
        self.fig.tight_layout()
        # self.ax.view_init(elev=0, azim=0)
        if self.projection_2d:
            self.ax.view_init(elev=10, azim=0)
        else:
            self.ax.view_init(elev=0, azim=0)

    def add_body(self, body):
        self.bodies.append(body)

    def update_all(self):
        self.bodies.sort(key=lambda item: item.position[0])
        for body in self.bodies:
            body.move()
            body.draw()

    def draw_all(self):
        self.ax.set_xlim((-self.size, self.size))
        self.ax.set_ylim((-self.size, self.size))
        self.ax.set_zlim((-self.size, self.size))

        if self.projection_2d:
            self.ax.xaxis.set_ticklabels([])
            self.ax.yaxis.set_ticklabels([])
            self.ax.zaxis.set_ticklabels([])
        else:
            self.ax.axis(False)

        plt.pause(0.001)
        self.ax.clear()

    def calculate_all_interaction(self):
        bodies_copy = self.bodies.copy()
        for idx, first in enumerate(bodies_copy):
            for second in bodies_copy[idx + 1 :]:
                first.accelerate_gravity(second)


class SolarSystemBody:
    MIN_DISPLAY_SIZE = 10
    DISPLAY_LOG_BASE = 1.3

    def __init__(self, solar_system, mass, position=(0, 0, 0), velocity=(0, 0, 0)):
        self.solar_system = solar_system
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.display_size = max(
            math.log(self.mass, self.DISPLAY_LOG_BASE),
            self.MIN_DISPLAY_SIZE,
        )
        self.color = "black"
        self.solar_system.add_body(self)

    def move(self, time=1):
        self.position = (
            self.position[0] + self.velocity[0] * time,
            self.position[1] + self.velocity[1] * time,
            self.position[2] + self.velocity[2] * time,
        )

    def draw(self):
        self.solar_system.ax.plot(
            *self.position,
            marker="o",
            markersize=self.display_size + self.position[0] / 30,
            color=self.color,
        )
        if self.solar_system.projection_2d:
            self.solar_system.ax.plot(
                self.position[0],
                self.position[1],
                self.solar_system.size / 2,
                marker="o",
                markersize=self.display_size / 2,
                color=(0.5, 0.5, 0.5),
            )

    def accelerate_gravity(self, other):
        distance = Vector(*self.position) - Vector(*other.position)
        distance_magnitude = distance.get_magnitude()
        force_mag = self.mass * other.mass / (distance_magnitude ** 2)
        force = distance.normalize() * force_mag
        reverse = 1
        for body in [self, other]:
            acceleration = force / body.mass
            velocity = Vector(*body.velocity)
            velocity += acceleration * reverse
            reverse = -1


class Sun(SolarSystemBody):
    def __init__(
        self, solar_system, mass=10000, position=(0, 0, 0), velocity=(0, 0, 0)
    ):
        super().__init__(solar_system, mass, position=position, velocity=velocity)
        self.color = "yellow"


class Planet(SolarSystemBody):
    colors = itertools.cycle([(1, 0, 0), (0, 1, 0), (0, 0, 1)])

    def __init__(self, solar_system, mass=10, position=(0, 0, 0), velocity=(0, 0, 0)):
        super().__init__(solar_system, mass, position=position, velocity=velocity)
        self.color = next(Planet.colors)
