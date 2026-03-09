from manim import *
from planet import Planet

class EffectOfSun(Scene):
    def construct(self):
        earth = Planet(radius = 2).shift(LEFT*3.5)
        moon = Planet(radius = 0.8,image = "moon.png").shift(RIGHT*4.5)
        sun = Planet(radius = 4,image = "sun.png").shift(RIGHT*12)
        self.add(earth,moon,sun)
        
        moon_force = DashedLine(start = earth.c,end = moon.c,buff = 0,color = GRAY,z_index = -1)
        sun_force = DashedLine(start = earth.c,end = sun.c,buff = 0,color = GRAY,z_index = -1)

        def moon_force_update(moon_force):
            moon_force.put_start_and_end_on(earth.c,moon.c)

        def sun_force_update(sun_force):
            sun_force.put_start_and_end_on(earth.c,sun.c)
        
        self.play(Create(moon_force),Create(sun_force),run_time = 0.5)
        moon_force.add_updater(moon_force_update)
        sun_force.add_updater(sun_force_update)

        self.play(earth.animate.move_to([-3.5,-1.2,0]).scale(0.5),moon.animate.move_to([-5,1.6,0]).rotate(PI/6).scale(0.4),sun.animate.move_to([8,0,0]),run_time = 2)
        self.wait()

        t1 = MathTex(r"\frac{a_s}{a_m} = \frac{M_s/r_s^3}{M_m/r_m^3} \approx 46\%").to_edge(UP,buff = 0.8)
        t2 = MathTex(r"\frac{g_s}{g_m} = \frac{M_s/r_s^2}{M_m/r_m^2} \approx 179").next_to(t1,DOWN,buff = 0.5)
        
        self.play(Write(t1))
        self.wait()
        self.play(Write(t2))
        self.wait()

        t3 = VGroup(MathTex(r"\vec{a}_{\text{tide}}",color = BLUE),MathTex(r"="),MathTex(r"\vec{g}_{\text{surface}}",color = ORANGE),MathTex(r"-"),MathTex(r"\vec{g}_{\text{center}}",color = RED)).arrange(RIGHT).to_edge(DOWN,buff = 1)
        self.play(Write(t3))
        self.wait()

        r_moon = MathTex(r"3.8 \times 10^8 \text{km}",color = GRAY).move_to(moon_force.get_center()).scale(0.5).rotate(moon_force.get_angle() - PI).shift(LEFT*0.3).shift(UP*0.1)
        r_sun = MathTex(r"1.5 \times 10^{11} \text{km}",color = GRAY).move_to(sun_force.get_center()).scale(0.5).rotate(sun_force.get_angle()).shift(DOWN*0.2)
        self.play(Write(VGroup(r_moon,r_sun)))
        self.wait()

class PositionalRelationship(Scene):
    def construct(self):
        earth = Planet(radius = 1).move_to([-2,0,0])
        moon = Planet(radius = 0.4,image = "moon.png").move_to([1,0,0]).rotate(3*PI/4,about_point = earth.c)
        sun = Planet(radius = 4,image = "sun.png").move_to([8,0,0])
        self.add(earth,moon,sun)

        earth_orbit = Circle(radius = 10,color = GRAY_D,stroke_width = 2,z_index = -2).move_to([8,0,0])
        moon_orbit = Circle(radius = 3,color = GRAY_B,stroke_width = 2,z_index = -2).move_to([-2,0,0])

        self.add(earth_orbit,moon_orbit)
        
        moon_water = Circle(radius = 1.15,color = BLUE_B,stroke_width = 0,fill_opacity = 0.5,z_index = -1).move_to(earth.c).stretch_to_fit_width(2.6).stretch_to_fit_height(2.0).rotate(3*PI/4)
        sun_water = Circle(radius = 1.15,color = BLUE_D,stroke_width = 0,fill_opacity = 0.5,z_index = -1).move_to(earth.c).stretch_to_fit_width(2.3).stretch_to_fit_height(2.075)
        self.add(sun_water,moon_water)
        self.wait()
        
        def moon_update(moon,dt):
            moon.rotate(dt*PI/4,about_point = earth.c)

        def earth_update(earth,dt):
            earth.rotate(dt*27.43*PI/4,about_point = earth.c)
        
        def moon_water_update(moon_water,dt):
            moon_water.rotate(dt*PI/4,about_point = earth.c)
        
        moon180 = moon.copy().rotate(PI/4,about_point = earth.c).set_z_index(-1)
        moon90 = moon.copy().rotate(-PI/4,about_point = earth.c).set_z_index(-1)
        
        moon.add_updater(moon_update)
        earth.add_updater(earth_update)
        moon_water.add_updater(moon_water_update)
        self.wait()
        self.add(moon180)
        self.wait(4)
        moon.remove_updater(moon_update)
        earth.remove_updater(earth_update)
        moon_water.remove_updater(moon_water_update)
        self.wait()
        self.play(FadeOut(moon180))
        moon.add_updater(moon_update)
        earth.add_updater(earth_update)
        moon_water.add_updater(moon_water_update)
        self.wait(2)
        self.add(moon90)
        self.wait(4.1)
        moon.remove_updater(moon_update)
        earth.remove_updater(earth_update)
        moon_water.remove_updater(moon_water_update)
        self.wait()
        