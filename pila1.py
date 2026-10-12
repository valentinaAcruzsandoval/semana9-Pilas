stack = []

def push(item, capacity):
    if not is_full(capacity):   
        stack.append(item)
        return "Elemnto apilado...."
    return "pila llena"

def isEmpty():
    return not len(stack)

def is_full(capacity):
    return len(stack) == capacity

def peek():
    if not isEmpty():
        return stack[-1]
    return "pila vacia...." 

def pop():
    if not isEmpty():
        return stack.pop()
    return "Pila Vacia"

def show():
    message = ""
    for item in reversed(stack):
        message += f"|{item :>6}|\n"
        message += f"L" + "-"*8 + "L\n"
    return message

capacity = int (input("Dime el tamaño de la pila: ")) 
while True:
    item  = input("Dime un valor: ")
    print(push (item, capacity))
    answer = input("Deseas agregar otro dato: [S/N]: ")
    if answer.lower() == "n":
        break

print("Mostrar tope")
print(peek())
print(peek())

print(show())

print("Desapilar")
while True:
    answer = input("Deseas desapilar [S/N]: ")
    if answer.lower() == "s":
        print(pop())
    elif answer.lower() == "n":
        break
    else:
        print("OPCION INVALIDA..........")