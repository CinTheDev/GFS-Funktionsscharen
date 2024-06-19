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
    
    def graph_function(self, x, a):
        return math.exp(x) - a * x
