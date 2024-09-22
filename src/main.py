import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica
from tkinter import messagebox  # Importa a caixa de mensagem para exibir avisos
from tkinter import ttk  # Importa a biblioteca ttk para widgets temáticos

class TelaInicial:
    def __init__(self, master):
        self.master = master  # Guarda a referência à janela principal
        self.master.title("Início do Jogo da Velha")  # Define o título da janela
        self.master.geometry("300x200")  # Define o tamanho da janela inicial

        # Label e entrada para o Jogador 1
        self.label_jogador1 = ttk.Label(master, text="Nome do Jogador 1 (X):")  # Cria uma label usando ttk
        self.label_jogador1.pack(pady=(10, 0))  # Adiciona a label à janela com espaçamento superior
        self.entry_jogador1 = ttk.Entry(master)  # Cria um campo de entrada para o nome usando ttk
        self.entry_jogador1.pack(pady=(0, 10))  # Adiciona o campo à janela com espaçamento inferior

        # Label e entrada para o Jogador 2
        self.label_jogador2 = ttk.Label(master, text="Nome do Jogador 2 (O):")  # Cria uma label usando ttk
        self.label_jogador2.pack(pady=(10, 0))  # Adiciona a label à janela
        self.entry_jogador2 = ttk.Entry(master)  # Cria um campo de entrada para o nome usando ttk
        self.entry_jogador2.pack(pady=(0, 10))  # Adiciona o campo à janela

        # Botão para iniciar o jogo
        self.botao_iniciar = ttk.Button(master, text="Iniciar Jogo", command=self.iniciar_jogo)  # Cria um botão usando ttk
        self.botao_iniciar.pack(pady=(10, 0))  # Adiciona o botão à janela com espaçamento superior

    def iniciar_jogo(self):
        # Obtém os nomes dos jogadores ou usa padrões se os campos estiverem vazios
        nome_jogador1 = self.entry_jogador1.get() or "Jogador 1"
        nome_jogador2 = self.entry_jogador2.get() or "Jogador 2"
        self.master.destroy()  # Fecha a janela inicial
        root = tk.Tk()  # Cria uma nova janela para o jogo
        jogo = JogoDaVelha(root, nome_jogador1, nome_jogador2)  # Inicia o jogo
        root.mainloop()  # Executa o loop da janela do jogo

class JogoDaVelha:
    def __init__(self, master, jogador1, jogador2):
        self.master = master  # Guarda a referência à janela principal do jogo
        self.master.title("Jogo da Velha")  # Define o título da janela do jogo
        self.master.geometry("400x400")  # Define o tamanho da janela do jogo
        self.jogador1 = jogador1  # Guarda o nome do Jogador 1
        self.jogador2 = jogador2  # Guarda o nome do Jogador 2
        self.reset_game()  # Chama o método para reiniciar o jogo

    def reset_game(self):
        self.tabuleiro = [""] * 9  # Inicializa o tabuleiro vazio
        self.atual = "X"  # Define o jogador atual como "X"
        self.botoes = []  # Lista para guardar os botões do tabuleiro

        for i in range(9):  # Loop para criar 9 botões
            # Cria um botão para cada posição do tabuleiro usando ttk
            botao = ttk.Button(self.master, text="", command=lambda i=i: self.jogar(i), width=5, style='TButton')
            botao.grid(row=i // 3, column=i % 3, padx=10, pady=10, sticky="nsew")  # Adiciona espaçamento e define o layout

            self.botoes.append(botao)  # Adiciona o botão à lista

        # Configura o grid para expansão
        for i in range(3):  # Loop para configurar colunas e linhas
            self.master.grid_columnconfigure(i, weight=1)  # Permite que as colunas se expandam
            self.master.grid_rowconfigure(i, weight=1)  # Permite que as linhas se expandam

        # Título do jogo
        titulo = ttk.Label(self.master, text="Jogo da Velha", font=("Arial", 18))  # Cria uma label para o título usando ttk
        titulo.grid(row=3, column=0, columnspan=3, pady=20)  # Posiciona o título na grade com espaçamento

        # Botão para reiniciar o jogo
        reiniciar_botao = ttk.Button(self.master, text="Reiniciar", command=self.reset_game)  # Cria um botão de reinício usando ttk
        reiniciar_botao.grid(row=4, column=0, columnspan=3, pady=10)  # Posiciona o botão de reinício na grade

    def jogar(self, i):
        if self.tabuleiro[i] == "":  # Verifica se a posição está vazia
            self.tabuleiro[i] = self.atual  # Marca a posição com o jogador atual
            self.botoes[i].config(text=self.atual)  # Atualiza o botão visualmente
            if self.verificar_vitoria():  # Verifica se há um vencedor
                vencedor = self.jogador1 if self.atual == "X" else self.jogador2  # Determina o vencedor
                messagebox.showinfo("Fim de Jogo", f"{vencedor} ganhou!")  # Exibe mensagem de vitória
                self.reset_game()  # Reinicia o jogo
            elif "" not in self.tabuleiro:  # Verifica se o tabuleiro está cheio
                messagebox.showinfo("Fim de Jogo", "Deu Velha!")  # Exibe mensagem de empate
                self.reset_game()  # Reinicia o jogo
            else:
                self.atual = "O" if self.atual == "X" else "X"  # Alterna o jogador

    def verificar_vitoria(self):
        # Conjuntos de posições que representam uma vitória
        vitoria = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                   (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                   (0, 4, 8), (2, 4, 6)]
        for a, b, c in vitoria:  # Loop pelas combinações de vitória
            if self.tabuleiro[a] == self.tabuleiro[b] == self.tabuleiro[c] != "":  # Verifica se todos têm o mesmo valor
                return True  # Retorna verdadeiro se houver vitória
        return False  # Retorna falso se não houver vitória

if __name__ == "__main__":
    root = tk.Tk()  # Cria a janela principal
    tela_inicial = TelaInicial(root)  # Cria a tela inicial
    root.mainloop()  # Executa o loop da janela
