from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

glossario = [
    {'termo': 'Programação', 'significado': 'O processo de escrever código para criar software.'},
    {'termo': 'Algoritmo', 'significado': 'Um conjunto de passos sequenciais para realizar uma tarefa.'},
    {'termo': 'Variável', 'significado': 'Um espaço de armazenamento nomeado que contém um valor.'},
    {'termo': 'Condicionais', 'significado': 'Instruções que executam diferentes ações com base em condições.'},
    {'termo': 'Loop', 'significado': 'Uma estrutura de controle que repete um bloco de código várias vezes.'},
    {'termo': 'Função', 'significado': 'Um bloco de código reutilizável que realiza uma tarefa específica.'},
    {'termo': 'Python', 'significado': 'Uma linguagem de programação de alto nível conhecida por sua simplicidade e legibilidade.'},
    {'termo': 'IDE', 'significado': 'Ambiente de Desenvolvimento Integrado, uma ferramenta que fornece recursos para facilitar o desenvolvimento de software.'},
    {'termo': 'Módulo', 'significado': 'Um arquivo contendo código Python reutilizável, geralmente organizado por funcionalidade.'},
    {'termo': 'Importação', 'significado': 'O processo de trazer um módulo ou parte dele para o seu programa.'},
    {'termo': 'Função', 'significado': 'Um bloco de código reutilizável que realiza uma tarefa específica.'},
    {'termo': 'Parâmetro', 'significado': 'Um valor que pode ser passado para uma função.'},
    {'termo': 'Retorno', 'significado': 'O valor que uma função devolve quando concluída.'},
    {'termo': 'Framework', 'significado': 'Um conjunto de ferramentas e convenções que simplificam o desenvolvimento de software em uma linguagem específica.'},
    {'termo': 'Flask', 'significado': 'Um framework leve para construir aplicativos web em Python.'},
    {'termo': 'Django', 'significado': 'Um framework web de alto nível para desenvolvimento rápido em Python.'}
]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/equipe')
def equipe():
    return render_template('equipe.html')

@app.route('/glossario')
def glossario_page():
    return render_template('glossario.html', glossario=glossario)

@app.route('/adicionar_termo', methods=['POST'])
def adicionar_termo():
    termo = request.form.get('termo')
    significado = request.form.get('significado')

    glossario.append({'termo': termo, 'significado': significado})

    return redirect(url_for('glossario_page'))

if __name__ == '__main__':
    app.run(debug=True)
