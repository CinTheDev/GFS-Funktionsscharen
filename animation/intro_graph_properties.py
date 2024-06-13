#!/usr/bin/env python

from manim import *

class IntroGraphProperties(Scene):
    def construct(self):
        self.graph()
        self.description()
    
    def graph(self):
        self.next_section("Empty_Graph")
        screen = FullScreenRectangle()

        # Draw coordinate system

        grid = Axes(
            x_range=(-5, 5, 1),
            y_range=(-2, 3, 1),
            x_length=screen.width,
            y_length=screen.height,
            axis_config={
                'include_numbers': True,
            },
        )

        x_label = grid.get_x_axis_label("x")
        y_label = grid.get_y_axis_label("f(x)")
        grid_labels = VGroup(x_label, y_label)

        self.add(grid, grid_labels)
        self.wait()

    def description(self):
        pass
