#!/usr/bin/env python

from manim import *

class CalculationTurningPoints(Scene):
    def construct(self):
        self.solve_x()
        self.solve_type()
        # TODO: Visualize solution on graph
        # TODO: Analyze for type (Tiefpunkt, Hochpunkt, ...) [next scene]
    
    def animate_solve_steps(self, top_equation, string_list):
        steps = VGroup(top_equation)
        old_position = top_equation

        for step in string_list:
            step_tex = MathTex(
                step,
                substrings_to_isolate="a"
            )
            step_tex.set_color_by_tex("a", color=PURPLE)
            step_tex.next_to(old_position, DOWN)

            self.play(
                Write(step_tex),
                run_time=0.5,
            )
            self.wait()
            self.next_section("Solve_Step")

            steps.add(step_tex)
            old_position = step_tex
        
        return steps
    
    def solve_x(self):
        self.title = Tex("2. Fall: Extrempunkte", color=YELLOW)

        self.play(
            Write(self.title)
        )
        self.wait()

        self.next_section("Turning_Point_Example")

        # Move title out of way

        self.title.generate_target()
        self.title.target.move_to(UP * 3)

        self.play(
            MoveToTarget(self.title),
        )

        # Write equation

        equation = MathTex(
            r"f_a(x) = x^4 - 0.4ax^2",
            substrings_to_isolate="a",
        )
        equation.set_color_by_tex("a", color=PURPLE)

        self.play(
            Write(equation),
            run_time=0.5,
        )

        self.next_section("Derive")

        comment = Tex("Wir wollen Hoch-/Tiefpunkte herausfinden", color=YELLOW)
        comment.scale(0.6)
        comment.next_to(equation, UP)

        equation_derivative = MathTex(
            r"f'_a(x) = 4x^3 - 0.8ax",
            substrings_to_isolate="a",
        )
        equation_derivative.set_color_by_tex("a", color=PURPLE)
        equation_derivative.next_to(equation, DOWN)

        comment.generate_target()
        comment.move_to(equation)
        comment.set_opacity(0)

        equation_derivative.generate_target()
        equation_derivative.move_to(equation)
        equation_derivative.set_opacity(0)

        self.play(
            MoveToTarget(comment)
        )
        self.play(
            MoveToTarget(equation_derivative)
        )
        self.wait()

        self.next_section("Start_solving")

        self.play(
            FadeOut(equation),
            FadeOut(comment),
            run_time=0.5
        )

        equation_derivative.generate_target()
        equation_derivative.target.move_to(UP * 2)

        self.play(
            MoveToTarget(equation_derivative),
            run_time=0.5
        )
        self.wait()
        
        self.next_section("Solve_Step")

        solve_steps_first = [
            r"0 = 4x^3 - 0.8ax",
            r"0 = x(4x^2 - 0.8a)",
            r"x_1 = 0; x_{2;3} = ...",
        ]

        steps_first = self.animate_solve_steps(equation_derivative, solve_steps_first)

        # Move steps out of way

        steps_first.generate_target()
        steps_first.target.move_to(steps_first.get_center() + LEFT * 3)

        self.play(
            MoveToTarget(steps_first)
        )
        self.wait()

        # Solve second half

        equation_secondary = MathTex(
            r"0 = 4x^2 - 0.8a",
            substrings_to_isolate="a"
        )
        equation_secondary.set_color_by_tex("a", color=PURPLE)
        equation_secondary.move_to(UP * 2 + RIGHT * 3)

        self.play(
            Write(equation_secondary),
            run_time=0.5
        )
        self.wait()

        self.next_section("Solve_Step")

        solve_steps_secondary = [
            r"0.8a = 4x^2",
            r"0.2a = x^2",
            r"\pm \sqrt{0.2a} = x_{2;3}",
        ]

        steps_secondary = self.animate_solve_steps(equation_secondary, solve_steps_secondary)

        self.next_section("Solution_Summary")

        self.solution = MathTex(r"x_1 = 0; x_{2;3} = \pm \sqrt{0.2a}")
        self.solution.move_to(DOWN * 2.5)

        self.play(
            Write(self.solution)
        )
        self.play(
            Circumscribe(self.solution)
        )
        self.wait()

        self.next_section("Fadeout")

        self.solution.generate_target()
        self.solution.target.center()

        self.play(
            FadeOut(steps_first),
            FadeOut(steps_secondary),
            run_time=0.5
        )
        self.play(
            MoveToTarget(self.solution),
            run_time=0.5,
        )

    def solve_type(self):
        comment = Tex("Hochpunkt, Tiefpunkt, Sattelpunkt??", color=YELLOW)
        comment.scale(0.6)
        comment.next_to(self.solution, UP)

        self.play(
            Write(comment)
        )
        self.wait()

        self.next_section("Make_Space")

        solution_x1 = MathTex(r"x_1 = 0")
        solution_x1.move_to(UP * 2)

        self.play(
            Unwrite(comment),
            run_time=0.5
        )
        self.play(
            Transform(self.solution, solution_x1),
            run_time=0.5
        )
        self.wait()

        self.next_section("Insert_x1")

        equation_second_derivative = MathTex(
            r"f''_a(x) = 12x^2 - 0.8a",
            substrings_to_isolate="a",
        )
        equation_second_derivative.set_color_by_tex("a", color=PURPLE)
        equation_second_derivative.next_to(solution_x1, DOWN)

        equation_second_derivative_insert = MathTex(
            r"f''_a(0) = -0.8a",
            substrings_to_isolate="a",
        )
        equation_second_derivative_insert.set_color_by_tex("a", color=PURPLE)
        equation_second_derivative_insert.next_to(equation_second_derivative, DOWN)

        self.play(
            Write(equation_second_derivative),
            run_time=0.5
        )
        self.wait()

        self.play(
            Write(equation_second_derivative_insert),
            run_time=0.5
        )
        self.wait()
