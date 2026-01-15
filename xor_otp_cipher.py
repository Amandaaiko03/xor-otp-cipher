import os

def gerar_chave(tamanho):

    return os.urandom(tamanho)

def xor_operacao(conteudo_bytes, chave_bytes):
    """
    Realiza a operação XOR (OU-EXCLUSIVO) byte a byte.

    """
    # Cria uma lista de bytes resultantes da operação XOR entre cada par
    resultado = bytes([b1 ^ b2 for b1, b2 in zip(conteudo_bytes, chave_bytes)])
    return resultado

def cifrar():
    mensagem = input("\n[CIFRAR] Digite a mensagem: ")
    if not mensagem:
        print("Erro: A mensagem não pode ser vazia.")
        return

    # Converter string para bytes 
    mensagem_bytes = mensagem.encode('utf-8')
    
    # Gerar One-Time Pad 
    chave = gerar_chave(len(mensagem_bytes))
    
    # Realizar a operação XOR
    mensagem_cifrada = xor_operacao(mensagem_bytes, chave)
    
    print("-" * 40)
    print(f"Mensagem Original: {mensagem}")
    print(f"CHAVE: {chave.hex()}")
    print(f"MENSAGEM CIFRADA:     {mensagem_cifrada.hex()}")
    print("-" * 40)

def decifrar():
    print("\n[DECIFRAR] - Use os valores em Hexadecimal gerados anteriormente.")
    try:
        msg_hex = input("Cole a MENSAGEM CIFRADA (hex): ")
        chave_hex = input("Cole a CHAVE (hex): ")
        
        # Converter de Hexadecimal de volta para bytes
        mensagem_cifrada_bytes = bytes.fromhex(msg_hex)
        chave_bytes = bytes.fromhex(chave_hex)
        
        # Verificar se tamanhos batem 
        if len(mensagem_cifrada_bytes) != len(chave_bytes):
            print("Erro: A chave deve ter o mesmo tamanho da mensagem cifrada!")
            return

        # A operação inversa do XOR é o próprio XOR
        mensagem_decifrada_bytes = xor_operacao(mensagem_cifrada_bytes, chave_bytes)
        
        # Converte de volta para texto legível
        print("-" * 40)
        print(f"MENSAGEM ORIGINAL: {mensagem_decifrada_bytes.decode('utf-8')}")
        print("-" * 40)
        
    except ValueError:
        print("Erro: Certifique-se de colar apenas os caracteres hexadecimais corretos.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def menu():
    while True:
        print("\n=== SISTEMA DE CRIPTOGRAFIA XOR (ONE-TIME PAD) ===")
        print("1. Cifrar mensagem")
        print("2. Decifrar mensagem")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            cifrar()
        elif escolha == '2':
            decifrar()
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()