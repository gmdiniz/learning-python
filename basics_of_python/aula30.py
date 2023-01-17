'''
CONSTANTE = 'Variaveis' que não vão mudar
Muitas condições no mesmo if (ruim)
    <- contagem de complexidade (ruim)
'''

velocidade = 61 # velocidade atual do carro
local_carro = 101   # local em que o carro está na estrada

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_max_radar_atingida = velocidade > RADAR_1
carro_passou_radar1 = local_carro >= (LOCAL_1 + RADAR_RANGE) and local_carro >= (LOCAL_1 - RADAR_RANGE)
carro_multado_radar1 = carro_passou_radar1 and velocidade_max_radar_atingida

if velocidade_max_radar_atingida:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar1:
    print('Carro passou radar 1')