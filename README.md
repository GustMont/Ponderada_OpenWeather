# Ponderada_OpenWeather
Criação de uma ETL em flask com teste de integração que leia da API OpenWeather, manipule os dados em uma tabela nova guardando as informações em 4 colunas: Data da Ingestão, Tipo, Valores, Uso

## Passos para o funcionamento do código

### Requisitos
Python 3.x instalado
Pip instalado

### Configuração da Chave da API OpenWeather
A partir da chave da API fornecida no sistema da faculdade, ou uma chave gerada no site https://openweathermap.org/api:
Substitua 'put_the_api_key_here' em ponderada_openweather.py pela chave real

### Executando o Aplicativo Flask
Considerando que o ambiente virtual está ativado, execute o aplicativo Flask com o comando:
python PODEMUDARONOME_app.py

O endereço, por padrão definido pelo Flask estará disponível em: http://127.0.0.1:5000/

Ao executar o aplicativo Flask, um arquivo do banco de dados SQLite é gerado.

### Executando o Teste
Execute o teste com pytest de com o comando:
pytest tests/

## Explicação Geral do Código: ponderada_openweather.py
### Configuração do Flask
Importa classe Flask, configurando e definindo aplicativo com a função create_app().

Utiliza o SQLAlchemy para interagir com um banco de dados SQLite, definindo um modelo que representa a estrutura da tabela para armazenar dados climáticos.

### Implementação da ETL
Define uma rota /get_openweatherdata que responde a requisições GET.
Dentro da rota, faz chamadas à API OpenWeather para obter dados climáticos de cidades específicas, realizando uma chamada à API OpenWeather para obter dados climáticos de cidades específicas no Brasil.

### Descrição do Armazenamento dos Dados
O SQLAlchemy carrega os dados transformados na tabela PODEMUDARONOMEData do banco de dados SQLite.
Define uma tabela no banco de dados SQLite chamada openweatherdata com colunas para armazenar a data da ingestão, o tipo, os valores e o uso.

Em relação à chave da API, deve ser utilizada a fornecida no sistema da faculdade ou no site https://openweathermap.org/api e substituir a string de chave no código put_the_api_key_here

Os dados climáticos processados são persistidos no banco de dados SQLitee armazenando as informações.

A rota /get_openweatherdata retorna os dados processados em formato JSON, proporcionando uma interface para que outros aplicativos ou serviços possam consumir esses dados.

