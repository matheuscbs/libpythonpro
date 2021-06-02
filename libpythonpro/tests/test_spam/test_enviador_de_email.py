from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'matheuscbsmsn1994@gmail.com',
        'matheuscbsmsn1994@gmail.com',
        'Curso Python Pro',
        'Primeira turma Guido Von Rossum Aberto'
    )
    assert 'matheuscbsmsn1994@gmail.com' in resultado