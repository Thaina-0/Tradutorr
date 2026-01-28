num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

soma: int = int(num1 + num2)
multiplicacao: int = int(num1 * num2)
subtracao: int = int(num1 - num2)

if num2 != 0:
    divisao: float = num1/num2
else:
    divisao = "Erro, divisao por zero"

print(f"soma: {soma}\n multiplicacao: {multiplicacao}\n subtracao: {subtracao}\n divisao: {divisao}")

