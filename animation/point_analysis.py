#!/usr/bin/env python

from manim import *

class PointAnalysis(Scene):
    def construct(self):
        self.graph()
    
    def graph(self):
        self.next_section("Draw_Graph")
        screen = FullScreenRectangle()

        self.grid = NumberPlane(
            x_range=(-5, 5, 1),
            y_range=(-1.5, 3.5, 1),
            x_length=screen.width,
            y_length=screen.height,
            tips=True,
            background_line_style={
                "stroke_color": ORANGE,
                "stroke_opacity": 0.6,
            },
            axis_config={
                "include_numbers": True,
                "tip_shape": StealthTip,
            },
        )

        x_label = self.grid.get_x_axis_label("x")
        y_label = self.grid.get_y_axis_label("f(x)")
        grid_labels = VGroup(x_label, y_label)

        self.param_a = Variable(
            0,
            Tex("a", color=PURPLE),
            num_decimal_places=2,
        )

        function_equation = MathTex(r"f_{{ a }}(x) = 2x^2 - 8{{ a }}x + 9{{ a }}^2")
        function_equation.set_color_by_tex("a", color=PURPLE)

        equations = VGroup(function_equation, self.param_a)
        equations.arrange(DOWN)
        equations.move_to(LEFT * 4 + DOWN * 3)
        equations.add_background_rectangle(opacity=1, stroke_width=1, stroke_opacity=1, stroke_color=ORANGE, buff=0.1)

        self.base_function = always_redraw(
            lambda: self.grid.plot(
                lambda x: self.graph_function(x),
                color=BLUE,
            )
        )

        self.play(
            Create(self.grid),
            Write(grid_labels),
            Write(self.base_function),
            FadeIn(equations),
            run_time=2,
        )
        self.wait()
    
    def graph_function(self, x):
        a = self.param_a.tracker.get_value()
        return 2 * x**2 - 8 * a * x + 9 * a**2
