#!/usr/bin/env python

from generic_solve_blocks import *

class Practice_Bundles(GenericSolveBlocks):
    def construct(self):
        self.default_color = BLUE
        self.transition()

        self.write_first_problem()
        self.solve_first_problem()
    
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
    
    def write_first_problem(self):
        equation = MathTex(r"f_r(x) = 2(x + 5) \cdot e^{rx}")
        self.blocks.append(VGroup(equation))

        self.play(
            Write(equation),
            run_time=1,
        )
        self.wait()

        self.next_section("Move_Aside")

        equation.generate_target()
        equation.target.move_to(UP * 3)

        self.play(
            MoveToTarget(equation),
            run_time=0.5,
        )
    
    def solve_first_problem(self):
        steps_1 = [
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

        self.block("Auflösen", UP * 2, steps_1)
        self.block("Nullprodukt", UP * 2 + RIGHT * 5, steps_2)
