#!/usr/bin/env python

from generic_solve_blocks import *

class Practice_Locus(GenericSolveBlocks):
    def construct(self):
        self.default_color = RED
        self.transition()

        self.introduce_first_problem()
        self.solve_first_problem()
    
    def transition(self):
        title = Tex("Bestimme die Ortskurve aller Tiefpunkte", color=RED)
        title.scale(0.6)
        title.move_to(UP * 3.5)

        self.add(title)
    
    def introduce_first_problem(self):
        equation = MathTex(r"f_a(x) = e^{x-a} - x")
        self.blocks.append(equation)

        self.play(
            Write(equation),
            run_time=1,
        )
        self.wait()

        self.next_section("Make_room")

        equation.generate_target()
        equation.target.scale(0.8)
        equation.target.move_to(UP * 3)

        self.play(
            MoveToTarget(equation),
            run_time=1
        )
    
    def solve_first_problem(self):
        solve_turning_point = [
            r"f'_a(x) = (1)e^{x-a} - 1",
            r"e^{x-a} - 1 = 0",
            r"e^{x-a} = 1",
            r"x - a = 0",
            r"x = a",
        ]
        solve_height = [
            r"y = f_a(a)",
            r"y = e^{a-a} - a",
            r"y = 1 - a",
        ]
        solve_finally = [
            r"y = 1 - x",
        ]

        self.block("Extremstelle", UP * 2 + LEFT * 4, solve_turning_point)
        self.block("Tiefpunkt", UP * 2, solve_height)
        self.block("Umwandeln", UP * 2 + RIGHT * 4, solve_finally)
