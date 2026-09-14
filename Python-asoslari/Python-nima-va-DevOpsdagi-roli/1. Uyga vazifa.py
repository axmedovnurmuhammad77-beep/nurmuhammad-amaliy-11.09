# Python interpretatorlari va muhit vositalari

## Python implementatsiyalari haqida qisqa referat

Python tili yagona dastur emas, balki turli implementatsiyalarda ishlaydigan til
spetsifikatsiyasidir. Eng mashhur implementatsiya CPython bo'lib, u C tilida
yozilgan va Python kodini bytecode'ga kompilyatsiya qilib, uni virtual mashinada
ishlatadi. CPython standart kutubxonasi, uchinchi tomon paketlari va C kengaytmalari
bilan eng yaxshi moslikka ega. Uning asosiy xususiyati Global Interpreter Lock
(GIL) bo'lib, bir jarayondagi Python bytecode iplarini cheklaydi; CPU-og'ir ishlar
uchun multiprocessing yoki native kengaytmalar ishlatiladi.

PyPy Python tilida yozilgan JIT (Just-In-Time) kompilyatorga ega implementatsiya.
U uzoq ishlaydigan, ko'p marta takrorlanadigan sof Python kodini ish vaqtida
optimallashtirib, CPython'dan tezroq bajarishi mumkin. Biroq CPython uchun yozilgan
ayrim C kengaytmalari PyPy'da to'liq mos kelmasligi yoki boshqacha ishlashi mumkin.

Jython Python'ni Java Virtual Machine ustida ishlatadi va Java kutubxonalariga
qulay kirish beradi, ammo CPython C kengaytmalari bilan mosligi cheklangan.
IronPython esa .NET platformasiga yo'naltirilgan bo'lib, CLR kutubxonalaridan
foydalanish imkonini beradi. MicroPython va CircuitPython xotirasi kichik
mikrokontrollerlar uchun yaratilgan; ular to'liq CPython standart kutubxonasini
bermaydi, lekin qurilma boshqaruvi uchun yengil va amaliy.

Xulosa qilib, umumiy server va desktop loyihalarida CPython eng xavfsiz tanlov,
sof Python kodining tezligi muhim bo'lsa PyPy foydali, Java/.NET ekotizimlari
uchun Jython/IronPython, cheklangan qurilmalar uchun esa MicroPython mos keladi.

## `venv`, `virtualenv` va Poetry taqqoslanishi

| Vosita | Afzalliklari | Kamchiliklari |
|---|---|---|
| `venv` | Python bilan birga keladi; sodda; qo'shimcha paket talab qilmaydi | Dependency lock fayli yo'q; dependency boshqaruvi `pip`ga bog'liq | 
| `virtualenv` | Eski Python versiyalarida ham ishlaydi; tez; ko'p interpreterlar bilan qulay | Alohida o'rnatiladi; paketlarni boshqarish va lock qilishni o'zi hal qilmaydi |
| Poetry | `pyproject.toml`, dependency resolution, lock fayl va build/publish bir joyda | O'rganish va o'rnatish murakkabroq; ba'zi eski workflow'lar bilan farq qiladi |

Kichik mashqlar uchun `venv` yetarli, katta va takrorlanuvchi loyihalarda Poetry
dependency versiyalarini aniqroq boshqaradi.

## CLI sinovi

`cli.py` `argparse` subparsers ishlatadi:

```powershell
python cli.py start --name web
python cli.py stop --name web
```

Natijalar mos ravishda `Xizmat ishga tushirildi: web` va
`Xizmat to'xtatildi: web` bo'ladi.

## Yangi virtual muhitda `requirements.txt` sinovi

Avvalgi muhitdan yaratilgan `requirements.txt` yangi `.venv-test` muhitida
`pip install -r requirements.txt` bilan o'rnatildi va `requests==2.34.2` importi
muvaffaqiyatli tekshirildi. Yangi muhitdagi `pip freeze` natijasi asosiy faylga
mos keldi.

## `crontab` tajribasi

Joriy kompyuter Windows bo'lgani uchun Unix `crontab` buyrug'i mavjud emas.
`crontab -l` buyrug'ini ishga tushirishda `crontab` topilmadi. Windows muqobili Task Scheduler
yoki `schtasks` hisoblanadi. Unix/Linux muhitida esa misol:

```cron
*/5 * * * * /absolute/path/.venv/bin/python /absolute/path/cli.py start --name cron-demo
```

Qiyinchiliklar: Windows'da `crontab` yo'qligi, virtual muhit Python yo'lini
absolute ko'rsatish zarurligi va cron'da ishchi papka/PATH interaktiv terminaldagidan
farq qilishi. Shu sabab loyiha skriptlari uchun `schtasks` yoki to'liq yo'l bilan
Task Scheduler sozlamasi ishlatiladi.