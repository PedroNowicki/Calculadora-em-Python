#João Pedro Mendes Nowicki - Matricula: 202308232746.
#Rafael Kahl Konorath - Matricula: 202308232711.

import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")

        self.rotulo_tarefa = tk.Label(root, text="Digite uma tarefa:")
        self.rotulo_tarefa.pack()

        self.entrada_tarefa = tk.Entry(root)
        self.entrada_tarefa.pack()

        self.botao_adicionar = tk.Button(root, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        self.botao_adicionar.pack()

        self.lista_tarefas = tk.Listbox(root)
        self.lista_tarefas.pack()

        self.botao_remover = tk.Button(root, text="Remover Tarefa", command=self.remover_tarefa)
        self.botao_remover.pack()

        self.tarefas = []

    def adicionar_tarefa(self):
        tarefa = self.entrada_tarefa.get()
        if tarefa:
            self.tarefas.append(tarefa)
            self.atualizar_lista_tarefas()
            self.entrada_tarefa.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Você deve digitar uma tarefa.")

    def remover_tarefa(self):
        try:
            indice_selecionado = self.lista_tarefas.curselection()[0]
            del self.tarefas[indice_selecionado]
            self.atualizar_lista_tarefas()
        except IndexError:
            messagebox.showwarning("Aviso", "Você deve selecionar uma tarefa para remover.")

    def atualizar_lista_tarefas(self):
        self.lista_tarefas.delete(0, tk.END)
        for tarefa in self.tarefas:
            self.lista_tarefas.insert(tk.END, tarefa)

if __name__ == "__main__":
    raiz = tk.Tk()
    app = ToDoListApp(raiz)
    raiz.mainloop()