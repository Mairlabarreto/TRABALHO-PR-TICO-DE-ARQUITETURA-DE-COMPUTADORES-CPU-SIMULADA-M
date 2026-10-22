from cpu import CPU

def rodar_todos_os_testes():
    print("==================================")
    print("   INICIANDO TESTES AUTOMÁTICOS   ")
    print("==================================")
    
    # Teste de LOAD
    cpu = CPU()
    cpu.memoria[0] = "LOAD R0, 15"
    cpu.memoria[1] = "HALT"
    cpu.executar()
    assert cpu.registradores["R0"] == 15
    print("[PASSOU] Teste de LOAD")

    # Teste de STORE
    cpu2 = CPU()
    cpu2.memoria[0] = "LOAD R1, 42"
    cpu2.memoria[1] = "STORE R1, 10"
    cpu2.memoria[2] = "HALT"
    cpu2.executar()
    assert cpu2.memoria[10] == 42
    print("[PASSOU] Teste de STORE")

    # Teste de ULA (ADD e SUB)
    cpu3 = CPU()
    cpu3.memoria[0] = "LOAD R0, 20"
    cpu3.memoria[1] = "LOAD R1, 5"
    cpu3.memoria[2] = "ADD R0, R1"
    cpu3.memoria[3] = "SUB R0, R1"
    cpu3.memoria[4] = "HALT"
    cpu3.executar()
    assert cpu3.registradores["R0"] == 20
    print("[PASSOU] Teste de ULA (ADD e SUB)")

    print("==================================")
    print(" TODOS OS TESTES PASSARAM COM SUCESSO! ")
    print("==================================")

if __name__ == "__main__":
    rodar_todos_os_testes()
