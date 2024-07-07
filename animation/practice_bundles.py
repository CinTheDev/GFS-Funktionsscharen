#!/usr/bin/env python

from generic_solve_blocks import *

class Practice_Bundles(GenericSolveBlocks):
    def construct(self):
        self.default_color = BLUE
        self.transition()
        self.write_all_problems()

        self.solve_first_problem()
        self.clear_blocks()

        self.solve_second_problem()
    
    def transition(self):
        self.next_section("Transition")
        page_num = Tex("Seite 163 Nummer 4")

        self.add(page_num)
        self.wait()

        self.next_section("Make_Space")

        page_num.generate_target()
        page_num.target.scale(0.4)
        page_num.target.move_to(LEFT * 6 + UP * 3.75)

        self.play(
            MoveToTarget(page_num),
            run_time=1,
        )
    
    def write_all_problems(self):
        all_problems = [
            r"f_r(x) = 2(x + 5) \cdot e^{rx}",
            r"f_t(x) = x e^{t(x - 2)} + 3",
        ]

        problem_text = Tex("Untersuche die Schar auf Funktionsbündel", color=BLUE)

        all_problems_tex = VGroup()

        for i in range(len(all_problems)):
            number = Tex(str(i) + ": ", color=BLUE)
            problem_tex = MathTex(all_problems[i])
            line = VGroup(number, problem_tex).arrange(RIGHT)
            all_problems_tex.add(line)
        
        all_problems_tex.arrange(DOWN, aligned_edge=LEFT)

        all_problems_block = VGroup(problem_text, all_problems_tex)
        all_problems_block.arrange(DOWN)

        self.play(
            FadeIn(problem_text, shift=UP),
            run_time=0.7,
        )
        self.play(
            LaggedStart(
                [Write(p) for p in all_problems_tex],
                lag_ratio=0.3,
                run_time=3,
            ),
        )

        steps = [
            r"f_a(x) = f_b(x); \:\: a \neq b",
        ]
        steps_block = self.block("Methode", DOWN * 2.5, steps, invincible=True)

        self.next_section("Clear_Problems")

        self.play(
            LaggedStart(
                [Unwrite(p) for p in all_problems_block],
                lag_ratio=0.3,
                run_time=3,
            ),
            Unwrite(steps_block)
        )

        self.heading = Tex("Lösungen", color=BLUE)
        self.heading.scale(0.6)
        self.heading.move_to(UP * 3.5)

        self.play(
            FadeIn(self.heading, shift=DOWN),
            run_time=0.7,
        )
    
    def solve_first_problem(self):
        steps_1 = [
            r"f_r(x) = 2(x + 5) \cdot e^{rx}",
            r"f_{0}(x) = f_1(x)",
            r"2(x + 5) = 2(x + 5) \cdot e^x",
            r"0 = 2(x + 5) \cdot e^x - 2(x + 5)",
            r"0 = 2(x + 5)(e^x - 1)",
        ]
        steps_2 = [
            r"0 = x_1 + 5",
            r"x_1 = -5",
            r"0 = e^{x_2} - 1",
            r"e^{x_2} = 1",
            r"x_2 = ln(1)",
            r"x_2 = 0",
        ]

        steps_ctrl = [
            r"f_r(-5) = 2(0) \cdot e^{-5r}",
            r"f_r(-5) = 0",
            r"f_r(0) = 2(5) \cdot 1",
            r"f_r(0) = 10",
        ]

        self.block("Auflösen", UP * 2, steps_1)
        self.block("Nullprodukt", UP * 2 + LEFT * 5, steps_2)
        self.block("Kontrolle", UP * 2 + RIGHT * 5, steps_ctrl, scale=0.8)
    
    def solve_second_problem(self):
        steps_1 = [
            r"f_t(x) = x e^{t(x - 2)} + 3",
            r"f_0(x) = f_1(x)",
            r"x e^0 + 3 = x e^{x - 2} + 3",
            r"x = x e^{x - 2}",
            r"0 = x e^{x - 2} - x",
            r"0 = x(e^{x - 2} - 1)",
        ]
        steps_2 = [
            r"x_1 = 0",
            r"0 = e^{x_2 - 2} - 1",
            r"x_2 - 2 = ln(1)",
            r"x_2 = 2",
        ]

        steps_ctrl = [
            r"f_t(0) = 3",
            r"f_t(2) = 2 e^{t(2 - 2)} + 3",
            r"f_t(2) = 2 + 3 = 5",
        ]

        self.block("Auflösen", UP * 2, steps_1)
        self.block("Nullprodukt", UP * 2 + LEFT * 5, steps_2)
        self.block("Kontrolle", UP * 2 + RIGHT * 4.75, steps_ctrl)
