from colorama import Fore

print(Fore.BLUE + "Bem vindo a calculadora do Miguel!")
print(Fore.WHITE + "")
nome = input("Qual seu nome? ")
print(Fore.WHITE + f"Certo {nome}, para usa-la é so digitar dois numeros e eu irei multiplicar eles para você.")

try:
    numero1 = int(input(Fore.BLACK + "Digite o primeiro numero: "))
    numero2 = int(input(Fore.BLACK + "Digite o segundo numero: "))
    resultado = numero1 * numero2
    print(Fore.GREEN + f"O resultado é {resultado}")
    print(Fore.WHITE + "")
except ValueError:
    print(Fore.RED + "Por favor, digite apenas numeros.")