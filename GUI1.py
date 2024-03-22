import tkinter as tk
import math as m
from tkinter import ttk


rhoL=54.99   # density of liquid(oil in this case)
rhog=0.0806
g=32.17
HL = 0
rhom_bar = 0
Re=0


def calculate_Liquid_viscosity_number():
    global HL, rhom_bar, Re
    try:
        ul = float(input1.get())
        rho_l = float(input2.get())
        sfl = float(input3.get())
        Vsl = float(input4.get()) if input4.get() else 0 
        Vsg = float(input5.get()) if input5.get() else 0
        P_bar = float(input6.get()) if input6.get() else 0
        Nd = float(input7.get()) if input7.get() else 0
       

        

        NL = ul * (g / rho_l * sfl ** 3) ** 0.25
        CNL = (0.0019 + 0.0322 * NL - 0.6642 * NL ** 2 + 4.9951 * NL ** 3) / (
                1 - 10.0147 * NL + 33.8696 * NL ** 2 + 277.2817 * NL ** 3)

        NLv = Vsl * (rho_l / g * sfl) ** 0.25
        NGv=Vsg*(rho_l/g*sfl)**0.25
        
        phi = 0  # Default value
        if NGv != 0 and Nd != 0:
            phi = (NLv / NGv**0.575) * (P_bar / 14.7) * 0.1 * (CNL / Nd)
            
            k=((0.0047+1123.32*phi+729489.64*phi**2)/(1+1097.1566*phi+722153.97*phi**2))**0.5
            phis=(NGv*NL**0.380)/Nd**2.14 
            j=(1.0886-69.9473*phis+2334.3497*phis**2-12896.683*phis**3)/(
                1-53.4401*phis+1517.9369*phis**2-8419.8115*phis**3)
            
            HL=k*j
            rhom_bar= rhoL*HL + rhog*(1-HL)
            
            if HL>1:
                result_label.config(
                text="Invlaid HL value"    
            )
            elif HL<0:
                result_label.config(
                text="Invlaid HL value"    
            )
                
        
            

        if input4.get() == "":
            result_label.config(
            text=f"• The liquid viscosity number is: {NL}\n "
                f"• The liquid viscosity coefficient is: {CNL}"
        )
        elif input5.get() == "":
            result_label.config(
            text=f"The liquid viscosity number is: {NL}\n "
                f"• The liquid viscosity coefficient is: {CNL}\n "
                f"• The liquid viscosity number: {NLv}\n "
        )
        elif input6.get() == "" and input7.get() == "":
            result_label.config(
            text=f"The liquid viscosity number is: {NL}\n "
                f"• The liquid viscosity coefficient is: {CNL}\n "
                f"• The liquid viscosity number: {NLv}\n "
                f"• The gas viscosity number is: {NGv}"
        )
        elif input6.get() != "" and input7.get() != "":
            result_label.config(
            text=f"The liquid viscosity number is: {NL}\n "
                f"• The liquid viscosity coefficient is: {CNL}\n "
                f"• The liquid viscosity number: {NLv}\n "
                f"• The gas viscosity number is: {NGv}\n "
                f"• The pipe diameter number is: {phi}\n"
                f"• The liquid holdup is: {HL}\n"
                f"• The Average density is: {rhom_bar}"      
        )
        # elif input8.get() != "" and input9.get() != ""  and input10.get() !="" and input11.get() != "":
            
        #     Re=(1.48*ql*rho)/(d*u)
        #     result_label.config(
        #     text=f"The liquid viscosity number is: {NL}\n "
        #         f"• The liquid viscosity coefficient is: {CNL}\n "
        #         f"• The liquid viscosity number: {NLv}\n "
        #         f"• The gas viscosity number is: {NGv}\n "
        #         f"• The pipe diameter number is: {phi}\n"
        #         f"• The liquid holdup is: {HL}\n"
        #         f"• The Average density is: {rhom_bar}\n"  
        #         f"The flow is Laminar" if Re <= 2100 else ("The flow is Turbulent" if Re >= 4000 else "The flow is Transitional")
                    
        # )
        
    except ValueError:
        result_label.config(text="Invalid input")
        
def calculate_flow():
    try:
        ql = float(input8.get())
        rho = float(input9.get()) 
        d = float(input10.get())
        u = float(input11.get())
        
        Re = (1.48 * ql * rho) / (d * u)
       
        if Re <= 2100:
            f = 16 / Re 
            result_label1.config(
                text=f"The flow is Laminar\nThe friction factor is {f}"
            )
        elif Re > 2100:
            a=-4*m.log10(0.0002698-(5.0452/Re)*m.log10((0.0001629)+(7.149/Re)**0.8981))
            f=1/a**2
            result_label1.config(
                text=f"The flow is Turbulent\nThe friction factor is {f}"
            )
        else:
            f = "Not Available"
            result_label1.config(
                text="The flow is Transitional\nFriction factor calculation not available"
            )
    
    except ValueError:
        result_label1.config(text="Invalid input")
        


def refresh_values():
    inputs = [input1, input2, input3, input4, input5, input6, input7]
    for i in inputs:
        i.delete(0, tk.END)
    result_label.config(text="")

def main():
    global input1, input2, input3, input4, input5, input6, input7, input8, input9, input10, input11, result_label, result_label1
    root = tk.Tk()
    root.title("Side by Side Containers")
    root.configure(background="#333333")

    style = ttk.Style()
    style.configure("Dark.TFrame", background="#333333", borderwidth=2, relief="solid", padding=10)

    container_frame = ttk.Frame(root, style="Dark.TFrame")
    container_frame.pack(expand=True, fill="both", padx=10, pady=10)
    
    heading_label = ttk.Label(container_frame, text="Viscosity Calculation", foreground="white", background="#333333", font=("Helvetica", 16, "bold"))
    heading_label.grid(row=0, column=0, columnspan=4, pady=10)

    label1 = ttk.Label(container_frame, text="Please enter the value of your liquid viscosity?", foreground="white", background="#333333", font=("Helvetica", 10))
    label1.grid(row=1, column=0, padx=(20, 10), pady=20, sticky="nsew")

    input1_style = ttk.Style()
    input1_style.configure("Custom.TEntry", borderwidth=2, relief="solid", foreground="black", background="white", padding=5, bordercolor="#555555")
    input1 = ttk.Entry(container_frame, width=30, style="Custom.TEntry")
    input1.grid(row=1, column=1, padx=(0, 20), pady=20, sticky="nsew")

    label2 = ttk.Label(container_frame, text="What is the density of the liquid:", foreground="white", background="#333333", font=("Helvetica", 10))
    label2.grid(row=1, column=2, padx=(20, 10), pady=20, sticky="nsew")

    input2 = ttk.Entry(container_frame, width=30, style="Custom.TEntry")
    input2.grid(row=1, column=3, padx=(0, 20), pady=20, sticky="nsew")

    label3 = ttk.Label(container_frame, text="What is the surface tension of the liquid:", foreground="white", background="#333333", font=("Helvetica", 10))
    label3.grid(row=2, column=0, padx=(20, 10), pady=20, sticky="nsew")

    input3 = ttk.Entry(container_frame, width=30, style="Custom.TEntry")
    input3.grid(row=2, column=1, padx=(0, 20), pady=20, sticky="nsew")
    
    label4 = ttk.Label(container_frame, text="What is the value of the liquid velocity?", foreground="white", background="#333333", font=("Helvetica", 10))
    label4.grid(row=2, column=2, padx=(20, 10), pady=20, sticky="nsew")

    input4 = ttk.Entry(container_frame, width=30, style="Custom.TEntry")
    input4.grid(row=2, column=3, padx=(0, 20), pady=20, sticky="nsew")
    

    label5 = ttk.Label(container_frame, text="What is the value of the gas viscosity?", foreground="white", background="#333333", font=("Helvetica", 10))
    label5.grid(row=3, column=0, padx=(20, 10), pady=20, sticky="nsew")

    input5 = ttk.Entry(container_frame, width=30, style="Custom.TEntry")
    input5.grid(row=3, column=1, padx=(0, 20), pady=20, sticky="nsew")
    
    label6 = ttk.Label(container_frame, text="Please enter the value of average pressure", foreground="white", background="#333333", font=("Helvetica", 10))
    label6.grid(row=3, column=2, padx=(20, 10), pady=20, sticky="nsew")
    
    input6 = ttk.Entry(container_frame, width=30, style="Custom.TEntry")
    input6.grid(row=3, column=3, padx=(0, 20), pady=20, sticky="nsew")
    
    label7 = ttk.Label(container_frame, text="Please enter your value of Nd", foreground="white", background="#333333", font=("Helvetica", 10))
    label7.grid(row=4, column=0, padx=(20, 10), pady=20, sticky="nsew")

    input7 = ttk.Entry(container_frame, width=30, style="Custom.TEntry")
    input7.grid(row=4, column=1, padx=(0, 20), pady=20, sticky="nsew")
    
    label8 = ttk.Label(container_frame, text="What is your value for ql?", foreground="white", background="#333333", font=("Helvetica", 10))
    label8.grid(row=4, column=2, padx=(20, 10), pady=20, sticky="nsew")

    input8 = ttk.Entry(container_frame, width=30, style="Custom.TEntry")
    input8.grid(row=4, column=3, padx=(0, 20), pady=20, sticky="nsew")
    
    label9 = ttk.Label(container_frame, text="What is your value for rho?", foreground="white", background="#333333", font=("Helvetica", 10))
    label9.grid(row=5, column=0, padx=(20, 10), pady=20, sticky="nsew")

    input9 = ttk.Entry(container_frame, width=30, style="Custom.TEntry")
    input9.grid(row=5, column=1, padx=(0, 20), pady=20, sticky="nsew")
    
    label10 = ttk.Label(container_frame, text="What is your value for d?", foreground="white", background="#333333", font=("Helvetica", 10))
    label10.grid(row=5, column=2, padx=(20, 10), pady=20, sticky="nsew")

    input10 = ttk.Entry(container_frame, width=30, style="Custom.TEntry")
    input10.grid(row=5, column=3, padx=(0, 20), pady=20, sticky="nsew")
    
    label11 = ttk.Label(container_frame, text="What is your value for u?", foreground="white", background="#333333", font=("Helvetica", 10))
    label11.grid(row=6, column=0, padx=(20, 10), pady=20, sticky="nsew")

    input11 = ttk.Entry(container_frame, width=30, style="Custom.TEntry")
    input11.grid(row=6, column=1, padx=(0, 20), pady=20, sticky="nsew")
    
    calculate_button1 = ttk.Button(container_frame, text="Check type of flow", command=calculate_flow)
    calculate_button1.grid(row=6, column=2, pady=10)
    
    result_label1 = ttk.Label(container_frame, text="", foreground="white", background="#333333", font=("Helvetica", 10))
    result_label1.grid(row=6 ,column=3, pady=10)

    
    calculate_button = ttk.Button(container_frame, text="Calculate", command=calculate_Liquid_viscosity_number)
    calculate_button.grid(row=7, column=0, pady=10)

    refresh_button = ttk.Button(container_frame, text="Refresh", command=refresh_values)
    refresh_button.grid(row=7, column=1, pady=10)

    result_label = ttk.Label(container_frame, text="", foreground="white", background="#333333", font=("Helvetica", 10))
    result_label.grid(row=7, column=2, pady=10)
    
    
  
    
   
    
    

   

    

    

   

   
    
   

   
    
    

    # label12 = ttk.Label(container_frame, text="What is the value of your elevation? ", foreground="white", background="#333333", font=("Helvetica", 10))
    # label12.grid(row=5, column=2, padx=(20, 10), pady=20, sticky="nsew")

    # input12 = ttk.Entry(container_frame, width=30, style="Custom.TEntry")
    # input12.grid(row=5, column=3, padx=(0, 20), pady=20, sticky="nsew")


    # label13 = ttk.Label(container_frame, text="Please enter the value of the diameter of the pipe ", foreground="white", background="#333333", font=("Helvetica", 10))
    # label13.grid(row=6, column=0, padx=(20, 10), pady=20, sticky="nsew")

    # input13 = ttk.Entry(container_frame, width=30, style="Custom.TEntry")
    # input13.grid(row=6, column=1, padx=(0, 20), pady=20, sticky="nsew")
    root.mainloop()

if __name__ == "__main__":
    main()
