#!/usr/bin/env python

from generic_solve_blocks import *

class LocusCalculation(GenericSolveBlocks):
    def construct(self):
        self.default_color=RED
        self.transition()

        self.solve_local_minimum()
        self.solve_height()
    
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

        self.block("Extremstelle bestimmen", LEFT * 4.25 + UP * 3.25, steps, scale=0.8)
    
    def solve_height(self):
        steps = [
            r"y = f_a(ln(\frac{a}{2}))",
            r"y = e^{2 ln(\frac{a}{2})} - a e^{ln(\frac{a}{2})}",
            r"y = (\frac{a}{2})^2 - a(\frac{a}{2})",
            r"y = \frac{a^2}{4} - \frac{a^2}{2}",
            r"y = -\frac{a^2}{4}",
        ]

        solution = [
            r"x = ln(\frac{a}{2})",
            r"y = -\frac{a^2}{4}",
        ]

        self.block("Tiefpunkt bestimmen", RIGHT * 4.25 + UP * 2.5, steps)
        self.block("Lösung ??", UP, solution)
