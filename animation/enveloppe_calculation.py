#!/usr/bin/env python

from generic_solve_blocks import *

class EnveloppeCalculation(GenericSolveBlocks):
    def construct(self):
        self.default_color = PINK

        self.parametric()
        self.derive()
        self.solve_null()
    
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
        self.clear_blocks()
    
    def derive(self):
        begin = [
            r"f_\theta(x) = tan(\theta) x - (\frac{g}{2 v^2 \cdot cos^2(\theta)}) x^2",
            r"h_x(\theta) = f_\theta(x)",
        ]

        steps = [
            r"h_x(\theta) = tan(\theta) x - (\frac{g}{2 v^2 \cdot cos^2(\theta)}) x^2",
            r"h'_x(\theta) = \frac{1}{cos^2(\theta)} x - (-sin(\theta))(-2)(\frac{1}{cos^3(\theta)})(\frac{g}{2 v^2}) x^2",
            r"h'_x(\theta) = \frac{x}{cos^2(\theta)} - \frac{sin(\theta)}{cos^3(\theta)}(\frac{g x^2}{v^2})",
            r"h'_x(\theta) = \frac{x}{cos^2(\theta)} - \frac{tan(\theta)}{cos^2(\theta)}(\frac{g x^2}{v^2})",
        ]

        self.block("Variablen tauschen", UP * 3.5, begin, scale=0.8)
        self.block(r"Nach $ \theta $ ableiten", UP * 1.25, steps, scale=0.7)
        self.clear_blocks()
    
    def solve_null(self):
        steps = [
            r"h'_x(\theta) = \frac{x}{cos^2(\theta)} - \frac{tan(\theta)}{cos^2(\theta)}(\frac{g x^2}{v^2})",
            r"0 = \frac{x}{cos^2(\theta)} - \frac{tan(\theta)}{cos^2(\theta)}(\frac{g x^2}{v^2})",
            r"0 = x - tan(\theta)(\frac{g x^2}{v^2})",
            r"tan(\theta)(\frac{g x^2}{v^2}) = x",
            r"tan(\theta) = \frac{v^2}{g x}",
            r"\theta = tan^{-1}(\frac{v^2}{g x})",
        ]

        self.block(r"Nullsetzen \& nach $ \theta $ auflösen", UP * 3, steps, scale=0.7)
        self.clear_blocks()
