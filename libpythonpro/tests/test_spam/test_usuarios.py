from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Matheus', email='matheuscbsmsn1994@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(conexao, sessao):
    usuarios = [
        Usuario(nome='Matheus', email='matheuscbsmsn1994@gmail.com'),
        Usuario(nome='Barbara', email='matheuscbsmsn1994@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
