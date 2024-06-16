#!/usr/bin/env python

from manim import *

class AnalysisExponentialAdvanced(Scene):
    blocks = []

    def construct(self):
        self.transition()

    def transition(self):
        self.next_section("Transition")
        title = Tex("Noch ein Beispiel", color=YELLOW)
        title.move_to(UP * 3)

        self.play(
            Write(title),
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

            eq_tex.add(border)
            eq_tex.add(cross)

            self.play(
                Write(border),
                Write(cross)
            )
        else:
            border = SurroundingRectangle(eq_tex, color=YELLOW, corner_radius=0.1)

            eq_tex.add(border)

            self.play(
                Write(border)
            )

        self.blocks.append(eq_tex)
        self.wait()
