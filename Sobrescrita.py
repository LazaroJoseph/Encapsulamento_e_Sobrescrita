class Integrante_IFRN:
    def __init__(self, ):
    
    def exibirMensagem(self):
        print ('Seja bem vindo(a) ao IFRN!!!')
        
class Professor(Integrante_IFRN):
    def __init__(self, ):
    def super().__init__(self):

    def exibirMensagem(self):
        print ('Meus alunos são os melhores!!!')

class Aluno(Integrante_IFRN):
    def __init__(self, ):
    def super().__init__(self):
    
    def exibirMensagem(self):
        print ('Vou estudar para tirar 100 em POO!!!')
