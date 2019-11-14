"""
Ideia principal do algoritmo:

O algoritmo inicialmente realiza leitura do arquivo de acordo com a instância informada, retornando o cabeçalho com
as configurações de entrada. Em seguida a lista de tarefas é ordenada de forma decrescente a fim de alocar as tarefas
com maior tempo de execução primeiro. Após isso, com a função "resolve", tenta alocar o maior número de tarefas por
máquina. Antes de realizar a alocação da tarefa na máquina, é verificado se isso é possível, ou seja, se o tempo
total de execução das tarefas da máquina, não ultrapassa o deadline informado no arquivo de entrada. Ao realizar a
alocação da tarefa em determinada máquina, ela é adicionada na lista de tarefas concluídas e removida da lista de
tarefas. O método "resolve" termina quando a lista de tarefas estiver vazia. Por fim, é calculado a função objetivo
de acordo com a fórmula informada no enunciado do trabalho.
"""


def le_arquivo(arquivo):
    # Abre arquivo para leitura
    f = open("instances/" + arquivo, "r")

    # Pega as linhas
    linhas = f.readlines()

    # Pega as tres primeiras linhas (número de máquinas, número de itens n, due date d)
    cabecalho = [int(linhas[i].replace("\n", "")) for i in range(3)]

    # Lê as n linhas de tarefas
    lista_de_tarefas = [int(linhas[i].replace("\n", "")) for i in range(3, cabecalho[1])]

    # Retorna o cabeçalho e a lista de tarefas
    return cabecalho, lista_de_tarefas


def verifica_factibilidade(maquina, deadline, tarefa):
    # Checa se a máquina está vazia
    if len(maquina) == 0:
        return True
    # Verifica se o tempo da ultima, mais o tempo da tarefa a ser aloca é menor ou igual ao deadline
    if maquina[len(maquina) - 1] + tarefa <= deadline:
        return True
    # Caso contrário retorna false
    return False


def resolve(lista_de_tarefas, lista_de_maquinas, deadline):
    # Variável para critério de parada
    stop = False
    index_maquina = 0
    while not stop:
        # Vetor de tarefas concluídas da máquina index_maquina
        tarefas_concluidas = []

        # Para todas as tarefas na lista de tarefas
        for tarefa in lista_de_tarefas:
            # Verifica a factibilidade de alocação da tarefa na máquina index_maquina
            if verifica_factibilidade(lista_de_maquinas[index_maquina], deadline, tarefa):

                # Se a lista de máquina estiver vazia, apenas adiciona a tarefa na máquina
                if len(lista_de_maquinas[index_maquina]) == 0:
                    lista_de_maquinas[index_maquina].append(tarefa)
                # senão, soma o tempo da tarefa com o tempo da ultima tarefa da máquina
                else:
                    # Pega o tempo da ultima tarefa da máquina
                    tempo_ultima_tarefa_maquina = lista_de_maquinas[index_maquina][
                        len(lista_de_maquinas[index_maquina]) - 1]
                    # Adiciona a tarefa com tempo atualizado na lista de máquinas
                    lista_de_maquinas[index_maquina].append(tarefa + tempo_ultima_tarefa_maquina)

                # Adiciona a tarefa na lista de tarefas concluídas
                tarefas_concluidas.append(tarefa)

        # Remove todas as tarefas concluídas da lista de tarefas
        for tarefa in tarefas_concluidas:
            lista_de_tarefas.remove(tarefa)

        # Se a lista de tarefas estiver vazia, sai do while
        if not lista_de_tarefas:
            stop = True

        # Soma a o indexe de máquinas
        index_maquina += 1

        # Verifica se ultrapassou o número de máquinas disponíveis
        if index_maquina == len(lista_de_maquinas):
            # se ultrapassou, reseta a lista de maquinas e são do while
            lista_de_maquinas = []
            stop = True

    # Retorna a lista de máquinas com as listas de tarefas
    return lista_de_maquinas


def calcula_funcao_objetivo(lista_de_maquinas, deadline):
    # Inicializa variável de soma da f.o.
    soma = 0

    # Para todas as maquinas,
    for maquina in lista_de_maquinas:
        # e para todas as tarefas das máquinas
        for tarefa in maquina:
            # realiza a soma da diferença do deadline com tarefa
            soma += deadline - tarefa
    # Retorna a soma
    return soma


def run(instancia):
    # Lê entradas do arquivo
    cabecalho, lista_de_tarefas = le_arquivo(instancia)

    # numero de tarefas
    numero_de_tarefas = cabecalho[1]

    # Tempo máximo
    deadline = cabecalho[2]

    # Lista de máquina
    lista_de_maquinas = [[] for _ in range(cabecalho[0])]

    # Ordena a lista de tarefas decrescente
    lista_de_tarefas.sort(reverse=True)

    lista_de_maquinas = resolve(lista_de_tarefas, lista_de_maquinas, deadline)

    # Verifica se a lista de máquinas é vazia, se for vazia, foi informado na função resolve que
    # ultrapassou o número de maquinas disponíveis
    if not lista_de_maquinas:
        print("Solução não encontrada.")
    else:
        print("Valor de função objetivo: " + str(calcula_funcao_objetivo(lista_de_maquinas, deadline)))


if __name__ == '__main__':
    instancias = [
        "bpwt_500_1.dat",
        "bpwt_500_2.dat",
        "bpwt_500_3.dat",
        "bpwt_500_4.dat",
        "bpwt_1000_1.dat",
        "bpwt_1000_2.dat",
        "bpwt_1000_3.dat",
        "bpwt_1000_4.dat",
        "bpwt_2000_1.dat",
        "bpwt_2000_2.dat",
        "bpwt_2000_3.dat",
        "bpwt_2000_4.dat"
    ]

    for instancia in instancias:
        print("Executando: " + instancia)
        run(instancia)
        print()
