import math as m
rhoL=54.99   # density of liquid(oil in this case)
rhog=0.0806
ul= float(input("Please enter the value of your liquid viscosity?"))
g=32.17
rho_l=int(input("What is the density of the liquid?"))
sfl= int(input("What is the surface tension of the liquid?"))
NL=ul*(g/rho_l*sfl**3)**0.25  # liquid viscosity number
print("The liquid viscosity number is",NL)
CNL=(0.0019+0.0322*NL - 0.6642*NL**2 + 4.9951*NL**3)/(1-10.0147*NL + 33.8696*NL**2 + 277.2817*NL**3) # liquid viscosity coefficient
print("The liquid viscosity coefficient is",CNL)
Vsl=float(input("What is the value of the liquid velocity?"))
NLv=Vsl*(rho_l/g*sfl)**0.25 # liquid viscosity number
print("The liquid viscosity number is",NLv)
Vsg=float(input("What is the value of the gas viscosity?"))
NGv=Vsg*(rho_l/g*sfl)**0.25 # gas viscosity number
print("The gas viscosity number is",NGv)
P_bar=float(input("Please enter the value of average pressure"))
Nd=float(input("Please enter your value of Nd"))
phi=(NLv/NGv**0.575)*(P_bar/14.7)*0.1 * (CNL/Nd) # pipe diameter number
print("The pipe diameter number",phi)
k=((0.0047+1123.32*phi+729489.64*phi**2)/(1+1097.1566*phi+722153.97*phi**2))**0.5
phis=(NGv*NL**0.380)/Nd**2.14 # secondary correction factor correlating parameter
j=(1.0886-69.9473*phis+2334.3497*phis**2-12896.683*phis**3)/(1-53.4401*phis+1517.9369*phis**2-8419.8115*phis**3)
HL=k*j # Liquid holdup
print("The liquid holdup is",HL)
if HL>1:
    print("Please enter a valid liquid holdup value")
elif HL<0:
    print("Please enter a valid liquid holdup value")
else:
    rhom_bar= rhoL*HL + rhog*(1-HL)
    print("The average density is",rhom_bar)
ql = float(input("What is your value for ql? ")) # this represents the flowrate
rho = int(input("What is your value for rho? ")) 
d = int(input("What is your value for d? "))
u = int(input("What is your value for u? "))
def reynolds_number(ql,rho,d,u):
    Re=(1.48*ql*p)/(d*u)
    if Re <= 2100:
        print("The flow is laminar")
    elif Re >= 4000:
        print("The flow is turbulent")
    else:
        print("The flow is transitional")
    return Re
print(reynolds_number(ql,rho,d,u))
Re = (1.48*ql*rho)/(d*u)
def friction_factor(Re):
    if Re<=2100:
        f=16/Re
    elif Re>2100:
        a=-4*m.log10(0.0002698-(5.0452/Re)*m.log10((0.0001629)+(7.149/Re)**0.8981))
        f=1/a**2
    return f'The friction factor is {f}'
a=-4*m.log10(0.0002698-(5.0452/Re)*m.log10((0.0001629)+(7.149/Re)**0.8981))
f=1/a**2
vm=5.615
M=rhom_bar*vm
delta_h=int(input("What is the value of your elevation?"))
D=int(input("Please enter the value of the diameter of the pipe"))
gc=32.17
delta_p = ((delta_h*rhom_bar)/144)+(f*ql**2*M**2*delta_h)/(4.2699*10**13*D**5*rhom_bar) + (rhom_bar*(vm**2)/(2*gc))/(144)
print("The pressure drop of the pipe is",delta_p)
 
