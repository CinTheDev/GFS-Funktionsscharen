#!/usr/bin/env python

from manim import *

class Bundles(Scene):
    def construct(self):
        self.transition()

        self.first_example()
        self.first_example_graph()

        self.second_example()
        self.second_example_graph()
    
    def transition(self):
        self.next_section("Transition")

        title = Tex("Spezielle Eigenschaften von Funktionenscharen", color=BLUE)

        self.subtitle = Tex("1: Bestimmen von Funktionsbündeln", color=BLUE)
        self.subtitle.scale(0.6)
        self.subtitle.next_to(title, DOWN)

        self.play(
            Write(title),
        )
        self.play(
            FadeIn(self.subtitle, shift=UP),
            run_time=0.7,
        )
        self.wait()

        self.next_section("Make_Room")

        self.subtitle.generate_target()
        self.subtitle.target.move_to(UP * 3.5)

        self.play(
            Unwrite(title),
            run_time=0.5,
        )
        self.play(
            MoveToTarget(self.subtitle),
            run_time=0.7
        )
        self.wait()
    
    def first_example(self):
        self.next_section("First_Example")

        equation = MathTex(r"f_a(x) = ax^2 - 4a")

        self.play(
            Write(equation),
            run_time=0.7,
        )
        self.wait()

        self.next_section("Move_Equation")

        equation.generate_target()
        equation.target.move_to(UP * 2)

        self.play(
            MoveToTarget(equation),
            run_time=0.7,
        )
        steps_left = [
            MathTex(r"f_a(x) = f_b(x); {{ a \neq b }}"),
            MathTex(r"f_1(x) = f_2(x)"),
            MathTex(r"1 \cdot x^2 - 4 \cdot 1 = 2 \cdot x^2 - 4 \cdot 2"),
            MathTex(r"x^2 - 4 = 2x^2 - 8"),
            MathTex(r"4 = x^2"),
            MathTex(r"\pm 2 = x"),
            #MathTex(r"f_a(-2) = 0 = f_a(2)"),
        ]
        steps_right = [
            MathTex(r"f_a(-2) = a(-2)^2 - 4a"),
            MathTex(r"f_a(-2) = 4a - 4a"),
            MathTex(r"f_a(-2) = 0"),
            MathTex(r"f_a(2) = a(2)^2 - 4a"),
            MathTex(r"f_a(2) = 0"),
        ]

        last_pos = equation
        equations_left = VGroup(equation)

        steps_left[0].submobjects[1].set_color(ORANGE)

        for step in steps_left:
            tex = step
            tex.next_to(last_pos, DOWN)

            self.play(
                FadeIn(tex, shift=UP),
                run_time=0.5
            )
            self.wait()
            self.next_section("Solve_Step")

            last_pos = tex
            equations_left.add(tex)
        
        self.next_section("Move_equations")

        equations_left.generate_target()
        equations_left.target.shift(LEFT * 4),

        self.play(
            MoveToTarget(equations_left),
            run_time=1.5,
        )

        heading_right = Tex("Höhe", color=BLUE)
        heading_right.scale(0.6)
        heading_right.move_to(UP * 2.5 + RIGHT * 4)

        self.play(
            Write(heading_right),
            run_time=0.5,
        )

        last_pos = heading_right
        equations_right = VGroup(heading_right)

        for step in steps_right:
            tex = step
            tex.next_to(last_pos, DOWN)

            self.play(
                FadeIn(tex, shift=LEFT),
                run_time=0.5,
            )
            self.wait()
            self.next_section("Solve_Step")

            last_pos = tex
            equations_right.add(tex)
        
        self.next_section("Clear_First_Example")

        self.play(
            LaggedStart(
                [Unwrite(eq) for eq in equations_left],
                lag_ratio=0.1,
                run_time=1
            ),
            LaggedStart(
                [Unwrite(eq) for eq in equations_right],
                lag_ratio=0.1,
                run_time=1
            ),
        )
    
    def first_example_graph(self):
        function = lambda x, a: a * x**2 - 4*a
        bundles = [-2, 2]
        two_vals = (1, 2)
        animate_steps = [
            -1,
            0.5,
        ]
        animate_lengths = [
            3,
            2,
        ]

        self.quick_graph(function, bundles, two_vals, 1, animate_steps, animate_lengths)
    
    def second_example(self):
        equation = MathTex(r"f_a(x) = x^2 - (a + 2)x + (a - 2)a")

        self.play(
            Write(equation),
            run_time=0.5,
        )
        self.wait()

        self.next_section("Move_Equation")

        equation.generate_target()
        equation.target.move_to(UP * 2)

        self.play(
            MoveToTarget(equation),
            run_time=1,
        )

        steps_left = [
            r"f_{-2}(x) = f_{2}(x)",
            r"x^2 - (-2 + 2)x + (-2 - 2)(-2) = x^2 - (2 + 2)x + (2 - 2)(2)",
            r"x^2 + 8 = x^2 - 4x",
            r"8 = -4x",
            r"x = 2",
        ]
        steps_right = [
            r"f_a(2) = (2)^2 - (a + 2)(2) + (a - 2)a",
            r"f_a(2) = 4 - 2a + 4 + a^2 - 2a",
            r"f_a(2) = 8 - 4a + a^2",
        ]

        last_pos = equation
        equations_left = VGroup(equation)

        for step in steps_left:
            tex = MathTex(step)
            tex.next_to(last_pos, DOWN)

            self.play(
                FadeIn(tex, shift=UP),
                run_time=0.5,
            )
            self.wait()
            self.next_section("Solve_left")

            last_pos = tex
            equations_left.add(tex)
        
        self.next_section("Move_equations")

        top = MathTex(r"x = 2")
        top.move_to(UP * 2)

        self.play(
            Transform(equations_left, top, replace_mobject_with_target_in_scene=True),
            run_time=1,
        )

        last_pos = top
        equations_right = VGroup(top)

        for step in steps_right:
            tex = MathTex(step)
            tex.next_to(last_pos, DOWN)

            self.play(
                FadeIn(tex, shift=LEFT),
                run_time=0.5,
            )
            self.wait()
            self.next_section("Solve_right")

            last_pos = tex
            equations_right.add(tex)
        
        self.next_section("Cross")

        comment = Tex("Ist KEIN Funktionsbündel!", color=RED)
        comment.next_to(equations_right, DOWN)
        underline = Underline(comment, color=RED)

        self.play(
            Write(comment),
            run_time=1,
        )
        self.play(
            Create(underline),
            run_time=1,
        )
        self.wait()

        self.next_section("Second_Example_Clear")

        self.play(
            LaggedStart(
                [Unwrite(eq) for eq in equations_right],
                lag_ratio=0.1,
            ),
            Unwrite(comment),
            Uncreate(underline),
            run_time=1,
        )
    
    def second_example_graph(self):
        function = lambda x, a: x**2 - (a + 2)*x + (a - 2)*a
        bundles = []
        two_vals = (-2, 2)
        animate_steps = [
            -1,
            8,
        ]
        animate_lengths = [
            5,
            3,
        ]

        self.quick_graph(function, bundles, two_vals, 1, animate_steps, animate_lengths, fadeout=False, y_range=(-4, 15, 2))
    
    def quick_graph(self, function, bundles_x, two_vals, initial_param, animate_steps, animate_lengths, fadeout=True, x_range=(-7, 7, 1), y_range=(-5, 5, 1)):
        self.subtitle.generate_target()
        self.subtitle.target.shift(UP)

        self.play(
            MoveToTarget(self.subtitle),
            run_time=0.5,
        )

        screen = FullScreenRectangle()

        grid = NumberPlane(
            x_range=x_range,
            y_range=y_range,
            x_length=screen.width,
            y_length=screen.height,
            background_line_style={
                "stroke_color": YELLOW,
                "stroke_opacity": 0.6,
            },
            axis_config={
                'include_numbers': True,
                "include_tip": True,
            },
        )

        x_label = grid.get_x_axis_label("x")
        y_label = grid.get_y_axis_label("f(x)")
        grid_labels = VGroup(x_label, y_label)

        self.play(
            Create(grid),
            Write(grid_labels),
            run_time=1,
        )

        param_a = Variable(
            two_vals[0],
            Tex("a", color=BLUE),
            num_decimal_places=2,
        )
        param_a.move_to(LEFT * 5 + DOWN * 3.25)

        draw_function = always_redraw(
            lambda: grid.plot(
                lambda x: function(x, param_a.tracker.get_value()),
                color=BLUE,
            )
        )
        draw_function_2 = grid.plot(
            lambda x: function(x, two_vals[1]),
            color=GREEN,
        )

        draw_bundles = VGroup()
        
        for bundle in bundles_x:
            draw_bundle = Dot(point=grid.input_to_graph_point(bundle, draw_function), color=ORANGE)
            draw_bundles.add(draw_bundle)

        self.play(
            Create(draw_function),
            Create(draw_function_2),
            [GrowFromCenter(b, point_color=RED) for b in draw_bundles],
            run_time=2,
        )

        self.wait()

        self.next_section("Unify")

        self.play(
            param_a.tracker.animate.set_value(initial_param),
            Uncreate(draw_function_2),
            run_time=1,
        )

        self.play(
            Write(param_a),
            run_time=0.5,
        )
        
        self.wait()

        if len(animate_steps) != len(animate_lengths):
            raise Exception("ERROR IN Bundles::quick_graph() - animate_steps does not have same length as animate_lengths.")
        
        for i in range(len(animate_steps)):
            self.next_section("Graph_value_animate")
            self.play(
                param_a.tracker.animate.set_value(animate_steps[i]),
                run_time=animate_lengths[i],
                rate_func=rate_functions.smooth,
            )
            self.wait()
        
        if not fadeout:
            return

        self.next_section("Remove_graph")

        self.play(
            Uncreate(grid),
            Uncreate(draw_function),
            Unwrite(grid_labels),
            Unwrite(param_a),
            [ShrinkToCenter(draw_bundle) for draw_bundle in draw_bundles],
            run_time=1,
        )

        self.subtitle.generate_target()
        self.subtitle.target.shift(DOWN)
        self.play(
            MoveToTarget(self.subtitle),
            run_time=0.5,
        )
