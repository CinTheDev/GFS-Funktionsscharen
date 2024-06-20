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

        turning_point_x_marker = always_redraw(
            lambda: self.get_turning_point_x_marker()
        )

        self.play(
            Write(turning_point_x_marker),
        )

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

        return a and -1.0 / a or 99
    
    def get_inflection_point(self):
        a = self.param_a.tracker.get_value()

        return a and -2.0 / a or 99
    
    def get_turning_point_x_marker(self):
        a = self.param_a.tracker.get_value()
        x = self.get_turning_point()

        marker_string = [
            "-{1} \over ",
            "{0:.2f}".format(a)
        ]

        marker = MathTex(*marker_string, color=YELLOW)
        marker.set_color_by_tex(".", color=PURPLE)

        return self.get_x_marker(x, marker)

    def get_x_marker(self, x, marker):
        grid_origin = self.grid.get_origin()

        a = self.param_a.tracker.get_value()

        fx = self.graph_function(x)
        point = self.grid.input_to_graph_point(x, self.function)

        if fx >= 0:
            #marker.move_to(grid_origin + DOWN * 1)
            marker.next_to(grid_origin, DOWN)
        else:
            #marker.move_to(grid_origin + UP * 0.5)
            marker.next_to(grid_origin, UP)
        
        marker.set_x(point[0])

        point_center = point.copy()
        point_center[1] = grid_origin[1]

        line_length = abs(point[1] - point_center[1])
        line_length -= 0.2

        line = DashedLine(start=point, end=point_center)
        line.set_length(line_length)

        return VGroup(marker, line)
