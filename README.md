<h1>📚 Sistema de Cadastro de Alunos</h1>
<strong>Este é um simples sistema de cadastro de alunos feito em Python com funcionalidades de entrada de dados, exibição de informações e estatísticas.</strong>

<h2>🔧Funções usadas</h2>
<li>Estruturas condicionais (if, match)</li>
<li>Estruturas de repetição (while, for)</li>
<li>Tipos de dados: list, dict, str, int, float</li>
<li>Funções internas: input(), print(), sum()</li>

<h2>🧠 Funcionalidades do Programa</h2>

<h3>1. Menu Principal</h3>
<h4>O sistema roda em um loop infinito while True até que o usuário selecione a opção de sair. As opções do menu são:</h4>

<li>1. Cadastrar Aluno</li>  
<li>2. Lista de alunos cadastrados</li> 
<li>3. Ver estatísticas</li>
<li>4. Sair do programa</li>

<h3>2.Cadastro de Aluno (case '1')</h3>
<h4>Permite ao usuário cadastrar um novo aluno com:</h4>

<li>Nome</li>
<li>Idade (validação para aceitar apenas números inteiros positivos)</li>
<li>3 Notas (validação para aceitar apenas valores entre 0 e 10)</li>
<li>Esses dados são armazenados em um dicionário e adicionados à lista alunos.</li>

<h3>3. Listar Alunos Cadastrados (case '2')</h3>
<h4>Exibe os alunos cadastrados com:</h4>

<li>Nome</li>
<li>Idade</li>
<li>Notas</li>
<li>Média das notas</li>
<li>Situação (Aprovado ou Reprovado, com base na média ≥ 7)</li>

<h3>4. Ver Estatísticas (case '3')</h3>
<h4>Gera e exibe:</h4>

<li>Média de idade dos alunos</li>
<li>Nome do aluno com a maior média</li>
<li>Quantidade de alunos aprovados</li>

<h3>5. Sair do Programa (case '4')</h3>
<h4>Encerra o loop e finaliza a execução.</h4>

<h2>⚠️ Validações Importantes</h2>
<li>Idade: Aceita apenas números inteiros positivos.</li>

<li>Notas: Devem ser números reais entre 0 e 10.</li>

<li>Todos os campos são obrigatórios para o cadastro do aluno.</li>

