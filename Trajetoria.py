from PoseWithHeader import PoseWithHeader
from Referencial import Referencial
import numpy as np
import re
import os

class Trajetoria:
    def __init__(self, nome):
        self.pontos = []
        self.referencial = Referencial()
        self.nome = nome
        
    def __str__(self):
        return "Ponto: \n " + str(self.pontos) + "\nOrientação: \n " + str(self.referencial) + "\nNome: " + str(self.nome)
    
    def readLog(self):
        # flag = 0
        # paths = os.listdir("Logs/")
        # #print(paths)
        # end_size = len(paths)

        # print("-----------------------------------")
        # print ("\nEscolha entre os seguintes Logs:")
        # for index, ele in enumerate(paths):
        #     paths[index] = "Logs/" + ele
        #     print("\n", index, " -> ", paths[index])

        # print("\n-----------------------------------")
        # while (flag != 1):
        #     choice = int(input("\nDigite os valor corresponde ao Log: \n"))

        #     if (choice in range(0, end_size)):
        #         print("\n Escolheu o Log ", paths[choice])
        #         flag = 1
        #     else:
        #         print("\nNão escolheu nenhum dos possiveis volte a escolher \n")
        #         print("-----------------------------------")
        #         print ("\nEscolha entre os seguintes Logs:")
        #         for index, ele in enumerate(paths):
        #             print("\n", index, " -> ", ele)
        #             print("\n-----------------------------------")



        # file = open(paths[choice],"r")
        # data = file.read()

        file = open("Logs/drone1.txt")
        data = file.read()

        sequences = re.split('---', data)
        for sequence in sequences:
            dados = PoseWithHeader()
            match_seq = re.search(r'seq: ([-]?\d+\d+)', sequence)
            if match_seq: 
                 dados.header.seq = (int(match_seq.group(1)))
            match_secs = re.search(r'secs: ([-]?\d+\d+)', sequence)
            if match_secs:
                dados.header.tempo.sec = (int(match_secs.group(1)))
                match_nsecs = re.search(r'nsecs:\s*([-]?\d+\d+)', sequence)
            if match_nsecs:
                dados.header.tempo.nsec = (int(match_nsecs.group(1)))
                match_frame = re.search(r'frame_id: "(\w+)"\)?', sequence)
            if match_frame:
                dados.header.frame = (str(match_frame.group(1)))
            match = re.search(r'position:\s*\n\s*x: ([-]?\d+\.\d+)', sequence)
            if match:
                dados.pose.ponto.x = (float(match.group(1)))
                match = re.search(r'y: ([-]?\d+\.\d+)', sequence)
            if match:
                dados.pose.ponto.y = (float(match.group(1)))
                match = re.search(r'z: ([-]?\d+\.\d+)', sequence)
            if match:
                dados.pose.ponto.z = (float(match.group(1)))
            match_orientation = re.search( r'orientation:.*\n\s*x: ([-]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)\n\s*y: ([-]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)\n\s*z: ([-]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)\n\s*w: ([-]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)', sequence)
            if match_orientation:
                dados.pose.orientacao.q1 = (float(match_orientation.group(1)))
                dados.pose.orientacao.q2 = (float(match_orientation.group(2)))
                dados.pose.orientacao.q3 = (float(match_orientation.group(3)))
                dados.pose.orientacao.q0 = (float(match_orientation.group(4)))
            self.pontos.append(dados)   
            #print(self.posewithheader)
            
            
    
    def coord(self):
        x = []
        y = []
        z = []
        for item in self.pontos:
            x.append(item.pose.ponto.x)
            y.append(item.pose.ponto.y)
            z.append(item.pose.ponto.z)
        return x,y,z
    
    def RotAndTrans(self, flag):

        """------------------------------- Coordendas incrementais -------------------------------------"""

        """------------------------------- Defenição de Variáveis -------------------------------------"""

        calc_x = float(0)
        calc_y = float(0)
        calc_z = float(0)

        """-------------------------- Calculo da Translação no eixo X ----------------------------------"""
        if flag == 1:

            if self.referencial.origen.x == 0.00:  

                self.referencial.origen.x = self.referencial.transformacao.translacao.x
                calc_x = self.referencial.origen.x

            elif self.referencial.origen.x > 0 and self.referencial.transformacao.translacao.x > 0:

                if self.referencial.origen.x > self.referencial.transformacao.translacao.x:

                    calc_x = self.referencial.transformacao.translacao.x- self.referencial.origen.x
                    self.referencial.origen.x = self.referencial.origen.x + calc_x

                elif self.referencial.origen.x < self.referencial.transformacao.translacao.x:

                    calc_x = self.referencial.transformacao.translacao.x - self.referencial.origen.x
                    self.referencial.origen.x = self.referencial.origen.x + calc_x

            elif self.referencial.origen.x < 0 and self.referencial.transformacao.translacao.x < 0: 

                if self.referencial.origen.x > self.referencial.transformacao.translacao.x:

                    calc_x = -(-self.referencial.transformacao.translacao.x + self.referencial.origen.x)
                    self.referencial.origen.x = self.referencial.origen.x + calc_x

                elif self.referencial.origen.x < self.referencial.transformacao.translacao.x:

                    calc_x = -(-self.referencial.transformacao.translacao.x + self.referencial.origen.x)
                    self.referencial.origen.x = self.referencial.origen.x + calc_x

            elif self.referencial.origen.x > 0 and self.referencial.transformacao.translacao.x < 0:

                calc_x = -(self.referencial.origen.x - self.referencial.transformacao.translacao.x)
                self.referencial.origen.x = self.referencial.origen.x + calc_x

            elif self.referencial.origen.x < 0 and self.referencial.transformacao.translacao.x > 0:

                calc_x = self.referencial.transformacao.translacao.x - self.referencial.origen.x
                self.referencial.origen.x = self.referencial.origen.x + calc_x

        """---------------------------------------------------------------------------------------------"""
        
        """--------------------------- Calculo da Translação no eixo Y ---------------------------------"""
        if flag == 2:
        
            if self.referencial.origen.y == 0.00: 

                self.referencial.origen.y = self.referencial.transformacao.translacao.y
                calc_y = self.referencial.origen.y

            elif self.referencial.origen.y > 0 and self.referencial.transformacao.translacao.y > 0:

                if self.referencial.origen.y > self.referencial.transformacao.translacao.y:
                    calc_y = self.referencial.transformacao.translacao.y - self.referencial.origen.y
                    self.referencial.origen.y = self.referencial.origen.y + calc_y

                elif self.referencial.origen.y < self.referencial.transformacao.translacao.y:
                    calc_y = self.referencial.transformacao.translacao.y - self.referencial.origen.y
                    self.referencial.origen.y = self.referencial.origen.y + calc_y

            elif self.referencial.origen.y < 0 and self.referencial.transformacao.translacao.y < 0:  

                if self.referencial.origen.y > self.referencial.transformacao.translacao.y:
                    calc_y = -(-self.referencial.transformacao.translacao.y + self.referencial.origen.y)
                    self.referencial.origen.y = self.referencial.origen.y + calc_y

                elif self.referencial.origen.y < self.referencial.transformacao.translacao.y:
                    calc_y = -(-self.referencial.transformacao.translacao.y + self.referencial.origen.y)
                    self.referencial.origen.y = self.referencial.origen.y + calc_y

            elif self.referencial.origen.y > 0 and self.referencial.transformacao.translacao.y < 0:
                
                calc_y = -(self.referencial.origen.y - self.referencial.transformacao.translacao.y)
                self.referencial.origen.y = self.referencial.origen.y + calc_y

            elif self.referencial.origen.y < 0 and self.referencial.transformacao.translacao.y > 0:

                calc_y = self.referencial.transformacao.translacao.y - self.referencial.origen.y
                self.referencial.origen.y =  self.referencial.origen.y + calc_y

        """---------------------------------------------------------------------------------------------"""

        """---------------------------- Calculo da Translação no eixo Z --------------------------------"""
        if flag == 3:

            if self.referencial.origen.z == 0.00:

                self.referencial.origen.z = self.referencial.transformacao.translacao.z
                calc_z = self.referencial.origen.z

            elif self.referencial.origen.z > 0 and self.referencial.transformacao.translacao.z > 0:

                if self.referencial.origen.z > self.referencial.transformacao.translacao.z:

                    calc_z = self.referencial.transformacao.translacao.z - self.referencial.origen.z
                    self.referencial.origen.z = self.referencial.origen.z + calc_z

                elif self.referencial.origen.z < self.referencial.transformacao.translacao.z:

                    calc_z = self.referencial.transformacao.translacao.z - self.referencial.origen.z
                    self.referencial.origen.z = self.referencial.origen.z + calc_z

            elif self.referencial.origen.z < 0 and self.referencial.transformacao.translacao.z < 0: 

                if self.referencial.origen.z > self.referencial.transformacao.translacao.z:

                    calc_z = -(-self.referencial.transformacao.translacao.z + self.referencial.origen.z)
                    self.referencial.origen.z = self.referencial.origen.z + calc_z

                elif self.referencial.origen.z < self.referencial.transformacao.translacao.z:

                    calc_z = -(-self.referencial.transformacao.translacao.z + self.referencial.origen.z)
                    self.referencial.origen.z = self.referencial.origen.z + calc_z

            elif self.referencial.origen.z > 0 and self.referencial.transformacao.translacao.z < 0:

                calc_z = -(self.referencial.origen.z - self.referencial.transformacao.translacao.z)
                self.referencial.origen.z = self.referencial.origen.z + calc_z

            elif self.referencial.origen.z < 0 and self.referencial.transformacao.translacao.z > 0:

                calc_z = self.referencial.transformacao.translacao.z - self.referencial.origen.z
                self.referencial.origen.z = self.referencial.origen.z + calc_z

        """---------------------------------------------------------------------------------------------"""

        """---------------------------------- Translação dos Pontos ------------------------------------"""
        x = []
        y = []
        z = []
        for ele in self.pontos:
            ele.pose.ponto.x = ele.pose.ponto.x + calc_x
            ele.pose.ponto.y = ele.pose.ponto.y + calc_y
            ele.pose.ponto.z = ele.pose.ponto.z + calc_z
            x.append(ele.pose.ponto.x)
            y.append(ele.pose.ponto.y)
            z.append(ele.pose.ponto.z)
        return x,y,z

