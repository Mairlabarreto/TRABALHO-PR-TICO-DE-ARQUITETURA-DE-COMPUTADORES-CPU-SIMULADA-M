class CPU:
    def __init__(self):
        # Registradores gerais de 8 bits
        self.registradores = {
            "R0": 0,
            "R1": 0,
            "R2": 0,
            "R3": 0
        }
        # Memória com 16 posições (índices 0 a 15)
        self.memoria = [0] * 16
        # Program Counter (indica a próxima instrução)
        self.pc = 0
        # Estado de execução da CPU
        self.halted = False

    # Garante que os valores respeitem o limite de 8 bits (0 a 255)
    def limitar_8bits(self, valor):
        return valor & 0xFF

    # ULA: Unidade Lógica e Aritmética
    def ula(self, operacao, a, b):
        if operacao == "ADD":
            resultado = a + b
        elif operacao == "SUB":
            resultado = a - b
        elif operacao == "AND":
            resultado = a & b
        elif operacao == "OR":
            resultado = a | b
        elif operacao == "XOR":
            resultado = a ^ b
        else:
            raise ValueError("Operação da ULA inválida")
        return self.limitar_8bits(resultado)

    # EXECUÇÃO DE UMA INSTRUÇÃO (Decodifica e Executa)
    def executar_instrucao(self, instrucao):
        if not isinstance(instrucao, str):
            raise ValueError(f"Instrução inválida no PC {self.pc}: {instrucao}")

        # Limpa vírgulas e separa a instrução dos operandos
        partes = instrucao.replace(",", "").split()
        operacao = partes[0]

        # 1. LOAD reg, valor
        if operacao == "LOAD":
            registrador = partes[1]
            valor = int(partes[2])
            self.registradores[registrador] = self.limitar_8bits(valor)
            self.pc += 1

        # 2. STORE reg, endereco
        elif operacao == "STORE":
            registrador = partes[1]
            endereco = int(partes[2])
            valor = self.registradores[registrador]
            self.memoria[endereco] = valor
            self.pc += 1

        # 3. ADD regA, regB (regA = regA + regB)
        elif operacao == "ADD":
            reg_destino = partes[1]
            reg_origem = partes[2]
            a = self.registradores[reg_destino]
            b = self.registradores[reg_origem]
            self.registradores[reg_destino] = self.ula("ADD", a, b)
            self.pc += 1

        # 4. SUB regA, regB (regA = regA - regB)
        elif operacao == "SUB":
            reg_destino = partes[1]
            reg_origem = partes[2]
            a = self.registradores[reg_destino]
            b = self.registradores[reg_origem]
            self.registradores[reg_destino] = self.ula("SUB", a, b)
            self.pc += 1

        # 5. AND regA, regB
        elif operacao == "AND":
            reg_destino = partes[1]
            reg_origem = partes[2]
            a = self.registradores[reg_destino]
            b = self.registradores[reg_origem]
            self.registradores[reg_destino] = self.ula("AND", a, b)
            self.pc += 1

        # 6. OR regA, regB
        elif operacao == "OR":
            reg_destino = partes[1]
            reg_origem = partes[2]
            a = self.registradores[reg_destino]
            b = self.registradores[reg_origem]
            self.registradores[reg_destino] = self.ula("OR", a, b)
            self.pc += 1

        # 7. XOR regA, regB
        elif operacao == "XOR":
            reg_destino = partes[1]
            reg_origem = partes[2]
            a = self.registradores[reg_destino]
            b = self.registradores[reg_origem]
            self.registradores[reg_destino] = self.ula("XOR", a, b)
            self.pc += 1

        # 8. JMP endereco (Desvio incondicional)
        elif operacao == "JMP":
            endereco = int(partes[1])
            self.pc = endereco

        # 9. HALT (Encerra a execução)
        elif operacao == "HALT":
            self.halted = True
            self.pc += 1

        else:
            raise ValueError(f"Instrução desconhecida: {operacao}")

    # CICLO DA CPU: Fetch -> Decode -> Execute
    def ciclo(self):
        if self.pc >= len(self.memoria):
            self.halted = True
            return
        
        # FETCH: Busca instrução na memória apontada pelo PC
        instrucao = self.memoria[self.pc]
        print("-" * 40)
        print(f"PC: {self.pc:02d} | Instrução atual: {instrucao}")
        
        # DECODE + EXECUTE
        self.executar_instrucao(instrucao)
        
        # Mostra o estado atual dos registradores após o ciclo
        self.mostrar_estado()

    # EXECUÇÃO COMPLETA (Loop do ciclo)
    def executar(self):
        while not self.halted and self.pc < len(self.memoria):
            self.ciclo()

    # MOSTRAR ESTADO (Exigido no passo a passo)
    def mostrar_estado(self):
        print("Registradores:")
        for nome, valor in self.registradores.items():
            print(f"  {nome} = {valor:02X} (Decimal: {valor})")
            
