from manim import *
from planet import Planet


class RocheLimit(Scene):
    def construct(self):
        earth = Planet(radius = 1.2).move_to([-5,0,0])
        moon = Planet(radius = 0.4,image = "moon.png").move_to([5.5,0,0])       
        
        self.add(earth,moon)
        self.wait()

        self.play(earth.animate.move_to([-8,0,0]).scale_to_fit_width(7),moon.animate.move_to(ORIGIN).stretch_to_fit_width(2*1.5*1.2).stretch_to_fit_height(2*1.5/1.2))
        self.wait()

        point = moon.get_edge_center(LEFT)
        lp = Dot(point)
        tidal_force = Arrow(point,point + [-1.5,0,0],buff = 0,color = BLUE)
        gravity = Arrow(point,point + [1.5,0,0],buff = 0,color = RED)
        t_f_l = Text("潮汐力",color = BLUE).scale(0.5).next_to(tidal_force.get_end(),UP)
        g_l = Text("自身引力",color = RED).scale(0.5).next_to(gravity.get_end(),DOWN)

        t1 = VGroup(MathTex(r"a_{\text{tide}}",color = BLUE),MathTex(r"="),MathTex(r"g",color = RED)).arrange(RIGHT).to_edge(UR)
        t2 = MathTex(r"\frac{2GM_eR_m}{r_\text{limit}^3} = \frac{GM_m}{R_m^2}").next_to(t1,DOWN,aligned_edge = RIGHT)
        t3 = MathTex(r"r_\text{limit} = R_m\sqrt[3]{\frac{2M_e}{M_m}}").move_to(t2)

        self.play(Write(VGroup(lp,tidal_force,gravity,t_f_l,g_l)))
        self.play(Write(t1))
        self.wait()

        crash = Circle(color = RED,stroke_width = 0,fill_opacity = 0.5).move_to(moon).stretch_to_fit_width(2*1.5*1.2).stretch_to_fit_height(2*1.5/1.2)

        self.play(FadeIn(crash),run_time = 0.5)
        self.play(FadeOut(crash),run_time = 0.5)
        self.wait()

        self.play(ReplacementTransform(t1.copy(),t2))
        self.wait()
        self.play(ReplacementTransform(t2,t3))
        self.wait()

        self.play(FadeOut(VGroup(lp,tidal_force,gravity,t_f_l,g_l)))
        self.play(earth.animate.move_to([-6,0,0]).scale_to_fit_width(0.4),moon.animate.move_to([6,0,0]).stretch_to_fit_width(0.1).stretch_to_fit_height(0.1),run_time = 1)

        orbit = Circle(radius = 12,z_index = -1,color = WHITE,stroke_width = 2).move_to(earth.c)
        roche_limit = Circle(radius = 0.3,z_index = -1,color = RED,stroke_width = 2).move_to(earth.c)
        l = DashedLine(earth.c,moon.c,color = GRAY,z_index = -1)

        self.play(GrowFromPoint(orbit,earth.c),GrowFromPoint(roche_limit,earth.c),GrowFromPoint(l,earth.c),VGroup(t1,t3).animate.shift(LEFT*2))
        
        t5 = Text("月球轨道384400km",color = WHITE).scale(0.4).next_to(moon,DL)
        t4 = Text("洛希极限9500km",color = RED).scale(0.4).next_to(roche_limit,RIGHT).align_to(t5,DOWN)

        self.play(FadeIn(VGroup(t4,t5)))
        self.wait()


        