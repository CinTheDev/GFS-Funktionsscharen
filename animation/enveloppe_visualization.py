#!/usr/bin/env python

from manim import *
import math

class EnveloppeVisualization(Scene):
    def construct(self):
        screen = FullScreenRectangle()

        grid = NumberPlane(
            x_range=(-10, 10, 2),
            y_range=(-1, 4.5, 1),
            x_length=screen.width,
            y_length=screen.height,
            background_line_style={
                "stroke_color": PINK,
                "stroke_opacity": 0.6,
            },
            axis_config={
                "include_numbers": True,
            },
        )

        x_label = grid.get_x_axis_label("x")
        y_label = grid.get_y_axis_label("f(x)")
        grid_labels = VGroup(x_label, y_label)

        self.param_theta = Variable(
            45 * (math.pi / 180),
            MathTex(r"\theta", color=BLUE),
            num_decimal_places=2,
        )
        self.param_theta.move_to(RIGHT * 4 + UP * 3)

        function = always_redraw(
            lambda: grid.plot_parametric_curve(
                lambda t: self.graph_function(t),
                t_range=[-10, 10, 0.1],
                color=BLUE,
            )
        )

        self.add(
            grid,
            grid_labels,
            self.param_theta,
            function,
        )
        self.wait()
    
    def graph_function(self, t):
        theta = self.param_theta.tracker.get_value()
        speed = 8
        gravity = 9.81

        return [
            speed * math.cos(theta) * t,
            -0.5 * gravity * t**2 + speed * math.sin(theta) * t,
            0,
        ]
