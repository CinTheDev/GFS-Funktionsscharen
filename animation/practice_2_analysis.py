#!/usr/bin/env python

from generic_solve_blocks import *

class Practice_2(GenericSolveBlocks):
    def construct(self):
        self.transition()

        self.introduce_problem()

        self.solve_nullstellen()
        self.clear_blocks()

        self.solve_turning_points()
        self.clear_blocks()
        
        self.solve_inflection_points()
        self.clear_blocks()
    
    def transition(self):
        self.next_section("Transition")
        title = Tex("Ok, jetzt machen wir eine vollständige Analyse")

        self.add(title)
        self.wait()

        self.next_section("Prepare")

        self.play(
            Unwrite(title),
            run_time=0.5,
        )
    
    def introduce_problem(self):
        equation = MathTex(r"f_a(x) = x^3 - ax^2")

        comment = Tex("Vollständige Analyse der Funktion, also:", color=YELLOW)
        comment.scale(0.6)

        subcomments = [
            Tex("- Nullpunkte herausfinden", color=YELLOW).scale(0.5),
            Tex("- Extrempunkte bestimmen (auch die Art)", color=YELLOW).scale(0.5),
            Tex("- Wendepunkte bestimmen (ohne Krümmung)", color=YELLOW).scale(0.5),
        ]

        comment_group = VGroup(comment, *subcomments)
        comment_group.arrange(DOWN, aligned_edge=LEFT)
        comment_group.next_to(equation, DOWN)

        self.play(
            Write(equation),
            run_time=0.5,
        )
        self.play(
            LaggedStart(
                [Write(c) for c in comment_group],
                lag_ratio=0.5,
                run_time=5,
            )
        )
        self.wait()

        self.next_section("Make_Room")

        functions = [
            r"f_a(x) = x^3 - ax^2",
            r"f'_a(x) = 3x^2 - 2ax",
            r"f''_a(x) = 6x - 2a",
            r"f'''_a(x) = 6",
        ]

        self.play(
            Unwrite(comment_group),
            Unwrite(equation),
            run_time=0.5,
        )

        self.block(r"Funktionen \& Ableitungen", LEFT * 5 + UP * 3.25, functions, scale=0.8, invincible=True)
    
    def solve_nullstellen(self):
        self.nullstellen_solve()
    
    def nullstellen_solve(self):
        steps = [
            r"f_a(x) = 0",
            r"x^3 - ax^2 = 0",
            r"x^2(x - a) = 0",
            r"x_1 = 0; x_2 = a",
        ]

        self.block("Nullstellen", UP * 2 + RIGHT * 2, steps)
    
    def solve_turning_points(self):
        pass
    
    def solve_inflection_points(self):
        pass
