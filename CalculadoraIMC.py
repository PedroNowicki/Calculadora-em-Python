#João Pedro Mendes Nowicki - Matricula: 202308232746.
#Rafael Kahl Konorath - Matricula: 202308232711.

import tkinter as tk

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IMC")
        self.root.geometry("681x374")
        self.root.resizable(True, True)

        self.instrucao_label = tk.Label(self.root, text="Para separar casas decimais usar ponto, exemplo: para uma altura de um metro e setenta centímetros usar 1.70", font=("Arial", 10, "italic"), justify="center")
        self.altura_entry = tk.Entry(self.root)
        self.peso_entry = tk.Entry(self.root)
        self.calcular_button = tk.Button(self.root, text="Calcular IMC")
        self.resultado_label = tk.Label(self.root, text="")

        self.altura_label = tk.Label(self.root, text="Altura:")
        self.peso_label = tk.Label(self.root, text="Peso:")

        self.instrucao_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.altura_entry.grid(row=1, column=1, padx=10, pady=10)
        self.peso_entry.grid(row=2, column=1, padx=10, pady=10)
        self.calcular_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.resultado_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.altura_label.grid(row=1, column=0, padx=10, pady=10)
        self.peso_label.grid(row=2, column=0, padx=10, pady=10)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)

        self.calcular_button.config(command=self.calcular_imc)

    def calcular_imc(self):
        altura = float(self.altura_entry.get())
        peso = float(self.peso_entry.get())

        imc = peso / (altura ** 2)
        self.resultado_label.config(text=f"Seu IMC é: {imc:.2f}")

        if imc < 18.5:
            self.show_bmi_category("Abaixo do peso")
        elif imc < 25:
            self.show_bmi_category("Peso normal")
        elif imc < 30:
            self.show_bmi_category("Sobrepeso")
        else:
            self.show_bmi_category("Obesidade")

    def show_bmi_category(self, categoria):
        self.resultado_label.config(text=f"Seu IMC é: {categoria}")

if __name__ == "__main__":
    root = tk.Tk()
    calculadora = BMICalculator(root)
    root.mainloop()