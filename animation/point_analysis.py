#!/usr/bin/env python

from manim import *

class PointAnalysis(Scene):
    def construct(self):
        self.graph()
        self.simple_insertion()
        self.solve_turning_point()
    
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
        self.grid_labels = VGroup(x_label, y_label)

        self.param_a = Variable(
            0,
            Tex("a", color=PURPLE),
            num_decimal_places=2,
        )

        self.function_equation = MathTex(r"f_{{ a }}(x) = 2x^2 - 8{{ a }}x + 9{{ a }}^2")
        self.function_equation.set_color_by_tex("a", color=PURPLE)

        equations = VGroup(self.function_equation, self.param_a)
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
            Write(self.grid_labels),
            Write(self.base_function),
            FadeIn(equations),
            run_time=2,
        )
        self.wait()

        self.next_section("Goes_Left")

        self.play(
            self.param_a.tracker.animate.set_value(-1.5),
            run_time=2,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("Goes_Right")

        self.play(
            self.param_a.tracker.animate.set_value(1.5),
            run_time=4,
            rate_func=rate_functions.smooth,
        )
        self.wait()
    
    def simple_insertion(self):
        self.next_section("Transition")

        self.play(
            Unwrite(self.base_function),
            Unwrite(self.grid_labels),
            Unwrite(self.param_a),
            run_time=1,
        )

        self.simple_insertion_function = always_redraw(
            lambda: self.grid.plot(
                lambda a: self.graph_point_function(a),
                color=PURPLE,
            )
        )
        new_labels = VGroup(
            self.grid.get_x_axis_label("a"),
            self.grid.get_y_axis_label("f_a(x)"),
        )
        new_param = Variable(
            0,
            Tex("x", color=RED),
            num_decimal_places=2,
        )
        new_param.move_to(self.param_a)

        self.grid_labels.become(new_labels)
        self.param_a.become(new_param)

        self.play(
            Write(self.simple_insertion_function),
            Write(self.grid_labels),
            Write(self.param_a),
            run_time=2,
        )
        self.wait()

        self.next_section("Move_left")

        self.play(
            self.param_a.tracker.animate.set_value(-3),
            run_time=1,
        )
        self.wait()

        self.next_section("Move_center")

        self.play(
            self.param_a.tracker.animate.set_value(0),
            run_time=2,
        )
        self.wait()
    
    def solve_turning_point(self):
        self.next_section("Start_Solving_turning_point")
        steps = [
            r"f'_a(x) = 0",
            r"4x - 8a = 0",
            r"4x = 8a",
            r"x = 0.5a",
        ]

        heading = Tex("Extremstelle herausfinden", color=ORANGE)
        heading.scale(0.6)
        heading.move_to(LEFT * 4.5 + UP * 2)

        steps_tex = VGroup(heading)

        last_pos = heading

        for step in steps:
            step_tex = MathTex(step)
            step_tex.next_to(last_pos, DOWN)
            
            steps_tex.add(step_tex)
            last_pos = step_tex
        
        steps_background = BackgroundRectangle(steps_tex, buff=0.1, fill_opacity=1, stroke_color=ORANGE, stroke_opacity=1, stroke_width=1)

        self.play(
            GrowFromCenter(steps_background),
            run_time=1,
        )

        for step in steps_tex:
            self.play(
                Write(step),
                run_time=0.5,
            )
            self.wait()
            self.next_section("Write_equations")
        
        steps_tex.add(steps_background)
    
    def graph_function(self, x):
        a = self.param_a.tracker.get_value()
        return 2 * x**2 - 8 * a * x + 9 * a**2

    def graph_point_function(self, a):
        x = self.param_a.tracker.get_value()
        return 2 * x**2 - 8 * a * x + 9 * a**2
