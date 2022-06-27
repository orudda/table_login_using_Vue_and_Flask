#Login page and table handling with Vue.js and Flask enviroment

Neste trabalho eu realizei uma simples aplicação de Vue.js com Python/Flask. 
Há presente neste trabalho uma tela de login com 2 tabelas. A primeira mostra o cadastro das empresas e os atributos de cada uma delas. Já a segunda tabela mostra os usuários cadastrados de cada empresa e, também, seus respectivos atributos.
O ambiente inicial contém 2 uauários e 2 empresas.

##Adicionais

Vale notar que, neste trabalho, foi implementado algumas funcionalidades do dia-a-dia como, por exemplo: 
- um usuário só pode se cadastrar em uma empresa previamente cadastrada;
- quando uma empresa é removida, todos os usuários daquela empresa também são removidos;
- há atributos usados como chave primária. Então o usuário é obrigado a fornecê-los para garantir o funcionamento da empresa (o botão de cadastro não aparece com os campos obrigatórios vazios);
- quando um usuário é removido, aparece mensegem: 
  --user removed 
  quando uma empresa é removida, aparece a mensagem:
  --company removed
  quando uma empresa, com usuários cadastrados, é removida, aparece a mensagem:
  --company and user removed;  


## Ambiente

Este trabalho foi construído e testado em um ambiente Linux(Ubuntu), utilizando os seguintes pacotes:
- NPM = 7.4.3;
- Node = 15.7.0;
- vue = 2.6.11;
- bootstrap = 4.6.0;
- python = 3.9.12;
- flask = 2.0.1;
- flask-cors = 3.0.10

## Run

Com o ambiente acima configurado, é necessário entrar na pasta do projeto em './backend' e realizar o comando: $python\ main.py$ ou $python3\ main.py$

E, depois, na pasta './frontend/frontend' e realizar o comando: $npm\  install$ e $npm\  run\  serve$
