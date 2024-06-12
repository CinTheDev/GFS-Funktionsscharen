#!/usr/bin/env python

from manim import *

class Intro(Scene):
    def construct(self):
        self.title()
        self.intro()
        self.play_graph()

    def title(self):
        self.next_section("Title")
        title = Tex(r"GFS Funktionsscharen")
        formula = Tex(r"Mit \LaTeX \:yeah whats going on")

        VGroup(title, formula).arrange(DOWN)

        self.play(
            Write(title)
        )
        self.wait()

        self.next_section("Example")

        self.play(
            Write(formula)
        )
        self.wait()

        self.next_section("Transition")

        self.play(
            FadeOut(title),
            FadeOut(formula),
        )
    
    def intro(self):
        base_function = MathTex(r"f_a(x)")
        function_linear1 = MathTex(r"f_a(x) = ax")
        function_linear2 = MathTex(r"f_a(x) = x + a")

        function = base_function.copy()

        # Linear function examples

        self.play(
            Write(function)
        )
        self.wait()
        self.next_section("Linear1")

        self.play(
            Transform(function, function_linear1)
        )
        self.wait()
        self.next_section("Linear2")

        self.play(
            Transform(function, function_linear2)
        )
        self.wait()
        self.next_section("Names")

        # Different names for "Funktionsscharen"

        names = [
            Tex("- Funktionsschar", color=YELLOW),
            Tex("- Funktionenschar", color=YELLOW),
            Tex("- Kurvenschar", color=YELLOW),
            Tex("- Parameterfunktion", color=YELLOW),
        ]

        names_list = VGroup()
        names_animations = []

        function.generate_target()
        names_list.add(function.target)

        for name in names:
            names_list.add(name)
            names_animations.append(Write(name))

        names_list.arrange(DOWN, aligned_edge=LEFT)
        function.target.set_x(0) # Align function in center

        self.play(
            MoveToTarget(function)
        )
        self.play(
            LaggedStart(
                *names_animations,
                lag_ratio=0.25,
                run_time=2,
            )
        )
        self.wait()

        self.next_section("Transition")

        self.play(
            FadeOut(function),
            FadeOut(names_list),
        )
    
    def play_graph(self):
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
                color=YELLOW
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
            r"f_a(x) = x + a",
            substrings_to_isolate="a",
        )
        new_equation.set_color_by_tex("a", PURPLE)
        new_equation.move_to(function_equation.get_center())

        new_parabola = always_redraw(
            lambda: grid.plot(
                lambda x: x*x + param_a.tracker.get_value(),
                color=YELLOW
            )
        )

        self.play(
            Transform(function_equation, new_equation, replace_mobject_with_target_in_scene=True),
            Transform(parabola, new_parabola, replace_mobject_with_target_in_scene=True),
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
