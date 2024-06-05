import subprocess
import logging

def download_video(url, service, current_time):
    if service == 'snaptik':
        command = f"python3 -m tiktok_downloader --url \"{url}\" --snaptik --save video_{current_time}.mp4"
    elif service == 'tikmate':
        command = f"python3 -m tiktok_downloader --url \"{url}\" --tikmate --save video_{current_time}.mp4"
    elif service == 'tikdown':
        command = f"python3 -m tiktok_downloader --url \"{url}\" --tikdown --save video_{current_time}.mp4"
    else:
        logging.error("Serviço não suportado.")
        return

    # Executar o comando
    logging.info(f"Executando comando de download: {command}")
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro ao executar o comando: {e}")
        return