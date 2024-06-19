#!/usr/bin/env python

from manim import *
import math

class VisualizeAnalysisExponential(Scene):
    def construct(self):
        self.next_section("Construct_Scene")
        screen = FullScreenRectangle()

        grid = Axes(
            x_range=(-5, 5, 1),
            y_range=(-2, 3, 1),
            x_length=screen.width,
            y_length=screen.height,
            axis_config={
                "include_numbers": True,
            },
        )

        x_label = grid.get_x_axis_label("x")
        y_label = grid.get_y_axis_label("f(x)")
        grid_labels = VGroup(x_label, y_label)

        self.add(grid, grid_labels)
        #self.wait()

        #self.next_section("Create_Function")

        param_a = Variable(
            0,
            Tex("b", color=PURPLE),
            num_decimal_places=2,
        )

        function_equation = MathTex(
            r"f_b(x) = e^x - bx",
            substrings_to_isolate="b",
        )
        function_equation.set_color_by_tex("b", color=PURPLE)

        equations = VGroup(function_equation, param_a)
        equations.arrange(DOWN)
        equations.move_to(RIGHT * 4 + DOWN * 3)

        function = always_redraw(
            lambda: grid.plot(
                lambda x: self.graph_function(x, param_a.tracker.get_value()),
                color=YELLOW
            )
        )

        self.play(
            Write(equations),
            Create(function),
        )
        self.wait()

        self.next_section("Negative_b")

        self.play(
            param_a.tracker.animate.set_value(-1),
            run_time=3,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("Positive_b_small")

        self.play(
            param_a.tracker.animate.set_value(0.1),
            run_time=2,
            rate_func=rate_functions.smooth,
        )

        point_minimum = always_redraw(
            lambda: Dot(point=grid.input_to_graph_point(self.get_local_minimum(param_a.tracker.get_value()), function), color=ORANGE)
        )

        self.play(
            Create(point_minimum),
            Flash(point_minimum),
            run_time=0.5,
        )
        self.wait()

        # TODO: Add Text

        x_marker = always_redraw(
            lambda: self.get_x_marker(param_a.tracker.get_value())
        )

        y_marker = always_redraw(
            lambda: self.get_y_marker(param_a.tracker.get_value())
        )

        self.play(
            Write(x_marker),
        )

        self.next_section("Positive_b_large")

        self.play(
            param_a.tracker.animate.set_value(3.5),
            run_time=3,
            rate_func=rate_functions.smooth,
        )
    
    def get_x_marker(self, a):
        #marker_string = "ln({a:.2f})".format(a=a)
        marker_string="ln(a)"
        return MathTex(marker_string)
    
    def get_y_marker(self, a):
        #marker_string = "1 - ln({a:.2f})".format(a=a)
        marker_string="1 - ln(a)"
        return MathTex(marker_string)

    def graph_function(self, x, a):
        return math.exp(x) - a * x
    
    def get_local_minimum(self, a):
        return math.log(a)
