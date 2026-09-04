# ⚡ Gestão de Consumo de Energia (Energetic Demand)

Este repositório contém a documentação e a implementação em Python de um sistema via console para gestão e estimativa de consumo de energia elétrica, estruturado a partir de User Stories.

## 📋 Product Backlog e Tasks Técnicas

### US01 - Cadastro de Novo Usuário
> *Como um visitante, eu quero criar uma conta com nome, e-mail e senha, para que eu possa ter um perfil seguro no sistema.*

- [ ] Criar interface de menu no console para o usuário selecionar a opção "Cadastrar" ou "Entrar".
- [ ] Implementar laço `while` para validar se a opção escolhida foi "Entrar" e exibir mensagem iterativa de negação de acesso.
- [ ] Implementar captura de dados (nome, e-mail e senha) via função `input()` caso a opção seja "Cadastrar".
- [ ] Exibir mensagem formatada de confirmação no console com os dados inseridos e aviso de sucesso.

### US02 - Login no Sistema
> *Como um usuário cadastrado, eu quero fazer login com minhas credenciais, para acessar o painel das minhas casas.*

- [ ] Definir variáveis estáticas (`nome_cadastrado`, `email_cadastrado`, `senha_cadastrada`) para validação.
- [ ] Criar prompts de `input()` para receber as credenciais de login do usuário no console.
- [ ] Desenvolver loop de validação (`while`) que solicite os dados novamente caso não coincidam com as variáveis do sistema.
- [ ] Imprimir mensagem de "Logado com sucesso!" após a validação correta das credenciais via bloco `if`.

### US03 - Cadastro de Casa
> *Como um usuário logado, eu quero cadastrar uma nova casa (ex: "Minha Casa", "Casa de Praia"), para organizar os meus gastos por endereço.*

- [ ] Adicionar `input()` que pergunte ao usuário a quantidade de casas a serem cadastradas, convertendo a entrada para `int`.
- [ ] Implementar um loop de repetição `for` baseado na quantidade informada.
- [ ] Dentro do loop, utilizar `input()` iterativo para capturar o nome de cada casa (1ª casa, 2ª casa, etc.).
- [ ] Exibir mensagem de sucesso dinâmica para cada casa inserida.

### US04 - Listagem de Casas
> *Como um usuário logado, eu quero visualizar uma lista de todas as casas que cadastrei, para escolher qual desejo gerenciar no momento.*

- [ ] Inicializar uma estrutura de lista vazia (`listagem_casas = []`) antes do loop de cadastro de casas.
- [ ] Adicionar instrução `.append()` dentro do loop de cadastro para salvar o nome de cada casa na lista.
- [ ] Criar um novo bloco `for` para iterar sobre a `listagem_casas`.
- [ ] Imprimir no console todas as casas armazenadas na lista.

### US05 - Cadastro de Equipamento
> *Como um usuário logado gerenciando uma casa, eu quero adicionar um equipamento informando seu nome, potência em Watts e tempo de uso diário.*

- [ ] Solicitar via `input()` a quantidade de tipos diferentes de equipamentos que serão registrados.
- [ ] Criar um loop `for` configurado para rodar a quantidade de vezes informada.
- [ ] Capturar, a cada iteração, os dados do equipamento via `input()`: nome (string), potência em W (int) e uso diário em horas (int).
- [ ] Exibir mensagem de confirmação de sucesso para cada equipamento assim que ele for inserido.

### US06 - Listagem de Equipamentos da Casa
> *Como um usuário logado, eu quero ver todos os equipamentos cadastrados em uma casa específica, para ter controle do que já foi inserido.*

- [ ] Criar uma estrutura de lista vazia (`listagem_equipamento = []`) antes do laço de equipamentos.
- [ ] Inserir o método `.append(equipamento)` ao final do bloco de cadastro para persistir o nome do aparelho.
- [ ] Implementar um segundo loop `for` que itere pela quantidade total de equipamentos.
- [ ] Imprimir no console o nome de todos os equipamentos armazenados na lista sequencialmente.

### US07 - Edição e Remoção de Equipamento
> *Como um usuário logado, eu quero alterar o tempo de uso ou remover um equipamento da lista, para simular diferentes cenários ou corrigir um cadastro errado.*

- [ ] Criar variável de controle (`permicao_edicao = 1`) para suportar o laço `while` de edição.
- [ ] Solicitar via `input("s/n")` se o usuário deseja fazer alterações no cadastro dos equipamentos.
- [ ] Implementar fluxo "s": solicitar nova quantidade, resetar a `listagem_equipamento` e rodar um novo loop `for` para sobrescrever os dados.
- [ ] Implementar fluxo "n": exibir mensagem de "Fim dos cadastros!" e acionar `break` para encerrar o laço `while`.

### US08 - Cálculo de Gasto em kWh
> *Como um usuário logado, eu quero visualizar o consumo total de energia da casa em kWh, baseado na soma de todos os equipamentos cadastrados.*

- [ ] Inicializar variável acumuladora `consumo_energia_total = 0`.
- [ ] Aplicar a fórmula matemática `(potencia * uso_diario) / 1000` dentro dos laços principal e de edição.
- [ ] Atualizar o totalizador acumulando o kWh do equipamento atual (`consumo_energia_total += consumo_energia`).
- [ ] Imprimir no console o gasto diário de cada item limitando a formatação a duas casas decimais (`:.2f`).
- [ ] Exibir o consumo total somado (kWh) ao final dos cadastros.

### US09 - Estimativa de Custo Financeiro
> *Como um usuário logado, eu quero inserir o valor da tarifa de energia da minha região (R$/kWh), para ver a estimativa em dinheiro da minha próxima conta de luz.*

- [ ] Adicionar requisição da tarifa regional de energia (`tarifa_energia`) convertendo o valor para `float`.
- [ ] Criar variável acumuladora `gasto_consumo_energia_total = 0`.
- [ ] Calcular o custo em Reais multiplicando o consumo em kWh do equipamento pela tarifa inserida.
- [ ] Imprimir o gasto individual diário em R$ para cada equipamento.
- [ ] Calcular e exibir o gasto financeiro total por mês multiplicando o acumulador diário por 30.

### US10 - Ranking de Consumo
> *Como um usuário logado, eu quero ver quais equipamentos gastam mais energia em uma lista ordenada, para saber onde focar meus esforços de economia.*

- [ ] Criar lista `listagem_consumo = []` e preenchê-la com os gastos em kWh via `.append()`.
- [ ] Desenvolver algoritmo de ordenação (com dois laços `for` aninhados) comparando índices subsequentes para estruturar os itens do maior para o menor.
- [ ] Sincronizar as trocas de posições (usando variáveis `aux_consumo` e `aux_equipamento`) tanto para a lista de consumos quanto para a lista de nomes.
- [ ] Iterar sobre as listas reordenadas.
- [ ] Exibir o Ranking de Consumo final estruturado com posição, nome do equipamento e respectivo valor em kWh.
