from manim import *
from manim.opengl import *
from scipy import special
import numpy as np

# TWO_SIDED_VIRIDIS = [
#     "#bddf26",
#     "#29af7f",
#     "#2e6f8e",
#     "#482173",
#     "#2e6f8e",
#     "#29af7f",
#     "#bddf26",
# ]
TWO_SIDED_VIRIDIS = "#bddf26"


class Membrane(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES)

        def u_mn(r, theta, t=0, m=2, n=3):
            a = 11.6198
            A = B = C = D = 1
            return (
                0.4
                * (A * np.cos(a * t) + B * np.sin(a * t))
                * special.jv(m, a * r)
                * (C * np.cos(m * theta) + D * np.sin(m * theta))
            )

        axes = ThreeDAxes(x_range=(-1, 1), y_range=(-1, 1), z_range=(-0.40, 0.40))

        def f(dt=0):
            axes.rotate(angle=dt / 50 * PI / 2, axis=OUT)
            obj = OpenGLSurface(
                uv_func=lambda r, theta: axes.c2p(
                    r * np.cos(theta), r * np.sin(theta), u_mn(r, theta, dt)
                ),
                u_range=(-1e-5, 1),
                v_range=(0, TAU),
                axes=axes,
                color=TWO_SIDED_VIRIDIS,
            )
            return obj

        current = f()

        def update_membrane(current, alpha):
            dt = interpolate(0, 1, alpha)
            new = f(dt)
            current.become(new)

        self.add(current)
        self.play(
            UpdateFromAlphaFunc(current, update_membrane), rate_func=linear, run_time=10
        )
