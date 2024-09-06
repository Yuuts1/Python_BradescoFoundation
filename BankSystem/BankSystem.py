class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")
    
    def saque(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para saque.")
        else:
            print("O valor do saque deve ser positivo.")
    
    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

def main():
    print("Bem-vindo ao sistema bancário!")
    
    nome = input("Digite o nome do titular da conta: ")
    conta = ContaBancaria(nome)
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Depósito")
        print("2. Saque")
        print("3. Consultar Saldo")
        print("4. Sair")
        
        escolha = input("Digite o número da opção desejada: ")
        
        if escolha == '1':
            valor = float(input("Digite o valor do depósito: R$"))
            conta.deposito(valor)
        elif escolha == '2':
            valor = float(input("Digite o valor do saque: R$"))
            conta.saque(valor)
        elif escolha == '3':
            conta.consultar_saldo()
        elif escolha == '4':
            print("Obrigado por usar o sistema bancário. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
