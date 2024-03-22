import tkinter as tk
from tkinter import ttk

def calculate_sum():
    try:
        num1 = float(input1.get())
        num2 = float(input2.get())
        result = num1 + num2
        result_label.config(text=f"Sum: {result}")
    except ValueError:
        result_label.config(text="Invalid input")

def main():
    global input1, input2, result_label  # Declare variables as global

    root = tk.Tk()
    root.title("Side by Side Containers")
    root.configure(background="#333333")

    style = ttk.Style()
    style.configure("Dark.TFrame", background="#333333", borderwidth=2, relief="solid", padding=10)

    container_frame = ttk.Frame(root, style="Dark.TFrame")
    container_frame.pack(expand=True, fill="both", padx=10, pady=10)

    label1 = ttk.Label(container_frame, text="Number 1:", foreground="white", background="#333333", font=("Helvetica", 10))
    label1.grid(row=0, column=0, padx=(50, 20), pady=20, sticky="w")

    input1 = ttk.Entry(container_frame, width=30)
    input1.grid(row=0, column=1, padx=(0, 50), pady=20)

    label2 = ttk.Label(container_frame, text="Number 2:", foreground="white", background="#333333", font=("Helvetica", 10))
    label2.grid(row=0, column=2, padx=(50, 20), pady=20)

    input2 = ttk.Entry(container_frame, width=30)
    input2.grid(row=0, column=3, padx=(0, 50), pady=20)

    calculate_button = ttk.Button(container_frame, text="Calculate", command=calculate_sum)
    calculate_button.grid(row=1, column=0, columnspan=4, pady=10)

    result_label = ttk.Label(container_frame, text="", foreground="white", background="#333333", font=("Helvetica", 10))
    result_label.grid(row=2, column=0, columnspan=4, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
