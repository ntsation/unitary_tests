def calcular_media(lista)
   if len(lista) == 0
      raise ValueError("A lista não pode ser vazia")
   total = sum(lista)
   return total / len(lista)

if __name__ == "__main__":
   numeros = [10, 20, 30, 40, 50]
   media = calcular_media(lista)
   print(f"A média é {media}")