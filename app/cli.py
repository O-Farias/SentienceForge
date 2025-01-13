from app.models.ia import IA
from app.models.environment import Environment
from app.services.interaction_service import executar_interacao
from colorama import Fore, Style

def menu():
    while True:
        print(Fore.CYAN + "\n=== SentienceSim - Simulador de IA ===" + Style.RESET_ALL)
        print(Fore.YELLOW + "=" * 50 + Style.RESET_ALL)
        print(Fore.GREEN + "[1]" + Style.RESET_ALL + " Criar IA")
        print(Fore.GREEN + "[2]" + Style.RESET_ALL + " Criar Ambiente")
        print(Fore.GREEN + "[3]" + Style.RESET_ALL + " Simular Interação")
        print(Fore.RED + "[4] Sair" + Style.RESET_ALL)
        opcao = input(Fore.CYAN + "Escolha uma opção: " + Style.RESET_ALL)

        if opcao == "1":
            # Criar IA
            nome = input(Fore.CYAN + "Digite o nome da IA: " + Style.RESET_ALL)
            capacidades = input(Fore.CYAN + "Digite as capacidades da IA separadas por vírgula: " + Style.RESET_ALL).split(",")
            ia = IA(nome, [cap.strip() for cap in capacidades])
            print(Fore.GREEN + f"✅ IA criada: {ia}" + Style.RESET_ALL)

        elif opcao == "2":
            # Criar Ambiente
            descricao = input(Fore.CYAN + "Digite a descrição do ambiente: " + Style.RESET_ALL)
            desafios = input(Fore.CYAN + "Digite os desafios do ambiente separados por vírgula: " + Style.RESET_ALL).split(",")
            ambiente = Environment(descricao, [des.strip() for des in desafios])
            print(Fore.GREEN + f"✅ Ambiente criado: {ambiente}" + Style.RESET_ALL)

        elif opcao == "3":
            # Simular Interação
            if 'ia' in locals() and 'ambiente' in locals():
                executar_interacao(ia, ambiente)
            else:
                print(Fore.RED + "⚠️ Crie uma IA e um Ambiente primeiro!" + Style.RESET_ALL)

        elif opcao == "4":
            print(Fore.GREEN + "Saindo... 👋" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "⚠️ Opção inválida. Tente novamente." + Style.RESET_ALL)

if __name__ == '__main__':
    menu()
