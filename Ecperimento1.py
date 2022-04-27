from numpy import array
import seaborn as sns

class Exp1:

    def __init__(self, vetor=[]):

        self.vetor = vetor
        self.media = 0.0
        self.erro_media = 0.0
        self.desvio = 0.0
        self.compatibilidade = ""


    def mediaVetor(self):

        self.media = float(sum(self.vetor))/(len(self.vetor))

        return self.media

    def desvioPadrao(self):

        for i in self.vetor:
            self.desvio += (i - self.media)**2

        self.desvio = self.desvio/(len(self.vetor)-1)
        self.desvio = self.desvio**(1/2)
        return self.desvio

    def erroMedia(self):

        self.erro_media = self.desvio/(len(self.vetor))**(1/2)
        
        return self.erro_media

    def testeCompatibilidade(self, MediaRef, DesvioRef):

        D = self.media - MediaRef
        if D < 0:
            D = D * (-1)
        C = ((self.desvio**2) + (DesvioRef**2))**(1/2)
        Z = D / C

        if Z > 0 and Z < 1:
            self.compatibilidade = "Compátivel"

        if Z > 1 and Z < 3:
            self.compatibilidade = "Compátivel; Baixa probabilidade"

        if Z > 3:
            self.compatibilidade = "Incopátivel"

        return self.compatibilidade

    def histograma(self):

        numpy_array = array(self.vetor)

        sns.histplot(data =numpy_array, kde = True);

    def __str__(self):

        a = f"Média: {self.media}"+"\n"+f"Desvio: {self.desvio}"+"\n"+f"Erro da média{self.erro_media}"+"\n"+f"Compátibilidade: {self.compatibilidade}"

        return a
