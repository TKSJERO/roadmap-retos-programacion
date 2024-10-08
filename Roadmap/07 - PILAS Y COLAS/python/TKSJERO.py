"""
Ejercicio
"""

# Pila/Stock (Lifo)

stack = []

# push
stack.append("1")
stack.append("2")
stack.append("3")
print(stack)

# pop
stack_item = stack[len(stack) - 1]
del stack[len(stack) - 1]
print(stack_item)

print(stack.pop())

print(stack)

# Cola/ Queue (FIFO)

queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

# dequeue
queue_item = queue[0]
del queue[0]
print(queue_item)

print(queue.pop(0))

print(queue)

"""
Extra
"""

# Web

def web_navegation():

  stack = []

  while True:

      action = input(
          "Añada una url o interactua con palabras adelante/atras/salir: "
      )

      if action == "salir":
        print("Saliendo del navegador web.")
        break
      elif action == "adelante":
        pass
      elif action == "atras":
        if len(stack) > 0:
          stack.pop()
      else:
        stack.append(action)

      if len(stack) > 0:
         print(f"Has navegado a la web: {stack[len(stack) - 1]}")
      else:
        print("Estas en la pagina de inicio")

web_navegation()

def shared_printer():

  queue = []

  while True:
    
    action = input("Añade un documento o selecciona imprimir/salir:")

    if action == "salir":
      break
    elif action == "imprimir":
      if len(queue) > 0:
        print(f"Imprimiendo: {queue.pop(0)}")
    else: 
      queue.append(action)

    print(f"Cola de impresion: {queue}")
    

shared_printer()
