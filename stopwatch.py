import time

def cronometro():
    print("=== Cronômetro ===")
    print("Comandos:")
    print("[I] Iniciar")
    print("[P] Pausar")
    print("[R] Reiniciar")
    print("[S] Sair")

    segundos = 0
    rodando = False

    while True:
        comando = input("\nDigite um comando: ").strip().upper()

        if comando == "I":
            if not rodando:
                rodando = True 
                print("Cronômetro iniciado!")
                while rodando:
                    try:
                        print(f"\rTempo: {segundos} segundos", end="")
                        time.sleep(1)
                        segundos += 1
                    except KeyboardInterrupt:
                        print("\nPausado. Pressione [R] para reiniciar ou [S] para sair.")
                        rodando = False
        elif comando == "P":
            rodando = False
            print(f"\nCronômetro pausado em {segundos} segundos.")
        elif comando == "R":
            segundos = 0
            print("Cronômetro reiniciado!")
        elif comando == "S":
            print("Encerrando o cronômetro. Até logo!")
            break
        else:
            print("Comando inválido. Tente novamente.")

if __name__ == "__main__":
    cronometro()
