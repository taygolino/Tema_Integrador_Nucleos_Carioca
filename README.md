# Tema Integrador - Núcleos Cariocas
Trabalho de extensão do curso de Ciência da Computação (EAD), com foco na documentação, modelagem e implementação básica de um banco de dados para um sistema de apoio a uma academia popular voltada ao público idoso.

## Sobre o Projeto
O **NÚCLEOS CARIOCAS** é um projeto da Secretaria Municipal de Assistência Social do Rio de Janeiro, que visa promover a inserção social em áreas de vulnerabilidade.<br>
Atualmente, são mais de 75 núcleos em toda a cidade, cujas atividades beneficiam crianças, adolescentes, adultos e idosos.<br>
Cada núcleo oferece atividades de cultura, esporte e lazer, com o objetivo de aumentar a autoestima e a autonomia dos participantes.<br>
As atividades são desenvolvidas de acordo com as necessidades locais e são realizadas em parceria com os Centros de Referência em Assistência Social (CRAS), que encaminham os usuários às atividades.<br>
Para esse projeto, estamos atuando na academia popular, realizada na Associação de Moradores de Oswaldo Cruz.<br>
O responsável pelo projeto em Oswaldo Cruz é o Segio Corrêa, professor de Educação Física e quem ministra as aulas.


## Objetivo
Esse trabalho é a continuação do tema integrador anterior. Através de ferramentas, como o MariaDB e o Flask, irei, com a orientação da professora Denise, criar uma aplicação web para registro e controle de dados dos alunos e professores do projeto Núcleos Cariocas.<br>
Começamos o projeto com a criação de um banco de dados, que se conectará ao html através do python. Utilizando também a interface de rotas do Flask, a aplicação permite cadastro, alteração, exclusão e busca no banco da dados criados.<br>
O foco é que todo o sistema funcione, com o mínimo de erros possível. O design ainda está um pouco “cru”, mas espero melhora-lo em próximas versões.


## ODS 17 — Parcerias e Meios de Implementação
Essa ODS fala sobre:
- cooperação;
- parcerias;
- integração entre comunidade, instituições e sociedade;
- compartilhamento de conhecimento e tecnologia para melhorar a qualidade de vida das pessoas.

Essa ODS se relaciona com o nosso trabalho, pois ele foi pensado para apoiar um projeto social comunitário voltado ao público idoso, promovendo a colaboração e melhoria na gestão das atividades realizadas.<br>
Além disso, o sistema proposto contribui para facilitar a comunicação entre professores e alunos, centralizar informações importantes e ampliar a acessibilidade digital para os participantes do projeto. Dessa forma, a iniciativa demonstra como a tecnologia pode ser utilizada para fortalecer ações sociais e apoiar a inclusão da população idosa em atividades comunitárias.


## Estrutura do repositório
- `docs/`: documentação do projeto, requisitos, regras de negócio e diagramas.
- `database/`: Banco de dados do projeto. Foi usado o MariaDB nesse projeto.
- `models/`: Onde ficam as Classes em Python.
- `repositories`: Onde ficam os códigos do CRUD, para deixa-los separados e organizados.
- `templates`: As folhas de html do Flask ficam aqui.
- `static`: As folhas de estilo do Flask ficam aqui.
- `superados`: Os arquivos antigos ficam aqui, apenas para manter o histórico.

## Tecnologias e ferramentas
- MariaDB
- SQL
- HeidiSQL
- Draw.io
- Lucid.app
- GitHub
- Python 3.15.2
- Visual Studio Code
- Flask
- ChatGPT
- ClaudeIA


## Próximos passos
Próximas funcionalidades a serem implementadas:
1. Login e controle de usuários;
2. Tratamento de senhas usando hash;
3. Formatação dos campos de cpf, cref, telefone;
4. Adicionar seletores em campos que precisam existir no DB, para auxiliar o preenchimento;
5. Melhorias de acessibilidade e responsividade;
6. Relatórios de frequência e participação.


## Autor
Fabiano H. Carminatti Jr

## Profª Orientadora
Denise Moraes
