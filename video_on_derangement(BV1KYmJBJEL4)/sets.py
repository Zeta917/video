from manim import *

class Sets(Scene):
    def construct(self):
        c = VGroup()
        for k in range(0,6):
            c += Circle(color = BLUE,fill_opacity = 0.4).shift(LEFT*0.5).rotate(k * PI/3,about_point = ORIGIN)
        c.to_edge(RIGHT,buff = 1.5)

        i = VGroup()
        i += c[0].copy().set_color(BLUE_B)
        i += Intersection(c[0],c[1],fill_opacity = 0.5,color = GREEN)
        i += Intersection(c[0],c[1],c[2],fill_opacity = 0.5,color = PINK)
        i += Intersection(c[0],c[1],c[2],c[3],fill_opacity = 0.5,color = ORANGE)
        
        self.play(Create(c))
        self.wait()
        for j in range(0,4):
            self.play(FadeIn(i[j]))
            self.wait(0.5)
            self.play(FadeOut(i[j]))
            self.wait(0.5)
        self.play(Unwrite(c))
        
