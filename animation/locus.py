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

        grid_downshift = 1.5
        visible_y_range=(-1.5, 3.5, 1)
        visible_dy = visible_y_range[1] - visible_y_range[0]
        y_extend = visible_dy * grid_downshift
        y_range = (3.5 - y_extend, 3.5, 1)

        self.grid = NumberPlane(
            x_range=(-5, 5, 1),
            y_range=y_range,
            x_length=screen.width,
            y_length=screen.height * grid_downshift,
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
        self.grid.align_on_border(UP, buff=0)

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

        self.function = always_redraw(
            lambda: self.grid.plot(
                lambda x: self.graph_function(x),
                color=BLUE,
            )
        )

        self.play(
            Create(self.grid),
            Write(self.grid_labels),
            Write(self.function),
            FadeIn(equations),
            run_time=2,
        )
        self.wait()

        self.dot_local_minimum = always_redraw(
            lambda: Dot(point=self.grid.input_to_graph_point(self.get_local_minimum(), self.function), color=ORANGE)
        )

        self.next_section("Goes_Down")

        self.add(self.dot_local_minimum)
        self.play(
            self.param_a.tracker.animate.set_value(2),
            run_time=3,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("Show_Locus")

        # Scroll down

        self.grid.generate_target()
        x_label.generate_target()

        self.grid.target.shift(UP * 3)
        x_label.target.shift(UP * 3)

        self.play(
            MoveToTarget(self.grid),
            MoveToTarget(x_label),
            run_time=1,
            rate_func=rate_functions.smooth,
        )

        self.locus_function = always_redraw(
            lambda: self.grid.plot(
                lambda x: self.graph_locus_function(x),
                color=PURPLE,
            )
        )

        self.play(
            Create(self.locus_function)
        )
        self.wait()

        self.next_section("Goes_Down_Further")

        self.play(
            self.param_a.tracker.animate.set_value(3),
            run_time=2,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("Goes_Back_Up")
        
        self.play(
            self.param_a.tracker.animate.set_value(-1),
            run_time=2,
            rate_func=rate_functions.smooth,
        )
        self.wait()
    
    def graph_function(self, x):
        a = self.param_a.tracker.get_value()

        return math.exp(2*x) - a * math.exp(x)
    
    def graph_locus_function(self, x):
        return -1 * math.exp(2 * x)
    
    def get_local_minimum(self):
        a = self.param_a.tracker.get_value()

        if a < 0.01:
            return -10.0

        return math.log(a / 2.0)
