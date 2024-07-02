#!/usr/bin/env python

from generic_solve_blocks import *

class Practice_Locus(GenericSolveBlocks):
    def construct(self):
        self.default_color = RED
        self.transition()

        self.introduce_first_problem()
        self.solve_first_problem()
        self.clear_blocks()

        self.introduce_second_problem()
        self.solve_second_problem()
        self.clear_blocks()

        self.introduce_third_problem()
        self.solve_third_problem()
    
    def transition(self):
        # TODO: Better transition
        title = Tex("Bestimme die Ortskurve aller Tiefpunkte", color=RED)
        title.scale(0.6)
        title.move_to(UP * 3.5)

        self.add(title)
    
    def introduce_first_problem(self):
        equation = MathTex(r"f_a(x) = e^{x-a} - x")
        self.blocks.append(equation)

        page_num = Tex("Seite 165 Nummer 19")
        page_num.scale(0.4)
        page_num.move_to(LEFT * 5 + UP * 3.75)

        self.play(
            Write(equation),
            FadeIn(page_num, shift=DOWN),
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
    
    def introduce_second_problem(self):
        equation = MathTex(r"f_a(x) = e^x - ax")
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
    
    def solve_second_problem(self):
        solve_turning_point = [
            r"f'_a(x) = e^x - a",
            r"e^x - a = 0",
            r"e^x = a",
            r"x = ln(a)",
        ]
        solve_height = [
            r"y = f_a(ln(a))",
            r"y = e^{ln(a)} - ln(a) a",
            r"y = a - ln(a) a",
        ]
        solve_a_x = [
            r"x = ln(a)",
            r"a = e^x",
        ]
        solve_function = [
            r"y = e^x - ln(e^x) e^x",
            r"y = e^x - x e^x",
        ]

        self.block("Extremstelle", UP * 2 + LEFT * 5, solve_turning_point)
        self.block("Tiefpunkt", UP * 2, solve_height)
        self.block("Nach a auflösen", UP * 2 + RIGHT * 5, solve_a_x)
        self.block("Einsetzen", RIGHT * 5, solve_function)
    
    def introduce_third_problem(self):
        equation = MathTex(r"f_a(x) = e^x - a^2x; a \neq 0")
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
    
    def solve_third_problem(self):
        solve_turning_point = [
            r"f'_a(x) = e^x - a^2",
            r"e^x - a^2 = 0",
            r"e^x = a^2",
            r"x = ln(a^2)",
        ]
        solve_height = [
            r"y = f_a(ln(a^2))",
            r"y = e^{ln(a^2)} - ln(a^2) a^2",
            r"y = a^2 - ln(a^2) a^2",
        ]
        solve_a_x = [
            r"x = ln(a^2)",
            r"a^2 = e^x",
        ]
        solve_function = [
            r"y = e^x - ln(e^x) e^x",
            r"y = e^x - x e^x",
        ]

        self.block("Extremstelle", UP * 2 + LEFT * 5, solve_turning_point)
        self.block("Tiefpunkt", UP * 2, solve_height)
        self.block("Nach a auflösen", UP * 2 + RIGHT * 5, solve_a_x)
        self.block("Einsetzen", RIGHT * 5, solve_function)
