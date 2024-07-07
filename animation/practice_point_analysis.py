#!/usr/bin/env python

from generic_solve_blocks import *

class PracticePointAnalysis(GenericSolveBlocks):
    def construct(self):
        self.default_color = ORANGE

        self.write_steps()
        self.introduce_problems()

        self.introduce_first_problem()
        self.solve_first_problem()
        self.clear_blocks()

        self.introduce_second_problem()
        self.solve_second_problem()

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

        all_problems = [
            r"f_t(x) = x^2 - tx + 4t^2 - 3t",
            r"f_t(x) = x^2 - 8x + 20 + t^2 + 6t",
        ]

        all_problems_tex = VGroup()

        for i in range(len(all_problems)):
            number = Tex(str(i) + ": ", color=ORANGE)
            problem_tex = MathTex(all_problems[i])
            line = VGroup(number, problem_tex).arrange(RIGHT)
            all_problems_tex.add(line)
        
        all_problems_tex.arrange(DOWN)

        all_problems_block = VGroup(self.title, all_problems_tex)
        all_problems_block.arrange(DOWN)
        all_problems_block.shift(DOWN)

        self.play(
            Write(self.title),
            FadeIn(self.page_num, shift=DOWN),
            run_time=1,
        )

        self.play(
            LaggedStart(
                [Write(p) for p in all_problems_tex],
                lag_ratio=0.3,
                run_time=3,
            )
        )
        self.wait()

        self.next_section("Make_room")

        self.title.generate_target()
        self.title.target.scale(0.5)
        self.title.target.move_to(UP * 3.5)

        self.play(
            MoveToTarget(self.title),
            Unwrite(all_problems_tex),
            run_time=1,
        )
    
    def introduce_first_problem(self):
        equation = MathTex(r"f_t(x) = x^2 - tx + 4t^2 - 3t")
        equation.scale(0.8)
        equation.move_to(UP * 1.5)

        self.blocks.append(equation)

        self.play(
            Write(equation),
            run_time=0.5,
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
    
    def introduce_second_problem(self):
        equation = MathTex(r"f_t(x) = x^2 - 8x + 20 + t^2 + 6t")
        equation.scale(0.8)
        equation.move_to(UP * 1.5)

        self.blocks.append(equation)

        self.play(
            Write(equation),
            run_time=0.5,
        )
        self.wait()
    
    def solve_second_problem(self):
        steps_solve_first = [
            r"f'_t(x) = 2x - 8",
            r"2x - 8 = 0",
            r"2x = 8",
            r"x = 4",
        ]
        steps_create_function = [
            r"g(t) = f_t(4)",
            r"g(t) = 4^2 - 8(4) + 20 + t^2 + 6t",
            r"g(t) = 16 - 32 + 20 + t^2 + 6t",
            r"g(t) = t^2 + 6t + 4",
        ]
        steps_solve_second = [
            r"g'(t) = 2t + 6",
            r"2t + 6 = 0",
            r"2t = -6",
            r"t = -3",
        ]

        self.block("Extremstellen von f", RIGHT * 5 + UP * 2, steps_solve_first)
        self.block("Höhenfunktion der Extremstelle", LEFT * 3, steps_create_function)
        self.block("Extremstellen der Höhenfunktion", RIGHT * 4.25 + DOWN * 1.1, steps_solve_second)
