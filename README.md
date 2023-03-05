# Listagem de Jogos

O projeto consiste em uma aplicação web desenvolvida em Python utilizando o framework Flask. A aplicação tem como objetivo permitir que o usuário liste jogos que foram adicionados e crie novos jogos para serem adicionados. Para garantir a segurança da aplicação, foi adicionada uma rota de login que verifica se o usuário está autenticado e permite que ele acesse outras rotas da aplicação.

A autenticação é realizada por meio de um formulário de login que solicita o nome de usuário e a senha. Após o login bem-sucedido, o usuário é redirecionado para a página principal da aplicação, onde pode visualizar a lista de jogos adicionados e criar novos jogos.

Caso o usuário tente acessar outras rotas sem estar autenticado, a aplicação verifica sua autenticação e redireciona-o para a página de login, impedindo o acesso não autorizado.

A aplicação também possui uma rota de logout que permite que o usuário faça logout da aplicação e seja redirecionado para a página de login novamente.

Para melhorar a experiência do usuário, a aplicação utiliza um pouco de JavaScript para criar botões e facilitar a navegação entre as páginas. Também foi utilizado o framework Bootstrap para estilizar a aplicação.

Em resumo, o projeto consiste em uma aplicação web em Python com o framework Flask,feita ao assistir o curso da Alura sobre flask, que permite ao usuário listar e criar jogos. A aplicação é segura e utiliza JavaScript e Bootstrap para melhorar a experiência do usuário.