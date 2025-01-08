# furia-chal-01

Este repositório referênciará todo o Desafio 01 da Mentoria Furia TECH - Intensivo Computer Science + Esports

MVP 0.1:
  Criar um Webchat (optamos pelo Telegram Bot) na qual irá informar os próximos jogos, estatísticas da line-up de CS2 e redes sociais, tudo isso de forma interativa e conversacional.

O código foi desenvolvido em Python e há uma pequena Infra na AWS, na qual buscamos as  informações que gostaríamos, entregando assim escalabilidade (para caso entrem outros times como a Furia Academy), alta disponibilidade, desacoplamento e segurança.

Pesquisamos para buscarmos API's nos sites mais famosos, afim de termos sempre dados atualizados sobre o time além de notícias e os resultados das partidas futuras, presentes e passadas. Porém, para o nosso infortúnio, apenas a Liquipedia tem uma API pública que é solicitada por meio de requisição no discord oficial deles. Por esse motivo e outros como prazo de entrega e "custo de evolução" optamos por armazenar os dados mais recentes (Jan./25) num DynamoDB em que nossa aplicação fará chamadas mediante a interação com o Bot.
