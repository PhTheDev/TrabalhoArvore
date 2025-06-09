import csv
from datetime import datetime

class Pessoa:
    def __init__(self, cpf, rg, nome, data_nasc, cidade):
        self.cpf = cpf.strip()
        self.rg = rg.strip()
        self.nome = nome.strip()
        # Converte string para objeto data (remove espaços extras)
        self.data_nasc = datetime.strptime(data_nasc.replace(" ", ""), "%d/%m/%Y")
        self.cidade = cidade.strip()
    
    def __str__(self):
        return f"CPF: {self.cpf} | Nome: {self.nome} | Nasc: {self.data_nasc.strftime('%d/%m/%Y')} | Cidade: {self.cidade}"

class NoAVL:
    def __init__(self, chave, pessoa):
        self.chave = chave
        self.pessoa = pessoa  # Armazena referência ao objeto
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None
    
    def altura(self, no):
        return no.altura if no else 0
    
    def atualizar_altura(self, no):
        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))
    
    def balanceamento(self, no):
        return self.altura(no.esquerda) - self.altura(no.direita) if no else 0
    
    def rotacao_direita(self, y):
        x = y.esquerda
        T2 = x.direita
        
        x.direita = y
        y.esquerda = T2
        
        self.atualizar_altura(y)
        self.atualizar_altura(x)
        
        return x
    
    def rotacao_esquerda(self, x):
        y = x.direita
        T2 = y.esquerda
        
        y.esquerda = x
        x.direita = T2
        
        self.atualizar_altura(x)
        self.atualizar_altura(y)
        
        return y
    
    def inserir(self, raiz, chave, pessoa):
        if not raiz:
            return NoAVL(chave, pessoa)
        
        if chave < raiz.chave:
            raiz.esquerda = self.inserir(raiz.esquerda, chave, pessoa)
        elif chave > raiz.chave:
            raiz.direita = self.inserir(raiz.direita, chave, pessoa)
        else:
            # Chaves iguais (pode acontecer em nomes/datas)
            return raiz
        
        self.atualizar_altura(raiz)
        
        balance = self.balanceamento(raiz)
        
        # Casos de desbalanceamento
        if balance > 1 and chave < raiz.esquerda.chave: 
            # Caso LL (Left-Left): Desbalanceamento à esquerda + filho à esquerda
            return self.rotacao_direita(raiz)
            
        if balance < -1 and chave > raiz.direita.chave:
            # Caso RR (Right-Right): Desbalanceamento à direita + filho à direita
            return self.rotacao_esquerda(raiz)
            
        if balance > 1 and chave > raiz.esquerda.chave:
            # Caso LR (Left-Right): Desbalanceamento à esquerda + filho à direita
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)
            
        if balance < -1 and chave < raiz.direita.chave:
            # Caso RL (Right-Left): Desbalanceamento à direita + filho à esquerda
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)
            
        return raiz
    
    def buscar_cpf(self, raiz, cpf):
        if not raiz:
            return None
            
        if cpf < raiz.chave:
            return self.buscar_cpf(raiz.esquerda, cpf)
        elif cpf > raiz.chave:
            return self.buscar_cpf(raiz.direita, cpf)
        else:
            return raiz.pessoa
    
    def buscar_nome_prefixo(self, raiz, prefixo, resultados):
        if raiz:
            if raiz.chave.startswith(prefixo):
                resultados.append(raiz.pessoa)
            self.buscar_nome_prefixo(raiz.esquerda, prefixo, resultados)
            self.buscar_nome_prefixo(raiz.direita, prefixo, resultados)
    
    def buscar_data_intervalo(self, raiz, inicio, fim, resultados):
        if raiz:
            if inicio <= raiz.chave <= fim:
                resultados.append(raiz.pessoa)
            if inicio < raiz.chave:
                self.buscar_data_intervalo(raiz.esquerda, inicio, fim, resultados)
            if fim > raiz.chave:
                self.buscar_data_intervalo(raiz.direita, inicio, fim, resultados)

# Carregar dados do arquivo CSV
def carregar_dados(nome_arquivo):
    pessoas = []
    with open(nome_arquivo, 'r', encoding='utf-8') as file:
        leitor = csv.reader(file, delimiter=';')
        for linha in leitor:
            if len(linha) == 5:
                pessoas.append(Pessoa(*linha))
    return pessoas

# Menu principal
def main():
    # Inicializar árvores
    arvore_cpf = ArvoreAVL()
    arvore_nome = ArvoreAVL()
    arvore_data = ArvoreAVL()
    
    # Carregar dados
    arquivo = input("Digite o nome do arquivo: ")
    pessoas = carregar_dados(arquivo)
    
    # Construir índices
    for p in pessoas:
        arvore_cpf.raiz = arvore_cpf.inserir(arvore_cpf.raiz, p.cpf, p)
        arvore_nome.raiz = arvore_nome.inserir(arvore_nome.raiz, p.nome, p)
        arvore_data.raiz = arvore_data.inserir(arvore_data.raiz, p.data_nasc, p)
    
    while True:
        print("\n--- MENU DE CONSULTAS ---")
        print("1. Buscar por CPF")
        print("2. Buscar por prefixo de nome")
        print("3. Buscar por intervalo de datas")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cpf = input("Digite o CPF: ").strip()
            pessoa = arvore_cpf.buscar_cpf(arvore_cpf.raiz, cpf)
            print("\nRESULTADO:")
            print(pessoa if pessoa else "Pessoa não encontrada!")
        
        elif opcao == '2':
            prefixo = input("Digite o prefixo do nome: ").strip().upper()
            resultados = []
            arvore_nome.buscar_nome_prefixo(arvore_nome.raiz, prefixo, resultados)
            print(f"\n{len(resultados)} PESSOAS ENCONTRADAS:")
            for p in resultados:
                print(p)
        
        elif opcao == '3':
            data_inicio = input("Data inicial (DD/MM/AAAA): ").strip()
            data_fim = input("Data final (DD/MM/AAAA): ").strip()
            try:
                dt_inicio = datetime.strptime(data_inicio, "%d/%m/%Y")
                dt_fim = datetime.strptime(data_fim, "%d/%m/%Y")
                resultados = []
                arvore_data.buscar_data_intervalo(arvore_data.raiz, dt_inicio, dt_fim, resultados)
                print(f"\n{len(resultados)} PESSOAS ENCONTRADAS:")
                for p in resultados:
                    print(p)
            except ValueError:
                print("Formato de data inválido!")
        
        elif opcao == '4':
            break
        
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()