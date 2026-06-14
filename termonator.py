#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ##########################################################################
#
# Authors: Miguel Nahuatlato, Alex Girón, Sarah
# License: MIT
#
# H2O - Heating Curve
#
# ## ##########################################################################
import math
import matplotlib.pyplot as plt
import numpy as np

def sensible_heat(power, timei, mass0, temp0): #FUNCION - CALCULA TEMPERATURA EN FUNCION DE LA POTENCIA
 temp=((power*timei)/(mass0*4186))+temp0
 return temp

def phase_change_mass(enthalpy, power, time_enthalpy): #FUNCION - CALCULA MASA COMVERTIDA EN VAPOR EN FUNCION DE LA POTENCIA
  minusmass=(power*time_enthalpy)/enthalpy
  return minusmass

def enthalpy_of_vaporization(t): # FUNCION - CALCULA LA ENTALPIA DE VAPORIZACION EN FUNCION DE LA TEMPERATURA DE SATURACION
 k=273.15
 numerator=(1-((t+k)/647.096))
 denominator=(1-0.57665623)
 fracc = (numerator/denominator)**0.375
 h=2256.4*fracc
 return h

def saturation_temperature(pressure): # FUNCION - CALCULA LA TEMPERATURA DE SATURACION EN FUNCION DE LA PRESION
 n1=1167.0521452767
 n2=-724213.16703206
 n3=-17.073846940092
 n4=12020.824702470
 n5=-3232555.0322333
 n6=14.915108613530
 n7=-4823.2657361591
 n8=405113.40542057
 n9=-0.23855557567849
 n10=650.17534844798
 k=273.15

 β = (pressure**0.25)
 E = (β**2)+(n3*β)+(n6)
 F = (n1*(β**2))+(n4*β)+n7
 G = (n2*(β**2))+(n5*β)+n8
 D = (2*G)/(-F-(math.sqrt((F**2)-(4*E*G))))

 T = (((n10)+(D)-(math.sqrt(((n10+D)**2)-(4*(n9+n10*D)))))/2.0)-273.15
 return (T)

@np.vectorize
def constant_function(x,pressure): # FUNCION - CTE = TEMPERATURA DE SATURACION
  temp_satur= saturation_temperature(pressure)
  return temp_satur

@np.vectorize
def constant_function2(x,mass0): # FUNCION - CTE = MASA INICIAL
  return mass0

def plot(t,s,t1,temp_satur,pressure,time_satur,time,time_massis0, mass1,temp1): # FUNCION - GRAFICA TEMPERATURA-TIEMPO
 plt.title("TEMPERATURA-TIEMPO")
 plt.plot(t, s, "b-", color="red")

 if(temp1>temp_satur):
  plt.plot(t1,constant_function(t1,pressure),color="red")

 if(temp1>=temp_satur):
  plt.scatter(time_satur,temp_satur,color="red")

 if(mass1<=0):
  plt.scatter(time_massis0,temp_satur,color="blue")

 plt.legend(["x = TIEMPO"])
 plt.legend(["y = TEMPERATURA [°C]"])

 plt.xlabel("Valores de TIEMPO [s]",fontsize=20)
 plt.ylabel("Valores de TEMPERATURA [°C] ",fontsize=20)

 plt.grid(True, linestyle="-.", linewidth= 0.5, color="gray")
 plt.xticks(np.linspace(0,time,10))

 plt.yticks(np.linspace(0,temp_satur+(temp_satur/20),20))
 plt.show()

def plot2(f,m,f1,mass0,time,mass1,time_satur,time_massis0,temp_satur,temp0): # FUNCION - GRAFICA MASA-TIEMPO
 plt.title("MASA-TIEMPO")
 if(temp0<temp_satur):
  plt.plot(f1,constant_function2(f1,mass0),color="brown")

 if(mass1<mass0):
  plt.plot(f, m, "b-", color="brown")

  plt.scatter(time_satur,mass0,color="red")

 if(mass1<=0):
  plt.scatter(time_massis0,0,color="blue")

 plt.legend(["x = TIEMPO [s]"])
 plt.legend(["y = MASA [Kg]"])

 plt.xlabel("Valores de TIEMPO [s]",fontsize=20)
 plt.ylabel("Valores de MASA [Kg]",fontsize=20)

 plt.grid(True, linestyle="-.", linewidth= 0.5, color="gray")
 plt.xticks(np.linspace(0,time,10))
 plt.yticks(np.linspace(0,mass0+(mass0/20),20))
 plt.show()

def get_data(time_massis0, time_satur, power, mass0, temp0): # FUNCION - GENERA LAS REGLAS DE CORRESPONDENCIAS E INTERVALOS DE LASFUNCION GRAFICA TEMPERATURA-TIEMPO
 t = np.linspace(0,time_satur,100)
 t1= np.arange(time_satur,time_massis0,0.1)
 s = sensible_heat(power, t , mass0, temp0)
 return t,s,t1

def get_data2(time_massis0, time_satur,power, mass0,enthalpy): # FUNCION - GENERA LAS REGLAS DE CORRESPONDENCIAS E INTERVALOS DE LASFUNCION GRAFICA MASA-TIEMPO
 f = np.linspace(0,time_massis0-time_satur,100)
 f1= np.arange(0,time_satur,0.1)
 m=(mass0)-(phase_change_mass(enthalpy, power, f))
 f = f+time_satur
 return f,m,f1

def main(): # FUNCION PRINCIPAL

 print("CURVA DE CALENTAMIENTO H2O")

 print("\n 1.-Temperatura inicial.")
 temp0=float(input("Introduzca la temperatura inicial del sistema en [°C]: "))

 print("\n 2.-Masa inicial del agua.")
 mass0=float(input("Introduzca la masa inicial del sistema en [Kg]: "))

 print("\n 3.-Intervalo de tiempo para obtener la temperatura y la masa del sistema.")
 time=int(input("Introduzca el intervalo de tiempo del sistema en [S]: "))

 print("\n 4.-Potencia de la parrilla.")
 power=float(input("Introduzca la potencia de la parrrilla en [W]: "))

 print("\n 5.-Presión atmosférica.")
 pressure = float(input("Introduzca la presión del sistema en [MPa]: "))

 temp_satur = saturation_temperature(pressure) # LLAMA A LA FUNCION saturation_temperature(): PARA CALCULAR LA TEMPERATURA DE SATURACION A DICHA PRESION
 enthalpy = (enthalpy_of_vaporization(temp_satur))*1000 # LLAMA A LA FUNCION enthalpy_of_vaporization(): PARA CALCULAR LA ENTALPIA DE SATURACION A DICHA TEMPERATURA

 temp1 = temp0
 time_enthalpy = 1.0
 time_massis0 = 0
 time_satur = 0
 mass1=mass0

 print("\n t[s]  ||  T[°C]    ||    m[Kg]" )
 for timei in range(time):
  temp1 = sensible_heat(power, timei, mass0, temp0)
  if(temp1<=temp_satur):
   print("",timei,"[s]   ",round(temp1,1), "[°C]   "," ",round(mass0,3),"[Kg]")
   time_satur=timei
  else:
   minusmass = phase_change_mass(enthalpy, power, time_enthalpy)
   mass1=(mass0)-(minusmass)
   if (mass1>=0):
    print("",timei,"[s]   ",round(temp_satur,3), "[°C]   "," ",round(mass1,3),"[Kg]")
    time_massis0 = timei
   else:
    print("",timei,"[s]   ", "VAPOR SOBRECALENTADO h =",round((enthalpy/1000),3),"[Kj/Kg]")

   time_enthalpy = time_enthalpy + 1.0

 t,s,t1 = get_data(time_massis0, time_satur, power, mass0, temp0)
 plot(t,s,t1,temp_satur,pressure,time_satur,time,time_massis0, mass1,temp1)

 f,m,f1 = get_data2(time_massis0, time_satur,power, mass0,enthalpy)
 plot2(f,m,f1,mass0,time,mass1,time_satur,time_massis0,temp_satur,temp0)

if __name__ == '__main__':
  main()