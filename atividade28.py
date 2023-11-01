# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.


from datetime import date 

today = date.today()
anoAtual = today.year 
idadeMaior = [] 
IdadeMenor = [] 

for i in range(8):
    anoNascimento = int(input("digite seu ano de nascimento"))
    
    if anoAtual - anoNascimento >=18:
     print("voce e maior de idade")
    else:
        anoAtual - anoNascimento <=18
        print("voce menor de idade")
    