from src.NotaFiscal import NotaFiscal

class SMTP:
  def envia(self, nf: NotaFiscal) -> bool:
    print("enviando por smtp", nf.cliente)
    return True
