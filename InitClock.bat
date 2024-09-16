@ECHO OFF

CHCP 65001 > NUL

call "C:\Program Files\Git\git-bash.exe"
cd "C:\RelojMonumental\Reloj"
py reloj_analogico.py

exit

PAUSE > nul