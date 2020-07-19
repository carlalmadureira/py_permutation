from termcolor import colored
from mimic import Mimic

def run() -> None:
    
    print('\n')
    palavra = str(input(colored("Digite a palavra desejada *sugestão: pode ser mimic ;)*  \n", 'magenta', attrs=['bold'])))
    mimic = Mimic(palavra)
    qtd_permutacoes = mimic.fatorial(mimic.qtd_letras())
    permutacoes = mimic.permutacao()

    print(colored(f'\n A quantidade de possíveis permutações é: {qtd_permutacoes} \n', color='magenta'))
    print(colored(f'\n A quantidade de permutações *únicas* é: {len(permutacoes)} \n', color='magenta'))
    print(colored(f'\n As permutações únicas são: ', color='magenta'))
    print(permutacoes)

if __name__ == "__main__":
    run()