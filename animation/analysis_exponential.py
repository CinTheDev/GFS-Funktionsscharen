#!/usr/bin/env python

from manim import *

class AnalysisExponential(Scene):
    def construct(self):
        self.transition()
        self.write_derivatives()
        self.solve_x()
        self.solve_y()
        self.solve_minimum()
        self.solve_maximum()
        self.solve_saddle_points()
    
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
    
    def construct_equations(self, tex_strings, top_equation, scale=1):
        all_equations = VGroup(top_equation)

        for string in tex_strings:
            tex = MathTex(
                string,
                substrings_to_isolate="b"
            )
            tex.set_color_by_tex("b", color=PURPLE)
            tex.scale(scale)

            tex.next_to(top_equation, DOWN)
            all_equations.add(tex)

            top_equation = tex
        
        return all_equations
    
    def block(self, heading, pos, equations, highlighted=[], wrong=False, scale=1):
        top = Tex(heading, color=YELLOW)
        top.scale(0.6)
        top.move_to(pos)

        eq_tex = self.construct_equations(equations, top, scale)

        for index in highlighted:
            eq_tex[index].set_color(RED)

        for eq in eq_tex:
            self.wait()
            self.next_section("Draw_Equation")

            self.play(
                Write(eq),
                run_time=0.5,
            )

        if wrong:
            border = SurroundingRectangle(eq_tex, color=RED, corner_radius=0.0)
            cross = Cross(border)

            self.play(
                Write(border),
                Write(cross)
            )
        else:
            border = SurroundingRectangle(eq_tex, color=YELLOW, corner_radius=0.1)

            self.play(
                Write(border)
            )

        self.wait()
    
    def write_derivatives(self):
        equations = [
            r"f_b(x) = e^x - bx",
            r"f'_b(x) = e^x - b",
            r"f''_b(x) = e^x",
        ]

        self.block("Ableitungen", UP * 2, equations)
    
    def solve_x(self):
        steps = [
            r"f'_b(x) = 0",
            r"e^x - b = 0",
            r"e^x = b",
            r"x = ln(b)",
            r"b > 0",
        ]

        self.block("Extremstellen", UP * 3 + LEFT * 4, steps, [-1])
    
    def solve_y(self):
        steps = [
            r"y = f_b(ln(b))",
            r"y = e^{ln(b)} - b ln(b)",
            r"y = b - b ln(b)",
            r"y = b (1 - ln(b))",
            r"E(ln(b) | b(1 - ln(b)))",
        ]

        self.block("Extrempunkte", UP * 3 + RIGHT * 4.5, steps, scale=0.8)
    
    def solve_minimum(self):
        steps = [
            r"f''_b(ln(b)) > 0",
            r"e^{ln(b)} > 0",
            r"b > 0",
        ]

        self.block("Tiefpunkte", DOWN * 1 + LEFT * 4, steps)
    
    def solve_maximum(self):
        steps = [
            r"f''_b(ln(b)) < 0",
            r"e^{ln(b)} < 0",
            r"b < 0",
        ]

        self.block("Hochpunkte", DOWN * 1, steps, [-1], wrong=True)
    
    def solve_saddle_points(self):
        steps = [
            r"f''_b(ln(b)) = 0",
            r"e^{ln(b)} = 0",
            r"b = 0",
        ]

        self.block("Sattelpunkte", DOWN * 1 + RIGHT * 4, steps, [-1], wrong=True)
