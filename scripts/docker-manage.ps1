param(
    [Parameter(Mandatory=$true)]
    [ValidateSet('start','stop','restart','status','backup','clean')]
    [string]$Action
)

$ErrorActionPreference = 'Stop'
$ProjectName = "masclet-imperi"
$BackupDir = Join-Path $PSScriptRoot "../backups"
$DockerComposePath = Join-Path $PSScriptRoot "../docker-compose.yml"

function Test-DockerHealth {
    $health = docker inspect -f '{{.State.Health.Status}}' masclet_imperi_db
    return $health -eq "healthy"
}

function New-Backup {
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $backupFile = Join-Path $BackupDir "backup_$timestamp.sql"
    
    if (-not (Test-Path $BackupDir)) {
        New-Item -ItemType Directory -Path $BackupDir
    }

    docker exec masclet_imperi_db pg_dump -U postgres masclet_imperi > $backupFile
    Write-Host "Backup created at: $backupFile"

    # Mantener solo las últimas 4 copias
    Get-ChildItem $BackupDir | Sort-Object LastWriteTime -Descending | Select-Object -Skip 4 | Remove-Item
}

switch ($Action) {
    'start' {
        Write-Host "Starting containers..."
        docker compose -f $DockerComposePath up -d
        $retries = 0
        while (-not (Test-DockerHealth) -and $retries -lt 5) {
            Write-Host "Waiting for database to be healthy..."
            Start-Sleep -Seconds 5
            $retries++
        }
    }
    'stop' {
        Write-Host "Stopping containers..."
        docker compose -f $DockerComposePath down
    }
    'restart' {
        Write-Host "Restarting containers..."
        docker compose -f $DockerComposePath restart
    }
    'status' {
        Write-Host "Container status:"
        docker ps --filter "name=masclet_imperi*"
    }
    'backup' {
        Write-Host "Creating backup..."
        New-Backup
    }
    'clean' {
        Write-Host "Cleaning unused resources..."
        docker system prune -f
    }
}