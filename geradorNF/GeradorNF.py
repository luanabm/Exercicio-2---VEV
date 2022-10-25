from src.enums.TipoFatura import TipoFatura
from src.entities.Fatura import Fatura
from src.entities.NotaFiscal import NotaFiscal

class GeradorNF:
  def execute(self, fatura: Fatura) -> NotaFiscal:
    if(fatura.tipo == TipoFatura.CONSULTORIA):
      imposto = fatura.valor * 0.25
    elif(fatura.tipo == TipoFatura.TREINAMENTO):
      imposto = fatura.valor * 0.15
    else:
      imposto = fatura.valor * 0.06
    return NotaFiscal(fatura.cliente, fatura.valor, imposto) 