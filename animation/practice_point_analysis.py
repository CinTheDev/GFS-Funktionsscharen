#!/usr/bin/env python

from generic_solve_blocks import *

class PracticePointAnalysis(GenericSolveBlocks):
    def construct(self):
        self.default_color = ORANGE

        self.write_steps()
        self.introduce_problems()

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
        #title.move_to(UP * 3)

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
        self.wait()
