#!/usr/bin/env python

from manim import *

class PointAnalysis(Scene):
    def construct(self):
        self.transition()

        self.graph_first()
        self.graph_second()
        self.simple_insertion()

        self.solve_turning_point()
        self.solve_cool_function()
        self.graph_cool_function()
    
    def transition(self):
        self.next_section("Transition")

        title = Tex("2: Extremwerte der Extrempunkte", color=ORANGE)

        self.add(title)
        self.wait()

        self.next_section("Make_Room")

        self.play(
            FadeOut(title),
            run_time=0.5,
        )
    
    def graph_first(self):
        #self.next_section("Draw_Graph")
        screen = FullScreenRectangle()

        grid = NumberPlane(
            x_range=(-5, 5, 1),
            y_range=(-1.5, 3.5, 1),
            x_length=screen.width,
            y_length=screen.height,
            background_line_style={
                "stroke_color": ORANGE,
                "stroke_opacity": 0.6,
            },
            axis_config={
                "include_numbers": True,
                "include_tip": True,
            },
        )

        x_label = grid.get_x_axis_label("x")
        y_label = grid.get_y_axis_label("f(x)")
        grid_labels = VGroup(x_label, y_label)

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
        equations.set_z_index(1)
        equations.add_background_rectangle(opacity=1, stroke_width=1, stroke_opacity=1, stroke_color=ORANGE, buff=0.1)

        self.base_function = always_redraw(
            lambda: grid.plot(
                lambda x: self.graph_function(x),
                color=BLUE,
            )
        )

        self.first_graph = VGroup(grid, grid_labels)

        self.play(
            Create(grid),
            Write(grid_labels),
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
    
    def graph_second(self):
        self.next_section("Show_Second_Graph")
        screen = FullScreenRectangle()

        grid_second = NumberPlane(
            x_range=(-1.5, 1.5, 0.5),
            y_range=(-5.5, 7.5, 2),
            x_length=screen.width / 2,
            y_length=screen.height,
            background_line_style={
                "stroke_color": RED,
                "stroke_opacity": 0.6,
            },
            axis_config={
                "include_numbers": True,
                "include_tip": True,
            },
        )
        grid_second.next_to(self.first_graph, RIGHT)

        x_label = grid_second.get_x_axis_label("x")
        y_label = grid_second.get_y_axis_label("f(x)")
        grid_labels = VGroup(x_label, y_label)

        self.second_graph = VGroup(grid_second, grid_labels)

        self.add(self.second_graph)

        # Shrink left coordinate system so the right one fits into screen

        grid_first_old = self.first_graph[0]

        grid_first_labels = self.first_graph[1]
        grid_first_labels.generate_target()

        grid_first = NumberPlane(
            x_range=(-1.5, 1.5, 0.5),
            y_range=(-5.5, 7.5, 2),
            x_length=screen.width / 2,
            y_length=screen.height,
            background_line_style={
                "stroke_color": ORANGE,
                "stroke_opacity": 0.6,
            },
            axis_config={
                "include_numbers": True,
                "include_tip": True,
            },
        )
        grid_first.align_on_border(LEFT, buff=0)

        grid_first_labels.target.become(
            VGroup(
                grid_first.get_x_axis_label("x"),
                grid_first.get_y_axis_label("f(x)"),
            )
        )

        grid_second.generate_target()
        grid_second.target.align_on_border(RIGHT, buff=0)

        grid_labels.generate_target()
        grid_labels.target.become(
            VGroup(
                grid_second.target.get_x_axis_label("a"),
                grid_second.target.get_y_axis_label("f(x)"),
            )
        )

        seperator = Line(start=UP * 4, end=DOWN * 4, color=YELLOW)

        self.play(
            Uncreate(self.base_function),
            run_time=0.5,
        )
        self.play(
            Transform(grid_first_old, grid_first, replace_mobject_with_target_in_scene=True),
            MoveToTarget(grid_first_labels),
            MoveToTarget(grid_second),
            MoveToTarget(grid_labels),
            self.param_a.tracker.animate.set_value(0.25),
            run_time=2,
        )
        self.play(
            Write(seperator),
            run_time=1,
        )

        self.first_graph[0] = grid_first

        # Reinstance base_function because otherwise it's wrong
        self.base_function = always_redraw(
            lambda: grid_first.plot(
                lambda x: self.graph_function(x),
                color=BLUE,
            )
        )
        self.play(
            Create(self.base_function),
            run_time=0.5,
        )
    
    def simple_insertion(self):
        grid_first = self.first_graph[0]
        grid_second = self.second_graph[0]

        self.param_x = Variable(
            0.5,
            Tex("x", color=RED),
            num_decimal_places=2,
        )
        self.param_x.move_to(RIGHT * 5 + DOWN * 3)
        self.param_x.set_z_index(1)
        self.param_x.add_background_rectangle(opacity=1, stroke_width=1, stroke_opacity=1, stroke_color=RED, buff=0.1)

        self.simple_insertion_function = always_redraw(
            lambda: grid_second.plot(
                lambda a: self.graph_point_function(a),
                color=PURPLE,
            )
        )

        self.play(
            FadeIn(self.param_x, shift=UP),
            Create(self.simple_insertion_function),
            run_time=1,
        )
        self.wait()

        self.next_section("Create_markers")

        self.marker_x = always_redraw(
            lambda: DashedLine(
                start=grid_first.c2p(self.param_x.tracker.get_value(), 20),
                end=grid_first.c2p(self.param_x.tracker.get_value(), -10),
                color=RED,
            )
        )

        self.marker_a = always_redraw(
            lambda: DashedLine(
                start=grid_second.c2p(self.param_a.tracker.get_value(), 20),
                end=grid_second.c2p(self.param_a.tracker.get_value(), -10),
                color=PURPLE,
            )
        )

        self.marker_horizontal = always_redraw(
            lambda: DashedLine(
                start=grid_first.input_to_graph_point(self.param_x.tracker.get_value(), self.base_function),
                end=grid_second.input_to_graph_point(self.param_a.tracker.get_value(), self.simple_insertion_function),
                color=YELLOW
            )
        )

        self.play(
            Create(self.marker_x),
            Create(self.marker_a),
            Create(self.marker_horizontal),
            run_time=1,
        )
        self.wait()

        self.next_section("a_0d5")

        self.play(
            self.param_a.tracker.animate.set_value(0.5),
            run_time=3,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("a_m0d3")

        self.play(
            self.param_a.tracker.animate.set_value(-0.3),
            run_time=3,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("x_0d2")

        self.play(
            self.param_x.tracker.animate.set_value(0.2),
            run_time=3,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("x_1")

        self.play(
            self.param_x.tracker.animate.set_value(1),
            run_time=3,
            rate_func=rate_functions.smooth,
        )
        self.wait()
    
    def solve_turning_point(self):
        self.next_section("Start_Solving_turning_point")
        steps = [
            r"f'_a(x) = 0",
            r"4x - 8a = 0",
            r"4x = 8a",
            r"x = 2a",
        ]

        heading = Tex("Extremstelle herausfinden", color=ORANGE)
        heading.scale(0.6)
        heading.move_to(LEFT * 4.5 + UP * 2)

        self.steps_tex_left = VGroup(heading)

        last_pos = heading

        for step in steps:
            step_tex = MathTex(step)
            step_tex.next_to(last_pos, DOWN)
            
            self.steps_tex_left.add(step_tex)
            last_pos = step_tex
        
        steps_background = BackgroundRectangle(
            self.steps_tex_left,
            buff=0.1,
            fill_opacity=1,
            stroke_color=ORANGE,
            stroke_opacity=1,
            stroke_width=1
        )

        self.play(
            GrowFromCenter(steps_background),
            run_time=1,
        )

        for step in self.steps_tex_left:
            self.play(
                Write(step),
                run_time=0.5,
            )
            self.wait()
            self.next_section("Write_equations")
        
        self.steps_tex_left.add(steps_background)
    
    def solve_cool_function(self):
        self.next_section("Solve_cool_function")

        steps = [
            r"g(a) = f_a(2a)",
            r"g(a) = 2(2a)^2 - 8a(2a) + 9a^2",
            r"g(a) = 8a^2 - 16a^2 + 9a^2",
            r"g(a) = a^2",
        ]

        self.steps_tex_right = VGroup()

        for step in steps:
            step_tex = MathTex(step)
            self.steps_tex_right.add(step_tex)
        
        self.steps_tex_right.arrange(DOWN)
        self.steps_tex_right.move_to(RIGHT * 3 + UP * 1)

        steps_background = BackgroundRectangle(
            self.steps_tex_right,
            buff=0.1,
            fill_opacity=1,
            stroke_color=ORANGE,
            stroke_opacity=1,
            stroke_width=1
        )

        self.play(
            GrowFromCenter(steps_background),
            run_time=1,
        )

        for step in self.steps_tex_right:
            self.play(
                Write(step),
                run_time=0.5,
            )
            self.wait()
            self.next_section("Draw_step")
        
        self.steps_tex_right.add(steps_background)
    
    def graph_cool_function(self):
        self.next_section("Compress_Blocks")

        grid_first = self.first_graph[0]
        grid_second = self.second_graph[0]

        cool_function_equation = MathTex(r"g({{ a }}) = {{ a }}^2")
        cool_function_equation.set_color_by_tex("a", color=PURPLE)
        cool_function_equation.move_to(RIGHT * 4 + DOWN * 3)
        cool_function_equation.add_background_rectangle(
            opacity=1,
            stroke_width=1,
            stroke_opacity=1,
            stroke_color=ORANGE,
            buff=0.1,
        )

        self.play(
            ShrinkToCenter(self.steps_tex_left),
            FadeOut(self.param_x, shift=DOWN),
            Transform(self.steps_tex_right, cool_function_equation),
            run_time=1,
        )
        self.play(
            #Uncreate(self.marker_a),
            Uncreate(self.marker_x),
            Uncreate(self.marker_horizontal),
            Uncreate(self.simple_insertion_function),
            Unwrite(self.second_graph[1]),
            run_time=0.5
        )

        self.turning_point_function = always_redraw(
            lambda: grid_second.plot(
                lambda a: self.graph_turning_point_function(a),
                color=PINK,
            )
        )
        new_labels = VGroup(
            grid_second.get_x_axis_label("a"),
            grid_second.get_y_axis_label("g(x)"),
        )

        self.second_graph[1] = new_labels

        self.play(
            Create(self.turning_point_function),
            Write(self.second_graph[1]),
            run_time=0.5,
        )

        self.marker_horizontal = always_redraw(
            lambda: DashedLine(
                start=grid_first.input_to_graph_point(self.param_a.tracker.get_value() * 2, self.base_function),
                end=grid_second.input_to_graph_point(self.param_a.tracker.get_value(), self.turning_point_function),
                color=YELLOW
            )
        )

        self.play(
            Create(self.marker_horizontal),
            run_time=0.5
        )

        self.wait()

        self.next_section("a_left")

        self.play(
            self.param_a.tracker.animate.set_value(-0.5),
            run_time=3,
            rate_func=rate_functions.smooth,
        )
        self.wait()

        self.next_section("a_right")

        self.play(
            self.param_a.tracker.animate.set_value(0.5),
            run_time=3,
            rate_func=rate_functions.smooth,
        )
        self.wait()
    
    def graph_function(self, x):
        a = self.param_a.tracker.get_value()
        return 2 * x**2 - 8 * a * x + 9 * a**2

    def graph_point_function(self, a):
        x = self.param_x.tracker.get_value()
        return 2 * x**2 - 8 * a * x + 9 * a**2
    
    def graph_turning_point_function(self, a):
        return a**2
