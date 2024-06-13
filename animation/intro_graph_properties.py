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

        self.next_section("Create_Function")

        label_a = Tex("a", color=PURPLE)
        param_a = Variable(
            0,
            label_a,
            num_decimal_places=2
        )

        function_equation = MathTex(
            r"f_a(x) = x^4 - 0.4ax^2",
            substrings_to_isolate="a",
        )
        function_equation.set_color_by_tex("a", PURPLE)

        equations = VGroup(function_equation, param_a)
        equations.arrange(DOWN)
        equations.shift(RIGHT * 4)
        equations.shift(DOWN * 3)

        function = always_redraw(
            lambda: grid.plot(
                lambda x: x**4 - 0.4 * param_a.tracker.get_value() * x**2,
                color=YELLOW
            )
        )

        self.play(
            Write(equations),
        )
        self.play(
            Create(function),
        )
        self.wait()

        self.next_section("Test_animation")

        self.play(
            param_a.tracker.animate.set_value(-5),
            run_time=1,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.play(
            param_a.tracker.animate.set_value(5),
            run_time=5,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("Test_animation_2")

        self.play(
            param_a.tracker.animate.set_value(-1),
            run_time=10,
            rate_func=rate_functions.smooth
        )
        self.wait()

    def description(self):
        pass
