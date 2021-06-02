from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Matheus')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(conexao, sessao):
    usuarios = [Usuario(nome='Matheus'), Usuario(nome='Luciano')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
