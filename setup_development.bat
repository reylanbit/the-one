@echo off
echo Configurando ambiente de desenvolvimento para SortViz...

:: Criar ambiente virtual se não existir
if not exist venv (
    echo Criando ambiente virtual...
    python -m venv venv
)

:: Ativar ambiente virtual e instalar dependências
echo Instalando dependências...
call venv\Scripts\activate
pip install -r requirements.txt

echo Concluído! Para ativar o ambiente, use: venv\Scripts\activate
pause
