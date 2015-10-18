from app import app
from flask import render_template, flash, redirect
from .forms import TextInputForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = TextInputForm()
    if form.validate_on_submit():
        flash('Translate requested.')
        return redirect('/')
    return render_template('index.html', form=form)