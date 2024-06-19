#!/usr/bin/env python

from generic_solve_blocks import *

class AnalysisExponential(GenericSolveBlocks):
    def construct(self):
        self.transition()
        self.write_derivatives()
        self.solve_x()
        self.solve_y()
        self.solve_minimum()
        self.solve_maximum()
        self.solve_saddle_points()
        # TODO: Visualize solutions on graph
    
    def transition(self):
        self.next_section("Transition")
        title = Tex("2. Analysis-Beispiel", color=YELLOW)

        self.play(
            Write(title),
            run_time=1
        )
        self.wait()

        self.next_section("Make_Room")

        title.generate_target()
        title.target.move_to(UP * 3)

        self.play(
            MoveToTarget(title),
            run_time=1
        )
        self.wait()
    
    def write_derivatives(self):
        equations = [
            r"f_b(x) = e^x - bx",
            r"f'_b(x) = e^x - b",
            r"f''_b(x) = e^x",
        ]

        self.block(r"Funktion \& Ableitungen", UP * 2, equations, colored_var="b")
    
    def solve_x(self):
        steps = [
            r"f'_b(x) = 0",
            r"e^x - b = 0",
            r"e^x = b",
            r"x = ln(b)",
            r"b > 0",
        ]

        self.block("Extremstellen", UP * 3 + LEFT * 4.5, steps, colored_var="b", highlighted=[-1])
    
    def solve_y(self):
        steps = [
            r"y = f_b(ln(b))",
            r"y = e^{ln(b)} - b ln(b)",
            r"y = b - b ln(b)",
            r"y = b (1 - ln(b))",
            r"E(ln(b) | b(1 - ln(b)))",
        ]

        self.block("Extrempunkte", UP * 3 + RIGHT * 4.5, steps, colored_var="b", scale=0.8)
    
    def solve_minimum(self):
        steps = [
            r"f''_b(ln(b)) > 0",
            r"e^{ln(b)} > 0",
            r"b > 0",
        ]

        self.block("Tiefpunkte", DOWN * 1 + LEFT * 4.5, steps, colored_var="b")
    
    def solve_maximum(self):
        steps = [
            r"f''_b(ln(b)) < 0",
            r"e^{ln(b)} < 0",
            r"b < 0",
        ]

        self.block("Hochpunkte", DOWN * 1, steps, colored_var="b", highlighted=[-1], wrong=True)
    
    def solve_saddle_points(self):
        steps = [
            r"f''_b(ln(b)) = 0",
            r"e^{ln(b)} = 0",
            r"b = 0",
        ]

        self.block("Sattelpunkte", DOWN * 1 + RIGHT * 4.5, steps, colored_var="b", highlighted=[-1], wrong=True)
