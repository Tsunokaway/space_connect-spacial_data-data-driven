# ============================================================
# FIAP - Data Science
# Disciplina: Data Driven Application & Data Science
# Avaliação: 2026 - 1ª Global Solutions
# Integrantes: 
# (REPRESENTANTE) <Yasmin Yumi Tsunokawa>RM569408, 
# <Mariana Ayumi Dantas Kuramitsu>RM57278, 
# <Filipe Santos>RM572828
# ============================================================

tipos_eventos  = []
paises         = []
regioes        = []
cidades        = []
areas_afetadas = []
intensidades   = []
ocorrencias    = []

# ============================================================
# 1. ENTRADA DE DADOS
# ============================================================

# Solicita a quantidade de eventos com validação básica
while True:
        qtd = int(input("Insira a quantidade de eventos: "))
        if qtd > 0:
            break
        else:
            print("A quantidade deve ser maior que zero.")
    

# Loop para coletar os dados de cada evento
for i in range(qtd):
    print(f"\n--- Evento {i + 1} ---")

    # Tipo do evento 
    tipo = input("Tipo: ")
    tipos_eventos.append(tipo)

    # País 
    pais = input("País: ")
    paises.append(pais)

    # Região 
    regiao = input("Região: ")
    regioes.append(regiao)

    # Cidade 
    cidade = input("Cidade: ")
    cidades.append(cidade)

    # Área afetada (km²) — deve ser maior que zero
    while True:
        try:
            area = float(input("Área (km²): "))
            if area > 0:
                break
            else:
                print("A área deve ser maior que zero.")
        except ValueError:
            print("Valor inválido. Digite um número.")
    areas_afetadas.append(area)

    # Intensidade — deve estar entre 1 e 10
    while True:
        try:
            intensidade = int(input("Intensidade (1 a 10): "))
            if 1 <= intensidade <= 10:
                break
            else:
                print("A intensidade deve estar entre 1 e 10.")
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")
    intensidades.append(intensidade)

    # Número de ocorrências — deve ser maior que zero
    while True:
        try:
            ocorrencia = int(input("Ocorrências: "))
            if ocorrencia > 0:
                break
            else:
                print("O número de ocorrências deve ser maior que zero.")
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")
    ocorrencias.append(ocorrencia)

#a
total_eventos = (len(tipos_eventos))
#b
soma_areas_afetadas = sum(areas_afetadas)
#c
media_intensidade = sum(intensidades)/len(intensidades)
#d
indice = areas_afetadas.index(max(areas_afetadas))
evento_maior_area = tipos_eventos[indice]


#e. Região com maior número de ocorrências
regioes_unicas = []
for r in regioes:
    if r not in regioes_unicas:
        regioes_unicas.append(r)

soma_por_regiao = []
for i in regioes_unicas:
    soma = 0
    for indice in range(total_eventos):
        if regioes[indice] == r:
            soma += ocorrencias[indice]
    soma_por_regiao.append(soma)

regiao_mais_ocorrencias = regioes_unicas[soma_por_regiao.index(max(soma_por_regiao))]

#f. Densidade média (ocorrências ÷ área)
densidade_media= sum(ocorrencias) / sum(areas_afetadas)


#g. Quantidade de eventos acima da média de intensidade
qtde_eventos_acima_media = []
for i in range(len(intensidades)):
    if intensidades[i] > media_intensidade:
        qtde_eventos_acima_media.append(tipos_eventos[i])
qtde = len(qtde_eventos_acima_media)


#h. Identifique o evento mais crítico considerando:
#maior intensidade
#menor intensidade

indice_mais = intensidades.index(max(intensidades))
evento_mais_critico = tipos_eventos[indice_mais]

indice_menos = intensidades.index(min(intensidades))
evento_menos_critico = tipos_eventos[indice_menos]

print("\n" + "=" * 40)
print("        RELATÓRIO DE ANÁLISE")
print("=" * 40)
 
print(f"\nTotal de eventos registrados: {total_eventos}")
 
print("\n" + "-" * 40)
print("Resumo Geral")
print("-" * 40)
print(f"Área total afetada: {soma_areas_afetadas:.0f} km²")
print(f"Média de intensidade: {media_intensidade:.1f}")
 
print("\n" + "-" * 40)
print("Análises")
print("-" * 40)
print(f"Região com maior número de ocorrências: {regiao_mais_ocorrencias}")
print(f"Quantidade de eventos acima da média de intensidade: {qtde}")
print(f"Densidade média de ocorrências: {densidade_media:.2f} ocorrências/km²")
 
print("\n" + "-" * 40)
print("Evento Mais Crítico")
print("-" * 40)
print(f"Tipo: {evento_mais_critico}")
print(f"Local: {cidades[indice_mais]}, {regioes[indice_mais]}, {paises[indice_mais]}")
print(f"Intensidade: {intensidades[indice_mais]}")
print(f"Área afetada: {areas_afetadas[indice_mais]:.0f} km²")
 
print("\n" + "=" * 40)
print(f"Total de desastres registrados: {total_eventos}")