#!/usr/bin/env python

# Hüllkurven

from manim import *

class Envelope(Scene):
    def construct(self):
        self.transition()
        self.graph()
    
    def transition(self):
        self.next_section("Transition")
        title = Tex("4: Hüllkurven", color=PINK)

        self.add(title)
        self.wait()

        self.next_section("Graph")

        self.play(
            FadeOut(title)
        )
    
    def graph(self):
        screen = FullScreenRectangle()

        x_range=(-10, 10, 2)
        dx = x_range[1] - x_range[0]
        dy = dx * (screen.height / screen.width)
        y_range=(-1, -1 + dy, 2)

        grid = NumberPlane(
            x_range=x_range,
            y_range=y_range,
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

        self.graph = VGroup(grid, grid_labels)

        self.play(
            Create(self.graph),
            run_time=2,
        )
        self.wait()
