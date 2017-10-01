#pequeno desafio

def inputs_iniciais():
    """input iniciais para iniciar o jogo"""    
    lists = []
    while True:
        n = int(input('Escolha um número de 1 a 500:'))
        if n == 0:
            return lists
        game_list = []
        for _ in range(n):
            inp = input('digite o nome e o número separados por espaço ou 0 para começar o jogo: ')
            nome, numero = inp.split(' ')
            numero = int(numero)
            game_list.append((nome, numero))
        lists.append(game_list)
        

def play_game():
    """função principal do jogo."""
    lists = inputs_iniciais()
    for game_list in lists:
        index = game_list[0][1]
        if index%2 == 0:
            index = -index
        index = (index)%len(game_list)
        while len(game_list) > 1:
            number = game_list.pop(index)[1]
            if number%2 == 0:
                index = (index - number)%len(game_list)
            else:
                index = (index + number - 1)%len(game_list)
        print('Vencedor(a):', print(game_list.pop()[0]))

if __name__ == '__main__':
    play_game()
