Write-Host "Starting Maharashtrian Snacks App..." -ForegroundColor Green

# Start Backend
Write-Host "Starting Backend (FastAPI)..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd backend; uvicorn main:app --reload"

# Start Frontend
Write-Host "Starting Frontend (Vite)..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd frontend; npm run dev"

Write-Host "----------------------------------------------------------------"
Write-Host "App started successfully!" -ForegroundColor Green
Write-Host "Backend: http://127.0.0.1:8000"
Write-Host "Frontend: http://localhost:5173"
Write-Host "----------------------------------------------------------------"
Write-Host "Press any key to exit this launcher (terminals will stay open)..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
