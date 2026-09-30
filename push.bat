@echo off
call :main > "%~dp0push-log.txt" 2>&1
type "%~dp0push-log.txt"
pause
exit /b

:main
cd /d "%~dp0"
del /q .git\HEAD.lock .git\index.lock .git\objects\maintenance.lock 2>nul
for /r .git\objects %%f in (tmp_obj_*) do del /q "%%f" 2>nul
git add -A
git diff --cached --quiet || git commit -m "Site guncellemesi"
git remote get-url origin >nul 2>&1 || git remote add origin https://github.com/yigitk75/influvia-site.git
where gh >nul 2>&1 && (
  echo === gh: repo olustur ===
  gh repo view yigitk75/influvia-site >nul 2>&1 || gh repo create yigitk75/influvia-site --public --description "Influvia app web sitesi"
)
echo === git push ===
git push -u origin main
where gh >nul 2>&1 && (
  echo === gh: GitHub Pages ac ===
  gh api -X POST repos/yigitk75/influvia-site/pages -f "source[branch]=main" -f "source[path]=/" 2>nul || gh api -X PUT repos/yigitk75/influvia-site/pages -f "source[branch]=main" -f "source[path]=/"
  gh api repos/yigitk75/influvia-site/pages --jq .html_url
)
echo.
echo Bitti. Site birkac dakika icinde: https://yigitk75.github.io/influvia-site/
exit /b 0
