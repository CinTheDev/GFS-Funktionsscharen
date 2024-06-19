#!/usr/bin/env python

from generic_solve_blocks import *

class AnalysisExponentialAdvanced(GenericSolveBlocks):
    def construct(self):
        self.transition()
        self.write_equations()
        self.solve_x()
        self.solve_y()

        self.prepare_determining_types()
        self.determine_local_maximum()
        self.determine_local_minimum()
        self.determine_saddle_point()

        self.prepare_solve_inflection()
        self.inflection_solve_x()
        self.inflection_verify()
        self.inflection_solve_y()
        # TODO: Visualize solutions on graph

    def transition(self):
        self.next_section("Transition")
        title = Tex("Noch ein Beispiel", color=YELLOW)
        title.move_to(UP * 3)

        self.play(
            Write(title),
            run_time=1
        )
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

        start_equations = VGroup(eq_x, eq_ddx)
        self.blocks.append(start_equations)

        self.play(
            Write(start_equations),
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

        self.block("Sattelpunkte", RIGHT * 4, steps, highlighted=[-1], scale=0.7, wrong=True)
    
    def prepare_solve_inflection(self):
        self.clear_blocks()

        eq_ddx = MathTex(r"f''_h(x) = h^2 x \cdot e^{h x} + 2h \cdot e^{h x}")
        eq_ddx.move_to(UP * 2 + LEFT * 3)

        eq_dddx = MathTex(r"f'''_h(x) = h^3 x \cdot e^{h x} + 3h^2 \cdot e^{h x}")
        eq_dddx.next_to(eq_ddx, DOWN)

        start_equations = VGroup(eq_ddx, eq_dddx)
        self.blocks.append(start_equations)

        self.play(
            Write(start_equations),
            run_time=1
        )
        self.wait()
    
    def inflection_solve_x(self):
        steps = [
            r"f''_h(x) = 0",
            r"h^2 x e^{h x} + 2h e^{h x} = 0",
            r"h^2 x + 2h = 0",
            r"h^2 x = -2h",
            r"x = -\frac{2}{h}",
        ]

        self.block("Wendestelle", LEFT * 4, steps, scale=0.7)
    
    def inflection_verify(self):
        steps = [
            r"f'''_h(-\frac{2}{h}) \neq 0",
            r"h^3 (-\frac{2}{h}) e^{h (-\frac{2}{h})} + 3h^2 e^{h (-\frac{2}{h})} \neq 0",
            r"h^3 (-\frac{2}{h}) + 3 h^2 \neq 0",
            r"-2h^2 + 3h^2 \neq 0",
            r"h^2 \neq 0",
            r"h \neq 0",
        ]

        self.block("Wendestelle prüfen", UP * 2.5 + RIGHT * 4, steps, highlighted=[-1], scale=0.7)
    
    def inflection_solve_y(self):
        steps = [
            r"y = -\frac{2}{h} e^{h (-\frac{2}{h})}",
            r"y = -\frac{2}{he^2}"
        ]

        self.block("Wendepunkt", LEFT * 0.5, steps, scale=0.7)

