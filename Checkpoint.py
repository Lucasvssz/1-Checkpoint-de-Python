alunos = []

while True:
    print('\n1. Cadastrar Aluno')
    print('2. Lista de alunos cadastrados')
    print('3. Ver estatísticas')
    print('4. Sair do programa')

    escolha = input('\nEscolha uma das opções acima: ')

    match escolha:
        case '1':
            nome = input('Digite o nome do aluno: ')

            while True:
                idade = input('Digite a idade do aluno: ')
                valido = True
                for char in idade:
                    if char < '0' or char > '9':
                        valido = False
                        break
                if valido:
                    idade = int(idade)
                    if idade > 0:
                        break
                    else:
                        print("Idade inválida")
                else:
                    print("Apenas números aceitos")

            notas = []
            for i in range(1, 4):
                while True:
                    entrada = input(f'Digite a {i}ª nota: ')


                    if entrada.replace('.', '', 1).isdigit() and entrada.count('.') <= 1:
                        nota = float(entrada)
                        if 0 <= nota <= 10:
                            notas.append(nota)
                            break
                        else:
                            print('Nota inválida. A nota deve ser entre 0 e 10.')
                    else:
                        print('Erro: A nota deve ser um número válido.')

            aluno = {
                'nome': nome,
                'idade': idade,
                'notas': notas
            }
            alunos.append(aluno)
            print(f'Aluno {nome} cadastrado com sucesso!')

        case '2':
            print('\n--Alunos cadastrados--')

            if len(alunos) >= 1:
                print('\nLista de alunos')

                for aluno in alunos:
                    média = sum(aluno['notas']) / 3
                    situação = 'Aprovado' if média >= 7 else 'Reprovado'
                    notas_str = ", ".join([str(nota) for nota in aluno["notas"]])
                    print(
                        f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Notas: {notas_str} | Média: {média:.2f} | Situação: {situação}")
            else:
                print('\nNenhum aluno listado')

        case '3':
            soma_idades = 0
            top_média = 0
            top_aluno = None
            aprovados = 0

            if len(alunos) >= 1:
                print('\nEstatísticas dos alunos')

                for aluno in alunos:
                    soma_idades += aluno['idade']
                    média = sum(aluno['notas']) / 3
                    média_idades = soma_idades / len(alunos)
                    if média > top_média:
                        top_média = média
                        top_aluno = aluno
                    if média >= 7:
                        aprovados += 1

                print(f"Média de Idade dos Alunos: {média_idades:.2f}")
                print(f"Aluno com a maior média: {top_aluno['nome']} | Média: {top_média:.2f}")
                print(f"Quantidade de alunos aprovados: {aprovados}")
            else:
                print('\nNenhum dado para estatística')

        case '4':
            print('\nAté a próxima!')
            break

        case _:
            print('\nNão corresponde a nenhuma das opções')