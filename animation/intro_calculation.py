#!/usr/bin/env python

from manim import *

class IntroCalculation(Scene):
    def construct(self):
        self.transition()
        # TODO: Better function names
        self.first_option()
        self.second_option()
    
    def transition(self):
        self.next_section("Transition_Title")
        self.clear()

        title = Tex("Aber wie rechnet man mit sowas?")

        self.add(title)
        self.wait()

        self.next_section("Transition_Fadeout")

        self.play(
            FadeOut(title)
        )
    
    def first_option(self):
        title = Tex("1. Fall: Wert für a einsetzen", color=YELLOW)

        self.play(
            Write(title)
        )
        self.wait()

        self.next_section("First_Option_Example")

        # Move text to upper edge of screen
        title.generate_target()
        title.target.move_to(UP * 3)

        self.play(
            MoveToTarget(title)
        )

        # Write the equation
        equation = MathTex(
            r"f_a(x) = x^4 - 0.4ax^2",
            substrings_to_isolate="a",
        )
        equation.set_color_by_tex("a", color=PURPLE)

        self.play(
            Write(equation),
            run_time=0.5,
        )
        self.wait()

        self.next_section("Parameter_Assignment")

        parameter_equation = MathTex(
            r"a = 3",
            substrings_to_isolate="a",
        )
        parameter_equation.set_color_by_tex("a", color=PURPLE)
        parameter_equation.next_to(equation, DOWN)

        parameter_equation_invisible = parameter_equation.copy()
        parameter_equation_invisible.set_opacity(0)
        parameter_equation_invisible.move_to(equation)

        self.add(parameter_equation_invisible)
        self.play(
            FadeTransform(parameter_equation_invisible, parameter_equation, replace_mobject_with_target_in_scene=True),
            run_time=0.5,
        )
        self.wait()

        self.next_section("Parameter_Evaluation")

        # TODO: Improve animation (it kinda looks confusing; it should only transform changed parts)
        # TODO: Color the "3" purple
        equation_inserted = MathTex(r"f_3(x) = x^4 - 0.4(3)x^2")

        self.play(
            Transform(equation, equation_inserted),
        )
        self.wait()

        self.next_section("Parameter_Evaluation_solve")

        # TODO: Same as above
        equation_solved = MathTex(r"f_3(x) = x^4 - 1.2x^2")

        self.play(
            Transform(equation, equation_solved),
        )
        self.wait()

        self.next_section("Fadeout")

        self.play(
            FadeOut(equation),
            FadeOut(parameter_equation),
            FadeOut(title),
        )
    
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

    def second_option(self):
        title = Tex("2. Fall: Extrempunkte", color=YELLOW)

        self.play(
            Write(title)
        )
        self.wait()

        self.next_section("Turning_Point_Example")

        # Move title out of way

        title.generate_target()
        title.target.move_to(UP * 3)

        self.play(
            MoveToTarget(title),
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

        self.next_section("Secondary_Equation")

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
            r"0 = 4x^2 - 0.8a",
            r"0.8a = 4x^2",
            r"0.2a = x^2",
            r"\pm \sqrt{0.2a} = x_{2;3}",
        ]

        steps_secondary = self.animate_solve_steps(equation_secondary, solve_steps_secondary)

