from dataclasses import dataclass

@dataclass
class Mimic:
    """ classe responsavel por permutacao de palavras """ 
    palavra: str = None  

    def permutacoes(self, palavra:str) -> list: 
        """ retorna todas as permutacoes possiveis """ 

        ls_permutacao = list() 
        
        if len(palavra) <= 1: 
            return [palavra]
        
        for _ in palavra: 
            letras_restantes = "".join([rest for rest in palavra if rest != _ ])
            ls_permutacao.append(_)
            ls_permutacao.append(letras_restantes)
            for i in self.permutacoes(letras_restantes):
                ls_permutacao.append(_ + i) 
                
        return set(ls_permutacao)

    def numero_permutacoes(self, num:int) -> int: 
        """ retorna a quantidade possivel de permutacoes """ 

        if num == 1: 
            return 1 

        return num * self.numero_permutacoes(num - 1) 