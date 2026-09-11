# Python muhit va skriptlar bo'yicha konspekt

## 1. Virtual muhit

Windows PowerShell'da virtual muhit yaratish va faollashtirish:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Faollashtirilgan muhitda `requests` o'rnatildi:

```powershell
python -m pip install requests
python -m pip freeze > requirements.txt
```

`requirements.txt` fayli aynan virtual muhitdagi `pip freeze` chiqishidan yaratildi.

Ushbu kompyuterda PowerShell skript bajarish siyosati `Activate.ps1` ni bloklaydi.
Sessiya uchun vaqtinchalik ruxsat berib faollashtirish mumkin:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## 2. Python versiyasi va interpreter yo'li

Bu Windows kompyuterida Unix'ning `python3` va `which` buyruqlariga mos buyruqlar:

```text
python --version
Python 3.14.7

where python
C:\Users\user\AppData\Local\Programs\Python\Python314\python.exe
```

Loyiha virtual muhitini tekshirish uchun:

```powershell
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -c "import requests; print(requests.__version__)"
```

## 3. `argparse` bilan salomlashish

`greet.py` `--name` parametrini majburiy qabul qiladi:

```powershell
.\.venv\Scripts\python.exe greet.py --name Ali
```

Natija:

```text
Salom, Ali!
```

## 4. Bitta vazifa: papkadagi fayllar soni

Bir xil vazifa ikki skriptda bajarildi:

```powershell
bash count_files.sh .
.\.venv\Scripts\python.exe count_files.py .
```

Sinov natijasi: Python skripti `5` ta fayl topdi. Bash bu kompyuterda PATH orqali
mavjud emas, shuning uchun Bash buyrug'ini Git Bash yoki WSL terminalida ishga
tushirish kerak; skriptning o'zi `find` va `wc` bilan tayyor.

Har ikkisi ham berilgan papkaning faqat bevosita ichidagi oddiy fayllarni sanaydi; ichki papkalar rekursiv kiritilmaydi.

### Taqqoslash va xulosa

- Bash yechimi `find` va `wc` kabi tizim utilitalariga qisqa va qulay tayanadi.
- Python yechimi Windows, Linux va macOS'da bir xil ishlaydi hamda keyinroq filtrlash yoki boshqa mantiq qo'shishga qulay.
- Ushbu oddiy vazifada Bash kodi ixchamroq, lekin ko'chma va kengaytiriladigan dastur uchun Python ma'qulroq.

## 5. `os`, `sys`, `subprocess` va `os.environ`

`os_sys_tools.py` quyidagi amallarni bajaradi:

- `os.listdir()` bilan joriy papkadagi barcha nomlarni chiqaradi.
- `sys.argv[1]` orqali berilgan faylni UTF-8 formatida ochib, mazmunini chiqaradi.
- Windows'da `subprocess.run()` orqali `dir /a`, Unix tizimlarida esa `ls -la` buyrug'ini ishga tushiradi.
- `os.environ.get("PATH", "")` orqali `PATH` qiymatini chiqaradi.
- Berilgan papkada `.tmp` bilan tugaydigan fayllarni faqat ro'yxat qiladi, ularni o'zgartirmaydi yoki o'chirmaydi.

Ishga tushirish:

```powershell
.\.venv\Scripts\python.exe os_sys_tools.py konspekt.md .
```

Bu yerda `konspekt.md` fayl nomi, `.` esa `.tmp` fayllari qidiriladigan papkadir.

## 6. 2.2 uyga vazifa kodlari

Barcha asosiy kodlar bitta faylda joylashgan:

```text
homework_2_2.py
```

Fayl ichidagi qismlar:

- `servers` va `print_down_servers()` - statusi `down` serverlarni chiqaradi.
- `numbers = [...]` - 1 dan 50 gacha 3 ga bo'linadigan sonlarni tuzadi.
- `make_greeting()` - nested function va closure misoli.
- `InvalidServerNameError` va `check_server_name()` - custom exception misoli.
- `validate_port()` - portni `try/except` orqali tekshiradi.

Eng oson ishga tushirish:

```powershell
python homework_2_2.py
```

So'ng port so'ralganda, masalan `8080` kiriting.

## 7. JSON, YAML, CSV va logging uyga vazifasi

Barcha asosiy kodlar quyidagi faylda:

```text
homework_3.py
```

Menyu orqali:

```powershell
python homework_3.py
```

`0` - barcha 5 vazifani bajaradi. Qolgan tanlovlar:

- `1` - JSON konfiguratsiyani o'qiydi; `debug: true` bo'lsa DEBUG log chiqaradi.
- `2` - `.json` va `.yaml` fayllarni ikki tomonga konvertatsiya qiladi.
- `3` - katta CSV faylni qatorma-qator o'qib, `status=error` qatorlarni ajratadi.
- `4` - `RotatingFileHandler` bilan 1 MB hajm va 3 ta zaxira log sozlaydi.
- `5` - `.log` fayllardagi `ERROR` satrlarini hisobotga yozadi.

Sinov fayllari: `config.json`, `config.yaml`, `events.csv`, `service.log`.
Natijalar: `converted.json`, `errors.csv`, `rotating.log`, `error_report.txt`.