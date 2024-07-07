#!/usr/bin/env python

# Hüllkurven

from manim import *
import math

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

        self.graph = VGroup(grid, grid_labels)

        self.play(
            Create(self.graph),
            run_time=2,
        )

        self.param_theta = Variable(
            0,
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

        self.play(
            Write(self.param_theta),
            Write(function),
            run_time=3,
        )
        self.wait()

        self.next_section("Change_Angle")

        self.play(
            self.param_theta.tracker.animate.set_value(math.pi),
            run_time=5,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("Change_angle_efficient")

        self.play(
            self.param_theta.tracker.animate.set_value(45 * (math.pi / 180)),
            run_time=3,
            rate_func=rate_functions.smooth,
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
