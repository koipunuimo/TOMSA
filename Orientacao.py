import numpy as np
import math

class Orientacao:

    def __init__(self): #a utilizar o modo de representacao de quarterniao apresentado no pdf "Representing Attitude"
        self.q0 = float(1)
        self.q1 = float(1)
        self.q2 = float(1)
        self.q3 = float(1)
        self.norm = math.sqrt(self.q0**2 + self.q1**2 + self.q2**2 + self.q3**2)
        self.q0 = self.q0 / self.norm
        self.q1 = self.q1 / self.norm
        self.q2 = self.q2 / self.norm
        self.q3 = self.q3 / self.norm
        
        self.X  = 0
        self.Y  = 0
        self.Z  = 0

    @classmethod
    def from_euler_angles(self): #Angulo euler em 1,2,3 XYZ
        cth3 = np.cos(self.Z * 0.5)
        sth3 = np.sin(self.Z * 0.5)
        cth2 = np.cos(self.Y * 0.5)
        sth2 = np.sin(self.Y * 0.5)
        cth1 = np.cos(self.X * 0.5)
        sth1 = np.sin(self.X * 0.5)

        w = -sth1 * sth2 * sth3 + cth1 * cth2 * cth3
        x =  sth1 * cth2 * cth3 + sth2 * sth3 * cth1
        y = -sth1 * sth3 * cth2 + sth2 * cth1 * cth3
        z =  sth1 * sth2 * cth3 + sth3 * cth1 * cth2

        return (w,x,y,z)
    
    @classmethod
    def from_euler_angles313(self,theta1, theta2, theta3): #Angulo euler em 3,1,3 ZXZ

        w = np.cos(theta2 * 0.5)*np.cos( (theta1 + theta3) * 0.5)
        x = np.sin(theta2 * 0.5)*np.cos( (theta1 - theta3) * 0.5)
        y = np.sin(theta2 * 0.5)*np.sin( (theta1 - theta3) * 0.5)
        z = np.cos(theta2 * 0.5)*np.sin( (theta1 + theta3) * 0.5) 

        return (w,x,y,z)
    

    
    def __str__(self):
        return " q0: " +str(self.q0) + "\n q1: "+str(self.q1)+"\n q2: "+str(self.q2)+"\n q3: "+str(self.q3)
    
    
    def quaterniao_euler(self):
        t0 = +2.0 * (self.q0 * self.q1 + self.q2 * self.q3)
        t1 = +1.0 - 2.0 * (self.q1 * self.q1 + self.q2 * self.q2)
        X = np.arctan2(t0, t1)

        t2 = +2.0 * (self.q0 * self.q2 - self.q3 * self.q1)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        Y = np.arcsin(t2)

        t3 = +2.0 * (self.q0 * self.q3 + self.q1 * self.q2)
        t4 = +1.0 - 2.0 * (self.q2 * self.q2 + self.q3 * self.q3)
        Z = np.arctan2(t3, t4)
        
        self.X = X
        self.Y = Y
        self.Z = Z
        return "X= " + str(self.X) + " Y= " + str(self.Y) + " Z= " + str(self.Z)
    


    @classmethod
    def from_tait_bryan_angles(self, t1, t2, t3): # Ou Euler em configuração ZYX
        cy = np.cos(t3 * 0.5)
        sy = np.sin(t3 * 0.5)
        cp = np.cos(t2 * 0.5)
        sp = np.sin(t2 * 0.5)
        cr = np.cos(t1 * 0.5)
        sr = np.sin(t1 * 0.5)

        w = cr * cp * cy + sr * sp * sy
        x = sr * cp * cy - cr * sp * sy
        y = cr * sp * cy + sr * cp * sy
        z = cr * cp * sy - sr * sp * cy

        return (w, x, y, z)
    
    def to_tait_bryan_angles(self): # Ou Euler em configuração ZYX
        t1 = np.arctan2(2*(self.q0*self.q1 + self.q2*self.q3), 1 - 2*(self.q1**2 + self.q2**2))
        t2 = np.arcsin(2*(self.q0*self.q2 - self.q3*self.q1))
        t3 = np.arctan2(2*(self.q0*self.q3 + self.q1*self.q2), 1 - 2*(self.q2**2 + self.q3**2))
        return t1, t2, t3
    
    def to_rotation_matrix(self):
        r = np.array([[1 - 2*self.q2*self.q2 - 2*self.q3*self.q3 , 2*self.q1*self.q2 - 2*self.q0*self.q3   ,    2*self.q1*self.q3 + 2*self.q0*self.q2],
                      [2*self.q1*self.q2 + 2*self.q0*self.q3     , 1-2*self.q1*self.q1-2*self.q3*self.q3   ,    2*self.q2*self.q3 - 2*self.q0*self.q1],
                      [2*self.q1*self.q3 - 2*self.q0*self.q2     , 2*self.q2*self.q3 + 2*self.q0*self.q1   ,1 - 2*self.q1*self.q1 - 2*self.q2*self.q2]])
        return r