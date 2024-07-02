#!/usr/bin/env python

# Ortskurven

from manim import *
import math

class Locus(Scene):
    def construct(self):
        self.transition()
        self.graph()
    
    def transition(self):
        self.next_section("Transition")
        title = Tex("Ortskurven", color=RED)

        self.play(
            SpinInFromNothing(title, point_color=ORANGE)
        )
        self.wait()

        self.next_section("Graph")

        self.play(
            FadeOut(title)
        )
    
    def graph(self):
        screen = FullScreenRectangle()

        self.grid = NumberPlane(
            x_range=(-5, 5, 1),
            y_range=(-1.5, 3.5, 1),
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
        y_label = self.grid.get_y_axis_label("f(x)")
        self.grid_labels = VGroup(x_label, y_label)

        self.param_a = Variable(
            0,
            Tex("a", color=PURPLE),
            num_decimal_places=2,
        )

        self.function_equation = MathTex(r"f_{{ a }}(x) = e^{2x} - {{ a }} e^x")
        self.function_equation.set_color_by_tex("a", color=PURPLE)

        equations = VGroup(self.function_equation, self.param_a)
        equations.arrange(DOWN)
        equations.move_to(LEFT * 4 + DOWN * 3)
        equations.add_background_rectangle(opacity=1, stroke_width=1, stroke_opacity=1, stroke_color=RED, buff=0.1)

        self.base_function = always_redraw(
            lambda: self.grid.plot(
                lambda x: self.graph_function(x),
                color=BLUE,
            )
        )

        self.play(
            Create(self.grid),
            Write(self.grid_labels),
            Write(self.base_function),
            FadeIn(equations),
            run_time=2,
        )
        self.wait()
    
    def graph_function(self, x):
        a = self.param_a.tracker.get_value()

        return math.exp(2*x) - a * math.exp(x)
