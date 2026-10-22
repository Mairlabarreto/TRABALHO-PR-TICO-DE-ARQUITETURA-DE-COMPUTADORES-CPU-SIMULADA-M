# Simulador de CPU de 8 Bits em Python

Trabalho prático individual ou em dupla desenvolvido para a disciplina de Arquitetura de Computadores (2026.2).  
Universidade Federal do Ceará (UFC) - Campus Sobral  
Professor: Wendley S. Silva  

---

## 1. Visão Geral da Arquitetura

O projeto consiste na implementação de um modelo funcional e didático de uma CPU de 8 bits em Python. O objetivo é integrar em um único módulo os conceitos de Unidade Lógica e Aritmética (ULA), registradores de uso geral, memória principal, conjunto reduzido de instruções e o ciclo de execução passo a passo.

### Especificações Técnicas:
* Tamanho dos Dados: 8 bits (valores delimitados entre 0 e 255 / 0x00 a 0xFF)
* Registradores de Uso Geral: R0, R1, R2 e R3 (8 bits cada)
* Contador de Programa (PC): Registrador ponteiro para a próxima instrução a ser executada
* Memória Principal: 16 posições de 8 bits (endereços de 0 a 15)
* ULA: Suporte às operações ADD, SUB, AND, OR e XOR
* Ciclo de Execução: Sequência conceitual Fetch -> Decode -> Execute

---

## 2. Conjunto de Instruções

| Instrução | Exemplo | Função |
| :--- | :--- | :--- |
| LOAD | LOAD R0, 5 | Armazena um valor imediato no registrador especificado |
| STORE | STORE R0, 15 | Grava o conteúdo do registrador na posição de memória especificada |
| ADD | ADD R0, R1 | R0 <- R0 + R1 |
| SUB | SUB R0, R1 | R0 <- R0 - R1 |
| AND | AND R0, R1 | R0 <- R0 AND R1 (E lógico bit a bit) |
| OR | OR R0, R1 | R0 <- R0 OR R1 (OU lógico bit a bit) |
| XOR | XOR R0, R1 | R0 <- R0 XOR R1 (OU Exclusivo bit a bit) |
| JMP | JMP 8 | Altera o PC diretamente para o endereço especificado |
| HALT | HALT | Interrompe o ciclo de execução do processador |

---

## 3. Ciclo de Execução (Fetch -> Decode -> Execute)

1. FETCH: A CPU busca na memória a instrução armazenada no endereço apontado pelo PC.
2. DECODE: A Unidade de Controle identifica a operação e separa os operandos e registradores envolvidos.
3. EXECUTE: A operação é realizada na ULA ou na memória, atualizando o estado dos registradores e avançando o PC para a próxima instrução (exceto em desvios como JMP).

---

## 4. Estrutura dos Arquivos do Projeto

* cpu.py: Classe principal contendo os registradores, memória, ULA e o ciclo Fetch-Decode-Execute.
* main.py: Script principal contendo o programa de teste obrigatório e o programa próprio estendido.
* README.md: Documentação técnica da arquitetura simulada.

---

## 5. Como Executar

Para executar a simulação passo a passo no terminal, certifique-se de ter o Python 3 instalado e execute o seguinte comando no diretório do projeto:

python main.py

---

## 6. Informações de Entrega

* Link do Vídeo de Apresentação: [INSERIR LINK DO VÍDEO AQUI]
* Aluno: MAIRLA DE FATIMA RODRIGUES BARRETO - 588067
