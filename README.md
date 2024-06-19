1. Abrir um terminal e instalar o poetry (Criando app Flask no Lab moodle as duas primeiras linhas)
curl -sSL https://install.python-poetry.org | python3 -
export PATH="/home/estudante1/.local/bin:$PATH"

2. rm -rf <seu-projeto>

git clone <seu-projeto>

3. Abrir o projeto no vscode

4. No terminal do vscode
  poetry shell
  poetry install
 
5. Verificar se a extensão python está instalada, instalar caso necessário

Configurar o vscode com Ctrl+Shift+P e selecionar o
interpretador Python (caso não aparecer. fechar o vscode e abrir novamente e executar os passo 4 e 5)

6. Executar o projeto
poetry run flask --app projeto_lp3/app.py run