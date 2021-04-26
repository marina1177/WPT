import math
import numpy as np
from ctypes import *
from const import *


class WPT:
    def __init__(self, a=1, b=1, c=1, e=1, wavelength=0.01, D=100):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.e = float(e)
        self.wavelength = float(wavelength)
        self.D = float(D)

    def calc(self):

        r1 = {}
        for i in range(0, (2 * w) +1):
            for j in range(0, (2 * w)+1):
                r1[i, j] = 0

        for p in range(w+1):
            h = 0
            u = 0
            o = 0
            tArray = [0.0] * 19
            gArray = [0.0] * 19
            hArray = [0.0] * 19
            kArray = [0.0] * 19

            # Расчет полей излучения отдельных модулей.
            # 1
            #print("FIELD_1")
            for n in np.arange(-(S / 2), ((S - 2) / 2) + 1):
                for m in np.arange(-(V / 2), ((V - 2) / 2) + 1):
                    tArray[0] = tArray[0] + ((self.a + self.b) / (S * V)) * math.cos(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

                    gArray[0] = gArray[0] + ((self.a * self.b) / (S * V)) * math.sin(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

            #print("FIELD_2")
            for n in np.arange((S / 2), ((3 * S - 2) / 2) + 1):
                for m in np.arange(0, ((V - 1)) + 1):
                    tArray[1] = tArray[1] + ((self.a * self.b) / (S * V)) * math.cos(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

                    gArray[1] = gArray[1] + ((self.a * self.b) / (S * V)) * math.sin(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

            #print("FIELD_3")
            for n in np.arange((S / 2), ((3 * S - 2) / 2) + 1):
                for m in np.arange(-V, (-1) + 1):
                    tArray[2] = tArray[2] + ((self.a * self.b) / (S * V)) * math.cos(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

                gArray[2] = gArray[2] + ((self.a * self.b) / (S * V)) * math.sin(
                    (2 * math.pi / (self.wavelength * self.D))
                    * (((2 * n + 1) * (p) * self.a / (2 * S))
                       + ((2 * m + 1) * self.b * h / (2 * V))))

            #print("FIELD_4")
            for n in np.arange((-S / 2), ((S - 2) / 2) + 1):
                for m in np.arange(-(3 * V / 2), ((-V - 2) / 2) + 1):
                    tArray[3] = tArray[3] + ((self.a * self.b) / (S * V)) * math.cos(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

                gArray[3] = gArray[3] + ((self.a * self.b) / (S * V)) * math.sin(
                    (2 * math.pi / (self.wavelength * self.D))
                    * (((2 * n + 1) * (p) * self.a / (2 * S))
                       + ((2 * m + 1) * self.b * h / (2 * V))))

            #print("FIELD_5")
            for n in np.arange((-3 * S / 2), ((-S - 2) / 2) + 1):
                for m in np.arange(-V, (-1) + 1):
                    tArray[4] = tArray[4] + ((self.a * self.b) / (S * V)) * math.cos(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

                gArray[4] = gArray[4] + ((self.a * self.b) / (S * V)) * math.sin(
                    (2 * math.pi / (self.wavelength * self.D))
                    * (((2 * n + 1) * (p) * self.a / (2 * S))
                       + ((2 * m + 1) * self.b * h / (2 * V))))

            #print("FIELD_6")
            for n in np.arange((-3 * S / 2), ((-S - 2) / 2) + 1):
                for m in np.arange(0, (V - 1) + 1):
                    tArray[5] = tArray[5] + ((self.a * self.b) / (S * V)) * math.cos(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

                    gArray[5] = gArray[5] + ((self.a * self.b) / (S * V)) * math.sin(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

            #print("FIELD_7")
            for n in np.arange((-S / 2), ((S - 2) / 2) + 1):
                for m in np.arange((V / 2), ((3 * V - 2) / 2) + 1):
                    tArray[6] = tArray[6] + ((self.a * self.b) / (S * V)) * math.cos(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

                    gArray[6] = gArray[6] + ((self.a * self.b) / (S * V)) * math.sin(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

            #print("FIELD_8")
            for n in np.arange((3 * S / 2), ((5 * S - 2) / 2) + 1):
                for m in np.arange((V / 2), ((3 * V - 2) / 2) + 1):
                    tArray[7] = tArray[7] + ((self.a * self.b) / (S * V)) * math.cos(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

                    gArray[7] = gArray[7] + ((self.a * self.b) / (S * V)) * math.sin(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

            #print("FIELD_9")
            for n in np.arange((3 * S / 2), ((5 * S - 2) / 2) + 1):
                for m in np.arange(-(V / 2), (((V - 2) / 2) / 2) + 1):
                    tArray[8] = tArray[8] + ((self.a * self.b) / (S * V)) * math.cos(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

                    gArray[8] = gArray[8] + ((self.a * self.b) / (S * V)) * math.sin(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

            #print("FIELD_10")
            for n in np.arange((3 * S / 2), ((5 * S - 2) / 2) + 1):
                for m in np.arange(-(3 * V / 2), ((5 * V - 2) / 2) + 1):
                    tArray[9] = tArray[9] + ((self.a * self.b) / (S * V)) * math.cos(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

                    gArray[9] = gArray[9] + ((self.a * self.b) / (S * V)) * math.sin(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

            #print("FIELD_11")
            for n in np.arange((S / 2), ((3 * S - 2) / 2) + 1):
                for m in np.arange(-(2 * V / 2), ((-V - 1) / 2) + 1):
                    tArray[10] = tArray[10] + ((self.a * self.b) / (S * V)) * math.cos(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

                    gArray[10] = gArray[10] + ((self.a * self.b) / (S * V)) * math.sin(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

            #print("FIELD_12")
            for n in np.arange((-S / 2), ((S - 2) / 2) + 1):
                for m in np.arange(-(5 * V / 2), ((-3 * V - 2) / 2) + 1):
                    tArray[11] = tArray[11] + ((self.a * self.b) / (S * V)) * math.cos(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

                    gArray[11] = gArray[11] + ((self.a * self.b) / (S * V)) * math.sin(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

            #print("FIELD_13")
            for n in np.arange((-3 * S / 2), ((-S - 2) / 2) + 1):
                for m in np.arange(-(2 * V / 2), ((-V - 1) / 2) + 1):
                    tArray[12] = tArray[12] + ((self.a * self.b) / (S * V)) * math.cos(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

                    gArray[12] = gArray[12] + ((self.a * self.b) / (S * V)) * math.sin(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

            #print("FIELD_14")
            for n in np.arange((-5 * S / 2), ((-3 * S - 2) / 2) + 1):
                for m in np.arange(-(3 * V / 2), ((-V - 2) / 2) + 1):
                    tArray[13] = tArray[13] + ((self.a * self.b) / (S * V)) * math.cos(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

                    gArray[13] = gArray[13] + ((self.a * self.b) / (S * V)) * math.sin(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

            #print("FIELD_15")
            for n in np.arange((-5 * S / 2), ((-3 * S - 2) / 2) + 1):
                for m in np.arange(-(V / 2), ((V - 2) / 2) + 1):
                    tArray[14] = tArray[14] + ((self.a * self.b) / (S * V)) * math.cos(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

                    gArray[14] = gArray[14] + ((self.a * self.b) / (S * V)) * math.sin(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

            #print("FIELD_16")
            for n in np.arange((-5 * S / 2), ((-3 * S - 2) / 2) + 1):
                for m in np.arange((V / 2), ((3 * V - 2) / 2) + 1):
                    tArray[15] = tArray[15] + ((self.a * self.b) / (S * V)) * math.cos(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

                    gArray[15] = gArray[15] + ((self.a * self.b) / (S * V)) * math.sin(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

            #print("FIELD_17")
            for n in np.arange((-3 * S / 2), ((-S - 2) / 2) + 1):
                for m in np.arange((V), (2 * V - 1) + 1):
                    tArray[16] = tArray[16] + ((self.a * self.b) / (S * V)) * math.cos(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

                    gArray[16] = gArray[16] + ((self.a * self.b) / (S * V)) * math.sin(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

            #print("FIELD_18")
            for n in np.arange((-S / 2), ((S - 2) / 2) + 1):
                for m in np.arange((3 * V / 2), ((5 * V - 2) / 2) + 1):
                    tArray[17] = tArray[17] \
                                 + ((self.a * self.b) / (S * V)) \
                                 * math.cos((2 * math.pi / (self.wavelength * self.D))
                                            * (((2 * n + 1) * (p) * self.a / (2 * S))
                                               + ((2 * m + 1) * self.b * h / (2 * V))))

                    gArray[17] = gArray[17] + ((self.a * self.b) / (S * V)) * math.sin(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

            #print("FIELD_19")
            for n in np.arange((S / 2), ((3 * S - 2) / 2) + 1):
                for m in np.arange((V), (2 * V - 1) + 1):
                    tArray[18] = tArray[18] + ((self.a * self.b) / (S * V)) * math.cos(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

                    gArray[18] = gArray[18] + ((self.a * self.b) / (S * V)) * math.sin(
                        (2 * math.pi / (self.wavelength * self.D))
                        * (((2 * n + 1) * (p) * self.a / (2 * S))
                           + ((2 * m + 1) * self.b * h / (2 * V))))

            # Расчет фазового  распределения.
            #print("PHASE_1")
            kArray[0] = math.atan2(
                (tArray[0] + gArray[0] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))),
                (-gArray[0] + tArray[0] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))))

            #print("PHASE_2")
            kArray[1] = math.atan2(
                (tArray[1] + gArray[1] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))),
                (-gArray[1] + tArray[1] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))))

            #print("PHASE_3")
            kArray[2] = math.atan2(
                (tArray[2] + gArray[2] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))),
                (-gArray[2] + tArray[2] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))))

            #print("PHASE_4")
            kArray[3] = math.atan2(
                (tArray[3] + gArray[3] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))),
                (-gArray[3] + tArray[3] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))))

            #print("PHASE_5")
            kArray[4] = math.atan2(
                (tArray[4] + gArray[4] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))),
                (-gArray[4] + tArray[4] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))))

            #print("PHASE_6")
            kArray[5] = math.atan2(
                (tArray[5] + gArray[5] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))),
                (-gArray[5] + tArray[5] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))))

            #print("PHASE_7")
            kArray[6] = math.atan2(
                (tArray[6] + gArray[6] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))),
                (-gArray[6] + tArray[6] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))))

            #print("PHASE_8")
            kArray[7] = math.atan2(
                (tArray[7] + gArray[7] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))),
                (-gArray[7] + tArray[7] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))))

            #print("PHASE_9")
            kArray[8] = math.atan2(
                (tArray[8] + gArray[8] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))),
                (-gArray[8] + tArray[8] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))))

            # #print("PHASE_10")
            kArray[9] = math.atan2(
                (tArray[9] + gArray[9] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))),
                (-gArray[9] + tArray[9] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))))

            # ##print("PHASE_11")
            kArray[10] = math.atan2(
                (tArray[10] + gArray[10] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))),
                (-gArray[10] + tArray[10] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))))

            # #print("PHASE_12")
            kArray[11] = math.atan2(
                (tArray[11] + gArray[11] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))),
                (-gArray[11] + tArray[11] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))))

            # #print("PHASE_13")
            kArray[12] = math.atan2(
                (tArray[12] + gArray[12] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))),
                (-gArray[12] + tArray[12] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))))

            # #print("PHASE_14")
            kArray[13] = math.atan2(
                (tArray[13] + gArray[13] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))),
                (-gArray[13] + tArray[13] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))))

            # #print("PHASE_15")
            kArray[14] = math.atan2(
                (tArray[14] + gArray[14] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))),
                (-gArray[14] + tArray[14] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))))

            # #print("PHASE_16")
            kArray[15] = math.atan2(
                (tArray[15] + gArray[15] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))),
                (-gArray[15] + tArray[15] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))))

            # #print("PHASE_17")
            kArray[16] = math.atan2(
                (tArray[16] + gArray[16] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))),
                (-gArray[16] + tArray[16] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))))

            # #print("PHASE_18")
            kArray[17] = math.atan2(
                (tArray[17] + gArray[17] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))),
                (-gArray[17] + tArray[17] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))))

            # #print("PHASE_19")
            kArray[18] = math.atan2(
                (tArray[18] + gArray[18] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))),
                (-gArray[18] + tArray[18] * math.tan(
                    (2 * math.pi * (self.D + ((p * p + h * h) / (2 * self.D))) / self.wavelength))))

            # Расчет амплитудного распределения
            # #print("AMPLITUDES")
            CCe = (self.c * self.c * self.e / (self.wavelength * self.D * self.wavelength * self.D))
            E = self.e / (self.wavelength * self.D * self.wavelength * self.D)
            hArray[0] = math.sqrt(
                E * (math.pow(tArray[0], 2) + math.pow(gArray[0], 2)))
            hArray[1] = math.sqrt(
                E * (math.pow(tArray[1], 2) + math.pow(gArray[1], 2)))
            hArray[2] = math.sqrt(
                E * (math.pow(tArray[2], 2) + math.pow(gArray[2], 2)))
            hArray[3] = math.sqrt(
                E * (math.pow(tArray[3], 2) + math.pow(gArray[3], 2)))
            hArray[4] = math.sqrt(
                E * (math.pow(tArray[4], 2) + math.pow(gArray[4], 2)))
            hArray[5] = math.sqrt(
                E * (math.pow(tArray[5], 2) + math.pow(gArray[5], 2)))
            hArray[6] = math.sqrt(
                E * (math.pow(tArray[6], 2) + math.pow(gArray[6], 2)))
            hArray[7] = math.sqrt(
                CCe * (math.pow(tArray[7], 2) + math.pow(gArray[7], 2)))
            hArray[8] = math.sqrt(
                CCe * (math.pow(tArray[8], 2) + math.pow(gArray[8], 2)))
            hArray[9] = math.sqrt(
                CCe * (math.pow(tArray[9], 2) + math.pow(gArray[9], 2)))
            hArray[10] = math.sqrt(
                CCe * (math.pow(tArray[10], 2) + math.pow(gArray[10], 2)))
            hArray[11] = math.sqrt(
                CCe * (math.pow(tArray[11], 2) + math.pow(gArray[11], 2)))
            hArray[12] = math.sqrt(
                CCe * (math.pow(tArray[12], 2) + math.pow(gArray[12], 2)))
            hArray[13] = math.sqrt(
                CCe * (math.pow(tArray[13], 2) + math.pow(gArray[13], 2)))
            hArray[14] = math.sqrt(
                CCe * (math.pow(tArray[14], 2) + math.pow(gArray[14], 2)))
            hArray[15] = math.sqrt(
                CCe * (math.pow(tArray[15], 2) + math.pow(gArray[15], 2)))
            hArray[16] = math.sqrt(
                CCe * (math.pow(tArray[16], 2) + math.pow(gArray[16], 2)))
            hArray[17] = math.sqrt(
                CCe * (math.pow(tArray[17], 2) + math.pow(gArray[17], 2)))
            hArray[18] = math.sqrt(
                CCe * (math.pow(tArray[18], 2) + math.pow(gArray[18], 2)))

            # #print("RESULT FIELD:")
            r1[p,h] = hArray[0]
            + hArray[1] * math.cos(kArray[1] - kArray[0])
            + hArray[2] * math.cos(kArray[2] - kArray[0])
            + hArray[3] * math.cos(kArray[3] - kArray[0])
            + hArray[4] * math.cos(kArray[4] - kArray[0])
            + hArray[5] * math.cos(kArray[5] - kArray[0])
            + hArray[6] * math.cos(kArray[6] - kArray[0])
            + hArray[7] * math.cos(kArray[7] - kArray[0])
            + hArray[8] * math.cos(kArray[8] - kArray[0])
            + hArray[9] * math.cos(kArray[9] - kArray[0])
            + hArray[10] * math.cos(kArray[10] - kArray[0])
            + hArray[11] * math.cos(kArray[11] - kArray[0])
            + hArray[12] * math.cos(kArray[12] - kArray[0])
            + hArray[13] * math.cos(kArray[13] - kArray[0])
            + hArray[14] * math.cos(kArray[14] - kArray[0])
            + hArray[15] * math.cos(kArray[15] - kArray[0])
            + hArray[16] * math.cos(kArray[16] - kArray[0])
            + hArray[17] * math.cos(kArray[17] - kArray[0])
            + hArray[18] * math.cos(kArray[18] - kArray[0])

            print("p: " + str(p))
            print("h: " + str(h))
            print("r1^2: " + str(r1[p,h] * r1[p,h]))

        # Расчет КПД.
        #print("KPD")
        # for j in range(0, 2 * w+1):
        #     kpd = 0
        #     for p in range(0, 2*j+1):
        #         for h in range(0, j):
        #             kpd = (kpd + r1[p, h] * r1[p, h] / (10.5 + 12 * 1.5 * self.c * self.c))

        #print(str(kpd))
        # return r1
