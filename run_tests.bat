@echo off
echo Executando testes unitários com cobertura...

:: Ativar ambiente virtual se existir
if exist venv\Scripts\activate (
    call venv\Scripts\activate
)

:: Executar pytest com cobertura
python -m pytest --cov=src tests/ --cov-report=term-missing

pause
