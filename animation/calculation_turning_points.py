#!/usr/bin/env python

from manim import *

class CalculationTurningPoints(Scene):
    def construct(self):
        self.solve_x()
        self.solve_type_zero()
        self.solve_type_other()
    
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
        self.title = Tex("3. Fall: Extrempunkte", color=YELLOW)

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

    def solve_type_zero(self):
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

        self.next_section("Determine_local_maximum")

        constraint_local_maximum = MathTex(
            r"f''_a(x) < 0",
            substrings_to_isolate="a"
        )
        constraint_local_maximum.set_color_by_tex("a", color=PURPLE)
        constraint_local_maximum.move_to(LEFT * 4 + DOWN)

        comment_local_maximum = Tex("Hochpunkt", color=YELLOW)
        comment_local_maximum.scale(0.6)
        comment_local_maximum.next_to(constraint_local_maximum, UP)

        self.play(
            Write(constraint_local_maximum),
            Write(comment_local_maximum),
            run_time=1,
        )
        self.wait()

        self.next_section("Solve_Step")

        local_maximum_steps = [
            r"-0.8a < 0",
            r"-a < 0",
            r"a > 0",
        ]

        local_maximum_group = self.animate_solve_steps(constraint_local_maximum, local_maximum_steps)

        self.next_section("Determine_local_minimum")

        constraint_local_minimum = MathTex(
            r"f''_a(x) > 0",
            substrings_to_isolate="a",
        )
        constraint_local_minimum.set_color_by_tex("a", color=PURPLE)
        constraint_local_minimum.move_to(DOWN)

        comment_local_minimum = Tex("Tiefpunkt", color=YELLOW)
        comment_local_minimum.scale(0.6)
        comment_local_minimum.next_to(constraint_local_minimum, UP)

        self.play(
            Write(constraint_local_minimum),
            Write(comment_local_minimum),
            run_time=1
        )
        self.wait()

        self.next_section("Solve_Step")

        local_minimum_steps = [
            r"-0.8a > 0",
            r"-a > 0",
            r"a < 0",
        ]

        local_minimum_group = self.animate_solve_steps(constraint_local_minimum, local_minimum_steps)

        self.next_section("Determine_saddle_point")

        constraint_saddle = MathTex(
            r"f''_a(x) = 0",
            substrings_to_isolate="a",
        )
        constraint_saddle.set_color_by_tex("a", color=PURPLE)
        constraint_saddle.move_to(RIGHT * 4 + DOWN)

        comment_saddle = Tex("Sattelpunkt", color=YELLOW)
        comment_saddle.scale(0.6)
        comment_saddle.next_to(constraint_saddle, UP)

        self.play(
            Write(constraint_saddle),
            Write(comment_saddle),
            run_time=1
        )
        self.wait()

        self.next_section("Solve_Step")

        saddle_steps = [
            r"-0.8a = 0",
            r"a = 0",
        ]

        saddle_steps_group = self.animate_solve_steps(constraint_saddle, saddle_steps)

        self.next_section("Invalidation")

        invalid_equation = MathTex(r"f'''_a(0) = 0", color=RED)
        invalid_equation.next_to(saddle_steps_group, DOWN)

        self.play(
            Write(invalid_equation)
        )
        self.wait()

        self.next_section("Solution_cross_out")

        cross = Cross(saddle_steps_group)

        self.play(
            Write(cross)
        )
        self.wait()

        self.next_section("Fadeout")

        self.play(
            FadeOut(comment_saddle),
            FadeOut(constraint_saddle),
            FadeOut(saddle_steps_group),
            FadeOut(cross),
            FadeOut(invalid_equation),

            FadeOut(comment_local_minimum),
            FadeOut(constraint_local_minimum),
            FadeOut(local_minimum_group),
            
            FadeOut(comment_local_maximum),
            FadeOut(constraint_local_maximum),
            FadeOut(local_maximum_group),

            FadeOut(equation_second_derivative),
            FadeOut(equation_second_derivative_insert),
        )

        groups = [saddle_steps_group, local_minimum_group, local_maximum_group]

        # Remove single steps from groups
        # they would reappear otherwise
        for g in groups:
            for step in g:
                self.remove(step)
    
    def solve_type_other(self):
        solution_x2 = MathTex(r"x_{2;3} = \pm \sqrt{0.2a}")
        solution_x2.move_to(self.solution)

        self.play(
            Transform(self.solution, solution_x2),
            run_time=0.5
        )
        self.wait()

        self.next_section("Prepare_solving")

        equation_second_derivative = MathTex(
            r"f''_a(x) = 12x^2 - 0.8a",
            substrings_to_isolate="a",
        )
        equation_second_derivative.set_color_by_tex("a", color=PURPLE)
        equation_second_derivative.next_to(self.solution, DOWN)

        comment_minimum = Tex("Tiefpunkt", color=YELLOW)
        comment_minimum.scale(0.6)
        comment_minimum.next_to(equation_second_derivative, DOWN)
        comment_minimum.shift(LEFT * 4)

        comment_saddle = Tex("Sattelpunkt", color=YELLOW)
        comment_saddle.scale(0.6)
        comment_saddle.next_to(equation_second_derivative, DOWN)
        comment_saddle.shift(RIGHT * 4)

        constraint_minimum = MathTex(
            r"f''_a(x) > 0",
            substrings_to_isolate="a",
        )
        constraint_minimum.set_color_by_tex("a", color=PURPLE)
        constraint_minimum.next_to(comment_minimum, DOWN)

        constraint_saddle = MathTex(
            r"f''_a(x) = 0",
            substrings_to_isolate="a",
        )
        constraint_saddle.set_color_by_tex("a", color=PURPLE)
        constraint_saddle.next_to(comment_saddle, DOWN)

        self.play(
            Write(equation_second_derivative),
            run_time=0.5,
        )
        self.play(
            Write(comment_minimum),
            run_time=0.5,
        )
        self.play(
            Write(constraint_minimum),
            run_time=0.5,
        )
        self.wait()

        self.next_section("Solve_Step")

        solve_steps_minimum = [
            r"12(\pm \sqrt{0.2a})^2 - 0.8a > 0",
            r"12(0.2a) - 0.8a > 0",
            r"2.4a - 0.8a > 0",
            r"1.6a > 0",
            r"a > 0",
        ]

        self.animate_solve_steps(constraint_minimum, solve_steps_minimum)

        self.next_section("Saddle")

        self.play(
            Write(comment_saddle),
            Write(constraint_saddle),
            run_time=0.5,
        )
        self.wait()

        self.next_section("Solve_Step")

        solve_steps_saddle = [
            r"a = 0",
            r"f'''_a(x) \neq 0",
            r"24x \neq 0",
            r"x \neq 0",
        ]

        saddle_steps_group = self.animate_solve_steps(constraint_saddle, solve_steps_saddle)

        self.next_section("Cross")

        saddle_solution = saddle_steps_group[-1]

        self.play(
            Indicate(self.solution),
            Indicate(saddle_solution),
            run_time=1,
        )

        cross = Cross(saddle_steps_group, color=RED)

        self.play(
            Write(cross)
        )
        self.wait()
