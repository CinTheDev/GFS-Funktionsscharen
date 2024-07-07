#!/usr/bin/env python

from generic_solve_blocks import *

class EnveloppeCalculation(GenericSolveBlocks):
    def construct(self):
        self.default_color = PINK

        self.parametric()
    
    def parametric(self):
        equations_parametric = [
            r"x(t) = v \cdot cos(\theta) \cdot t",
            r"y(t) = -0.5 g t^2 + v \cdot sin(\theta) \cdot t",
        ]

        steps = [
            r"x = v \cdot cos(\theta) t",
            r"t = \frac{x}{v \cdot cos(\theta)}",
            r"f_\theta(x) = y = -0.5 g (\frac{x}{v \cdot cos(\theta)})^2 + v \cdot sin(\theta) \frac{x}{x \cdot cos(\theta)}",
            r"f_\theta(x) = \frac{v \cdot sin(\theta) x}{v \cdot cos(\theta)} - \frac{g x^2}{2 v^2 \cdot cos^2(\theta)}",
            r"f_\theta(x) = tan(\theta) x - (\frac{g}{2 v^2 \cdot cos^2(\theta)}) x^2",
        ]

        self.block("Funktion (Parameterisiert)", UP * 3.5, equations_parametric, scale=0.8)
        self.block("Funktion (hergeleitet)", UP * 1.5, steps, scale=0.7)
