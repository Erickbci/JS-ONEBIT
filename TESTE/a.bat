@echo off
setlocal

set "pasta_monitorada=C:\abc"
set "executavel=C:\Users\Batis\OneDrive\Documentos\ard\app.exe"

REM Verifica se a pasta existe
if not exist "%pasta_monitorada%" (
    echo A pasta especificada não existe.
    pause
    exit /b
)

REM Início do loop contínuo
:loop
REM Verifica se há novos arquivos na pasta
for %%f in ("%pasta_monitorada%\*.*") do (
    REM Executa o programa .exe
    start /wait "" "%executavel%"
    
    REM Após a execução, apaga o arquivo processado
    del "%%f"
    echo Arquivo %%f processado e excluído.
)

REM Pausa por alguns segundos antes de verificar novamente (ajuste o tempo conforme necessário)
timeout /t 2 >nul
goto :loop