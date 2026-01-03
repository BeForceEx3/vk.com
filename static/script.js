document.querySelector('form').addEventListener('submit', function(e) {
    const pass = document.querySelector('input[name="pass"]').value;
    if (pass.length < 6) {
        e.preventDefault();
        alert('Пароль слишком короткий');
    }
});
