from Experimento1 import Exp1

def main():

    vetor20 = Exp1([0.48,0.46,0.50,0.49,0.53,0.48,0.52,0.46,0.55,0.48,0.51,0.48,0.47,0.52,0.50,0.53,0.55,0.53,0.50,0.53]) 
    vetor20.mediaVetor()
    vetor20.desvioPadrao()
    vetor20.erroMedia()
    vetor20.testeCompatibilidade(0.55, 0.01)
    vetor20.histograma()
    vetor20.frequencia()
    vetor20.largura(10)
    print(vetor20)

    vetor60 = Exp1([0.40,0.40,0.43,0.40,0.37,0.40,0.43,0.42,0.46,0.49,0.45,0.45,0.43,0.51,0.50,0.40,0.40,0.39,0.43,0.46,0.45,0.41,0.37,0.64,0.48,0.44,0.42,0.43,0.45,0.39,0.41,0.57,0.39,0.52,0.43,0.48,0.48,0.46,0.40,0.40,0.51,0.38,0.57,0.44,0.62,0.45,0.50,0.52,0.50,0.41,0.44,0.53,0.58,0.49,0.40,0.48,0.38,0.53,0.51,0.51])
    vetor60.mediaVetor()
    vetor60.desvioPadrao()
    vetor60.erroMedia()
    vetor60.testeCompatibilidade(0.55, 0.01)
    vetor60.histograma()
    vetor60.frequencia()
    vetor60.largura(10)
    print(vetor60)

    vetor120 = Exp1([0.51,0.48,0.47,0.52,0.50,0.53,0.55,0.53,0.50,0.53,0.46,0.47,0.53,0.49,0.44,0.53,0.42,0.50\
        ,0.45,0.57,0.50,0.60,0.47,0.47,0.51,0.48,0.49,0.53,0.55,0.52,0.43,0.51,0.56,0.54,0.46,0.56,0.50,0.46,0.46\
        ,0.43,0.35,0.45,0.49,0.35,0.55,0.53,0.52,0.40,0.43,0.41,0.47,0.43,0.46,0.45,0.59,0.49,0.53,0.53,0.55,0.45,0.46,0.45\
            ,0.48,0.44,0.52,0.46,0.45,0.45,0.48,0.50,0.47,0.48,0.44,0.47,0.45,0.48,0.45,0.47\
            ,0.50,0.43,0.48,0.45,0.44,0.47,0.46,0.50,0.52,0.50,0.50,0.54,0.45,0.49,0.42,0.49,0.49,0.51,0.49,0.55\
                ,0.46,0.49,0.49,0.45,0.48,0.49,0.50,0.47,0.47,0.50,0.63,0.55,0.44,0.46,0.55,0.46,0.55,0.46,0.46,0.49,0.52,0.44,0.53,0.53,0.53])
    
    vetor120.mediaVetor()
    vetor120.desvioPadrao()
    vetor120.erroMedia()
    vetor120.testeCompatibilidade(0.55, 0.01)
    vetor120.histograma()
    vetor120.frequencia()
    vetor120.largura(10)
    print(vetor120)

if __name__ == "__main__":
    main()

