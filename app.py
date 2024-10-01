# app.py

def soma(a, b):
    """Função simples que soma dois números."""
    return a + b

def subtrai(a, b):
    """Função simples que subtrai dois números."""
    return a - b

def multiplica(a, b):
    """Função simples que multiplica dois números."""
    return a * b

def divide(a, b):
    """Função simples que divide dois números.
    Retorna uma mensagem de erro se a divisão por zero for tentada.
    """
    if b == 0:
        return "Erro: Divisão por zero não permitida"
    return a / b

if __name__ == "__main__":
    resultado_soma = soma(2, 3)
    resultado_subtracao = subtrai(10, 4)
    resultado_multiplicacao = multiplica(5, 6)
    resultado_divisao = divide(8, 2)
    resultado_divisao_erro = divide(5, 0)
    
    print(f"O resultado da soma é {resultado_soma}")
    print(f"O resultado da subtração é {resultado_subtracao}")
    print(f"O resultado da multiplicação é {resultado_multiplicacao}")
    print(f"O resultado da divisão é {resultado_divisao}")
    print(f"Tentativa de divisão por zero: {resultado_divisao_erro}")
