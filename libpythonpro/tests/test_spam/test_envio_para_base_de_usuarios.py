from unittest.mock import Mock

import pytest as pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Matheus', email='matheuscbsmsn1994@gmail.com'),
            Usuario(nome='Barbara', email='bahsantos1996@gmail.com')
        ],
        [
            Usuario(nome='Matheus', email='matheuscbsmsn1994@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'matheuscbsmsn1994@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Matheus', email='matheuscbsmsn1994@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'bahsantos1996@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'bahsantos1996@gmail.com',
        'matheuscbsmsn1994@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
