# def ConversaoRomano(valor):
#   romano = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#   i = 0
#   val_int = 0
#   while i < len(valor):
#     if i > 0 and romano[valor[i]] > romano[valor[i - 1]]:
#       val_int += romano[valor[i]] - 2 * romano[valor[i - 1]]
#       i += 1
#     else:
#       val_int += romano[valor[i]]
#       i += 1
#   return val_int


# print(ConversaoRomano("CDXLIII"))

def ConversaoRomano(valor):
  romano = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
  val_int = 0
  i = 0
  while i < len(valor):
    if i > 0 and romano[valor[i]] > romano[valor[i-1]]:
      val_int += romano[valor[i]] - 2 * romano[valor[i - 1]]
      i += 1
    else:
      val_int += romano[valor[i]]
      i += 1
  return val_int

print(ConversaoRomano("CDXLIII"))

