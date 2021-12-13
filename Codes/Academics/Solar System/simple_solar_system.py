from solar_system_3d import SolarSystem, SolarSystemBody, Sun, Planet
import itertools
import math
import matplotlib.pyplot as plt

solar_system = SolarSystem(600, projection_2d=True)
sun = Sun(solar_system, mass=10000)

planets = (
    Planet(solar_system, mass=25, position=(50, -50, 0), velocity=(10, 0, 5)),
    Planet(solar_system, mass=35, position=(-50, 50, 0), velocity=(5, 10, 0)),
    Planet(solar_system, mass=30, position=(-0, -50, 50), velocity=(-5, 0, 10)),
)

while True:
    solar_system.calculate_all_interaction()
    solar_system.update_all()
    solar_system.draw_all()
