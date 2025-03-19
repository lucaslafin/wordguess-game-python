import random
import os

def escolher_palavra():
    palavras = ["sapo", "cachorro", "hiena", "tartaruga", "minhoca"]
    return random.choice(palavras)

def verificar_tentativa(palavra, tentativa):
    corretas = []
    erradas = []
    
    for i, letra in enumerate(tentativa):
        if i < len(palavra): 
            if letra == palavra[i]:
                corretas.append(letra)
            elif letra in palavra:
                erradas.append(letra)
    
    return corretas, erradas

def gerar_dica(tentativa, corretas, erradas, palavra):
    dica = []
    for letra in tentativa:
        if letra in corretas:
            dica.append(f"{letra} (correta)")
        elif letra in erradas:
            dica.append(f"{letra} (correta, porém está em uma posição diferente dessa)")
        else:
            dica.append(f"{letra} (não está na palavra)")
    return dica

def jogo_adivinhacao():
    palavra_secreta = escolher_palavra()
    tentativas_maximas = 6
    tentativas_realizadas = 0
    
    print("""
░░░░░██╗░█████╗░░██████╗░░█████╗░  ██████╗░░█████╗░
░░░░░██║██╔══██╗██╔════╝░██╔══██╗  ██╔══██╗██╔══██╗
░░░░░██║██║░░██║██║░░██╗░██║░░██║  ██║░░██║███████║
██╗░░██║██║░░██║██║░░╚██╗██║░░██║  ██║░░██║██╔══██║
╚█████╔╝╚█████╔╝╚██████╔╝╚█████╔╝  ██████╔╝██║░░██║
░╚════╝░░╚════╝░░╚═════╝░░╚════╝░  ╚═════╝░╚═╝░░╚═╝

░█████╗░██████╗░██╗██╗░░░██╗██╗███╗░░██╗██╗░░██╗░█████╗░░█████╗░░█████╗░░█████╗░
██╔══██╗██╔══██╗██║██║░░░██║██║████╗░██║██║░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
███████║██║░░██║██║╚██╗░██╔╝██║██╔██╗██║███████║███████║██║░░╚═╝███████║██║░░██║
██╔══██║██║░░██║██║░╚████╔╝░██║██║╚████║██╔══██║██╔══██║██║░░██╗██╔══██║██║░░██║
██║░░██║██████╔╝██║░░╚██╔╝░░██║██║░╚███║██║░░██║██║░░██║╚█████╔╝██║░░██║╚█████╔╝
╚═╝░░╚═╝╚═════╝░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░\n""")

    print(f"A palavra tem {len(palavra_secreta)} letras e o tema é animais")
    
    while tentativas_realizadas < tentativas_maximas:
        tentativa = input("Digite sua tentativa: ").lower()
        
        tentativas_realizadas += 1
        
        corretas, erradas = verificar_tentativa(palavra_secreta, tentativa)
        
        if tentativa == palavra_secreta:
            os.system("cls")
            print(f"Parabéns você adivinhou!!! a palavra era ✔ {palavra_secreta} ✔ \n")
            jogar_novamente()
            break
        
        dica = gerar_dica(tentativa, corretas, erradas, palavra_secreta)
        print(f"Tentativa {tentativas_realizadas}: {dica}")
        print(f"Você ainda tem {tentativas_maximas - tentativas_realizadas} tentativas.")
    
    if tentativas_realizadas == tentativas_maximas:
        os.system("cls")
        print(f"Você perdeu! A palavra era: {palavra_secreta} ツ \n")
        jogar_novamente()

def jogar_novamente():
    opcao_escolhida = int(input('para jogar novamente  ➤ [1]: '))
    if opcao_escolhida == 1:
        os.system("cls")
        jogo_adivinhacao()

# Iniciar o jogo
jogo_adivinhacao()

