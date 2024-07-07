#!/usr/bin/env python

from manim import *

class CalculationTurningPointsVerification(Scene):
    def construct(self):
        self.next_section("Draw_coordinate_system")

        screen = FullScreenRectangle()

        grid = NumberPlane(
            x_range=(-5, 5, 1),
            y_range=(-2, 3, 1),
            x_length=screen.width,
            y_length=screen.height,
            background_line_style={
                "stroke_color": BLUE,
                "stroke_opacity": 0.6,
            },
            axis_config={
                'include_numbers': True,
                "include_tip": True,
            },
        )

        x_label = grid.get_x_axis_label("x")
        y_label = grid.get_y_axis_label("f(x)")

        label_a = Tex("a", color=PURPLE)
        param_a = Variable(
            -5,
            label_a,
            num_decimal_places=2,
        )

        function_equation = MathTex(
            r"f_a(x) = x^4 - 0.4ax^2",
            substrings_to_isolate="a"
        )
        function_equation.set_color_by_tex("a", color=PURPLE)

        equations = VGroup(function_equation, param_a)
        equations.arrange(DOWN)
        equations.move_to(RIGHT * 4 + DOWN * 3)

        function = always_redraw(
            lambda: grid.plot(
                lambda x: x**4 - 0.4 * param_a.tracker.get_value() * x**2,
                color=YELLOW
            )
        )

        self.add(
            grid,
            x_label,
            y_label,
            equations,
            function,
        )
        self.wait()

        self.next_section("a_5")

        self.play(
            param_a.tracker.animate.set_value(5),
            run_time=5,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("a_0")

        self.play(
            param_a.tracker.animate.set_value(0),
            run_time=3,
            rate_func=rate_functions.smooth,
        )
        self.wait()
