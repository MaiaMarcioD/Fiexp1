from numpy import array
import seaborn as sns

class Exp1:

    def __init__(self, vetor=[]):

        self.vetor = vetor
        self.frequencia_seg = {}
        self.media = 0.0
        self.erro_media = 0.0
        self.desvio = 0.0
        self.compatibilidade = ""
        self.porcentagem_relativa = {}
        self.tamanho = 0.0


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

    def frequencia(self):
        
        porcen_rel = 100/120
        for i in sorted(self.vetor):
            if i not in self.frequencia_seg:
                self.frequencia_seg[i] = 1

            if i in self.frequencia_seg:
                self.frequencia_seg[i] += 1

        for i, j in self.frequencia_seg.items():

            self.porcentagem_relativa[i] = porcen_rel * j

    def largura(self, tamanho):
        self.tamanho = (max(self.vetor) - min(self.vetor)) / tamanho


    def __str__(self):

        a ="\n"+ f"Média: {self.media}"+"\n"+f"Desvio: {self.desvio}"+"\n"+f"Erro da média: {self.erro_media}"+"\n"+f"Compátibilidade: {self.compatibilidade}"\
            +"\n"+f"Porcentagem relativa: {self.porcentagem_relativa}" + "\n" +f"Frequencia: {self.frequencia_seg}"+ '\n'+ f"Tamanho bins: {self.tamanho}" + "\n"

        return a
