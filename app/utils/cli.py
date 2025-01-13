from app.models.ia import IA
from app.models.environment import Environment
from colorama import Fore, Style

ia_atual = None
ambiente_atual = None

def menu():
    global ia_atual, ambiente_atual  
    while True:
        print(Fore.CYAN + "\n=== SentienceSim - Simulador de IA ===" + Style.RESET_ALL)
        print(Fore.YELLOW + "=" * 50 + Style.RESET_ALL)
        print(Fore.GREEN + "[1] Criar IA 🤖" + Style.RESET_ALL)
        print(Fore.GREEN + "[2] Criar Ambiente 🌍" + Style.RESET_ALL)
        print(Fore.GREEN + "[3] Simular Interação ⚙️" + Style.RESET_ALL)
        print(Fore.RED + "[4] Sair 🏩" + Style.RESET_ALL)
        print(Fore.YELLOW + "=" * 50 + Style.RESET_ALL)
        opcao = input(Fore.CYAN + "Escolha uma opção: " + Style.RESET_ALL)

        if opcao == "1":
            # Criar IA
            nome = input(Fore.CYAN + "Digite o nome da IA: " + Style.RESET_ALL).strip()
            if not nome:
                print(Fore.RED + "⚠️ O nome da IA não pode ser vazio. Tente novamente." + Style.RESET_ALL)
                continue

            capacidades = input(Fore.CYAN + "Digite as capacidades da IA separadas por vírgula: " + Style.RESET_ALL).split(",")
            capacidades = [cap.strip().lower() for cap in capacidades if cap.strip()]
            if not capacidades:
                print(Fore.RED + "⚠️ A IA precisa de pelo menos uma capacidade. Tente novamente." + Style.RESET_ALL)
                continue

            ia_atual = IA(nome, capacidades)
            print(Fore.GREEN + f"✅ IA criada: {ia_atual}" + Style.RESET_ALL)

        elif opcao == "2":
            # Criar Ambiente
            descricao = input(Fore.CYAN + "Digite a descrição do ambiente: " + Style.RESET_ALL).strip()
            if not descricao:
                print(Fore.RED + "⚠️ A descrição do ambiente não pode ser vazia. Tente novamente." + Style.RESET_ALL)
                continue

            desafios = input(Fore.CYAN + "Digite os desafios do ambiente separados por vírgula: " + Style.RESET_ALL).split(",")
            desafios = [des.strip().lower() for des in desafios if des.strip()]
            if not desafios:
                print(Fore.RED + "⚠️ O ambiente precisa de pelo menos um desafio. Tente novamente." + Style.RESET_ALL)
                continue

            ambiente_atual = Environment(descricao, desafios)
            print(Fore.GREEN + f"✅ Ambiente criado: {ambiente_atual}" + Style.RESET_ALL)

        elif opcao == "3":
            # Simular Interação
            if not ia_atual:
                print(Fore.RED + "⚠️ Nenhuma IA criada. Crie uma IA primeiro!" + Style.RESET_ALL)
            elif not ambiente_atual:
                print(Fore.RED + "⚠️ Nenhum ambiente criado. Crie um ambiente primeiro!" + Style.RESET_ALL)
            else:
                print(Fore.MAGENTA + "\n🤖 Iniciando a simulação..." + Style.RESET_ALL)
                desafios = ambiente_atual.challenges
                capacidades = ia_atual.capabilities

                sucessos = 0
                for desafio in desafios:
                    if desafio in capacidades:
                        print(Fore.GREEN + f"✅ {ia_atual.name} superou o desafio: {desafio}!" + Style.RESET_ALL)
                        sucessos += 1
                    else:
                        print(Fore.RED + f"❌ {ia_atual.name} falhou no desafio: {desafio}." + Style.RESET_ALL)

                total_desafios = len(desafios)
                print(Fore.CYAN + "\n--- Resumo da Simulação ---" + Style.RESET_ALL)
                print(Fore.YELLOW + f"Desafios Superados: {sucessos}/{total_desafios}" + Style.RESET_ALL)
                nota = (sucessos / total_desafios) * 10 if total_desafios > 0 else 0
                print(Fore.YELLOW + f"Nota da IA: {nota:.1f}" + Style.RESET_ALL)

                if nota > 8:
                    print(Fore.GREEN + "✨ Desempenho: Excelente! Sua IA está muito preparada!" + Style.RESET_ALL)
                elif nota > 5:
                    print(Fore.YELLOW + "⚡ Desempenho: Regular. Sua IA está na média, mas pode melhorar." + Style.RESET_ALL)
                else:
                    print(Fore.RED + "💥 Desempenho: Fraco. Sua IA precisa de mais capacidades!" + Style.RESET_ALL)

        elif opcao == "4":
            print(Fore.GREEN + "Saindo... 👋" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "⚠️ Opção inválida. Tente novamente." + Style.RESET_ALL)

if __name__ == '__main__':
    menu()
