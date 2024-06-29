#!/usr/bin/env python

from generic_solve_blocks import *

class PracticePointAnalysis(GenericSolveBlocks):
    def construct(self):
        self.default_color = ORANGE

        self.write_steps()
        self.introduce_problems()

        self.introduce_first_problem()
        self.solve_first_problem()

    def write_steps(self):
        steps = [
            r"1. Extremstelle herausfinden",
            r"2. $ x $ in $ f_a(x) $ einsetzen",
            r"\raggedright 3. Neue Funktion auf \\ \:\:\:\: Extremstellen überprüfen",
        ]

        self.block("Schritte", LEFT * 6 + UP * 3, steps, scale=0.6, invincible=True, math=False, aligned_edge=LEFT)
    
    def introduce_problems(self):
        self.title = Tex(
            r"Die Funktion $ f_t(x) $ hat einen Tiefpunkt."
            r"\\ Finde den Wert für $ t $, für welchen dieser am tiefsten liegt.",

            color=ORANGE,
        )
        self.title.scale(0.8)

        self.page_num = Tex("Seite Nummer 164 Nummer 11")
        self.page_num.scale(0.4)
        self.page_num.move_to(LEFT * 5 + UP * 3.75)

        self.next_section("Introduce_Problem")

        self.play(
            Write(self.title),
            FadeIn(self.page_num, shift=DOWN),
            run_time=1,
        )
        self.wait()

        self.next_section("Make room")

        self.title.generate_target()
        self.title.target.scale(0.5)
        self.title.target.move_to(UP * 3.5)

        self.play(
            MoveToTarget(self.title),
            run_time=1,
        )
    
    def introduce_first_problem(self):
        equation = MathTex(r"f_t(x) = x^2 - tx + 4t^2 - 3t")
        self.blocks.append(equation)

        self.play(
            Write(equation),
            run_time=0.5,
        )
        self.wait()

        self.next_section("Move_equation")

        equation.generate_target()
        equation.target.move_to(UP * 1.5)
        equation.target.scale(0.8)

        self.play(
            MoveToTarget(equation),
            run_time=1,
        )
        self.wait()
    
    def solve_first_problem(self):
        steps_solve_first = [
            r"f'_t(x) = 2x - t",
            r"2x - t = 0",
            r"2x = t",
            r"x = 0.5t",
        ]
        steps_create_function = [
            r"g(t) = f_t(0.5t)",
            r"g(t) = (0.5t)^2 - t(0.5t) + 4t^2 - 3t",
            r"g(t) = 0.25t^2 - 0.5t^2 + 4t^2 - 3t",
            r"g(t) = 3.75t^2 - 3t",
        ]
        steps_solve_second = [
            r"g'(t) = 7.5t - 3",
            r"7.5t - 3 = 0",
            r"7.5t = 3",
            r"t = 0.4",
        ]

        self.block("Extremstellen von f", RIGHT * 5 + UP * 2, steps_solve_first)
        self.block("Höhenfunktion der Extremstelle", LEFT * 3, steps_create_function)
        self.block("Extremstellen der Höhenfunktion", RIGHT * 4.25 + DOWN * 1.1, steps_solve_second)
