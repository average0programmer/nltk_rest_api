Щоб запустити проєкт потрібно:
0. Перейти до кореневої папки проєкту (test_task)
1. Створити віртуальне середовище
    • На Linux, MacOs "python3 -m venv venv"
    • На Windows "python -m venv venv"
2. Активувати середовище:
    • На Linux, MacOs "source venv/bin/activate"
    • На Windows "venv/Scripts/activate
3. Завантажити необхідні бібліотеки: "pip install -r requirements.txt"
4. Провести міграції до бази даних: "python3 manage.py migrate"
5. Запустити сервер: "python3 manage.py runserver"


Ендпоінти:
http://127.0.0.1:8000/api/tokenize
http://127.0.0.1:8000/api/pos_tag
http://127.0.0.1:8000/api/ner
