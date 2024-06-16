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
            Write(title)
            run_time=1
        )
        self.wait()

        self.next_section("Make_Room")

        title.generate_target()
        title.target.move_to(UP * 3)

        self.play(
            MoveToTarget(title)
            run_time=1
        )
        self.wait()
    
    def construct_equations(self, tex_strings, start_pos):
        all_equations = VGroup()

        for string in tex_strings:
            tex = MathTex(
                string,
                substrings_to_isolate="b"
            )
            tex.set_color_by_tex("b", color=PURPLE)

            tex.move_to(start_pos)
            all_equations.add(tex)
            start_pos.next_to(tex, DOWN)
    
    def solve_x(self):
        #self.next_section("Write equations")

        equations = [
            r"f_b(x) = e^x - bx",
            r"f'_b(x) = e^x - b",
            r"f''_b(x) = e^x",
        ]

        eq_tex = self.construct_equations(equations, UP)

        for eq in eq_tex:
            self.next_section("Draw_Equation")
            
            self.play(
                Write(eq),
                run_time=0.5
            )
            self.wait()
