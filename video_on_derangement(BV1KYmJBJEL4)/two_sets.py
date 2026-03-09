from manim import *

class TwoSets(Scene):
    def construct(self):
        c1 = Circle(radius = 1,color = BLUE,fill_opacity = 0.5).shift(LEFT*0.5)
        c2 = c1.copy().shift(RIGHT*1)
        c = VGroup(c1,c2)
        self.play(Create(c))
        self.wait()
        self.play(c.animate.shift(UP*1.5))

        i = Intersection(c1,c2,color = GREEN,fill_opacity = 0.5)
        u = Union(c1,c2,color = RED,fill_opacity = 0.5)
        eq = VGroup(u.copy(),MathTex(r"="),c1.copy(),MathTex(r"+"),c2.copy(),MathTex(r"-"),i.copy()).arrange(RIGHT).shift(DOWN*1.5)
        
        self.play(FadeIn(u))
        self.play(ReplacementTransform(u,eq[0]))
        self.play(Write(eq[1]))
        self.play(ReplacementTransform(c1.copy(),eq[2]),ReplacementTransform(c2.copy(),eq[4]),Write(eq[3]))
        self.play(Write(eq[5]))
        self.play(FadeIn(i))
        self.play(ReplacementTransform(i,eq[6]))
        self.wait()

        eq2 = MathTex(r"|A \cup B| = |A| + |B| - |A \cap B|").shift(DOWN*1.5)
        self.play(FadeOut(c),eq.animate.shift(UP*3))
        self.play(Write(eq2))
        self.wait()
