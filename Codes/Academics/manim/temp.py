from manim import *


class FirstGIF(Scene):
    def construct(self):
        triangle = Triangle(color=RED, fill_opacity=0.5).scale(2)
        sq = Square(side_length=3, fill_color=GREEN, fill_opacity=0.5)
        text = Tex("Hello World!").scale(2)

        self.play(Create(triangle), run_time=2)
        self.play(Create(sq), run_time=2)
        self.play(Create(text), run_time=2)
        self.wait()
