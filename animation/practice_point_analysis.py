#!/usr/bin/env python

from generic_solve_blocks import *

class PracticePointAnalysis(GenericSolveBlocks):
    def construct(self):
        self.write_steps()

    def write_steps(self):
        steps = [
            r"1. Extremstelle herausfinden",
            r"2. $ x $ in $ f_a(x) $ einsetzen",
            r"\raggedright 3. Neue Funktion auf \\ \:\:\:\: Extremstellen überprüfen",
        ]

        self.block("Schritte", LEFT * 6 + UP * 3, steps, scale=0.6, invincible=True, math=False, aligned_edge=LEFT)

