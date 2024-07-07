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

        self.add(
            grid,
            grid_labels,
        )
        self.wait()
