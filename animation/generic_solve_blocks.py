from manim import *

class GenericSolveBlocks(Scene):
    blocks = []

    def clear_blocks(self):
        self.next_section("Clear_blocks")

        self.play(
            [Unwrite(block) for block in self.blocks],
            run_time=1
        )
    
    def block(self, heading, pos, equations, colored_var=r"{a}", highlighted=[], wrong=False, scale=1):
        top = Tex(heading, color=YELLOW)
        top.scale(0.6)
        top.move_to(pos)

        all_equations = VGroup(top)

        # Construct MathTex equations
        for string in equations:
            tex = MathTex(
                string,
                substrings_to_isolate=colored_var,
            )
            tex.set_color_by_tex(colored_var, color=PURPLE)
            tex.scale(scale)

            tex.next_to(top, DOWN)

            all_equations.add(tex)
            top = tex
        
        # Highlight marked equations
        for index in highlighted:
            all_equations[index].set_color(RED)

        # Play animations
        for tex in all_equations:
            self.wait()
            self.next_section("Draw_Equation")

            self.play(
                Write(tex),
                run_time=0.5,
            )
        
        if wrong:
            self.next_section("Cross")

            border = SurroundingRectangle(all_equations, color=RED, corner_radius=0.0)
            cross = Cross(border)

            all_equations.add(border)
            all_equations.add(cross)

            self.play(
                Write(border),
                Write(cross),
            )
        else:
            border = SurroundingRectangle(all_equations, color=YELLOW, corner_radius=0.1)

            all_equations.add(border),

            self.play(
                Write(border),
            )
        
        self.blocks.append(all_equations)
        self.wait()
