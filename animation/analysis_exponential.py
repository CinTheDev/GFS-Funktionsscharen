#!/usr/bin/env python

from manim import *

class AnalysisExponential(Scene):
    def construct(self):
        self.transition()
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
    
    def solve_x(self):
        equations = [
            r"f'_b(x) = e^x - b",
            r"f''_b(x) = e^x",
        ]

        top_equation = MathTex(
            r"f_b(x) = e^x - bx",
            substrings_to_isolate="b"
        )
        top_equation.set_color_by_tex("b", color=PURPLE)
        top_equation.move_to(UP * 2)

        eq_tex = self.construct_equations(equations, top_equation)

        for eq in eq_tex:
            self.next_section("Draw_Equation")

            self.play(
                Write(eq),
                run_time=0.5
            )
            self.wait()
