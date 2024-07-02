#!/usr/bin/env python

from generic_solve_blocks import *

class LocusCalculation(GenericSolveBlocks):
    def construct(self):
        self.transition()
    
    def transition(self):
        self.next_section("Setup")
        equation = MathTex(r"f_a(x) = e^{2x} - a e^x")
        equation.move_to(UP * 3)

        self.add(equation)
        self.wait()
