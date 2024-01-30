# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Imports
import random
from os import system, name

# Função para limar a tela a cada execução
def limpa_tela():
 
    # Windows
    if name == 'nt':
        _ = system('cls')
 
    # Mac ou Linux
    else:
        _ = system('clear')

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# classe
class Hangman:
    
    # Metodo construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []

    # Metodo para adivinhar a letra
    def guess(self, letra):

        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)    

        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)

        else:
             return False

        return True

    # Metodo para verificar se o jogo terminou 
    def Hangman_over(self):
        return self.Hangman_won() or (len(self.letras_erradas) ==6)

    # Método para verificar se o jogador venceu
    def Hangman_won(self):

        if '_' not in self.hide_palavra():
            return True 
        return False

    # Método para não mostrar a letra no board
    def hide_palavra(self):

        rtn = ''

        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                rtn += '_'
            else:
                rtn += letra
        return rtn  

    # Método para checar o status do game e imprimir o board na tela                   
    def print_game_status(self):

        print (board[len(self.letras_erradas)])
        
        print ('\nPalavra: ' + self.hide_palavra())

        print ('\nLetrs erradas: ',)

        for letra in self.letras_erradas:
            print (letra)

        print () 
        
        print ('letras corretas: ',)

        for letra in self.letras_escolhidas:
            print (letra)

        print ()


# Método para ler uma palavra de forma aleatória do banco de palavras
def rand_palavra():

    palavras =  ['banana', 'abacate', 'uva', 'morango', 'laranja']       
    
    # escolher randomicamente uma palavra
    palavra = random.choice(palavras)

    return palavra

# Metodo Main - Execução do programa 
def main():
    
    limpa_tela()  

    # Cria o objeto e seleciona uma palavra randomicamente

    game = Hangman(rand_palavra())

    # Enquanto o jogo não tiver terminado, printi do status, solicita uma letra e faz a leitura do caracter
    while  not game.Hangman_over():

        # status do game 
        game.print_game_status()

        # Reebe input do terminal
        user_input = input('\nDigite uma letra: ')

        # verrificar se a letra digita faz parte da palavra
        game.guess(user_input)

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário

    if game.Hangman_won():
        print ('\nParabens! Você Venceu! !')

    else:
        print ('\ngame over! Você perdeu.')
        print ('A palavra era' + game.palavra)


    print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa        
if __name__ == "__main__":
    main()     


















