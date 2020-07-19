from dataclasses import dataclass

@dataclass
class Mimic:
    """ classe responsavel por permutacao de palavras """ 
    palavra: str 

    def permutacao(self): 
        """ retorna sem repeticoes todas as permutacoes """ 

        ls_permutacao = list() 
        
        if len(self.palavra) == 1: 
            return self.palavra
        
        for _ in self.palavra: 
            self.palavra = self.palavra.replace(_,'',1)
            for a in self.permutacao():
                ls_permutacao.append(_+a)
            
        return set(ls_permutacao)

    def fatorial(self, num:int) -> int: 
        """ retorna a quantidade possivel de permutacoes """ 

        if num == 1: 
            return 1 

        return num * self.fatorial(num - 1) 
        
    def qtd_letras(self) -> int:

       return len(self.palavra) 

if __name__ == "__main__":
    mimic = Mimic('palavra')
    qtd = mimic.qtd_letras()
    # print(mimic.fatorial(qtd))
    # print(mimic.permutacao())

    def permutations(string):
        if len(string) == 1:
            return string

        recursive_perms = []
        for c in string:
            print(f'c in string: {c}')
            teste = string.replace(c,'',1)
            print(f'string.replace: {teste}')
            for perm in permutations(string.replace(c,'',1)):
                print(f'perm: {perm}')
                print(f'perm: {c+perm}')
                recursive_perms.append(c+perm)


        return set(recursive_perms)
    
    print(permutations('par'))
    # print(len(permutations('par')))




