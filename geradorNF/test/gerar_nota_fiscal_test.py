from src.Fatura import Fatura
from src.TipoFatura import TipoFatura
from src.GeradorNF import GeradorNF

def test_gera_nota_fiscal():
  nome_cliente = "Amanda"
  endereco_cliente = "Rua Arnald"
  tipo_servico = TipoFatura.CONSULTORIA
  valor_fatura = 1000
  fatura = Fatura(nome_cliente, endereco_cliente, tipo_servico, valor_fatura)

  gerador_nf = GeradorNF()

  nf = gerador_nf.execute(fatura)
  assert nf.cliente == nome_cliente

def test_gera_nota_fiscal_25_imposto():
  nome_cliente = "Amanda"
  endereco_cliente = "Rua Arnald"
  tipo_servico = TipoFatura.CONSULTORIA
  valor_fatura = 1000
  fatura = Fatura(nome_cliente, endereco_cliente, tipo_servico, valor_fatura)

  gerador_nf = GeradorNF()

  nf = gerador_nf.execute(fatura)
  assert nf.valor == valor_fatura
  assert nf.imposto == valor_fatura * 0.25

def test_gera_nota_fiscal_15_imposto():
  nome_cliente = "Amanda"
  endereco_cliente = "Rua Arnald"
  tipo_servico = TipoFatura.TREINAMENTO
  valor_fatura = 1000
  fatura = Fatura(nome_cliente, endereco_cliente, tipo_servico, valor_fatura)

  gerador_nf = GeradorNF()

  nf = gerador_nf.execute(fatura)
  assert nf.valor == valor_fatura
  assert nf.imposto == valor_fatura * 0.15

def test_gera_nota_fiscal_6_imposto():
  nome_cliente = "Amanda"
  endereco_cliente = "Rua Arnald"
  tipo_servico = TipoFatura.AVULSA
  valor_fatura = 1000
  fatura = Fatura(nome_cliente, endereco_cliente, tipo_servico, valor_fatura)

  gerador_nf = GeradorNF()

  nf = gerador_nf.execute(fatura)
  assert nf.valor == valor_fatura
  assert nf.imposto == valor_fatura * 0.06
