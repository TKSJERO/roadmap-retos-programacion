"""
Operaciones
"""

s1 = "Hola"
s2 = "Pythonthon"

# Concatenacion
print(s1 + ", " + s2 + "!")

# Repeticion
print(s1 * 3)

# Indexacion
print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitud
print(len(s2))

# Slicing (porcion)
print(s2[2:6])
print(s2[2:])
print(s2[0:2])
print(s2[:2])

# Busqueda
print("a" in s1)
print("i" in s1)

# Reemplazo
print(s1.replace("o", "a"))

# Division
print(s2.split("t"))

# Mayusculas, minusculas y letras en mayuscula
print(s1.lower())
print(s1.upper())
print("jeronimo zuluaga".title())
print("jeronimo zuluaga".capitalize())

# Eliminacion de espacios al principio y al final
print(" jeronimo zuluaga ".strip())

# Busqueda al principio y al final
print(s1.startswith("Ho"))
print(s1.startswith("Py"))
print(s1.endswith("la"))
print(s1.endswith("thon"))

s3 = "Jeronimo Zuluaga @tksjero"

# Busqueda y posicion
print(s3.find("jero"))
print(s3.find("Jero"))
print(s3.find("j"))
print(s3.lower().find("jero"))

# Busqueda de ocurrencias
print(s3.lower().count("j"))

# Formateo
print("Saludo: {}, lenguaje: {}".format(s1, s2))

# Interpolacion
print(f"Saludo: {s1}, lenguaje: {s2}")

# Transformacion en lista de caracteres
print(list(s3))

# Transformacion de lista en cadena
l4 = [s1, ", ", s2, "!"]
print("".join(l4))

# Tranformaciones numericas
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.123"
s5 = float(s5)
print(s5)

# Comprobaciones varias
s4 = "123456"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())


"""
Extra
"""

def check(word1: str , word2: str):

  # Palindromos
  print(f"¿{word1} es un palindromo?: {word1 == word1[::-1]}")
  print(f"¿{word2} es un palindromo?: {word2 == word2[::-1]}")

  # Anagrama
  print(f"¿{word1} es un anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

  # Isograma

  def isogram(word: str) -> bool:

    word_dict = dict()
    for word in word:
      word_dict[word] = word_dict.get(word, 0) + 1

    isogram = True
    values = list(word_dict.values())
    isogram_len = values[0]
    for word_count in values:
      if word_count != isogram_len:
        isogram = False
        break

    return isogram # no se por que no se imprime

    
    print(f"¿{word1} es un isograma?: {isogram(word1)}")
    print(f"¿{word2} es un isograma?: {isogram(word2)}")



check("radar", "pythonpythonpythonpython")
# check("amor", "roma")
