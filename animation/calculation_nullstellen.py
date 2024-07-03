#!/usr/bin/env python

from manim import *

class CalculationNullstellen(Scene):
    def construct(self):
        self.solve_x()
    
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

            self.next_section("Solve_Step")
            self.play(
                Write(step_tex),
                run_time=0.5,
            )
            self.wait()

            steps.add(step_tex)
            old_position = step_tex
        
        return steps
    
    def solve_x(self):
        self.next_section("Intro")
        title = Tex("2. Fall: Nullstellen", color=YELLOW)

        self.play(
            Write(title)
        )
        self.wait()

        self.next_section("Setup")

        title.generate_target()
        title.target.move_to(UP * 3)

        self.play(
            MoveToTarget(title)
        )

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

        self.next_section("Comment")

        comment = Tex("Wir wollen Nullstellen herausfinden", color=YELLOW)
        comment.scale(0.6)
        comment.next_to(equation, UP)

        self.play(
            Write(comment)
        )
        self.wait()

        self.next_section("Start_Solving")

        equation.generate_target()
        equation.target.move_to(UP * 2)

        self.play(
            FadeOut(comment),
            run_time=0.5,
        )
        self.play(
            MoveToTarget(equation),
            run_time=0.5,
        )
        self.wait()

        # steps solving

        solve_steps_1 = [
            r"f_a(x) = 0",
            r"x^4 - 0.4ax^2 = 0",
            r"x^2(x^2 - 0.4a) = 0",
            r"x_1 = 0; x_{2;3} = ...",
        ]
        solve_steps_2 = [
            r"x^2 = 0.4a",
            r"x_{2;3} = \pm \sqrt{0.4a}",
        ]

        steps = self.animate_solve_steps(equation, solve_steps_1)
        
        self.next_section("Move_steps")
        steps.generate_target()
        steps.target.shift(LEFT * 4)

        self.play(
            MoveToTarget(steps),
            run_time=1,
        )

        equation_2 = MathTex(r"x^2 - 0.4a = 0", substrings_to_isolate="a")
        equation_2.set_color_by_tex("a", color=PURPLE)
        equation_2.move_to(UP * 2 + RIGHT * 4)

        self.play(
            Write(equation_2),
            run_time=1,
        )

        steps_2 = self.animate_solve_steps(equation_2, solve_steps_2)
