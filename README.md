# BACKEND

# Social Periódicos

## Descrição
Projeto Spring Boot para gerenciar perfis e afinidades.

## Pré-requisitos
- Java 11 ou superior
- Maven 3.6.0 ou superior~
- Node.js 14 ou superior
- Angular CLI 12 ou superior


## Configuração do Projeto

### Clonar o repositório

``` sh
``` git clone https://github.com/rodrigogregorioneri/socialperiodicos.git
``` cd socialperiodicos

## Compilar o projeto

mvn clean install

## Executar o projeto

mvn spring-boot:run

## Endpoints
## Criar Perfil

POST /perfil/affinities

## Gerar Documentação
## Para gerar a documentação do projeto, execute o seguinte comando:

mvn javadoc:javadoc

## Testes
## Para executar os testes, use o comando:

mvn test

FrontEnd

## Social Periódicos Frontend

## Descrição
Projeto frontend desenvolvido com Angular para gerenciar perfis e afinidades.

## Pré-requisitos
- Node.js 14 ou superior
- Angular CLI 12 ou superior

## Configuração do Projeto

### Clonar o repositório
```sh
``` git clone https://github.com/rodrigogregorioneri/socialperiodicos-frontend.git
``` cd socialperiodicos-frontend


Instalar dependências

npm install

ng serve

## O projeto estará disponível em http://localhost:4200.  
## Estrutura do Projeto

``` src/app: Contém os componentes, serviços e módulos do projeto.
``` src/assets: Contém os arquivos estáticos como imagens e estilos.
``` src/environments: Contém os arquivos de configuração de ambiente.


``` ng build --prod

## Os arquivos gerados estarão na pasta dist/.  

## Testes

## Para executar os testes unitários, use o comando:

``` ng test





```markdown
# Social Periódicos Backend em Python

## Descrição
Projeto backend desenvolvido em Python para gerenciar perfis e afinidades.

## Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)

## Configuração do Projeto

### Clonar o repositório
```sh
git clone https://github.com/rodrigogregorioneri/socialperiodicos-backend.git
cd socialperiodicos-backend
```

### Criar e ativar um ambiente virtual
```sh
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

### Instalar dependências
```sh
pip install -r requirements.txt
```

### Executar o projeto
```sh
python agents.py
```
## Estrutura do Projeto
- `agents.py`: Arquivo principal do aplicativo.
- `requirements.txt`: Lista de dependências do projeto.
- `scrapper/`: Contém o Scrapper responsavel por extrair texto dos periodicos.
- `agent/`: Contém o módulos Agent responsavel por usar IA para analisar e responder peguntas baseadas nas docs.

Obs. necessario criar uma API para consumir esses dados OPEN IA e Integrar com o backend Java

## Testes
Para executar os testes, use o comando:
```sh
pytest
```
```