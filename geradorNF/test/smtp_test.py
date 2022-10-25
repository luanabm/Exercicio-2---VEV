from src.SMTPService import SMTP
from src.TipoFatura import TipoFatura
from src.Fatura import Fatura
from src.GeradorNF import GeradorNF

def test_deve_enviar_smtp():
  smtp = SMTP()
  nome_cliente = "Amanda"
  endereco_cliente = "Rua Arnald"
  tipo_servico = TipoFatura.CONSULTORIA
  valor_fatura = 1000
  fatura = Fatura(nome_cliente, endereco_cliente, tipo_servico, valor_fatura)

  gerador_nf = GeradorNF()

  nf = gerador_nf.execute(fatura)

  res = smtp.envia(nf)

  assert res == True
