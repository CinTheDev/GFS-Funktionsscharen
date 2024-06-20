#!/usr/bin/env python

from manim import *
import math

class VisualizeAnalysisExponentialAdvanced(Scene):
    def construct(self):
        self.next_section("Construct_Scene")
        screen = FullScreenRectangle()

        self.grid = Axes(
            x_range=(-5, 5, 1),
            y_range=(-2, 3, 1),
            x_length=screen.width,
            y_length=screen.height,
            axis_config={
                "include_numbers": True,
            },
        )

        x_label = self.grid.get_x_axis_label("x")
        y_label = self.grid.get_y_axis_label("f(x)")
        grid_labels = VGroup(x_label, y_label)

        self.add(self.grid, grid_labels)

        self.param_a = Variable(
            0,
            Tex("h"),
            num_decimal_places=2,
        )

        function_equation = MathTex(r"f_h(x) = x \cdot e^{h x}")

        equations = VGroup(function_equation, self.param_a)
        equations.arrange(DOWN)
        equations.move_to(RIGHT * 4 + DOWN * 3)

        self.function = always_redraw(
            lambda: self.grid.plot(
                lambda x: self.graph_function(x),
                color=YELLOW,
            )
        )

        self.play(
            Write(equations),
            Create(self.function),
        )
        self.wait()

    def graph_function(self, x):
        a = self.param_a.tracker.get_value()
        return x * math.exp(a * x)
