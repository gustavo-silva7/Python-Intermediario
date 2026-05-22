# Sistema de Jogos
# Monte um ranking de jogadores baseado na pontuacao.

jogadores = [
    {"nome": "Ana", "pontuacao": 1500},
    {"nome": "Bruno", "pontuacao": 980},
    {"nome": "Carla", "pontuacao": 2100},
    {"nome": "Diego", "pontuacao": 1750},
]

ranking = sorted(jogadores, key=lambda jogador: jogador["pontuacao"], reverse=True)

print("Ranking de jogadores:")
for posicao, jogador in enumerate(ranking, start=1):
    print(f"{posicao}. {jogador['nome']} - {jogador['pontuacao']} pontos")
