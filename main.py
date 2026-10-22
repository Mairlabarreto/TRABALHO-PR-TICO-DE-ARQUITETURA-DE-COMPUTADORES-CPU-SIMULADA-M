from cpu import CPU

def rodar_programa_exemplo():
    print("========================================")
    print("   TESTE OBRIGATÓRIO: SOMA (5 + 8 = 13)  ")
    print("========================================")
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 5"
    cpu.memoria[1] = "LOAD R1, 8"
    cpu.memoria[2] = "ADD R0, R1"
    cpu.memoria[3] = "STORE R0, 15"
    cpu.memoria[4] = "HALT"
    
    cpu.executar()
    print(f"\n[FIM] Memória[15] esperada = 13 | Obtida = {cpu.memoria[15]}")


def rodar_programa_proprio():
    print("\n========================================")
    print("   PROGRAMA PRÓPRIO (>= 8 Instruções)   ")
    print("========================================")
    # Lógica do programa próprio:
    # 1. Carrega 25 em R0
    # 2. Carrega 10 em R1
    # 3. Subtrai R1 de R0 (R0 = 15)
    # 4. Carrega 12 em R2
    # 5. Faz OR entre R0 e R2 (15 | 12 = 15)
    # 6. Carrega 3 em R3
    # 7. Faz XOR entre R0 e R3 (15 ^ 3 = 12)
    # 8. Salva o resultado final de R0 na posição 12 da memória
    # 9. Para a execução (HALT)
    
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 25"  # Instrução 1
    cpu.memoria[1] = "LOAD R1, 10"  # Instrução 2
    cpu.memoria[2] = "SUB R0, R1"   # Instrução 3 (R0 vira 15)
    cpu.memoria[3] = "LOAD R2, 12"  # Instrução 4
    cpu.memoria[4] = "OR R0, R2"    # Instrução 5 (15 | 12 = 15)
    cpu.memoria[5] = "LOAD R3, 3"   # Instrução 6
    cpu.memoria[6] = "XOR R0, R3"   # Instrução 7 (15 ^ 3 = 12)
    cpu.memoria[7] = "STORE R0, 12" # Instrução 8 (Salva 12 na mem[12])
    cpu.memoria[8] = "HALT"         # Instrução 9 (Encerra

    cpu.executar()
    print(f"\n[FIM] Memória[12] esperada = 12 | Obtida = {cpu.memoria[12]}")


if __name__ == "__main__":
    rodar_programa_exemplo()
    print("\n" + "="*40 + "\n")
    rodar_programa_proprio()