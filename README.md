# TikTok-Downloader-python

Este é um projeto simples de um site para baixar vídeos do TikTok, desenvolvido com Flask e yt-dlp. O site permite que os usuários insiram a URL de um vídeo do TikTok e façam o download do vídeo diretamente para o seu dispositivo.

## Funcionalidades

- Interface amigável para download de vídeos do TikTok.
- Suporte para múltiplos serviços de download.
- Downloads com timestamp para evitar conflitos de nomes.
- Remoção automática de arquivos antigos e downloads concluídos após 5 minutos.

## Pré-requisitos

- Python 3.7+
- yt-dlp
- Flask

## Instalação

### Windows

1. Clone o repositório:
    ```bash
    git clone https://github.com/hd-ph7/TikTok-Downloader-python.git
    cd TikTok-Downloader-python
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute o aplicativo:
    ```bash
    python app.py
    ```

### Linux

1. Clone o repositório:
    ```bash
    git clone https://github.com/hd-ph7/TikTok-Downloader-python.git
    cd TikTok-Downloader-python
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute o aplicativo:
    ```bash
    python3 app.py
    ```

### Replit

1. Crie um novo Repl e escolha "Python" como a linguagem de programação.

2. Acesse o terminal do Repl e clone o repositório:
    ```bash
    git clone https://github.com/hd-ph7/TikTok-Downloader-python.git
    cd TikTok-Downloader-python
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure o arquivo `.replit` para definir o comando de execução padrão:
    ```plaintext
    run = "python app.py"
    ```

5. Execute o aplicativo clicando no botão "Run".

## Uso

1. Acesse o site através do navegador na URL onde o aplicativo está rodando.
2. Insira a URL do vídeo do TikTok na caixa de entrada.
3. Selecione o serviço de download desejado.
4. Clique em "Baixar Vídeo" e aguarde o download ser concluído.
5. O vídeo será baixado e removido automaticamente após 5 minutos.

## Estrutura do Projeto
