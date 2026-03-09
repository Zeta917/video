from manim import *

class Probability(Scene):
    def construct(self):
        t = MathTex("P(",") = ?").arrange(RIGHT).scale(5)
        t[0].to_edge(LEFT)
        t[1].to_edge(RIGHT)
        
        self.play(Write(t))
        self.wait()