from app import app
from flask import render_template, flash, redirect
from .forms import TextInputForm
from .translate import Translator


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = TextInputForm()
    translator = Translator()
    if form.validate_on_submit():
        flash('You entered: %s' % form.text.data)
        flash('Your message is: %s' % translator.computeTranslation(form.text.data))
        return redirect('/')
    return render_template('index.html', form=form, translator=translator)
