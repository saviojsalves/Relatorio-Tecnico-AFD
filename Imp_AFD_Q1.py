import tkinter as tk
from tkinter import messagebox
import time

#Questão 1.A
# Transições do AFD
def transicao(estado_atual, simbolo):
    if estado_atual == "q0":
        if simbolo == "0":
            return "q0"
        elif simbolo == "1":
            return "q1"
    elif estado_atual == "q1":
        if simbolo == "0":
            return "q2"
    elif estado_atual == "q2":
        if simbolo == "0":
            return "q0"
    return "qE"

# Função que executa a simulação com atraso (animação)
def executar_afd():
    cadeia = entrada.get()
    if not all(c in "01" for c in cadeia):
        messagebox.showerror("Erro", "Use apenas os símbolos 0 e 1.")
        return

    estado = "q0"
    resultado_label.config(text="")
    for label in estados_labels.values():
        label.config(bg="lightgray")

    for i, simbolo in enumerate(cadeia):
        proximo = transicao(estado, simbolo)

        atualizar_estado(estado)
        status_label.config(text=f"Passo {i+1}/{len(cadeia)} | Lido: '{simbolo}' → Indo para {proximo}")
        root.update()
        time.sleep(0.8)

        estado = proximo

    atualizar_estado(estado)
    if estado == "q0":
        resultado_label.config(text="✅ Cadeia ACEITA!", fg="green")
    else:
        resultado_label.config(text=f"❌ Cadeia REJEITADA! (terminou em {estado})", fg="red")

def atualizar_estado(atual):
    for estado, label in estados_labels.items():
        if estado == atual:
            label.config(bg="gold")
        else:
            label.config(bg="lightgray")

# Interface Gráfica
root = tk.Tk()
root.title("Simulador de AFD - 100")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="Digite uma cadeia (0 e 1):").pack(pady=10)
entrada = tk.Entry(root, font=("Arial", 14), justify="center")
entrada.pack()

tk.Button(root, text="Executar AFD", command=executar_afd, font=("Arial", 12)).pack(pady=10)

# Estados visuais
estados_frame = tk.Frame(root)
estados_frame.pack(pady=10)

estados_labels = {}
for nome in ["q0", "q1", "q2", "qE"]:
    lbl = tk.Label(estados_frame, text=nome, width=6, height=2, bg="lightgray", relief="solid", font=("Arial", 12))
    lbl.pack(side="left", padx=10)
    estados_labels[nome] = lbl

status_label = tk.Label(root, text="", font=("Arial", 11))
status_label.pack(pady=10)

resultado_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
resultado_label.pack(pady=10)

root.mainloop()

#Questão 1B

import tkinter as tk

# Transições: (estado_atual, símbolo) -> próximo_estado
transicoes = {
    ("q0", "a"): "q3", ("q0", "b"): "q0",
    ("q1", "a"): "q2", ("q1", "b"): "q1",
    ("q2", "a"): "q1", ("q2", "b"): "q0",
    ("q3", "a"): "q0", ("q3", "b"): "q1",
}

estado_inicial = "q0"
estado_final = "q0"
estados = ["q0", "q1", "q2", "q3"]

# Interface gráfica com Tkinter
class AFD_GUI:
    def __init__(self, root):
        self.root = root
        root.title("Simulador de AFD - Par de 'a' e termina em 'b'")
        root.geometry("620x420")

        tk.Label(root, text="Digite uma cadeia (a ou b):").pack(pady=5)

        self.entrada = tk.Entry(root, font=("Arial", 16))
        self.entrada.pack(pady=5)

        tk.Button(root, text="Executar AFD", command=self.executar_afd).pack(pady=5)

        self.caixas_estado = {}
        frame_estados = tk.Frame(root)
        frame_estados.pack(pady=10)

        for estado in estados:
            caixa = tk.Label(frame_estados, text=estado, width=6, height=2,
                             bg="lightgray", font=("Arial", 12), relief="groove", bd=2)
            caixa.pack(side=tk.LEFT, padx=5)
            self.caixas_estado[estado] = caixa

        self.status = tk.Label(root, text="", font=("Arial", 12))
        self.status.pack(pady=10)

        self.resultado = tk.Label(root, text="", font=("Arial", 16, "bold"))
        self.resultado.pack(pady=10)

    def executar_afd(self):
        cadeia = self.entrada.get()
        estado = estado_inicial
        self.limpar_cores()
        self.destacar_estado(estado)

        for i, simbolo in enumerate(cadeia):
            if simbolo not in ['a', 'b']:
                self.resultado.config(text="⚠️ Caracteres inválidos!", fg="orange")
                return

            proximo = transicoes.get((estado, simbolo), "qE")
            self.status.config(text=f"Passo {i+1}/{len(cadeia)} | Lido: '{simbolo}' → Indo para {proximo}")
            self.destacar_estado(proximo)
            estado = proximo
            self.root.update()
            self.root.after(400)  # Pausa visual para animação

        if estado == estado_final and cadeia.endswith("b"):
            self.resultado.config(text="✅ Cadeia ACEITA!", fg="green")
        else:
            self.resultado.config(text=f"❌ Cadeia REJEITADA! (terminou em {estado})", fg="red")

    def limpar_cores(self):
        for caixa in self.caixas_estado.values():
            caixa.config(bg="lightgray")

    def destacar_estado(self, estado):
        self.limpar_cores()
        if estado in self.caixas_estado:
            self.caixas_estado[estado].config(bg="yellow")

# Executar app
root = tk.Tk()
app = AFD_GUI(root)
root.mainloop()