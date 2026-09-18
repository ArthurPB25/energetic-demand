LINK KANBAN S2 - https://trello.com/invite/b/6aadbe3230663b431c53ee02/ATTI0eb92685ad416f14ac1350f92e1f71ac5E73D7D2/kanban-charge-demand
# 📋 Product Backlog — User Stories e Tasks
 
## 🔹 US01: Dimensionamento da Demanda e Potência Solar
* **Descrição:** Como analista energético, quero informar o consumo médio mensal da residência ($C_m$), a localização/HSP e o percentual de atendimento desejado ($f$), para que o sistema calcule a energia mensal alvo ($E_{FV}$) e a potência requerida do gerador em kWp ($P_{FV}$).
* **Critérios de Aceite:**
  * Rejeitar consumos mensais menores ou iguais a zero.
  * Validar o percentual de atendimento no intervalo de **1%** a **100%**.
  * Definir o rendimento global do sistema ($\eta$) com valor padrão de **0,78** (78%), permitindo parametrização.
  * Exibir o valor calculado de $P_{FV}$ em kWp com precisão de duas casas decimais.
* **Tasks (Tarefas Técnicas):**
  * `TASK-1.1`: Criar estrutura de dados de entrada ($C_m$, $f$, $HSP$, $\eta$).
  * `TASK-1.2`: Implementar a equação da energia mensal esperada: $E_{FV} = C_m \times f$.
  * `TASK-1.3`: Implementar a equação da potência necessária: $P_{FV} = \frac{E_{FV}}{HSP \times 30 \times \eta}$.
  * `TASK-1.4`: Implementar validações de entrada e tratamento de erros para valores nulos ou inválidos.
  * `TASK-1.5`: Mapear e documentar a fonte das Horas de Sol Pleno (HSP) por região (ex: CRESESB/INPE).
 
---
 
## 🔹 US02: Seleção Automática de Módulos Fotovoltaicos
* **Descrição:** Como projetista de sistemas, quero consultar o dataset `paineis.csv`, para que o sistema determine a quantidade mínima de módulos ($N_{móds}$) e a potência efetiva instalada ($P_{instalada}$).
* **Critérios de Aceite:**
  * O arquivo `paineis.csv` deve possuir a estrutura: `id`, `fabricante`, `modelo`, `potencia_Wp`, `eficiencia`, `preco`.
  * O número de módulos deve ser arredondado para cima usando a função teto ($\lceil \rceil$).
  * Calcular a potência efetivamente instalada via fórmula $P_{instalada} = \frac{N_{móds} \times P_{módulo\_Wp}}{1000}$.
  * Selecionar o módulo que ofereça o menor custo total de aquisição atendendo à meta de potência.
* **Tasks (Tarefas Técnicas):**
  * `TASK-2.1`: Estruturar o arquivo CSV `paineis.csv` com dados de equipamentos comerciais.
  * `TASK-2.2`: Criar módulo de leitura e extração de dados do CSV de painéis.
  * `TASK-2.3`: Implementar algoritmo de cálculo de quantidade mínima de placas: $N_{móds} = \left\lceil \frac{P_{FV} \times 1000}{P_{módulo\_Wp}} \right\rceil$.
  * `TASK-2.4`: Implementar cálculo de potência total instalada ($P_{instalada}$).
  * `TASK-2.5`: Desenvolver rotina de comparação financeira para definir o painel de melhor custo-benefício.
 
---
 
## 🔹 US03: Validação Técnica e Seleção do Inversor
* **Descrição:** Como projetista elétrico, quero filtrar o dataset `inversores.csv` considerando a potência instalada e a presença de baterias, para selecionar um inversor eletricamente compatível com o gerador.
* **Critérios de Aceite:**
  * O dataset `inversores.csv` deve conter os campos: `id`, `fabricante`, `modelo`, `potencia_kW`, `tipo` e `preco`.
  * A potência nominal do inversor deve atender à regra de compatibilidade mínima: $P_{inversor} \ge 0{,}85 \times P_{instalada}$.
  * Se houver armazenamento por baterias no projeto, o inversor deve ser obrigatoriamente do tipo `Hibrido`.
  * Retornar mensagem de erro tratada caso não existam inversores compatíveis no dataset.
* **Tasks (Tarefas Técnicas):**
  * `TASK-3.1`: Estruturar o arquivo CSV `inversores.csv` registrando especificações técnicas.
  * `TASK-3.2`: Criar leitor e filtro de dados para o CSV de inversores.
  * `TASK-3.3`: Implementar a regra de corte por potência nominal mínima ($0{,}85 \times P_{instalada}$).
  * `TASK-3.4`: Implementar o filtro condicional de topologia (Grid-Tie vs Híbrido) baseado na existência de baterias.
  * `TASK-3.5`: Desenvolver algoritmo para seleção do inversor compatível de menor preço.
 
---
 
## 🔹 US04: Dimensionamento Opcional de Baterias
* **Descrição:** Como cliente residencial, quero poder solicitar uma autonomia em horas, para que o sistema consulte o dataset `baterias.csv` e dimensione a capacidade útil necessária e a quantidade de baterias ($N_{bat}$).
* **Critérios de Aceite:**
  * Se a autonomia informada for **0 horas**, ignorar o dimensionamento e definir custo de baterias em **R$ 0,00**.
  * O dataset `baterias.csv` deve conter: `id`, `fabricante`, `modelo`, `tecnologia`, `capacidade_kWh`, `dod`, `tensao_V`, `preco`.
  * A capacidade requerida deve considerar a profundidade de descarga ($DoD$) da bateria.
  * A quantidade de unidades do banco de baterias ($N_{bat}$) deve ser arredondada para cima.
* **Tasks (Tarefas Técnicas):**
  * `TASK-4.1`: Estruturar o arquivo CSV `baterias.csv` com dados de baterias comerciais (ex: LiFePO4).
  * `TASK-4.2`: Criar leitor para extração dos parâmetros das baterias no CSV.
  * `TASK-4.3`: Implementar equação do consumo diário ($E_d = \frac{C_m}{30}$) e da energia de autonomia ($E_{autonomia} = E_d \times \frac{A}{24}$).
  * `TASK-4.4`: Implementar o cálculo da capacidade total ($C_{bat\_kWh} = \frac{E_{autonomia}}{DoD \times \eta_{bat}}$) e número de baterias ($N_{bat}$).
  * `TASK-4.5`: Integrar flag de ativação de baterias para direcionar a escolha do inversor híbrido na US03.
 
---
 
## 🔹 US05: Formação do Orçamento e Proposta Comercial
* **Descrição:** Como cliente, quero visualizar o detalhamento dos custos com equipamentos, despesas adicionais e estimativa de geração mensal, para avaliar a viabilidade do investimento.
* **Critérios de Aceite:**
  * O orçamento deve distinguir claramente o custo dos equipamentos do custo de instalação/estruturas adicionais.
  * Exibir o resumo completo: consumo de referência, $P_{instalada}$, detalhes dos painéis, inversor, baterias (se houver), geração mensal prevista e custo total.
  * Calcular a geração mensal estimada em kWh/mês com base no arranjo instalado e recurso solar regional.
* **Tasks (Tarefas Técnicas):**
  * `TASK-5.1`: Criar função de agregação dos custos de equipamentos ($C_{módulos} + C_{inversor} + C_{baterias}$).
  * `TASK-5.2`: Implementar regra de precificação de custos indiretos (estruturas, cabos, proteções e instalação).
  * `TASK-5.3`: Implementar cálculo de estimativa de geração mensal real: $G_{mensal} = P_{instalada} \times HSP \times 30 \times \eta$.
  * `TASK-5.4`: Desenvolver formatador de exibição da proposta comercial e resumo para o cliente.
 
---
 
## 🔹 US06: Integração Legada e Validação de Cenários
* **Descrição:** Como desenvolvedor do sistema, quero integrar o módulo fotovoltaico ao cadastro de imóvel/consumo das etapas anteriores e executar testes padronizados, para garantir o correto funcionamento e a reprodutibilidade dos resultados.
* **Critérios de Aceite:**
  * O sistema deve consumir os dados de consumo histórico sem necessidade de entradas duplicadas.
  * Executar obrigatoriamente a simulação do **Cenário A (Sem Baterias)** e validar os resultados.
  * Executar obrigatoriamente a simulação do **Cenário B (Com Baterias)** e validar os resultados.
* **Tasks (Tarefas Técnicas):**
  * `TASK-6.1`: Mapear e conectar as variáveis de entrada com as estruturas de dados do sistema legado.
  * `TASK-6.2`: Construir rotina de teste e validação do **Cenário 1 (Grid-Tie / Sem Baterias)**.
  * `TASK-6.3`: Construir rotina de teste e validação do **Cenário 2 (Híbrido / Com Baterias)**.
  * `TASK-6.4`: Organizar a documentação do projeto com a comprovação dos cálculos e origem dos dados técnicos.
