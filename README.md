

<h1 align="center">🔧 Automação de Interfaces - Dpainel</h1>

<p align="center">
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=flat-square" alt="status">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue.svg?style=flat-square" alt="python">
  <img src="https://img.shields.io/badge/Selenium-Automation-brightgreen?style=flat-square" alt="selenium">
</p>

<p align="center">
  <b>Automatize o cadastro de interfaces de rede no Dpainel com Selenium.</b><br>
  Login automático, preenchimento de formulários e submissão em lote.
  Objetivo: 
</p>

<hr>

<h2>📌 Funcionalidades</h2>

<ul>
  <li>✅ Login automático com Selenium WebDriver</li>
  <li>✅ Cadastro de até 48 interfaces sequenciais</li>
  <li>✅ Feedback visual de sucesso ou erro</li>
  <li>✅ Suporte a modo headless</li>
  <li>✅ Preenchimento seguro de campos MAC</li>
  <li>✅ Tempo de espera configurável entre ações</li>
</ul>

<h2>📂 Pré-requisitos</h2>

<ul>
  <li>Python 3.8+</li>
  <li>Google Chrome instalado</li>
  <li>ChromeDriver compatível com sua versão do Chrome</li>
  <LI>selenium==4.9.1</LI>
</ul>

<h2>⚙️ Configuração do Ambiente</h2>

<h3>1. Criar ambiente virtual (venv)</h3>

<details>
<summary><strong>Linux/macOS</strong></summary>


<p>python3 -m venv venv</p>
</p>source venv/bin/activate</p>

</details><details> <summary><strong>Windows</strong></summary>

<p>python -m venv venv</p>
<p>venv\Scripts\activate</p>

</details><h3>2. Instalar dependências</h3>


pip install -r requirements.txt

<h3>3. Configurar ChromeDriver</h3><ol> <li>Baixe o ChromeDriver compatível em <a href="https://chromedriver.chromium.org/downloads">chromedriver.chromium.org</a></li> <li>Extraia e coloque o executável em: <ul> <li><code>/usr/local/bin/</code> (Linux/macOS)</li> <li>Ou em qualquer diretório no PATH do sistema</li> </ul> </li> </ol>

<h2>🚀 Execução</h2>
<ol> <li>Edite as credenciais no arquivo principal:
python

<p>USERNAME = "seu_usuario"  # Substitua aqui</p>
<p>PASSWORD = "sua_senha"    # Substitua aqui</p>

</li> <li>Execute o script:


python main.py

</li> </ol><h2>⚙️ Personalização</h2><ul> <li>Para modo headless (sem interface gráfica), descomente:
python

options.add_argument("--headless=new")

<h2>🛡️ Avisos Importantes</h2><blockquote> ⚠️ Nunca compartilhe senhas reais ou dados sensíveis em repositórios públicos.<br> ⚠️ Use variáveis de ambiente ou arquivos .env para credenciais em produção.<br> ⚠️ Mantenha o ChromeDriver atualizado para evitar problemas de compatibilidade. </blockquote>
