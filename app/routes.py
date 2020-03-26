from flask import render_template, redirect, flash, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Яна'}
    posts = [
        {'author': 'кто-то1',
        'body': 'блаблабла1'},
        {'author': 'кто-то2',
        'body': 'блаблабла2'},
        {'author': 'кто-то3',
        'body': 'блаблабла3'},
        {'author': 'кто-то4',
        'body': 'блаблабла4'},
        {'author': 'кто-то5',
        'body': 'блаблабла5'}
    ]
    return render_template('index.html', title='Home', user = user, posts = posts)
    
   
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login {form.username.data}, remember {form.remember_me.data}")
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)