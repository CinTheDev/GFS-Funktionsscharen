#!/usr/bin/env python

from manim import *

class Outro(Scene):
    def construct(self):
        heading = Tex("GFS Funktionenscharen", color=RED)
        heading.scale(0.8)
        heading.move_to(UP * 3.5)

        subheading = Tex("Vielen Dank für Aufmerksamkeit", color=RED)
        subheading.scale(0.6)
        subheading.move_to(DOWN * 3)

        external_sources = self.construct_external_sources()
        animation_sources = self.construct_animation_sources()

        external_sources.align_on_border(RIGHT)
        external_sources.shift(UP * 2)

        animation_sources.align_on_border(LEFT)

        self.play(
            LaggedStart(
                Write(heading),
                LaggedStart(
                    [FadeIn(s, shift=DOWN) for s in external_sources],
                    lag_ratio=0.1,
                    run_time=3
                ),
                LaggedStart(
                    [FadeIn(s, shift=DOWN) for s in animation_sources],
                    lag_ratio=0.1,
                    run_time=3
                ),
                Write(subheading),
                lag_ratio=0.5,
                run_time=3,
            )
        )

        self.wait()

    def construct_external_sources(self):
        heading = Tex("Externe Quellen", color=YELLOW)
        heading.scale(0.6)

        block = VGroup(heading)

        sources = [
            f'<span fgcolor="{ORANGE}">Definition Funktionenschar</span>\nhttps://de.wikipedia.org/wiki/Kurvenschar',
        ]

        for s in sources:
            source_text = MarkupText(s)
            source_text.scale(0.4)
            block.add(source_text)
        
        block.arrange(DOWN, aligned_edge=RIGHT)
        return block
    
    def construct_animation_sources(self):
        block = VGroup()

        sources = [
            f'<span fgcolor="{YELLOW}">Animation mit Manim Community</span>',
            f'https://www.manim.community/',
            f'<span fgcolor="{YELLOW}">Presenter</span>',
            f'https://github.com/CinTheDev/mp4-presenter',
            f'<span fgcolor="{YELLOW}">GFS Projektdateien</span>',
            f'https://github.com/CinTheDev/GFS-Funktionsscharen',
        ]

        for s in sources:
            source_text = MarkupText(s)
            source_text.scale(0.4)
            block.add(source_text)

        block.arrange(DOWN, aligned_edge=LEFT)        
        return block
