# CRUD - Portal Universitario

Projeto Django para gerenciamento academico com cadastros de alunos, disciplinas e notas.

## Requisitos

- Python 3.12 ou superior
- pip
- Git, se for clonar o projeto

As dependencias do projeto estao em `requirements.txt`.

## Como executar no Windows

Abra o PowerShell na pasta onde deseja deixar o projeto.

### 1. Entrar na pasta do projeto

Se voce ja tem o projeto baixado:

```powershell
cd caminho\para\CRUD-portal_universitario
```

Se estiver clonando pelo Git:

```powershell
git clone <url-do-repositorio>
cd CRUD-portal_universitario
```

### 2. Criar o ambiente virtual

```powershell
python -m venv .venv
```

### 3. Ativar o ambiente virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativacao do ambiente, rode:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar as dependencias

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Aplicar as migrations

```powershell
python manage.py migrate
```

### 6. Executar o servidor

```powershell
python manage.py runserver
```

Acesse no navegador:

```text
http://127.0.0.1:8000/
```

## Como executar no Linux

Abra o terminal na pasta onde deseja deixar o projeto.

### 1. Entrar na pasta do projeto

Se voce ja tem o projeto baixado:

```bash
cd /caminho/para/CRUD-portal_universitario
```

Se estiver clonando pelo Git:

```bash
git clone <url-do-repositorio>
cd CRUD-portal_universitario
```

### 2. Criar o ambiente virtual

```bash
python3 -m venv .venv
```

Em algumas distribuicoes, pode ser necessario instalar o pacote de venv antes:

```bash
sudo apt install python3-venv
```

### 3. Ativar o ambiente virtual

```bash
source .venv/bin/activate
```

### 4. Instalar as dependencias

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Aplicar as migrations

```bash
python manage.py migrate
```

### 6. Executar o servidor

```bash
python manage.py runserver
```

Acesse no navegador:

```text
http://127.0.0.1:8000/
```

## Rotas principais

- `http://127.0.0.1:8000/alunos/`
- `http://127.0.0.1:8000/disciplinas/`
- `http://127.0.0.1:8000/notas/`
- `http://127.0.0.1:8000/admin/`

## Criar usuario administrador

Para acessar o painel `/admin/`, crie um superusuario:

```bash
python manage.py createsuperuser
```

No Windows, o comando e o mesmo se o ambiente virtual estiver ativo:

```powershell
python manage.py createsuperuser
```

## Rodar testes

Windows:

```powershell
python manage.py test
```

Linux:

```bash
python manage.py test
```

## Verificar problemas no projeto

```bash
python manage.py check
```

## Variaveis de ambiente para producao

Para rodar em producao, configure pelo menos:

- `DJANGO_PRODUCTION=True`
- `DJANGO_SECRET_KEY=<uma-chave-secreta-forte>`
- `DJANGO_ALLOWED_HOSTS=<dominios-permitidos>`

Exemplo no Linux:

```bash
export DJANGO_PRODUCTION=True
export DJANGO_SECRET_KEY="troque-por-uma-chave-forte"
export DJANGO_ALLOWED_HOSTS="seudominio.com,www.seudominio.com"
```

Exemplo no PowerShell:

```powershell
$env:DJANGO_PRODUCTION="True"
$env:DJANGO_SECRET_KEY="troque-por-uma-chave-forte"
$env:DJANGO_ALLOWED_HOSTS="seudominio.com,www.seudominio.com"
```

Para desenvolvimento local, essas variaveis nao sao obrigatorias.
