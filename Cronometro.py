#João Pedro Mendes Nowicki - Matricula: 202308232746.
#Rafael Kahl Konorath - Matricula: 202308232711.

import tkinter as tk

class Stopwatch:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cronômetro")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.frame_time = tk.Frame(self.root)
        self.frame_time.grid(row=0, column=0, sticky="nsew")

        self.label_time = tk.Label(self.frame_time, text="00:00:00", font=("Arial", 28))
        self.label_time.pack()

        self.frame_buttons = tk.Frame(self.root)
        self.frame_buttons.grid(row=1, column=0, sticky="nsew")

        self.button_start = tk.Button(self.frame_buttons, text="Iniciar", command=self.comecar_crono)
        self.button_start.pack(side=tk.LEFT)

        self.button_stop = tk.Button(self.frame_buttons, text="Parar", command=self.parar_crono)
        self.button_stop.pack(side=tk.LEFT)

        self.button_reset = tk.Button(self.frame_buttons, text="Resetar", command=self.resetar_crono)
        self.button_reset.pack(side=tk.LEFT)

        self.button_salvar_volta = tk.Button(self.frame_buttons, text="Salvar Volta", command=self.salvar_volta)
        self.button_salvar_volta.pack(side=tk.LEFT)

        self.frame_laps = tk.Frame(self.root)
        self.frame_laps.grid(row=2, column=0, sticky="nsew")

        self.laps_listbox = tk.Listbox(self.frame_laps)
        self.laps_listbox.pack(fill="both", expand=True)

        self.running = False
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.laps = []

    def comecar_crono(self):
        if not self.running:
            self.running = True
            self.atualizar_tempo()

    def parar_crono(self):
        self.running = False

    def resetar_crono(self):
        if not self.running:
            self.seconds = 0
            self.minutes = 0
            self.hours = 0
            self.label_time.config(text="00:00:00")
            self.laps = []
            self.laps_listbox.delete(0, tk.END)

    def atualizar_tempo(self):
        if self.running:
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
                if self.minutes == 60:
                    self.minutes = 0
                    self.hours += 1
            self.label_time.config(text=f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
            self.root.after(1000, self.atualizar_tempo)

    def salvar_volta(self):
        if self.running:
            lap_time = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
            self.laps.append(lap_time)
            self.laps_listbox.insert(tk.END, lap_time)

if __name__ == "__main__":
    stopwatch = Stopwatch()
    stopwatch.root.mainloop()