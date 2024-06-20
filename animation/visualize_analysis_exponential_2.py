#!/usr/bin/env python

from manim import *
import math

class VisualizeAnalysisExponentialAdvanced(Scene):
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
            Tex("h"),
            num_decimal_places=2,
        )

        function_equation = MathTex(r"f_h(x) = x \cdot e^{h x}")

        equations = VGroup(function_equation, self.param_a)
        equations.arrange(DOWN)
        equations.move_to(RIGHT * 4 + DOWN * 3)

        self.function = always_redraw(
            lambda: self.grid.plot(
                lambda x: self.graph_function(x),
                color=YELLOW,
            )
        )

        self.play(
            Write(equations),
            Create(self.function),
        )
        self.wait()

        self.next_section("h_1")

        self.play(
            self.param_a.tracker.animate.set_value(1),
            run_time=2,
            rate_func=rate_functions.smooth,
        )

        turning_point = always_redraw(
            lambda: Dot(point=self.grid.input_to_graph_point(self.get_turning_point(), self.function), color=ORANGE)
        )
        inflection_point = always_redraw(
            lambda: Dot(point=self.grid.input_to_graph_point(self.get_inflection_point(), self.function), color=RED)
        )

        self.play(
            Create(turning_point),
            Create(inflection_point),
            Flash(turning_point),
            Flash(inflection_point),
            run_time=0.5,
        )

        # TODO: Draw markers

        self.wait()

        self.next_section("h_n1")

        self.play(
            self.param_a.tracker.animate.set_value(-1),
            run_time=5,
            rate_func=rate_functions.smooth,
        )
        self.wait()

    def graph_function(self, x):
        a = self.param_a.tracker.get_value()
        return x * math.exp(a * x)
    
    def get_turning_point(self):
        a = self.param_a.tracker.get_value()

        if abs(a) < 0.01:
            return 999999

        return -1.0 / a
    
    def get_inflection_point(self):
        a = self.param_a.tracker.get_value()

        if abs(a) < 0.01:
            return 999999

        return -2.0 / a
