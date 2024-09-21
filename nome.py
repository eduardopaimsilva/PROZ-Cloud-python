def obter_informacoes():
    while True:
        try:
            nome = input("Digite seu nome completo: ")
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            
            # Verificar se o ano de nascimento está no intervalo correto
            if ano_nascimento < 1922 or ano_nascimento > 2021:
                print("Erro: O ano de nascimento deve ser entre 1922 e 2021.")
                continue

            idade = 2022 - ano_nascimento
            print(f"\nNome: {nome}")
            print(f"Idade que completou ou completará em 2022: {idade} anos")
            break

        except ValueError:
            print("Erro: Por favor, insira um ano válido.")

# Chamar a função
obter_informacoes()
