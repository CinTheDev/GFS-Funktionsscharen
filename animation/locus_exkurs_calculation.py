#!/usr/bin/env python

from generic_solve_blocks import *

class LocusExkursCalculation(GenericSolveBlocks):
    def construct(self):
        self.default_color = RED

        self.introduce_first_example()
        self.first_example_solve_x()
        self.first_example_insert()
        self.clear_blocks()

        self.introduce_second_example()
        self.second_example_solve_x()
        self.second_example_insert()
        self.second_example_show_graph()
    
    def introduce_first_example(self):
        functions = [
            r"x(a) = 3a",
            r"y(a) = a^2",
        ]

        self.block("Funktion", UP * 3, functions)

    def first_example_solve_x(self):
        steps = [
            r"x = 3a",
            r"a = \frac{1}{3} x",
        ]

        self.block("x-Teil nach a auflösen", UP * 2 + LEFT * 4, steps)
    
    def first_example_insert(self):
        steps = [
            r"y = a^2",
            r"y = (\frac{1}{3} x)^2",
            r"y = \frac{1}{6} x^2",
        ]

        self.block("In y-Teil einsetzen", UP * 2 + RIGHT * 4, steps)
    
    def introduce_second_example(self):
        functions = [
            r"x(a) = cos(a)",
            r"y(a) = sin(a)",
        ]

        self.block("Funktion", UP * 3, functions)
    
    def second_example_solve_x(self):
        steps = [
            r"x = cos(a)",
            r"a = cos^{-1}(x)",
        ]

        self.block("x-Teil nach a auflösen", UP * 2 + LEFT * 4, steps)
    
    def second_example_insert(self):
        steps = [
            r"y = sin(a)",
            r"y = sin(cos^{-1}(a))",
        ]

        self.block("In y-Teil einsetzen", UP * 2 + RIGHT * 4, steps)
    
    def second_example_show_graph(self):
        pass
