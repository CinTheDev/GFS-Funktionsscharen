#!/usr/bin/env python

from generic_solve_blocks import *

class Practice_1(GenericSolveBlocks):
    def construct(self):
        self.transition()

        self.write_first_problem()
        self.solve_first_problem()
        self.clear_blocks()

        self.write_second_problem()
        self.solve_second_problem()
        self.clear_blocks()

        self.write_third_problem()
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
    
    def write_first_problem(self):
        self.equation = MathTex(r"f_a(x) = x^2 - ax")

        comment = Tex("Berechne die Nullpunkte der Funktionenschar.", color=YELLOW)
        comment.scale(0.6)
        comment.next_to(self.equation, UP)

        self.play(
            Write(self.equation),
            FadeIn(comment, shift=UP),
            run_time=0.7,
        )
        self.wait()

        self.next_section("Make_Room")

        self.equation.generate_target()
        self.equation.target.move_to(UP * 3)

        self.play(
            FadeOut(comment),
            run_time=0.5,
        )
        self.play(
            MoveToTarget(self.equation),
            run_time=0.5,
        )
        self.wait()
    
    def solve_first_problem(self):
        steps = [
            r"f_a(x) = 0",
            r"x^2 - ax = 0",
            r"x(x - a) = 0",
            r"x_1 = 0; x_2 = a"
        ]

        self.block("Lösung", UP * 2, steps)
    
    def write_second_problem(self):
        self.play(
            Unwrite(self.equation),
            run_time=0.5,
        )

        new_equation = MathTex(r"f_a(x) = \frac{x^2 - a^2}{x}")
        new_equation.move_to(self.equation)
        self.equation.become(new_equation)

        self.play(
            Write(self.equation),
            run_time=0.5,
        )
        self.wait()

    def solve_second_problem(self):
        steps = [
            r"\frac{x^2 - a^2}{x} = 0",
            r"x^2 - a^2 = 0",
            r"x^2 = a^2",
            r"x_{1;2} = \pm a",
            r"x_{1;2} \neq 0",
        ]

        self.block("Lösung", UP * 2, steps, highlighted=[-1])
    
    def write_third_problem(self):
        self.play(
            Unwrite(self.equation),
            run_time=0.5,
        )

        new_equation = MathTex(r"f_a(x) = e^{\frac{x}{a}} - a")
        new_equation.move_to(self.equation)
        self.equation.become(new_equation)

        self.play(
            Write(self.equation),
            run_time=0.5,
        )
        self.wait()
    
    def solve_third_problem(self):
        steps = [
            r"e^{\frac{x}{a}} - a = 0",
            r"e^{\frac{x}{a}} = a",
            r"\frac{x}{a} = ln(a)",
            r"x = ln(a) \cdot a",
        ]

        self.block("Lösung", UP * 2, steps)
    
    def write_integral_problem(self):
        self.play(
            Unwrite(self.equation),
            FadeOut(self.page_num, shift=UP),
            run_time=0.5,
        )

        new_equation = MathTex(r"\int_0^a cos(ax) \, dx")
        self.equation.become(new_equation)

        comment = Tex("Löse das Integral", color=YELLOW)
        comment.scale(0.6)
        comment.next_to(new_equation, UP)

        self.play(
            Write(self.equation),
            run_time=0.5,
        )
        self.play(
            Write(comment),
            run_time=0.5,
        )
        self.wait()

        self.next_section("Integral_Move")

        self.equation.generate_target()
        self.equation.target.move_to(UP * 3)

        self.play(
            Unwrite(comment),
            run_time=0.5,
        )
        self.play(
            MoveToTarget(self.equation),
            run_time=0.5,
        )
        self.wait()
    
    def solve_integral_problem(self):
        steps = [
            r"\left[ \frac{1}{a} sin(ax) \right]_0^a",
            r"(\frac{1}{a} sin(a \cdot a)) - (\frac{1}{a} sin(a \cdot 0))",
            r"\frac{sin(a^2)}{a} - \frac{0}{a}",
            r"\frac{sin(a^2)}{a}",
        ]

        self.block("Lösung", UP * 2, steps)
