#!/usr/bin/env python

from generic_solve_blocks import *

class Practice_1(GenericSolveBlocks):
    def construct(self):
        self.transition()
        self.write_problem()
        self.solve_problem()
    
    def transition(self):
        self.next_section("Transition")
        title = Tex("Zeit für Übung")

        self.add(title)
        self.wait()

        self.next_section("Prepare")

        page_num = Tex("Seite 163 Nummer 1")
        page_num.scale(0.4)
        page_num.move_to(LEFT * 6 + UP * 5)

        page_num.generate_target()
        page_num.target.move_to(LEFT * 6 + UP * 3.75)

        self.add(page_num)
        self.play(
            FadeOut(title),
            run_time=0.5,
        )
        self.play(
            MoveToTarget(page_num),
            run_time=0.5,
        )
        #self.wait()
    
    def write_problem(self):
        #self.next_section("Write_problem")

        equation = MathTex(r"f_a(x) = x^2 - ax")

        comment = Tex("Berechne die Nullpunkte der Funktionenschar.", color=YELLOW)
        comment.scale(0.6)
        comment.next_to(equation, UP)

        self.play(
            Write(equation),
            FadeIn(comment, shift=UP),
            run_time=0.7,
        )
        self.wait()

        self.next_section("Make_Room")

        equation.generate_target()
        equation.target.move_to(UP * 3)

        self.play(
            FadeOut(comment),
            run_time=0.5,
        )
        self.play(
            MoveToTarget(equation),
            run_time=0.5,
        )
        self.wait()
    
    def solve_problem(self):
        steps = [
            r"f_a(x) = 0",
            r"x^2 - ax = 0",
            r"x^2 = ax",
            r"x = a",
        ]

        self.block("Lösung", UP * 2, steps)
