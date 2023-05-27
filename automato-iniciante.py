# Definição do AFND
qtd_estados = int (input('Digite quantos estados terá o automato: '))
estados = []
for i in range(qtd_estados):
    estado = input(f'Digite o {i+1}° estado: ')
    estados.append(estado)

print(estados)

qtd_simbolos = int(input('Digite quantos simbolos terá o automato: '))
simbolos = []
for i in range(qtd_simbolos):
    simbolo = input(f'Digite o {i+1}° simbolo: ')
    simbolos.append(simbolo)

print(simbolos)

qtd_estados_finais = int (input('Digite quantos estados finais terá o automato: '))
estados_finais = []
for i in range(qtd_estados_finais):
    estado_final = input(f'Digite o {i+1}° estado final: ')
    estados_finais.append(estado_final)

print(estados_finais)

estado_inicial = input('Digite o estado inicial do automato: ')

qtd_cadeias_entrada = int (input('Digite quantas cadeias de entrada terá o automato: '))
cadeias_entrada = []
for i in range(qtd_cadeias_entrada):
    cadeia_entrada = input(f'Digite a {i+1}ª cadeia de entrada: ')
    cadeias_entrada.append(cadeia_entrada)

print(cadeias_entrada)

transicoes = {}

for e in estados:
    for s in simbolos:
        transicoes[(e, s)] = set()

for e in estados:
    for s in simbolos:
        qtd_transicoes = int (input(f'Para o estado {e} e simbolo {s} quantas serão as trasições: '))
        for i in range(qtd_transicoes):
            transicao = input(f'Digite a {i+1}ª transição do estado {e} quando recebe o simbolo {s}: ')
            transicoes[(e, s)].add(transicao)

print(transicoes)
#estados = {'q0', 'q1', 'q2'}
#simbolos = {'0', '1'}
#transicoes = {
#    ('q0', '0'): {'q0', 'q1'},
#    ('q0', '1'): {'q0'},
#    ('q1', '1'): {'q2'},
#    ('q2', '0'): {'q2'}
#}
#estado_inicial = 'q0'
#estados_finais = {'q2', 'q1'}

# Testando cadeias de entrada
#cadeias_entrada = ['001', '110', '10', '0001']

for cadeia in cadeias_entrada:
    estados_atuais = {estado_inicial}

    i = 0
    while i < len(cadeia):
        simbolo = cadeia[i]

        proximos_estados = set()

        for estado in estados_atuais:
            if (estado, simbolo) in transicoes:
                prox_estados = transicoes[(estado, simbolo)]
                proximos_estados.update(prox_estados)

        estados_atuais = proximos_estados

        i += 1

    if estados_atuais.intersection(estados_finais):
        print(f'A cadeia "{cadeia}" é ACEITA pelo AFND.')
    else:
        print(f'A cadeia "{cadeia}" é RECUSADA pelo AFND.')
