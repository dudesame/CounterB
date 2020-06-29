from app import app
from flask import render_template, redirect
from app.forms import MyForm
from werkzeug.utils import secure_filename
import os
import secrets

@app.route('/')
@app.route('/index')
def hello():
    text='Классный сайт!!!ИИИХХХУУУ'
    countries = {'Russia':'Moscow','Italy':'Rome','Finland':'Oslo'}
    return render_template('index.html',title = text, data = countries)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    
    form = MyForm()
    if form.validate_on_submit():
        
        _, file_ext = os.path.splitext(form.file.data.filename)
        files_dir=os.path.join(os.getcwd(), 'files')
        filename=os.path.join(files_dir, secrets.token_hex(nbytes=16)+file_ext)
        if 'files' not in os.listdir(os.getcwd()):
            os.mkdir(files_dir)            
        form.file.data.save(filename)
        return render_template('index.html',title = form.name.data)
    return render_template('upload.html', form=form)