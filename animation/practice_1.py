#!/usr/bin/env python

from generic_solve_blocks import *

class Practice_1(GenericSolveBlocks):
    def construct(self):
        self.transition()
        self.write_all_problems()

        self.solve_first_problem()
        self.clear_blocks()

        self.solve_second_problem()
        self.clear_blocks()

        self.solve_third_problem()
        self.clear_blocks()

        self.write_integral_problem()
        self.solve_integral_problem()
    
    def transition(self):
        self.next_section("Transition")
        title = Tex("Zeit für Übung")

        self.add(title)
        self.wait()

        self.next_section("Prepare")

        self.page_num = Tex("Seite 163 Nummer 1")
        self.page_num.scale(0.4)
        self.page_num.move_to(LEFT * 6 + UP * 5)

        self.page_num.generate_target()
        self.page_num.target.move_to(LEFT * 6 + UP * 3.75)

        self.add(self.page_num)
        self.play(
            FadeOut(title),
            run_time=0.5,
        )
        self.play(
            MoveToTarget(self.page_num),
            run_time=0.5,
        )
    
    def write_all_problems(self):
        all_problems = [
            r"f_a(x) = x^2 - ax",
            r"f_a(x) = \frac{x^2 - a^2}{x}",
            r"f_a(x) = e^{\frac{x}{a}} - a",
        ]

        problem_text = Tex("Berechne die Nullpunkte der Funktionenschar.", color=YELLOW)

        all_problems_tex = VGroup(problem_text)

        for problem in all_problems:
            problem_tex = MathTex(problem)
            all_problems_tex.add(problem_tex)
        
        all_problems_tex.arrange(DOWN)

        self.play(
            FadeIn(problem_text, shift=UP),
            run_time=0.7,
        )
        self.play(
            LaggedStart(
                [Write(p) for p in all_problems_tex[1:]],
                lag_ratio=0.3,
                run_time=3,
            ),
        )
        self.wait()

        self.next_section("Clear_Problems")

        self.play(
            LaggedStart(
                [Unwrite(p) for p in all_problems_tex],
                lag_ratio=0.3,
                run_time=3,
            )
        )

        self.heading = Tex("Lösungen", color=YELLOW)
        self.heading.scale(0.6)
        self.heading.move_to(UP * 3.5)

        self.play(
            FadeIn(self.heading, shift=DOWN),
            run_time=0.7,
        )
    
    def solve_first_problem(self):
        steps = [
            r"f_a(x) = x^2 - ax",
            r"f_a(x) = 0",
            r"x^2 - ax = 0",
            r"x(x - a) = 0",
            r"x_1 = 0; x_2 = a"
        ]

        self.block("Erste Aufgabe", UP * 2, steps)

    def solve_second_problem(self):
        steps = [
            r"f_a(x) = \frac{x^2 - a^2}{x}",
            r"\frac{x^2 - a^2}{x} = 0",
            r"x^2 - a^2 = 0",
            r"x^2 = a^2",
            r"x_{1;2} = \pm a",
            r"x_{1;2} \neq 0",
        ]

        self.block("Zweite Aufgabe", UP * 2.5, steps, highlighted=[-1])
    
    def solve_third_problem(self):
        steps = [
            r"f_a(x) = e^{\frac{x}{a}} - a",
            r"e^{\frac{x}{a}} - a = 0",
            r"e^{\frac{x}{a}} = a",
            r"\frac{x}{a} = ln(a)",
            r"x = ln(a) \cdot a",
        ]

        self.block("Dritte Aufgabe", UP * 2, steps)
    
    def write_integral_problem(self):
        self.play(
            FadeOut(self.heading, shift=UP),
            FadeOut(self.page_num, shift=UP),
            run_time=0.5,
        )

        equation = MathTex(r"\int_0^{\frac{\pi}{a}} sin(ax) \, dx")

        comment = Tex("Löse das Integral", color=YELLOW)
        comment.scale(0.6)
        comment.next_to(equation, UP)

        self.play(
            Write(equation),
            run_time=0.5,
        )
        self.play(
            Write(comment),
            run_time=0.5,
        )
        self.wait()

        self.next_section("Integral_Move")

        equation.generate_target()
        equation.target.move_to(UP * 3)

        self.play(
            Unwrite(comment),
            run_time=0.5,
        )
        self.play(
            MoveToTarget(equation),
            run_time=0.5,
        )
        self.wait()
    
    def solve_integral_problem(self):
        steps = [
            r"= \left[ -\frac{1}{a} cos(ax) \right]_0^{\frac{\pi}{a}}",
            r"= (-\frac{1}{a} cos(a \cdot \frac{\pi}{a})) - (-\frac{1}{a} cos(a \cdot 0))",
            r"= -\frac{cos(\pi)}{a} + \frac{cos(0)}{a}",
            r"= \frac{1}{a}",
        ]

        self.block("Lösung", UP * 2, steps)
