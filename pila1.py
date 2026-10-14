def push(stack, item, capacity):
    """Agrega un elemento si la pila tiene espacio."""
    if len(stack) >= capacity:
        return False

    stack.append(item)
    return True


def is_empty(stack):
    """Comprueba si la pila está vacía."""
    return len(stack) == 0


def is_full(stack, capacity):
    """Comprueba si se alcanzó la capacidad máxima."""
    return len(stack) >= capacity


def peek(stack):
    """Devuelve el elemento del tope sin eliminarlo."""
    if is_empty(stack):
        return None

    return stack[-1]


def pop(stack):
    """Elimina y devuelve el elemento del tope."""
    if is_empty(stack):
        return None

    return stack.pop()


def show(stack):
    """Devuelve los elementos del tope al fondo."""
    return list(reversed(stack))