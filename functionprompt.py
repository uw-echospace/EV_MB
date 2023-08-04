function prompt {
    $base = "PS " + $(Get-Location) + ">"
    $env = conda info --env | Select-String '\*'
    if ($env) {
        $env_name = $env.Line -replace '\*',''
        $base = "($env_name) " + $base
    }
    $base
}
