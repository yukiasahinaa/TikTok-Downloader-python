from flask import Flask, render_template, request, send_file
import yt_dlp
import os
from datetime import datetime
from threading import Timer

app = Flask(__name__)
app.config['DOWNLOAD_FOLDER'] = 'downloads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['GET', 'POST'])
def download():
    if request.method == 'POST':
        url = request.form['url']
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            file_name = f"tiktok_{timestamp}.mp4"
            file_path = os.path.join(app.config['DOWNLOAD_FOLDER'], file_name)

            ydl_opts = {
                'outtmpl': file_path,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            # Programar a exclusão do arquivo após 300 segundos (5 minutos)
            Timer(300, lambda: os.remove(file_path)).start()

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

    # Remover arquivos antigos da pasta de downloads
    for root, dirs, files in os.walk(app.config['DOWNLOAD_FOLDER']):
        for file in files:
            file_path = os.path.join(root, file)
            file_age = datetime.now() - datetime.fromtimestamp(os.path.getctime(file_path))
            if file_age.total_seconds() > 300:
                os.remove(file_path)
                
    app.run(debug=True, host='0.0.0.0')
