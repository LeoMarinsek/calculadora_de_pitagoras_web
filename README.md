# Calculadora de Pitágoras Web
Este projeto é uma aplicação web que funciona como uma Calculadora de Pitágoras. Com ela, os usuários podem inserir os comprimentos dos dois lados de um triângulo retângulo e obter o comprimento da hipotenusa. Além disso, a aplicação mantém e exibe um histórico dos cálculos feitos pelo usuário.

## Funcionamento do Projeto
O projeto é desenvolvido em Python usando o framework Flask para o back-end e HTML, CSS e JavaScript para o front-end. O back-end recebe os comprimentos dos lados do triângulo através de um formulário HTML e realiza os cálculos necessários para obter a hipotenusa. Os dados dos cálculos são armazenados em um banco de dados SQLite para manter o histórico.
A interface do usuário é simples e amigável, permitindo que o usuário insira os comprimentos dos lados e clique em um botão para calcular a hipotenusa. O resultado é exibido na mesma página, juntamente com o histórico de cálculos anteriores.

## Requisitos do Projeto

### Front-end:
- Interface do usuário com campos para inserção dos comprimentos dos lados.
- Botão para calcular a hipotenusa.
- Exibição do resultado do cálculo e histórico de cálculos anteriores.

### Back-end:
- Receber os comprimentos dos lados como parâmetros.
- Calcular a hipotenusa usando a fórmula de Pitágoras.
- Armazenar os dados do cálculo (lados, hipotenusa e timestamp) no banco de dados.
- Entregar o histórico de cálculos para o front-end.

### Banco de Dados:
- Utilizar o SQLite para armazenar o histórico de cálculos.
- Cada entrada no banco de dados deve incluir os comprimentos dos lados, a hipotenusa calculada e o timestamp do cálculo.

## Estrutura de Arquivos
- app.py: Contém o código do back-end, incluindo as rotas para lidar com as requisições do front-end, os cálculos da hipotenusa e a interação com o banco de dados.
- templates/: Pasta contendo o arquivo HTML (index.html) que define a interface do usuário.
- static/: Pasta contendo o arquivo CSS (styles.css) para a estilização do front-end.

## Execução do Projeto
1. Certifique-se de ter Python e o pacote flask instalado.
2. Clone este repositório em sua máquina local.
3. Acesse a pasta do projeto no terminal.
4. Execute o comando python app.py.
5. O servidor Flask será iniciado e você poderá acessar a aplicação em seu navegador através do endereço http://localhost:5000/.

## Personalização
Você pode personalizar este projeto de acordo com suas preferências. Por exemplo, pode estilizar a interface de acordo com sua identidade visual, adicionar novas funcionalidades ou melhorar a usabilidade.

## Considerações Finais
A Calculadora de Pitágoras Web é um projeto simples, mas útil para entender conceitos fundamentais do desenvolvimento web. O projeto combina o uso de back-end com Python, front-end com HTML/CSS/JavaScript e banco de dados SQLite, proporcionando uma experiência completa de desenvolvimento web. Sinta-se à vontade para contribuir, melhorar e adaptar este projeto de acordo com suas necessidades.
