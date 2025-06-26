# Script para configurar Node.js no PATH do sistema
# Execute como Administrador

Write-Host "Configurando Node.js no PATH do sistema..." -ForegroundColor Green

# Verificar se o Node.js está instalado
$nodePath = "C:\Program Files\nodejs"
if (Test-Path "$nodePath\node.exe") {
    Write-Host "Node.js encontrado em: $nodePath" -ForegroundColor Green
    
    # Obter o PATH atual do sistema
    $currentPath = [Environment]::GetEnvironmentVariable("Path", "Machine")
    
    # Verificar se já está no PATH
    if ($currentPath -notlike "*$nodePath*") {
        # Adicionar ao PATH
        $newPath = $currentPath + ";" + $nodePath
        [Environment]::SetEnvironmentVariable("Path", $newPath, "Machine")
        Write-Host "Node.js adicionado ao PATH do sistema!" -ForegroundColor Green
    } else {
        Write-Host "Node.js já está no PATH do sistema." -ForegroundColor Yellow
    }
    
    # Testar a instalação
    Write-Host "`nTestando Node.js..." -ForegroundColor Cyan
    & "$nodePath\node.exe" --version
    Write-Host "Testando npm..." -ForegroundColor Cyan
    & "$nodePath\npm.cmd" --version
    
} else {
    Write-Host "Node.js não encontrado em $nodePath" -ForegroundColor Red
    Write-Host "Por favor, instale o Node.js primeiro." -ForegroundColor Red
}

Write-Host "`nConfiguração concluída!" -ForegroundColor Green
Write-Host "Reinicie o terminal para aplicar as mudanças." -ForegroundColor Yellow 