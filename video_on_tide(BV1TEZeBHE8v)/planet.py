from manim import *

class Planet(ImageMobject):
    def __init__(self,radius = 2,image = "earth2.png"):
        super().__init__(image)
        self.scale_to_fit_width(radius*2)
        self.r = radius
    
    @property
    def c(self):
        return self.get_center()

    def tidal_force(self,theta,scale,**kwargs):
        radius = self.r
        center = self.c
        cos_theta = np.cos(theta)
        sin_theta = np.sin(theta)
        r = radius * np.array([cos_theta,sin_theta,0])
        force = np.array([scale*2*cos_theta,-scale*sin_theta,0])
        color = RED if np.dot(force,r) > 0 else GREEN
        return Arrow(start = center + r,end = center + r + force,buff = 0,color = color,**kwargs)
    
    def tidal_forces(self,theta,scale,**kwargs):
        vecs = VGroup()
        for t in theta:
            vecs += self.tidal_force(t,scale,**kwargs)
        return vecs
    
    def gravitational_force(self,theta,target,scale,difference_ratio = 0.15,color = ORANGE):
        radius = self.r
        center = self.c
        cos_theta = np.cos(theta)
        sin_theta = np.sin(theta)
        r = radius * np.array([cos_theta,sin_theta,0])
        d = target - (center + r)
        distance = np.linalg.norm(d)
        center_distance = np.linalg.norm(target - center)
        force = (scale + difference_ratio * (center_distance - distance))/distance * d
        return Arrow(start = center + r,end = center + r + force,buff = 0,color = color)
    
    def gravitational_forces(self,theta,target,scale,difference_ratio = 0.15,color = ORANGE):
        vecs = VGroup()
        for t in theta:
            vecs += self.gravitational_force(t,target,scale,difference_ratio,color)
        return vecs
    
    def stretch_animation(self,target_ratio,**kwargs):
        return self.animate(**kwargs).stretch_to_fit_width(2 * self.r * target_ratio).stretch_to_fit_height(2 * self.r / target_ratio)
