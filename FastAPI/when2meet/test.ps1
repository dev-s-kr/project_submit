
. .\.venv\Scripts\Activate.ps1

# 컬러 변수 (PowerShell에서 간단히)
$COLOR_GREEN = "`e[32m"
$COLOR_NC = "`e[0m"

Write-Host "Starting black"
.\.venv\Scripts\python.exe -m black .
Write-Host "OK"

Write-Host "Starting ruff"
uv run ruff check --select I --fix
uv run ruff check --fix
Write-Host "OK"

Write-Host "Starting mypy"
uv run dmypy run -- .
Write-Host "OK"

Write-Host "Starting pytest with coverage"
# coverage가 측정할 패키지/파일 지정
.\.venv\Scripts\python.exe -m coverage run -m pytest
.\.venv\Scripts\python.exe -m coverage report -m
.\.venv\Scripts\python.exe -m coverage html
Write-Host "OK"

Write-Host "${COLOR_GREEN}All tests passed successfully!${COLOR_NC}"