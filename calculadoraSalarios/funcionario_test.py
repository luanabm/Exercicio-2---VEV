import pytest
from funcionario import *

def test_valid_params_funcionario_init():
    funcionario = Funcionario('Amanda', 'amanda@ccc.ufcg.edu.br', 0, 'DESENVOLVEDOR')
    assert funcionario.nome == 'Amanda'
    assert funcionario.email == 'amanda@ccc.ufcg.edu.br'
    assert funcionario.salario_base == 0
    assert funcionario.cargo == 'DESENVOLVEDOR'

def test_invalid_params_funcionario_init():
    with pytest.raises(ValueError):
        funcionario = Funcionario('', '', -1, '')
        funcionario = Funcionario('', '', 0, 'PO')
        funcionario = Funcionario('', '', 0, '')

def test_valid_params_get_cargo():
    funcionario = Funcionario('Amanda', 'amanda@ccc.ufcg.edu.br', 0, 'DESENVOLVEDOR')
    assert funcionario.get_cargo() == 'DESENVOLVEDOR'

    funcionario = Funcionario('Amanda', 'amanda@ccc.ufcg.edu.br', 0, 'Gerente')
    assert funcionario.get_cargo() == 'GERENTE'

def test_valid_calc_salario_liquido():
    funcionario = Funcionario('Amanda', 'amanda@ccc.ufcg.edu.br', 7000, 'DESENVOLVEDOR')
    assert funcionario.calc_salario_liquido() == 5600.00

    funcionario = Funcionario('Amanda', 'amanda@ccc.ufcg.edu.br', 3000, 'DESENVOLVEDOR')
    assert funcionario.calc_salario_liquido() == 2400.00

    funcionario = Funcionario('Amanda', 'amanda@ccc.ufcg.edu.br', 2900, 'DESENVOLVEDOR')
    assert funcionario.calc_salario_liquido() == 2610.00

    funcionario = Funcionario('Amanda', 'amanda@ccc.ufcg.edu.br', 2000, 'DBA')
    assert funcionario.calc_salario_liquido() == 1500.00

    funcionario = Funcionario('Amanda', 'amanda@ccc.ufcg.edu.br', 1900, 'DBA')
    assert funcionario.calc_salario_liquido() == 1615.00

    funcionario = Funcionario('Amanda', 'amanda@ccc.ufcg.edu.br', 3000, 'TESTADOR')
    assert funcionario.calc_salario_liquido() == 2250.00

    funcionario = Funcionario('Amanda', 'amanda@ccc.ufcg.edu.br', 2000, 'TESTADOR')
    assert funcionario.calc_salario_liquido() == 1500.00

    funcionario = Funcionario('Amanda', 'amanda@ccc.ufcg.edu.br', 1999, 'TESTADOR')
    assert funcionario.calc_salario_liquido() == 1699.15

    funcionario = Funcionario('Amanda', 'amanda@ccc.ufcg.edu.br', 4000, 'GERENTE')
    assert funcionario.calc_salario_liquido() == 3200.00

    funcionario = Funcionario('Amanda', 'amanda@ccc.ufcg.edu.br', 5000, 'GERENTE')
    assert funcionario.calc_salario_liquido() == 3500.00
