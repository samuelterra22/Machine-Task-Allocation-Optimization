# Machine Task Allocation Optimization

### Install linux dependencies

```shell script
sudo apt update
sudo apt install build-essential \
                 software-properties-common \
                 python3-pip \
                 python3-distutils
```

### Create environment and install python dependencies

```shell script
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Instance

Um conjunto de n tarefas, cada uma com tempo de processamento p[i] não negativos
, i=f, ..., n e número m de máquinas disponíveis e um deadline d.

### Solution

Determinar:
    (i) uma distribuição das tarefas às máquinas, tal que cada tarefa esteha em exatamente
    uma máquina;
    (ii) tempos de início s[i], i=1, ..., n, de cada tarefa, tal que tarefas na mesma
    máquina não tenham sobreposição durante as execuções, e tal que nenhuma tarefa
    termine depois do deadline.
    
### Goal

Minimizar o tempo de espera total das taredas antes do deadline, ou seja,
min...