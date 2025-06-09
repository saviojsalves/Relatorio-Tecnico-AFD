import tkinter as tk
from tkinter import scrolledtext, messagebox

class AutomatoComputador:
    def __init__(self, root):
        self.root = root
        self.root.title("Automato - Busca por 'computador'")
        self.root.geometry("700x500")
        
        # Configuração da interface
        self.criar_interface()
    
    def criar_interface(self):
        # Texto de exemplo
        texto_exemplo ="""O computador é uma máquina capaz de variados tipos de tratamento automático de
informações ou processamento de dados. Entende-se por computador um sistema físico que realiza
algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são ícones da era da
informação. O primeiro computador eletromecânico foi construído por Konrad Zuse (1910–1995).
Atualmente, um microcomputador é também chamado computador pessoal ou ainda computador
doméstico."""

        # Área de texto
        tk.Label(self.root, text="Texto T:", font=('Arial', 12)).pack(pady=5)
        self.texto_entrada = scrolledtext.ScrolledText(self.root, width=80, height=10, font=('Arial', 11))
        self.texto_entrada.insert(tk.END, texto_exemplo)
        self.texto_entrada.pack(pady=5)

        # Botão de busca
        tk.Button(self.root, text="Buscar 'computador'", command=self.buscar_palavra, 
                 bg="#4CAF50", fg="white", font=('Arial', 11)).pack(pady=10)

        # Área de resultados
        tk.Label(self.root, text="Resultados:", font=('Arial', 12)).pack(pady=5)
        self.resultados = scrolledtext.ScrolledText(self.root, width=80, height=10, font=('Arial', 11))
        self.resultados.pack(pady=5)
    
    def buscar_palavra(self):
        texto = self.texto_entrada.get("1.0", tk.END)
        palavra = "computador"
        ocorrencias = []
        
        # Limpa formatação anterior
        self.texto_entrada.tag_remove("destaque", "1.0", tk.END)
        
        # Busca por ocorrências exatas
        start = "1.0"
        while True:
            start = self.texto_entrada.search(palavra, start, stopindex=tk.END, 
                                            nocase=True, exact=True)
            if not start:
                break
            end = f"{start}+{len(palavra)}c"
            
            # Verifica se é uma palavra exata (não tem letras antes ou depois)
            antes = self.texto_entrada.get(f"{start}-1c", start)
            depois = self.texto_entrada.get(end, f"{end}+1c")
            
            if (not antes or not antes.isalpha()) and (not depois or not depois.isalpha()):
                # Adiciona à lista de ocorrências
                linha, col = map(int, start.split('.'))
                pos_absoluta = len('\n'.join(texto.split('\n')[:linha-1])) + col
                ocorrencias.append(pos_absoluta)
                
                # Destaca no texto
                self.texto_entrada.tag_add("destaque", start, end)
            
            start = end
        
        # Configura o destaque
        self.texto_entrada.tag_config("destaque", background="yellow", foreground="black")
        
        # Mostra resultados
        self.resultados.delete("1.0", tk.END)
        if ocorrencias:
            self.resultados.insert(tk.END, f"Palavra '{palavra}' encontrada nas posições:\n")
            for pos in ocorrencias:
                self.resultados.insert(tk.END, f"- Posição {pos}\n")
        else:
            self.resultados.insert(tk.END, f"Palavra '{palavra}' não encontrada no texto.")

# Executar aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = AutomatoComputador(root)
    root.mainloop()
