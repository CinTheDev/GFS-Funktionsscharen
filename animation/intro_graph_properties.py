#!/usr/bin/env python

from manim import *
import math

class IntroGraphProperties(Scene):
    def construct(self):
        self.graph()
        self.description()

    def graph_function(self, x, a):
        return x**4 - 0.4 * a * x**2
    
    def turning_points(self, a):
        if a < 0:
            return [0, 0]
        
        x_1 = math.sqrt(0.2 * a)
        x_2 = x_1 * -1

        return [x_1, x_2]
    
    def nullstellen(self, a):
        if a <= 0:
            return [0, 0, 0]
        
        x_1 = math.sqrt(0.4 * a)
        x_2 = x_1 * -1

        return [0, x_1, x_2]
    
    def graph(self):
        self.next_section("Create_Graph")
        screen = FullScreenRectangle()

        # Draw coordinate system

        grid = Axes(
            x_range=(-5, 5, 1),
            y_range=(-2, 3, 1),
            x_length=screen.width,
            y_length=screen.height,
            axis_config={
                'include_numbers': True,
            },
        )

        x_label = grid.get_x_axis_label("x")
        y_label = grid.get_y_axis_label("f(x)")
        grid_labels = VGroup(x_label, y_label)

        self.add(grid, grid_labels)

        label_a = Tex("a", color=PURPLE)
        param_a = Variable(
            0,
            label_a,
            num_decimal_places=2
        )

        function_equation = MathTex(
            r"f_a(x) = x^4 - 0.4ax^2",
            substrings_to_isolate="a",
        )
        function_equation.set_color_by_tex("a", PURPLE)

        equations = VGroup(function_equation, param_a)
        equations.arrange(DOWN)
        equations.shift(RIGHT * 4)
        equations.shift(DOWN * 3)

        function = always_redraw(
            lambda: grid.plot(
                lambda x: self.graph_function(x, param_a.tracker.get_value()),
                color=YELLOW
            )
        )

        self.play(
            Write(equations),
        )
        self.play(
            Create(function),
        )
        self.wait()

        self.next_section("graph_goes_down")

        self.play(
            param_a.tracker.animate.set_value(-5),
            run_time=1,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.play(
            param_a.tracker.animate.set_value(5),
            run_time=5,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("show_bundle")

        bundle_point = grid.input_to_graph_point(0, function)

        point_bundle = Dot(point=bundle_point, color=ORANGE)
        text_bundle = Tex("Bündel", color=YELLOW)
        text_bundle.move_to(DOWN * 3 + LEFT)

        arrow_bundle = Arrow(start=text_bundle, end=bundle_point, color=YELLOW)

        self.play(
            Create(point_bundle),
            Write(text_bundle),
            Create(arrow_bundle),
        )

        self.play(
            param_a.tracker.animate.set_value(-1),
            run_time=10,
            rate_func=rate_functions.smooth
        )
        self.wait()

        self.next_section("show_nullstellen")

        self.play(
            Unwrite(text_bundle),
            Uncreate(arrow_bundle),
        )

        nullstelle_middle = always_redraw(
            lambda: Dot(point=grid.input_to_graph_point(self.nullstellen(param_a.tracker.get_value())[0], function), color=ORANGE)
        )
        nullstelle_left = always_redraw(
            lambda: Dot(point=grid.input_to_graph_point(self.nullstellen(param_a.tracker.get_value())[1], function), color=ORANGE)
        )
        nullstelle_right = always_redraw(
            lambda: Dot(point=grid.input_to_graph_point(self.nullstellen(param_a.tracker.get_value())[2], function), color=ORANGE)
        )

        text_nullstellen = Tex("Nullstellen")
        text_nullstellen.move_to(DOWN * 3.5 + LEFT)

        arrow_nullstelle_left = always_redraw(
            lambda: Arrow(start=text_nullstellen.get_center(), end=nullstelle_left, color=YELLOW)
        )
        arrow_nullstelle_middle = always_redraw(
            lambda: Arrow(start=text_nullstellen.get_center(), end=nullstelle_middle, color=YELLOW)
        )
        arrow_nullstelle_right = always_redraw(
            lambda: Arrow(start=text_nullstellen.get_center(), end=nullstelle_right, color=YELLOW)
        )

        self.play(
            Create(nullstelle_middle),
            Create(nullstelle_left),
            Create(nullstelle_right),

            Write(text_nullstellen),

            Create(arrow_nullstelle_left),
            Create(arrow_nullstelle_middle),
            Create(arrow_nullstelle_right),
        )

        self.play(
            param_a.tracker.animate.set_value(5),
            run_time=10,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("show_turning_points")

        self.play(
            Uncreate(nullstelle_middle),
            Uncreate(nullstelle_left),
            Uncreate(nullstelle_right),

            Unwrite(text_nullstellen),

            Uncreate(arrow_nullstelle_left),
            Uncreate(arrow_nullstelle_middle),
            Uncreate(arrow_nullstelle_right),
        )

        point_left = always_redraw(
            lambda: Dot(point=grid.input_to_graph_point(self.turning_points(param_a.tracker.get_value())[0], function), color=ORANGE)
        )
        point_right = always_redraw(
            lambda: Dot(point=grid.input_to_graph_point(self.turning_points(param_a.tracker.get_value())[1], function), color=ORANGE)
        )

        text_points = Tex("Extrempunkte")
        text_points.move_to(DOWN * 3.5 + LEFT)

        arrow_left = always_redraw(
            lambda: Arrow(start=text_points.get_center(), end=point_left, color=YELLOW)
        )
        arrow_middle = always_redraw(
            lambda: Arrow(start=text_points.get_center(), end=point_bundle, color=YELLOW)
        )
        arrow_right = always_redraw(
            lambda: Arrow(start=text_points.get_center(), end=point_right, color=YELLOW)
        )

        self.play(
            Create(point_left),
            Create(point_right),
            Create(arrow_left),
            Create(arrow_middle),
            Create(arrow_right),
            Write(text_points),
        )

        self.play(
            param_a.tracker.animate.set_value(-1),
            run_time=10,
            rate_func=rate_functions.smooth,
        )

        self.wait()

    def description(self):
        self.next_section("Properties_Description")

        self.clear()
        title = Tex("Falls der Parameter sich ändert, können Extrempunkte...")

        bullet_points = [
            "- ... sich bewegen",
            "- ... erscheinen oder verschwinden",
            "- ... ihre \"Art\" ändern; z.B. Hochpunkt wird zum Tiefpunkt"
        ]

        bullet_points_tex = []
        bullet_points_animations = []

        for p in bullet_points:
            p_tex = Tex(p, color=YELLOW).scale(0.6)

            bullet_points_tex.append(p_tex)
            bullet_points_animations.append(Write(p_tex))
        
        text = VGroup(title, *bullet_points_tex).arrange(DOWN, aligned_edge=LEFT)

        self.add(title)
        self.wait()

        self.next_section("Properties_Description_text")

        self.play(
            LaggedStart(
                *bullet_points_animations,
                lag_ratio=0.5,
                run_time=5,
            )
        )
        self.wait()
