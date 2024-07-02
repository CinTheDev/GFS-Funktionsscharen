#!/usr/bin/env python

from manim import *

class ExkursParametricFunction(Scene):
    def construct(self):
        self.transition()
        self.linear_function()
        self.quadratic_function()
    
    def transition(self):
        self.next_section("Transition")

        title_intro = Tex("Kurzer Exkurs:", color=RED)
        title_text = Tex("Parameterisierte Funktionen", color=RED)
        title = VGroup(title_intro, title_text)
        title.arrange(DOWN)

        self.play(
            SpinInFromNothing(title_intro),
            run_time=1,
        )
        self.play(
            FadeIn(title_text, shift=UP),
            run_time=1,
        )
        self.wait()

        self.next_section("Transition_to_graph")

        screen = FullScreenRectangle()

        self.grid = NumberPlane(
            x_range=(-5, 5, 1),
            y_range=(-3, 3, 1),
            x_length=screen.width,
            y_length=screen.height,
            tips=True,
            background_line_style={
                "stroke_color": RED,
                "stroke_opacity": 0.6,
            },
            axis_config={
                "include_numbers": True,
                "tip_shape": StealthTip,
            },
        )

        x_label = self.grid.get_x_axis_label("x")
        y_label = self.grid.get_y_axis_label("y")

        graph_screen = VGroup(self.grid, x_label, y_label)

        # Remember position before moving away
        graph_screen.generate_target()

        graph_screen.next_to(screen, DOWN)

        self.add(graph_screen)

        title.generate_target()
        title.target.shift(UP * 6)

        self.play(
            MoveToTarget(graph_screen),
            MoveToTarget(title),
            run_time=2,
        )
        #self.wait()
    
    def linear_function(self):
        x_equation = MathTex(r"x(a) = a")
        y_equation = MathTex(r"y(a) = a")

        self.param_a = Variable(
            0,
            Tex("a", color=PURPLE),
            num_decimal_places=2,
        )

        self.equations = VGroup(x_equation, y_equation, self.param_a)
        self.equations.arrange(DOWN)
        self.equations.move_to(LEFT * 4 + UP * 2.5)
        self.equations.add_background_rectangle(opacity=1, stroke_width=1, stroke_opacity=1, stroke_color=RED, buff=0.4)

        function_partial = always_redraw(
            lambda: self.grid.plot_parametric_curve(
                lambda a: [
                    a,
                    a,
                    0,
                ],
                t_range=[-3, self.param_a.tracker.get_value()],
                color=BLUE,
            )
        )

        function_point = always_redraw(
            lambda: Dot(
                point=self.grid.input_to_graph_point(self.param_a.tracker.get_value(), function_partial),
                color=ORANGE,
            )
        )

        self.play(
            FadeIn(self.equations),
            Create(function_point),
            Flash(function_point),
            run_time=1,
        )
        self.wait()

        self.next_section("a_5")

        self.play(
            self.param_a.tracker.animate.set_value(2.5),
            run_time=2,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("a_n5")

        self.play(
            self.param_a.tracker.animate.set_value(-2.5),
            run_time=2,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("Draw_function")

        self.play(
            self.param_a.tracker.animate.set_value(-3),
            run_time=1,
            rate_func=rate_functions.smooth,
        )
        self.add(function_partial)

        self.play(
            self.param_a.tracker.animate.set_value(3),
            run_time=3,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("Different_slope")

        new_x_equation = x_equation.copy()
        new_y_equation = MathTex(r"y(a) = 0.5a")

        self.equations.remove(self.param_a)

        new_equations = VGroup(new_x_equation, new_y_equation)
        new_equations.arrange(DOWN)
        new_equations.move_to(self.equations)
        new_equations.add_background_rectangle(opacity=1, stroke_width=1, stroke_opacity=1, stroke_color=RED, buff=0.1)

        self.function = self.grid.plot_parametric_curve(
            lambda a: [
                a,
                0.5*a,
                0,
            ],
            t_range=[-10, 10],
            color=BLUE,
        )

        self.play(
            Transform(self.equations, new_equations),
            Transform(function_partial, self.function, replace_mobject_with_target_in_scene=True),
            FadeOut(self.param_a),
            FadeOut(function_point),
            run_time=0.5,
        )
        self.wait()

        self.next_section("Another_slope")

        new_x_equation = MathTex(r"x(a) = 1.3a")

        new_equations = VGroup(new_x_equation, new_y_equation)
        new_equations.arrange(DOWN)
        new_equations.move_to(self.equations)
        new_equations.add_background_rectangle(opacity=1, stroke_width=1, stroke_opacity=1, stroke_color=RED, buff=0.1)

        new_function = self.grid.plot_parametric_curve(
            lambda a: [
                1.3*a,
                0.5*a,
                0,
            ],
            t_range=[-10, 10],
            color=BLUE,
        )

        self.play(
            Transform(self.equations, new_equations),
            Transform(self.function, new_function),
            run_time=0.5,
        )
        self.wait()
    
    def quadratic_function(self):
        self.next_section("Transition_Quadratic")

        new_x_equation = MathTex(r"x(a) = 3a")
        new_y_equation = MathTex(r"y(a) = a^2")

        new_equations = VGroup(new_x_equation, new_y_equation)
        new_equations.arrange(DOWN)
        new_equations.move_to(self.equations)
        new_equations.add_background_rectangle(opacity=1, stroke_width=1, stroke_opacity=1, stroke_color=RED, buff=0.1)

        new_function = self.grid.plot_parametric_curve(
            lambda a: [
                3*a,
                a*a,
                0,
            ],
            t_range=[-10, 10],
            color=BLUE,
        )

        self.play(
            Transform(self.equations, new_equations),
            Transform(self.function, new_function),
        )
        self.wait()
