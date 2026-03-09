from manim import *

class Reanalysis(Scene):
    def construct(self):
        t1 = VGroup(MathTex(r"A_i: "),Text("第i位正确排列").scale(0.8)).arrange(RIGHT)
        t2 = VGroup(MathTex(r"|A_i| = "),Text("第i位正确排列的方法数").scale(0.8)).arrange(RIGHT)
        VGroup(t1,t2).arrange(DOWN)
        t3 = VGroup(MathTex(r"a_n = n!-"),Text("至少有一位排列正确的方法数").scale(0.8)).arrange(RIGHT).shift(DOWN)
        t4 = MathTex(r"a_n = n!-",r"|A_1 \cup A_2 \cup A_3 \cup \cdots \cup A_n|").move_to(t3)

        self.play(Write(t1))
        self.wait()
        self.play(Write(t2))
        self.wait()
        self.play(VGroup(t1,t2).animate.shift(UP),Write(t3))
        self.wait()
        self.play(ReplacementTransform(t3[1],t4[1]),t3[0].animate.shift(RIGHT*0.5))
        self.wait()
        self.play(Indicate(t4[1]))
        self.wait()
        