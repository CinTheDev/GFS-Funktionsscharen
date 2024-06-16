#!/usr/bin/env python

from manim import *

class AnalysisExponential(Scene):
    def construct(self):
        self.transition()
        self.write_derivatives()
        self.solve_x()
    
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
    
    def construct_equations(self, tex_strings, top_equation):
        all_equations = VGroup(top_equation)

        for string in tex_strings:
            tex = MathTex(
                string,
                substrings_to_isolate="b"
            )
            tex.set_color_by_tex("b", color=PURPLE)

            tex.next_to(top_equation, DOWN)
            all_equations.add(tex)

            top_equation = tex
        
        return all_equations
    
    def block(self, heading, pos, equations):
        top = Tex(heading, color=YELLOW)
        top.scale(0.6)
        top.move_to(pos)

        eq_tex = self.construct_equations(equations, top)

        for eq in eq_tex:
            self.next_section("Draw_Equation")

            self.play(
                Write(eq),
                run_time=0.5,
            )
            self.wait()
        
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

        self.block("Extremstellen", UP * 2.5 + LEFT * 4, steps)

        #steps_tex = self.construct_equations(steps, top)
        #steps_tex[-1].set_color(RED)
