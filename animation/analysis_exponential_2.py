#!/usr/bin/env python

from manim import *

class AnalysisExponentialAdvanced(Scene):
    blocks = []

    def construct(self):
        self.transition()
        self.write_equations()
        self.solve_x()
        self.solve_y()
        self.prepare_determining_types()
        self.determine_local_maximum()
        self.determine_local_minimum()
        self.determine_saddle_point()
    
    def clear_blocks(self):
        self.next_section("Clear blocks")

        self.play(
            [Unwrite(block) for block in self.blocks],
            run_time=1
        )

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
            )
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
        self.wait()
        for eq in eq_tex:
            self.wait()
            self.next_section("Draw_Equation")

            self.play(
                Write(eq),
                run_time=0.5,
            )

        if wrong:
            self.next_section("Cross")
            
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
    
    def write_equations(self):
        equations = [
            r"f_h(x) = x \cdot e^{h x}",
            r"f'_h(x) = h x \cdot e^{h x} + e^{h x}",
            r"f''_h(x) = h^2 x \cdot e^{h x} + 2h \cdot e^{h x}",
            r"f'''_h(x) = h^3 x \cdot e^{h x} + 3h^2 \cdot e^{h x}",
        ]

        self.block(r"Funktion \& Ableitungen", UP * 2 + LEFT * 3.5, equations)
    
    def solve_x(self):
        steps = [
            r"f'_h(x) = 0",
            r"h x \cdot e^{h x} + e^{h x} = 0",
            r"h x + 1 = 0",
            r"h x = -1",
            r"x = -\frac{1}{h}",
        ]

        self.block("Extremstellen", UP * 2 + RIGHT * 3.5, steps)
    
    def solve_y(self):
        steps = [
            r"y = -\frac{1}{h} \cdot e^{h \cdot -\frac{1}{h}} = -\frac{1}{he}",
        ]

        self.block("Extrempunkte", DOWN * 2 + LEFT * 3.5, steps)
    
    def prepare_determining_types(self):
        self.clear_blocks()

        eq_x = MathTex(r"x = -\frac{1}{h}")
        eq_x.move_to(UP * 2)

        eq_ddx = MathTex(r"f''_h(x) = h^2 x \cdot e^{h x} + 2h \cdot e^{h x}")
        eq_ddx.next_to(eq_x, DOWN)

        self.play(
            Write(eq_x),
            Write(eq_ddx),
            run_time=1
        )
        self.wait()
    
    def determine_local_maximum(self):
        steps = [
            r"f''_h(-\frac{1}{h}) < 0",
            r"h^2 (-\frac{1}{h}) e^{h(-\frac{1}{h})} + 2h e^{h(-\frac{1}{h})} < 0",
            r"-h e^{-1} + 2h e^{-1} < 0",
            r"h e^{-1} < 0",
            r"h < 0",
        ]

        self.block("Hochpunkte", LEFT * 4, steps, scale=0.7)
    
    def determine_local_minimum(self):
        steps = [
            r"f''_h(-\frac{1}{h}) > 0",
            #r"h^2 (-\frac{1}{h}) e^{h(-\frac{1}{h})} + 2h e^{h(-\frac{1}{h})} > 0",
            #r"-h e^{-1} + 2h e^{-1} > 0",
            #r"h e^{-1} > 0",
            r"h > 0",
        ]

        self.block("Tiefpunkte", RIGHT, steps, scale=0.7)
    
    def determine_saddle_point(self):
        steps = [
            r"f''_h(-\frac{1}{h}) = 0",
            #r"h^2 (-\frac{1}{h}) e^{h(-\frac{1}{h})} + 2h e^{h(-\frac{1}{h})} = 0",
            #r"-h e^{-1} + 2h e^{-1} = 0",
            #r"h e^{-1} = 0",
            r"h = 0",
        ]

        self.block("Sattelpunkte", RIGHT * 4, steps, [-1], scale=0.7, wrong=True)
