from manim import *

class TwoTide(Scene):
    def construct(self):
        a1 = Axes(x_range = [0,4,1],y_range = [0,5,5],x_length = 13,y_length = 3).shift(UP*1.75)
        a2 = a1.copy().shift(DOWN*3.5)
        solar = a1.plot(lambda x:np.cos(4*PI*x)+2.5,color = ORANGE,stroke_width = 4)
        moon = a2.plot(lambda x:2.17*np.cos(4*0.966443*PI*x)+2.5,color = BLUE,stroke_width = 4)
        
        t1 = a1.get_axis_labels(MathTex("t"),MathTex(r"h_{\text{sun}}")).shift(DOWN*0.1)
        t2 = a2.get_axis_labels(MathTex("t"),MathTex(r"h_{\text{moon}}")).shift(DOWN*0.1)
        t3 = a1.get_axis_labels(MathTex("t"),MathTex(r"h")).shift(DOWN*1.75)

        self.play(Write(VGroup(a1,a2,t1,t2)))
        self.wait()
        self.play(Write(VGroup(solar,moon)))
        self.wait()
        
        l1 = a1.get_vertical_line(a1.c2p(1,5))
        l2 = a2.get_vertical_line(a2.c2p(1.034722,5))
        
        self.play(Write(l1),run_time = 0.5)
        self.wait()
        self.play(Write(l2),run_time = 0.5)
        self.wait()
        
        self.play(VGroup(a1,solar).animate.shift(DOWN*1.75),
                  VGroup(a2,moon).animate.shift(UP*1.75),
                  FadeOut(VGroup(t1,t2,l1,l2)))
        self.play(FadeIn(t3))

        a = Axes(x_range = [0,4,1],y_range = [0,7,7],x_length = 13,y_length = 21/5)
        t = a.get_axis_labels(MathTex("t"),MathTex("h"))
        h = a.plot(lambda x:np.cos(4*PI*x)+2.17*np.cos(4*0.966443*PI*x)+3.5,color = YELLOW,stroke_width = 4)

        self.play(ReplacementTransform(VGroup(a1,a2,t3,solar),VGroup(a,t,h)),FadeOut(moon))
        self.wait()

class BigTide(Scene):
    def construct(self):
        xm = ValueTracker(4)
        a = Axes(x_range = [0,xm.get_value(),1],y_range = [0,7,7],x_length = 13,y_length = 21/5)
        t = a.get_axis_labels(MathTex("t"),MathTex("h"))
        h = FunctionGraph(lambda x:np.cos(4*PI*x)+2.17*np.cos(4*0.966443*PI*x)+3.5,x_range = [0,xm.get_value()],color = YELLOW).scale([13/xm.get_value(),(19.02/5)/6.34,1]).set_stroke(width = 4).move_to(a.c2p(0,3.5),aligned_edge=LEFT)

        def update_axes(mob):
            mob.become(Axes(x_range = [0,xm.get_value(),1],y_range = [0,7,7],x_length = 13,y_length = 21/5))
        def update_graph(mob):
            mob.become(FunctionGraph(lambda x:np.cos(4*PI*x)+2.17*np.cos(4*0.966443*PI*x)+3.5,x_range = [0,xm.get_value()],color = YELLOW).scale([13/xm.get_value(),(19.02/5)/6.34,1]).set_stroke(width = 4).move_to(a.c2p(0,3.5),aligned_edge=LEFT))

        a.add_updater(update_axes)
        h.add_updater(update_graph)

        self.add(a,t,h)
        self.wait()
        self.play(xm.animate.set_value(30),run_time = 6)
        self.wait()

class Algebra(Scene):
    def construct(self):
        t1 = MathTex(r"x = A_s \cos \omega_s t + A_m \cos \omega_m t").scale(0.7)
        t2 = MathTex(r"= \frac{1}{2} [(A_s + A_m)(\cos \omega_s t + \cos \omega_m t) + (A_s - A_m)(\cos \omega_s t - \cos \omega_m t)] ").scale(0.7)
        t3 = MathTex(r"= (A_s + A_m) \cos \frac{\omega_s - \omega_m}{2} t \cos \frac{\omega_s + \omega_m}{2} t + (A_s - A_m) \sin \frac{\omega_s - \omega_m}{2} t \sin \frac{\omega_s + \omega_m}{2} t").scale(0.7)
        VGroup(t1,t2,t3).arrange(DOWN,aligned_edge=LEFT).to_edge(UP,buff = 1)
        t1.shift(LEFT*0.3)
        
        self.play(Write(VGroup(t1,t2,t3)))
        self.wait()

        t4 = VGroup(Text("拍频",color = YELLOW),MathTex(r"f = |f_s - f_m|")).arrange(RIGHT).scale(0.7).next_to(t3,DOWN,aligned_edge=LEFT,buff = 1)
        self.play(Write(t4))

        t5 = VGroup(Text("大潮周期",color = YELLOW),MathTex(r"T = \frac{1}{f} = \frac{T_s T_m}{|T_s - T_m|}"),MathTex(r"\approx 14.8 \text{day}",color = BLUE)).arrange(RIGHT).scale(0.7).next_to(t4,DOWN,aligned_edge=LEFT)
        self.play(Write(t5))
        self.wait()