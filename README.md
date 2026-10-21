O Sistema de Reservas é uma aplicação desenvolvida para facilitar o gerenciamento de recursos, horários, valores e disponibilidade, permitindo organizar reservas de forma prática e segura, 
evitando conflitos de horários.


=========== TAREFAS =============

[OK] Criar tabela locacao
[OK] Fazer o GET da rota de locações
[OK] Passar a lógica que está no controller de recurso para service
[OK] Passar a lógica que está no controller de locacao para service



GET DE CONTROLLER LOCACAO E GET DE CONTROLLER RECURSO FEITO, PROXIMO PASSO FAZER POST?

[ ] Mover docker compose pro .env, criando git ignore e .env de fato
[OK] Corrigir estrutura do locacao
[OK] Adicionar a lógica de valores, considerando os dias do recurso alocado e o proprio valor do recurso, com timedelta e timezone no service de locacao
[OK] Rota de criar usuário
[OK] Executar testes de rota já com o usuário
[OK] Validar rota de usuarios (controller e service)
[OK] Fazer HASH
[ ] Em um melhor momento, adicionar token e refresh token, depois de executar testes com usuário e hash.
[ ] Melhorar status da locação
[ ] Criar a rota de login com token jwt (deixar refresh token para depois)