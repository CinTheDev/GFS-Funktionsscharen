#!/usr/bin/env python

from manim import *
import math

class VisualizeAnalysisExponential(Scene):
    def construct(self):
        self.next_section("Construct_Scene")
        screen = FullScreenRectangle()

        self.grid = Axes(
            x_range=(-5, 5, 1),
            y_range=(-2, 3, 1),
            x_length=screen.width,
            y_length=screen.height,
            axis_config={
                "include_numbers": True,
            },
        )

        x_label = self.grid.get_x_axis_label("x")
        y_label = self.grid.get_y_axis_label("f(x)")
        grid_labels = VGroup(x_label, y_label)

        self.add(self.grid, grid_labels)

        self.param_a = Variable(
            0,
            Tex("b", color=PURPLE),
            num_decimal_places=2,
        )

        function_equation = MathTex(
            r"f_b(x) = e^x - bx",
            substrings_to_isolate="b",
        )
        function_equation.set_color_by_tex("b", color=PURPLE)

        equations = VGroup(function_equation, self.param_a)
        equations.arrange(DOWN)
        equations.move_to(RIGHT * 4 + DOWN * 3)

        self.function = always_redraw(
            lambda: self.grid.plot(
                lambda x: self.graph_function(x),
                color=YELLOW
            )
        )

        self.play(
            Write(equations),
            Create(self.function),
        )
        self.wait()

        self.next_section("Negative_b")

        self.play(
            self.param_a.tracker.animate.set_value(-1),
            run_time=3,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("Positive_b_small")

        self.play(
            self.param_a.tracker.animate.set_value(0.1),
            run_time=2,
            rate_func=rate_functions.smooth,
        )

        point_minimum = always_redraw(
            lambda: Dot(point=grid.input_to_graph_point(self.get_local_minimum(), function), color=ORANGE)
        )

        self.play(
            Create(point_minimum),
            Flash(point_minimum),
            run_time=0.5,
        )

        # TODO: Add Text

        x_marker = always_redraw(
            lambda: self.get_x_marker()
        )

        y_marker = always_redraw(
            lambda: self.get_y_marker()
        )

        self.play(
            Write(x_marker),
        )
        self.wait()

        self.next_section("Positive_b_large")

        self.play(
            param_a.tracker.animate.set_value(3.5),
            run_time=3,
            rate_func=rate_functions.smooth,
        )
    
    def get_x_marker(self):
        a = self.param_a.tracker.get_value()
        #marker_string = "ln({a:.2f})".format(a=a)
        marker_string="ln(a)"
        return MathTex(marker_string)
    
    def get_y_marker(self):
        a = self.param_a.tracker.get_value()
        #marker_string = "1 - ln({a:.2f})".format(a=a)
        marker_string="1 - ln(a)"
        return MathTex(marker_string)

    def graph_function(self, x):
        a = self.param_a.tracker.get_value()
        return math.exp(x) - a * x
    
    def get_local_minimum(self):
        a = self.param_a.tracker.get_value()
        return math.log(a)
