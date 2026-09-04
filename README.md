# Backlog de Tarefas do Projeto (Visão Técnica)

### US01 - Cadastro de Novo Usuário
* **Task 1.1:** Implementar fluxo condicional inicial usando `if/while` para verificar a variável `acesso`. Se `acesso == "Entrar"`, exibir mensagem de erro em loop até a escolha correta.
* **Task 1.2:** Capturar as strings de entrada através de `input()` para as variáveis `nome`, `email` e `senha` caso a condição `acesso == "Cadastrar"` seja satisfeita.
* **Task 1.3:** Utilizar `f-strings` (ex: `f"Nome: {nome}"`) para formatar e imprimir o log de sucesso no console, validando a persistência das variáveis em memória.

### US02 - Login no Sistema
* **Task 2.1:** Declarar as constantes (hardcoded) de validação: `nome_cadastrado`, `email_cadastrado` e `senha_cadastrada`.
* **Task 2.2:** Utilizar `input()` para capturar os dados de tentativa de login nas variáveis locais `nome`, `email` e `senha`.
* **Task 2.3:** Implementar um laço `while` utilizando operadores lógicos `!=` e `or` para bloquear o avanço caso os inputs não correspondam às constantes estabelecidas, solicitando novas entradas iterativamente.
* **Task 2.4:** Condicionar a mensagem de sucesso a um `if` contendo operadores `and` para garantir a correspondência estrita de todas as três credenciais.

### US03 - Cadastro de Casa
* **Task 3.1:** Receber o número total de residências via `int(input())` e armazenar na variável inteira `quantidade_casas`.
* **Task 3.2:** Implementar um laço `for i in range(quantidade_casas):` para iterar sobre a quantidade definida de cadastros.
* **Task 3.3:** Dentro do laço, realizar o prompt de `nome_casa` e utilizar a expressão `i + 1` na `f-string` para exibir corretamente o índice de controle da casa para o usuário (ex: 1ª, 2ª).

### US04 - Listagem de Casas
* **Task 4.1:** Instanciar uma lista vazia `listagem_casas = []` antes do bloco de iteração de cadastro.
* **Task 4.2:** Utilizar o método `listagem_casas.append(nome_casa)` dentro do laço `for` de cadastro para popular o array com as strings das casas criadas.
* **Task 4.3:** Criar um segundo laço `for i in range(quantidade_casas):` para varrer o array e executar o `print(listagem_casas[i])` para exibir os índices salvos.

### US05 - Cadastro de Equipamento
* **Task 5.1:** Receber a quantidade de equipamentos na variável `qntd_equipamento` via type casting `int(input())`.
* **Task 5.2:** Criar um laço `for i in range(qntd_equipamento):` para capturar os atributos de cada equipamento.
* **Task 5.3:** Dentro do laço, declarar a variável string `equipamento` e forçar a tipagem inteira para as variáveis `potencia` e `uso_diario` usando `int(input())`.

### US06 - Listagem de Equipamentos da Casa
* **Task 6.1:** Inicializar a estrutura de dados em array `listagem_equipamento = []` para armazenar o log da sessão.
* **Task 6.2:** Embutir o método `.append(equipamento)` ao final do laço de captação de dados para empilhar o nome de cada item.
* **Task 6.3:** Varrer e listar os elementos armazenados imprimindo a posição do índice na memória através de `print(listagem_equipamento[i])` em um laço de repetição final.

### US07 - Edição e Remoção de Equipamento
* **Task 7.1:** Envolver o bloco de edição em um laço `while permicao_edicao == 1:` utilizando uma variável flag para controle de estado.
* **Task 7.2:** Capturar a string "s" ou "n" na variável `edicao` e implementar o controle de fluxo via `if`. Se "n", acionar o statement `break` para interromper o laço principal.
* **Task 7.3:** Se a variável `edicao` for avaliada como "s", reescrever as variáveis e recriar a lista, executando novamente a lógica de atribuição `listagem_equipamento.append(equipamento)` em um novo escopo de repetição para sobrescrever os dados anteriores.

### US08 - Cálculo de Gasto em kWh
* **Task 8.1:** Inicializar o acumulador numérico `consumo_energia_total = 0` na raiz do escopo de cadastro.
* **Task 8.2:** Dentro da iteração de cada equipamento, aplicar a expressão algébrica `consumo_energia = (potencia * uso_diario) / 1000` para converter Watts/hora para kWh.
* **Task 8.3:** Empregar o operador de atribuição aditiva `+=` para incrementar a variável `consumo_energia_total` com o valor de `consumo_energia` a cada iteração do loop.
* **Task 8.4:** Utilizar os formatadores de casas decimais em string (`:.2f`) nos retornos do console para garantir a exibição padrão de floats de grandezas físicas.

### US09 - Estimativa de Custo Financeiro
* **Task 9.1:** Adicionar o prompt da variável `tarifa_energia` utilizando o type casting de ponto flutuante `float(input())`.
* **Task 9.2:** Criar o acumulador `gasto_consumo_energia_total = 0` e calcular os custos isolados via `gasto_consumo_energia = consumo_energia * tarifa_energia` dentro do loop de equipamentos.
* **Task 9.3:** Somar iterativamente os gastos isolados na variável acumuladora utilizando `+=`.
* **Task 9.4:** Imprimir o output diário e o cálculo de projeção mensal efetuando a operação aritmética diretamente nos argumentos do print: `{gasto_consumo_energia_total * 30:.2f}`.

### US10 - Ranking de Consumo (Opcional - Proposição Técnica)
* **Task 10.1:** Refatorar a lista `listagem_equipamento` para aceitar dicionários iteráveis, ex: `{"nome": equipamento, "consumo": consumo_energia}` em vez de apenas strings.
* **Task 10.2:** Invocar a função `sorted()` ou o método `.sort()` na lista de dicionários, passando uma função lambda na key (`key=lambda x: x['consumo']`) e definindo o parâmetro `reverse=True`.
* **Task 10.3:** Criar um laço de repetição sobre a lista já indexada e ordenada para imprimir os itens decrescentes em conjunto com os valores armazenados de consumo.
