import pytest as pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['matheuscbsmsn1994@gmail.com', 'matheus.souza00310@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'bahsantos1996@gmail.com',
        'Curso Python Pro',
        'Primeira turma Guido Von Rossum Aberto'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    [' ', 'matheus.souza']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'bahsantos1996@gmail.com',
            'Curso Python Pro',
            'Primeira turma Guido Von Rossum Aberto'
        )
