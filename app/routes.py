from app import app
from flask import render_template, redirect
from app.forms import MyForm
from werkzeug.utils import secure_filename
import os
import secrets
from myLib import count_letters_RU, detectEncoding
import plotly.graph_objects as go
import plotly as py
import time

@app.route('/')
@app.route('/index')
def hello():
    text='Классный сайт!!!ИИИХХХУУУ'
    countries = {'Russia':'Moscow','Italy':'Rome','Finland':'Oslo'}
    return render_template('index.html',title = text, data = countries)


@app.route('/upload', methods=['GET', 'POST'])
def upload():    
    form = MyForm()
    if form.validate_on_submit ():  
        start_time = time.time()
        _, file_ext = os.path.splitext(form.file.data.filename)
        files_dir= os.path.join(os.getcwd(), 'files')
        html_dir = os.path.join(files_dir, 'html_results')
        fname=secrets.token_hex(nbytes=16)+file_ext
        filename=os.path.join(files_dir, fname)
        if 'files' not in os.listdir(os.getcwd()):
            os.mkdir(files_dir)
        if not os.path.exists(html_dir):
            os.mkdir(html_dir)
        prepeare_time = time.time()-start_time
        form.file.data.save(filename)
        f=open(filename,'r', encoding=detectEncoding(filename)['encoding'])
        open_time = time.time()-prepeare_time
        result=count_letters_RU(f.read())
        f.close()
        count_time = time.time() - open_time
        letters=list(result.keys())
        values=list(result.values())
        fig = go.Figure([go.Bar(x=letters, y=values)])
        py.offline.plot(fig, filename=os.path.join(html_dir, fname)+'.html' , auto_open=True)
        graph_time = time.time() - count_time
        print (f'Время подготовки %d c, время открытия файла %d c, \
                время подсчета %d c, время построения графика %d c' %\
                (prepeare_time, open_time, count_time, graph_time))
        return render_template('index.html',title = form.name.data)
    return render_template('upload.html', form=form)