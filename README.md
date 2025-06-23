# Sistema de Gerenciamento de Pessoas com Árvores AVL

Este projeto implementa um sistema básico para gerenciar e consultar dados de pessoas, utilizando Árvores AVL (Adelson-Velsky e Landis) para indexação e busca eficiente. Os dados são carregados a partir de um arquivo CSV, e o sistema oferece funcionalidades de busca por CPF, prefixo de nome e intervalo de datas de nascimento.

## Alunos

*   Pedro Henrique Faria dos Santos Soares
*   Mateus Afonso Miranda de Oliveira

## Funcionalidades

*   **Classe `Pessoa`**: Representa uma entidade com CPF, RG, nome, data de nascimento e cidade.
*   **Árvore AVL Auto-Balanceada**: Implementação de uma Árvore AVL para garantir operações de busca, inserção e remoção (embora a remoção não esteja exposta no menu) em tempo logarítmico (O(log n)).
*   **Indexação Múltipla**: Os dados são indexados em três árvores AVL distintas para permitir buscas eficientes por:
    *   **CPF**: Busca exata.
    *   **Nome**: Busca por prefixo.
    *   **Data de Nascimento**: Busca por intervalo.
*   **Carregamento de Dados CSV**: Capacidade de carregar informações de pessoas a partir de um arquivo CSV formatado.
*   **Interface de Linha de Comando**: Um menu interativo para realizar as consultas.

## Estrutura do Código

*   `Pessoa` (Classe): Define a estrutura dos dados de uma pessoa.
*   `NoAVL` (Classe): Representa um nó na árvore AVL, contendo a chave, a referência ao objeto `Pessoa` e informações para o balanceamento (altura, filhos).
*   `ArvoreAVL` (Classe): Implementa as operações da árvore AVL, incluindo inserção, rotações (direita, esquerda), atualização de altura e cálculo de balanceamento. Contém métodos de busca específicos para CPF, nome (prefixo) e data (intervalo).
*   `carregar_dados(nome_arquivo)` (Função): Lê o arquivo CSV e retorna uma lista de objetos `Pessoa`.
*   `main()` (Função): Ponto de entrada do programa, responsável por carregar os dados, construir as árvores de índice e apresentar o menu de interação.

## Pré-requisitos

*   Python 3.x

Não são necessárias bibliotecas externas além das padrão do Python (`csv`, `datetime`).

## Como Executar

1.  **Salve o código**: Salve o código Python fornecido em um arquivo chamado, por exemplo, `sistema_pessoas.py`.
2.  **Prepare o arquivo CSV**: Crie um arquivo CSV (ex: `dados.csv`) com os dados das pessoas. O formato esperado é: `CPF;RG;Nome Completo;DD/MM/AAAA;Cidade`.
    *   **Exemplo de `dados.csv`**:
        ```csv
        123.456.789-00;12.345.678-9;João Silva;01/01/1990;São Paulo
        987.654.321-11;98.765.432-1;Maria Oliveira;15/05/1985;Rio de Janeiro
        111.222.333-44;11.222.333-4;Ana Paula Souza;20/11/1992;Belo Horizonte
        ```
3.  **Execute o programa**: Abra um terminal ou prompt de comando, navegue até o diretório onde você salvou o arquivo `sistema_pessoas.py` e execute:

    ```bash
    python sistema_pessoas.py
    ```

4.  **Informe o nome do arquivo CSV**: O programa solicitará o nome do arquivo CSV que contém os dados. Digite `dados.csv` (ou o nome que você escolheu) e pressione Enter.

## Uso do Sistema

Após carregar os dados, o programa exibirá um menu de opções:

--- MENU DE CONSULTAS ---
1. Buscar por CPF
2. Buscar por prefixo de nome
3. Buscar por intervalo de datas
4. Sair Escolha uma opção:


*   **1. Buscar por CPF**: Digite o CPF completo da pessoa que deseja encontrar.
*   **2. Buscar por prefixo de nome**: Digite as primeiras letras do nome da pessoa. A busca não é case-sensitive para o prefixo (o código converte o prefixo para maiúsculas antes da busca).
*   **3. Buscar por intervalo de datas**: Digite a data inicial e a data final no formato `DD/MM/AAAA`.
*   **4. Sair**: Encerra o programa.

## Observações sobre as Árvores AVL

*   **Balanceamento**: As árvores AVL mantêm-se balanceadas automaticamente através de rotações (simples e duplas) após cada inserção, garantindo que a altura da árvore seja sempre logarítmica em relação ao número de nós. Isso é crucial para o desempenho das operações de busca em grandes volumes de dados.
*   **Chaves de Busca**:
    *   A árvore de CPF usa o CPF como chave.
    *   A árvore de nome usa o nome completo como chave.
    *   A árvore de data usa o objeto `datetime` da data de nascimento como chave.
*   **Busca por Prefixo/Intervalo**: Para buscas por prefixo de nome e intervalo de datas, os métodos percorrem a árvore de forma a encontrar todos os nós que satisfazem a condição, o que pode envolver a visita de múltiplos nós.
