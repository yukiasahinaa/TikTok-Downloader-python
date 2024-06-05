from flask import Flask, render_template, request, redirect, url_for, send_file
import yt_dlp
import os
from datetime import datetime, timedelta
import threading
import time

app = Flask(__name__)
app.config['DOWNLOAD_FOLDER'] = 'downloads'

def delete_old_files():
    while True:
        now = datetime.now()
        for filename in os.listdir(app.config['DOWNLOAD_FOLDER']):
            file_path = os.path.join(app.config['DOWNLOAD_FOLDER'], filename)
            if os.path.isfile(file_path):
                file_creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
                if now - file_creation_time > timedelta(minutes=5):
                    os.remove(file_path)
        time.sleep(60)  # Verifica a cada minuto

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        url = request.form['url']
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            ydl_opts = {
                'outtmpl': os.path.join(app.config['DOWNLOAD_FOLDER'], f'%(title)s_{timestamp}.%(ext)s'),
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                result = ydl.extract_info(url, download=True)
                file_path = os.path.join(app.config['DOWNLOAD_FOLDER'], f"{result['title']}_{timestamp}.{result['ext']}")
            return send_file(file_path, as_attachment=True)
        except Exception as e:
            return render_template('error.html', error_message=str(e))
    return render_template('download.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Página de erro personalizada
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error_message="Página não encontrada."), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', error_message="Erro interno do servidor."), 500

if __name__ == "__main__":
    if not os.path.exists(app.config['DOWNLOAD_FOLDER']):
        os.makedirs(app.config['DOWNLOAD_FOLDER'])
    
    # Inicia a thread para deletar arquivos antigos
    threading.Thread(target=delete_old_files, daemon=True).start()

    app.run(debug=True, host='0.0.0.0')