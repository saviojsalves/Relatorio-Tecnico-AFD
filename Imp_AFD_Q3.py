import tkinter as tk
import time

# Lista de moedas inseridas (em centavos)
entrada = [100, 25, 25, 25, 25, 100, 50, 50, 100, 100, 25, 50, 25, 25, 50, 25, 100]

# Inicializa variáveis
saldo = 0
saida = []

# Função que simula o funcionamento da máquina passo a passo
def iniciar_maquina():
    global saldo, saida
    saldo = 0
    saida = []
    texto_saida.delete(1.0, tk.END)

    for i, moeda in enumerate(entrada):
        saldo += moeda
        if saldo >= 100:
            saida.append(1)
            saldo -= 100
        else:
            saida.append(0)

        # Mostra resultado passo a passo na interface
        texto_saida.insert(tk.END, f"Moeda: {moeda} centavos -> Saída: {saida[-1]} | Saldo: {saldo}\n")
        texto_saida.see(tk.END)
        texto_saida.update()
        time.sleep(1)

    texto_saida.insert(tk.END, f"\nSequência de saída final:\n{saida}")

# Cria janela principal
janela = tk.Tk()
janela.title("Máquina de Refrigerante")
janela.geometry("400x300")

# Botão para iniciar a máquina
botao = tk.Button(janela, text="Iniciar Máquina", command=iniciar_maquina, font=("Arial", 12))
botao.pack(pady=10)

# Área de texto para mostrar a saída
texto_saida = tk.Text(janela, height=15, width=50, font=("Courier", 10))
texto_saida.pack()

# Inicia a interface gráfica
janela.mainloop()