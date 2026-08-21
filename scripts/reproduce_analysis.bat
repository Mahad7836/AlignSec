@echo off
setlocal
set "ROOT=%~dp0.."
cd /d "%ROOT%"
set "ALIGNSEC_PROJECT_ROOT=%ROOT%"
python scripts\verify_repository.py
if errorlevel 1 exit /b 1
jupyter nbconvert --to notebook --execute analysis\AlignSec_Final_Analysis.ipynb --output AlignSec_Final_Analysis_REPRODUCED.ipynb --ExecutePreprocessor.timeout=1200
endlocal
