#!/usr/bin/env python

from generic_solve_blocks import *

class Practice_Locus(GenericSolveBlocks):
    def construct(self):
        self.default_color = RED
        self.transition()

        self.solve_first_problem()
        self.clear_blocks()

        self.solve_second_problem()
        self.clear_blocks()

        self.solve_third_problem()
    
    def transition(self):
        transition_title = Tex("Letzte Übungsphase", color=RED)

        self.add(transition_title)
        self.wait()

        self.next_section("Show_Problems")

        title = Tex("Bestimme die Ortskurve aller Tiefpunkte", color=RED)
        title.scale(0.6)

        all_problems = [
            r"f_a(x) = e^{x-a} - x",
            r"f_a(x) = e^x - ax",
            r"f_a(x) = e^x - a^2x; a \neq 0",
        ]

        all_problems_tex = VGroup()

        for i in range(len(all_problems)):
            number = Tex(str(i) + ": ", color=RED)
            problem_tex = MathTex(all_problems[i])
            line = VGroup(number, problem_tex).arrange(RIGHT)
            all_problems_tex.add(line)
        
        all_problems_tex.arrange(DOWN, aligned_edge=LEFT)

        all_problems_block = VGroup(title, all_problems_tex)
        all_problems_block.arrange(DOWN)

        self.play(
            Transform(transition_title, title, replace_mobject_with_target_in_scene=True),
            run_time=0.5,
        )
        self.play(
            LaggedStart(
                [Write(p) for p in all_problems_tex],
                lag_ratio=0.3,
                run_time=3,
            ),
        )
        self.wait()
        
        self.next_section("Clear_Problems")

        self.play(
            LaggedStart(
                [Unwrite(p) for p in all_problems_block],
                lag_ratio=0.3,
                run_time=3,
            )
        )

        self.heading = Tex("Lösungen", color=RED)
        self.heading.scale(0.6)
        self.heading.move_to(UP * 3.5)

        self.play(
            FadeIn(self.heading, shift=DOWN),
            run_time=0.7,
        )
    
    def solve_first_problem(self):
        solve_turning_point = [
            r"f_a(x) = e^{x-a} - x",
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
    
    def solve_second_problem(self):
        solve_turning_point = [
            r"f_a(x) = e^x - ax",
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
    
    def solve_third_problem(self):
        solve_turning_point = [
            r"f_a(x) = e^x - a^2x; a \neq 0",
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

        self.block("Extremstelle", UP * 2 + LEFT * 4.25, solve_turning_point)
        self.block("Tiefpunkt", UP * 2 + RIGHT * 1, solve_height)
        self.block("Nach a auflösen", UP * 1.5 + RIGHT * 5, solve_a_x)
        self.block("Einsetzen", RIGHT * 5 + DOWN * 1.5, solve_function)
