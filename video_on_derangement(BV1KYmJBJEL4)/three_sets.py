from manim import *

class ThreeSets(Scene):
    def construct(self):
        c1 = Circle(color = BLUE,fill_opacity = 0.5,radius = 1).shift(LEFT*0.5)
        c2 = c1.copy().rotate(2*PI/3,about_point = ORIGIN)
        c3 = c2.copy().rotate(2*PI/3,about_point = ORIGIN)
        c = VGroup(c1,c2,c3)

        self.play(Create(c))
        self.wait()
        self.play(c.animate.shift(UP*1.5))

        u = Union(c1,c2,c3,color = RED,fill_opacity = 0.5)
        i12 = Intersection(c1,c2,color = GREEN,fill_opacity = 0.5)
        i13 = Intersection(c1,c3,color = YELLOW,fill_opacity = 0.5)
        i23 = Intersection(c2,c3,color = PINK,fill_opacity = 0.5)
        i = Intersection(c1,c2,c3,fill_opacity = 0.5)
        eq1 = VGroup(u.copy().scale(0.5),
                     MathTex("="),
                     c1.copy().scale(0.5),
                     MathTex("+"),
                     c2.copy().scale(0.5),
                     MathTex("+"),
                     c3.copy().scale(0.5)).arrange(RIGHT).shift(DOWN*1)
        eq2 = VGroup(MathTex("-"),
                     i12.copy().scale(0.5),
                     MathTex("-"),
                     i13.copy().scale(0.5),
                     MathTex("-"),
                     i23.copy().scale(0.5),
                     MathTex("+"),
                     i.copy().scale(0.5)).arrange(RIGHT).shift(DOWN*2.5)

        self.play(FadeIn(u))
        self.play(ReplacementTransform(u,eq1[0]))
        self.play(Write(eq1[1]))
        self.wait()
        self.play(ReplacementTransform(c1.copy(),eq1[2]),
                  ReplacementTransform(c2.copy(),eq1[4]),
                  ReplacementTransform(c3.copy(),eq1[6]),
                  Write(eq1[3]),
                  Write(eq1[5]),run_time = 2)
        self.wait()
        self.play(FadeIn(VGroup(i12,i13,i23)))
        self.play(Write(eq2[0]),
                  Write(eq2[2]),
                  Write(eq2[4]),
                  ReplacementTransform(i12,eq2[1]),
                  ReplacementTransform(i13,eq2[3]),
                  ReplacementTransform(i23,eq2[5]),run_time = 2)
        self.wait()
        self.play(FadeIn(i))
        self.play(Write(eq2[6]),
                  ReplacementTransform(i,eq2[7]),run_time = 2)
        self.wait()
        
        eq3 = MathTex(r"|A \cup B \cup C | = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|").scale(0.8).shift(DOWN*1.5)
        
        self.play(FadeOut(c),VGroup(eq1,eq2).animate.shift(UP*3))
        self.play(Write(eq3))
