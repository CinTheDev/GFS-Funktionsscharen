#!/usr/bin/env python

from manim import *

class IntroGraph(Scene):
    def construct(self):
        self.parameter_showcase()
    
    def parameter_showcase(self):
        screen = FullScreenRectangle()

        # Draw coordinate system

        grid = Axes(
            x_range=(-5, 5, 1),
            y_range=(-1, 5, 1),
            x_length=screen.width,
            y_length=screen.height,
            axis_config={
                'include_numbers': True,
            }
        )

        self.play(
            Write(grid, run_time=3, lag_ratio=0.1),
        )

        # Draw axis labels and function

        label_a = Tex("a", color=PURPLE)
        param_a = Variable(
            1,
            label_a,
            num_decimal_places=2,
        )

        x_label = grid.get_x_axis_label("x")
        y_label = grid.get_y_axis_label("f(x)")
        grid_labels = VGroup(x_label, y_label)

        parabola = always_redraw(
            lambda: grid.plot(
                lambda x: param_a.tracker.get_value() * x*x,
                color=YELLOW,
            )
        )

        self.play(
            Write(grid_labels),
            Create(parabola),
        )

        # Draw function equation

        function_equation = MathTex(
            r"f_a(x) = ax^2",
            substrings_to_isolate="a",
        )
        function_equation.set_color_by_tex("a", PURPLE)

        equations = VGroup(function_equation, param_a)
        equations.arrange(DOWN)
        equations.shift(RIGHT * 4)
        equations.shift(DOWN * 1)

        self.play(
            FadeIn(equations)
        )
        self.wait()
        self.next_section("Parabola_Animation")

        # Animate parameter a

        self.play(
            param_a.tracker.animate.set_value(-0.5),
            run_time=3,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.play(
            param_a.tracker.animate.set_value(10.0),
            run_time=3,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.play(
            param_a.tracker.animate.set_value(1.0),
            run_time=1,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("Parabola_Animation_zero")

        self.play(
            param_a.tracker.animate.set_value(0),
            run_time=3,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("Parameter_Change")

        new_equation = MathTex(
            r"f_a(x) = x^2 + a",
            substrings_to_isolate="a",
        )
        new_equation.set_color_by_tex("a", PURPLE)
        new_equation.move_to(function_equation.get_center())

        parabola_offset_y = always_redraw(
            lambda: grid.plot(
                lambda x: x*x + param_a.tracker.get_value(),
                color=YELLOW,
            )
        )

        self.play(
            Transform(function_equation, new_equation, replace_mobject_with_target_in_scene=False),
            Transform(parabola, parabola_offset_y, replace_mobject_with_target_in_scene=True),
        )
        self.wait()

        self.next_section("Parabola_Offset")

        self.play(
            param_a.tracker.animate.set_value(1.5),
            rate=2,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.play(
            param_a.tracker.animate.set_value(-0.5),
            rate=2,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.play(
            param_a.tracker.animate.set_value(0.0),
            rate=2,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("Parabola_Parameter_Change")

        new_equation = MathTex(
            r"f_a(x) = (x - a)^2",
            substrings_to_isolate="a",
        )
        new_equation.set_color_by_tex("a", PURPLE)
        new_equation.move_to(function_equation.get_center())

        parabola_offset_x = always_redraw(
            lambda: grid.plot(
                lambda x: (x - param_a.tracker.get_value()) * (x - param_a.tracker.get_value()),
                color=YELLOW
            )
        )

        self.play(
            Transform(function_equation, new_equation, replace_mobject_with_target_in_scene=False),
            Transform(parabola_offset_y, parabola_offset_x, replace_mobject_with_target_in_scene=True),
        )
        self.wait()

        self.next_section("Parabola_Offset_x")

        self.play(
            param_a.tracker.animate.set_value(3.0),
            rate=2,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.play(
            param_a.tracker.animate.set_value(-1.23),
            rate=2,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("Parabola_exoticfunction")

        self.play(
            param_a.tracker.animate.set_value(0),
            rate=3,
            rate_func=rate_functions.smooth,
        )

        new_equation = MathTex(
            r"f_a(x) = 0.5a^2 \cdot (x + 0.1a^3)^2",
            substrings_to_isolate="a",
        )
        new_equation.set_color_by_tex("a", PURPLE)
        new_equation.move_to(function_equation.get_center())

        parabola_exotic = always_redraw(
            lambda: grid.plot(
                lambda x: 0.5 * param_a.tracker.get_value()**2 * (x + 0.1 * param_a.tracker.get_value()**3)**2,
                color=YELLOW
            )
        )

        self.play(
            Transform(function_equation, new_equation, replace_mobject_with_target_in_scene=False),
            Transform(parabola_offset_x, parabola_exotic, replace_mobject_with_target_in_scene=True),
        )
        self.wait()

        self.next_section("Parabola_exoticmovement")

        self.play(
            param_a.tracker.animate.set_value(-2),
            rate=1,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.play(
            param_a.tracker.animate.set_value(2),
            run_time=5,
            rate_func=rate_functions.ease_in_out_sine,
        )
