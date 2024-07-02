#!/usr/bin/env python

from generic_solve_blocks import *

class LocusCalculation(GenericSolveBlocks):
    def construct(self):
        self.transition()

        self.solve_local_minimum()
    
    def transition(self):
        self.next_section("Setup")
        equation = MathTex(r"f_a(x) = e^{2x} - a e^x")
        equation.move_to(UP * 3)

        self.blocks.append(equation)

        self.add(equation)
        self.wait()
    
    def solve_local_minimum(self):
        steps = [
            r"f'_a(x) = 2e^{2x} - ae^x",
            r"2e^{2x} - ae^x = 0",
            r"2e^{2x} = ae^x",
            r"e^{2x} = \frac{a}{2} \cdot e^x",
            r"2x = ln(\frac{a}{2} \cdot e^x)",
            r"2x = ln(\frac{a}{2}) + ln(e^x)",
            r"2x = ln(\frac{a}{2}) + x",
            r"x = ln(\frac{a}{2})",
        ]

        self.block("Extremstelle bestimmen", LEFT * 4.25 + UP * 3, steps, scale=0.8)
