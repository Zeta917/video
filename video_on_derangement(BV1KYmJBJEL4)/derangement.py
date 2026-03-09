from manim import *

def item(*position,color = BLUE):
    item = VGroup()
    for i in range(1,len(position)+1):
        s = Square(side_length = 1,fill_opacity = 0.5,color = color)
        text = MathTex("x_{"+f"{i}"+"}").move_to(s.get_center())
        item += VGroup(s,text)
    item.arrange(RIGHT,buff = 1)
    position0 = [x.get_center() for x in item]
    for i in range(0,len(position)):
        item[i].move_to(position0[position[i]-1])
    return item

class Derangement(Scene):
    def construct(self):
        s = item(1,2,3,4,5,6,7).shift(UP*0.5)
        s1 = item(3,6,1,7,4,2,5).shift(UP*0.5)
        n = VGroup(*[MathTex(f"{i}").move_to(s[i-1]) for i in range(1,8)]).shift(DOWN*1.5)
        t = MathTex(r"a_n = \ \ ?").scale(2).shift(UP*1.5)

        self.play(Write(s))
        self.play(Write(n))
        self.wait()
        self.play(Transform(s,s1))
        self.wait()
        self.play(Write(t),VGroup(s,n).animate.shift(DOWN*0.8))

class Derangement1(Scene):
    def construct(self):
        s1 = item(1)
        t1 = MathTex("a_1 = 0")
        VGroup(s1,t1).arrange(DOWN,buff = 1)

        self.play(Write(s1))
        self.wait()
        self.play(Write(t1))
        self.wait()
        self.play(Unwrite(VGroup(s1,t1)))

        s2 = VGroup(item(1,2),item(2,1)).arrange(DOWN,buff = 1)
        t2 = MathTex("a_2 = 1")
        VGroup(s2,t2).arrange(DOWN,buff = 1)

        self.play(Write(s2))
        self.wait()
        self.play(Write(t2))
        self.wait()
        self.play(Unwrite(VGroup(s2,t2)))

        s31 = VGroup(item(1,2,3),item(1,3,2),item(2,1,3)).arrange(DOWN,buff = 1)
        s32 = VGroup(item(2,3,1),item(3,1,2),item(3,2,1)).arrange(DOWN,buff = 1)
        s3 = VGroup(s31,s32).arrange(RIGHT,buff = 2).scale(0.7)
        t3 = MathTex("a_3 = 2")
        VGroup(s3,t3).arrange(DOWN,buff = 1)

        self.play(Write(s3))
        self.wait()
        self.play(Write(t3))
        self.wait()
        self.play(Unwrite(VGroup(s3,t3)))
        self.wait()

class Derangement2(Scene):
    def construct(self):
        s = item(1,2,3,4,5,6,7,8,9,10,11,12).scale(0.6)
        s1 = item(4,10,7,3,8,5,9,2,6,12,11,1).scale(0.6)

        self.play(Write(s))
        self.wait()
        self.play(Transform(s,s1))
        self.wait()
        self.play(Unwrite(s))

class Derangement3(Scene):
    def construct(self):
        s1 = item(1,2,3,4,5)
        _s2 = item(1,2,3,4,5,6,7,color = RED)
        s2 = VGroup(_s2[-1],_s2[-2])

        s3 = VGroup(s1,s2).arrange(RIGHT,buff = 1).shift(DOWN)

        s4 = item(1,2,3,4,5).shift(UP)
        r = Rectangle(height = 1.3,width = 10,color = YELLOW).shift(UP)

        self.play(Create(s3),Create(r),run_time = 1)
        self.wait()
        
        self.play(s3[0][2].copy().animate.move_to(s4[0]),
                  s3[0][3].copy().animate.move_to(s4[1]),
                  s3[0][0].copy().animate.move_to(s4[2]),
                  s3[1][1].copy().animate.move_to(s4[3]),
                  s3[0][1].copy().animate.move_to(s4[4]))
        self.wait()