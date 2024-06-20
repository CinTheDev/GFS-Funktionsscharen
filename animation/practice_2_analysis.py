#!/usr/bin/env python

from generic_solve_blocks import *

class Practice_2(GenericSolveBlocks):
    def construct(self):
        self.transition()

        self.introduce_problem()
    
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

        equation.generate_target()
        equation.target.scale(0.8)
        equation.target.move_to(LEFT * 5 + UP * 3.25)

        self.play(
            Unwrite(comment_group),
            run_time=0.5,
        )
        self.play(
            MoveToTarget(equation),
            run_time=1,
        )
        self.wait()
