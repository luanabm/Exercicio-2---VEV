from src.TipoFatura import TipoFatura

class Fatura:
  def __init__(self, cliente: str, endereco: str, tipo: TipoFatura, valor: int) -> None:
    self.cliente = cliente
    self.endereco = endereco
    self.tipo = tipo
    self.valor = valor
