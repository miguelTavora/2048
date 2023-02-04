from random import random
from random import choice

# Trocar as linhas com as colunas
def trocar_linhas_com_colunas(grelha):

    # matriz transposta
    
    grelhazita = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    for i in range(len(grelha)):
        for j in range(len(grelha[0])):
           grelhazita[j][i] = grelha[i][j]
    return grelhazita

# Inverter a linha (ordem das colunas)
def inverter(grelha):
    
    for coluna in range(len(grelha[0])):
        nova_linha = []
        for linha in range(len(grelha)):
            nova_linha.append(grelha[linha][::-1])

    return nova_linha

# Controles
def mover_esquerda(uma_linha):

    nova_linha = []
    for valor in uma_linha:
        if valor != 0:
            nova_linha.append(valor)
            

    while len(nova_linha) < len(uma_linha):
        nova_linha.append(0)
                
    return nova_linha

def direita(jogo):

    (grelha, fim, vitoria, pontos) = jogo
    grelha_revertida = inverter(grelha)
    jogo_revertido = (grelha_revertida, fim, vitoria, pontos)
    jogo_revertido_atualizado = esquerda(jogo_revertido)
    (grelha, fim, vitoria, pontos) = jogo_revertido_atualizado
    grelha_revertida = inverter(grelha)
    jogo_atualizado = (grelha_revertida, fim, vitoria, pontos)
    return jogo_atualizado

def esquerda(jogo):

    
    grelha      = jogo[0]
    fim         = jogo[1]
    vitoria     = jogo[2]
    pontos      = jogo[3]
    grelha_alterada = []
    
    for linha in grelha:
        nova_linha = mover_esquerda(linha)
        (nova_linha2,pontos_somados) = somar_esquerda(nova_linha)
        grelha_alterada.append(nova_linha2)
        pontos += pontos_somados
    actualizar_grelha(grelha, grelha_alterada)
    fim = get_fim(grelha_alterada)
    
    if get_vitoria(grelha_alterada) == True:
        vitoria = True
   
    jogo_alterado = (grelha_alterada, fim, vitoria, pontos)

    return jogo_alterado

def abaixo(jogo):
    (grelha, fim, vitoria, pontos) = jogo
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_transposto = (grelha_transposta, fim, vitoria, pontos)
    jogo_transposto_atualizado = direita(jogo_transposto)
    (grelha, fim, vitoria, pontos) = jogo_transposto_atualizado
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_atualizado = (grelha_transposta, fim, vitoria, pontos)
    return jogo_atualizado

def acima(jogo):
    (grelha, fim, vitoria, pontos) = jogo
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_transposto = (grelha_transposta, fim, vitoria, pontos)
    jogo_transposto_atualizado = esquerda(jogo_transposto)
    (grelha, fim, vitoria, pontos) = jogo_transposto_atualizado
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_atualizado = (grelha_transposta, fim, vitoria, pontos)
    return jogo_atualizado   

def somar_esquerda(uma_linha):

    nova_linha = []
    pontos = 0
    indice = 0
    
    while indice < len(uma_linha)-1:
        if uma_linha[indice] == uma_linha[indice+1]:
            soma = uma_linha[indice] + uma_linha[indice+1]
            nova_linha.append(uma_linha[indice] + uma_linha[indice+1])
            pontos += soma
            indice = indice + 2
        else:
            nova_linha.append(uma_linha[indice])
            indice = indice + 1
           
    if indice == len (uma_linha) - 1:
        nova_linha.append(uma_linha[indice])
    
    while len(nova_linha) < len(uma_linha):
        nova_linha.append(0)
                
    return (nova_linha,pontos)

# Controles END

# Update Grelha
def actualizar_grelha(grelha_original, grelha_alterada):

    sao_iguais = True

    for l in range(len(grelha_original)):
        for c in range(len(grelha_original[l])):
            if grelha_original[l][c] != grelha_alterada[l][c]:
                sao_iguais = False

    if not sao_iguais:
        inserir_2ou4(grelha_alterada)
        
# Vitoria
def get_vitoria(grelha):

    # Procurar se existe o valor 2048
    # Se sim retorna true
    
    resultado = False
    
    for l in range(len(grelha)):
        for c in range(len(grelha[l])):
            if grelha[l][c] == 2048:
                resultado = True
                
    return resultado

# Procura adjacentes iguais
def ha_iguais_adjacentes(grelha):
    
    ha = False
    
    #
    for l in range(len(grelha)):
        for c in range((len(grelha[l]))-1):
            if grelha[l][c]==grelha[l][c+1]:
                ha=True
                
    #
    for l in range((len(grelha))-1):
        for c in range(len(grelha[l])):
            if grelha[l][c]==grelha[l+1][c]:
                ha=True
    return ha

# Verificar o fim
def get_fim(grelha):
    
    posicoes_vazias= get_posicoes_vazias(grelha)
    # Se Nao houver posicoes vazias e iguais adjacentes
    # Retorna True (Declara o fim do jogo)
    # Se nao, nao faz nada
    if (len(posicoes_vazias)==0) and (not ha_iguais_adjacentes(grelha)):

        return True

    else:
        return False

def valor(jogo, linha, coluna):
    
    # O 'jogo' é o tuplo (grelha, fim, vitoria, pontos)

    grelha = jogo[0]
    
    indice_linha = linha -1
    indice_coluna = coluna -1
    
    return grelha[indice_linha][indice_coluna]

# Retorna o valor do tuplo referente ao fim do jogo
def terminou(jogo):

    # O 'jogo' é o tuplo (grelha, fim, vitoria, pontos)
    
    return jogo[1]

# Retorna o valor do tuplo referente a vitoria
def ganhou_ou_perdeu(jogo):

    # O 'jogo' é o tuplo (grelha, fim, vitoria, pontos)
    
    return jogo[2]

# Retorna ao valor do tuplo referente a pontuacao
def pontuacao(jogo):

    # O 'jogo' é o tuplo (grelha, fim, vitoria, pontos)
    
    return jogo[3]

# Retorna TODAS as posicoes vazias
def get_posicoes_vazias(grelha):
    
    # Cria um 'array' novo para armazenar as posições vazias
    posicoes_vazias = []

    # Percorre todas as linhas da grelha
    # Dentro de cada linha percorre todas as colunas
    for linha in range(4):
        for coluna in range(4):
            # Se houver algum valor com zero
            # Dar append a variavel 'posicoes_vazias'
            if grelha[linha][coluna] == 0:
                posicoes_vazias.append([linha,coluna])

    return posicoes_vazias

# Retorna UMA posicao vazia [linha, coluna]
def get_posicao_vazia(grelha):

    
    linha = None
    coluna = None

    # Criar um 'array' com todas as posicoes vazias
    posicao_vazia = get_posicoes_vazias(grelha)

    # Escolher apenas UMA posicao          
    posicao_vazia = choice(posicao_vazia)

    # O indice zero refere-se a linha
    # O indice um refere-se a coluna
    linha = posicao_vazia[0]
    coluna = posicao_vazia [1]


    return [linha, coluna]

# Escolher ou um dois ou um quatro
def get_2ou4():
    
    #Random devolve um numero escolhido aleatoriamente entre 0.0 e 1.0

    # 90% das vezes tem de ser o numero 2
    # 10% das vezes tem de ser o numero 4
    if random() > 0.1:
        return 2
    else:
        return 4

# Inserir o valor (2 ou 4)
def inserir_2ou4(grelha):
    
    # Obtem um 2 com 90% probabilidade e um 4 com 10% probabilidade
    # Obtem a lista de posições vazias a partir da função get_posicoes_vazias
    # E a partir das posições vazias que encontrou põe aleatóriamente um 2 ou 4 comas probabilidade do #1
    # Finalmente coloca o numero
    
    dois_ou_quatro = get_2ou4()
    posicoes_vazias = get_posicoes_vazias(grelha)
    posicao_vazia = choice(posicoes_vazias)

    indice_linha = posicao_vazia[0]
    indice_coluna = posicao_vazia[1]
    grelha[indice_linha][indice_coluna] = dois_ou_quatro

# void NovoJogo ()
def novo_jogo():

    # Cria uma nova grelha vazia só com zeros
    # E coloca dois numeros aleatorios na grelha (2 ou 4)
    grelha = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    
    fim     = False
    vitoria = False
    pontos  = 0

    inserir_2ou4(grelha)
    inserir_2ou4(grelha)
    
    return(grelha, fim ,vitoria, pontos)
