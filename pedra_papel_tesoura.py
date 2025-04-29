import random

def jogo():
  vitoria = "Você ganhou! +1 ponto"
  derrota = "Você perdeu!"
  empate = "Empate!"
  decisao = [1, 2, 3]
  pontuacao = 0
  
  while True:
    maquina = random.choice(decisao)
    jogador = input("Escolha um número de 1 a 3 \n1: Pedra \n2: Papel \n3: Tesoura")
    if jogador == "sair":
      break
    
    if jogador == "1":
      if maquina == 1:
        resultado = empate
      elif maquina == 2:
        resultado = derrota
      elif maquina == 3:
        resultado = vitoria
        pontuacao += 1
        
    elif jogador == "2":
      if maquina == 1:
        resultado = vitoria
        pontuacao += 1
      elif maquina == 2:
        resultado = empate
      elif maquina == 3:
        resultado = derrota
        
    elif jogador == "3":
      if maquina == 1:
        resultado = derrota
      elif maquina == 2:
        resultado = vitoria
        pontuacao += 1
      elif maquina == 3:
        resultado = empate
    
    if maquina == 1:
      maquina = "Pedra"
    if maquina == 2:
      maquina = "Papel"
    if maquina == 3:
      maquina = "Tesoura"
      
    if jogador == "1":
      jogador = "Pedra"
    if jogador == "2":
      jogador = "Papel"
    if jogador == "3":
      jogador= "Tesoura"
      
    print(f"Jogador: {jogador} \nMáquina: {maquina} \n{resultado} \nPontuação: {pontuacao}\n ")
  
jogo()
