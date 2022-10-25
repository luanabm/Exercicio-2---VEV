from src.entities.NotaFiscal import NotaFiscal

class NFRepository:
  def salva(self, nf: NotaFiscal) -> bool:
    print("NF salva no banco", nf.cliente)
    return True