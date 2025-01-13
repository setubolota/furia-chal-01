# furia-chal-01

Este repositório referênciará todo o Desafio 01 da Mentoria Furia TECH - Intensivo Computer Science + Esports

MVP 0.1:
  Criar um Webchat (optamos pelo Telegram Bot) na qual irá informar os próximos jogos, estatísticas da line-up de CS2 e redes sociais, tudo isso de forma interativa e conversacional.

O código foi desenvolvido em Python e há uma pequena Infra na AWS, na qual buscamos as  informações que gostaríamos, entregando assim escalabilidade (para caso entrem outros times como a Furia Academy), alta disponibilidade, desacoplamento e segurança.

Pesquisamos para buscarmos API's nos sites mais famosos, afim de termos sempre dados atualizados sobre o time além de notícias e os resultados das partidas futuras, presentes e passadas. Porém, para o nosso infortúnio, apenas a Liquipedia tem uma API pública que é solicitada por meio de requisição no discord oficial deles. Por esse motivo e outros como prazo de entrega e "custo de evolução" optamos por armazenar os dados mais recentes (Jan./25) num DynamoDB em que nossa aplicação fará chamadas mediante a interação com o Bot.

----------------------------------------------------------------------------------------------------------------------------------

Temos o imenso prazer em compartilhar nosso código com a comunidade visando melhorias. 

# Documentação:

Hoje, fazemos uso da biblioteca do Telegram para python: python-telegram-bot - trazendo-nos a liberdade para criarmos, personalizarmos e até mesmo alterarmos informações do Bot via código. Assim que criamos o bot, recebemos um TOKEN na qual o mesmo servirá para vincularmos nossas chamadas a API, fazendo assim a conexão entre python -- Telegram.

Atualmente, há cerca de 4 comandos que escolhemos entregar ao usuário, sendo eles: 
    > /proximosjogos
    > /estatisticas
    > /resultados
    > /redes
    
Além propriamente do /start para incialização da conversa.

Ao iniciarmos a conversa com o comando */start*, o Bot responderá com a seguinte mensagem:

*"Falaaa Furiosx! Esperamos que esteja tudo bem! Para se comunicar digite ou clique nos comandos para interagir"
        "/proximosjogos - Próximos jogos da FURIA"
        "/estatisticas - Estatísticas do time"
        "/resultados - Resultados dos jogos passados"
        "/redes - Informe-se em nossas redes sociais!"*

Entregando assim suas opções ao usuário poder escolher quais informações ele deseja sobre a ORG e line-up.

# Caso 1:
Ao escolher */proximosjogos*, o Bot, automaticamente encaminhará uma requisição para a Lambda de nossa infra na AWS e retornará as próximas partidas em que o time de CS fará presença, juntamente com o nome do campeonato e as principais *streams* em que o usuário poderá acompanhar e prestigiar a equipe.

Tudo isso será feito pelo bloco de comandos disponibilizados na função *def proximos_jogos*

async def proximos_jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Os próximos jogos da nossa line serão:\n"
    )
    #REQ - API Gateway

Essa consulta será feita por uma API que se comunicará ao API Gateway na AWS, acionando assim uma Lambda que fará a execução e a chamada do DynamoDB, e para finalizar retornará os dados em um JSON. Ao devolver para a Lambda, haverá um processo de tratativa e limpeza desse JSON, disponibilizando assim somente o que o usuário final deseja saber, como o adversário, nome do torneio e data do jogo.

# Caso 2:
Este comando foi dedicado para o usuário ficar inteirado sobre informações da line-up, tal qual constará com:

  > ADR - Average Damage per Round;
  > KDR - Kill and Death per Round;
  > Impact - Medição de multikills, openning kills e clutches;
  > Função - Função atribuída ingame;
  > Nome - nick do player; 

Esses retornos estão anexados dentro do Dynamo, que serão obtidos por um método GET.

# Caso 3:
Comportamento similar ao *Caso 2* porém ao invés de retornar as estatística será devolvido os resultados dos últimos jogos, atribuindo assim placares, adversários e qual torneio.

# Caso 4: 
Quando o usuário optar por este comando, será encaminhado uma mensagem com as redes sociais da *FURIA*. Nossa intenção foi simples: Dependendo do usuário, talvez ele não siga as redes, deixando-o desinformado sobre os acontecimentos recentes, resultados e outras lines como por ex. a de R6, Rocket League ou Valorant. - Com isso, nos importamos em disponibilizar todo e qualquer meio de comunicação que um torcedor possa ficar por dentro de novidades, não se limitando apenas ao CS2, mas sim envolvendo-o em todo o ambiente FURIA.
