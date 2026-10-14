from flask import Flask, render_template, request, session
from pila import push, is_empty, is_full, peek, pop, show

app = Flask(__name__)

# Solo para desarrollo. Cambia esta clave antes de publicar la app.
app.secret_key = "clave-de-desarrollo-cambiar-antes-de-publicar"


@app.route("/", methods=["GET", "POST"])
def index():
    # Cada sesión tendrá su propia pila y capacidad.
    stack = list(session.get("stack", []))
    capacity = session.get("capacity", 5)
    message = ""
    message_type = "info"

    if request.method == "POST":
        action = request.form.get("action", "")

        if action == "configurar":
            try:
                new_capacity = int(request.form.get("capacity", ""))

                if new_capacity < 1:
                    raise ValueError

                if new_capacity < len(stack):
                    message = (
                        "La capacidad no puede ser menor "
                        "que los elementos actuales."
                    )
                    message_type = "warning"
                else:
                    capacity = new_capacity
                    message = "Capacidad actualizada correctamente."
                    message_type = "success"

            except ValueError:
                message = "Introduce una capacidad entera mayor que cero."
                message_type = "danger"

        elif action == "push":
            item = request.form.get("item", "").strip()

            if not item:
                message = "Escribe un elemento antes de apilar."
                message_type = "warning"
            elif push(stack, item, capacity):
                message = f"Elemento «{item}» apilado correctamente."
                message_type = "success"
            else:
                message = "La pila está llena."
                message_type = "warning"

        elif action == "pop":
            removed = pop(stack)

            if removed is None:
                message = "La pila está vacía."
                message_type = "warning"
            else:
                message = f"Elemento desapilado: {removed}"
                message_type = "success"

        elif action == "peek":
            top = peek(stack)

            if top is None:
                message = "La pila está vacía."
                message_type = "warning"
            else:
                message = f"El elemento del tope es: {top}"
                message_type = "info"

        elif action == "limpiar":
            stack.clear()
            message = "La pila se ha vaciado."
            message_type = "success"

        else:
            message = "La operación solicitada no es válida."
            message_type = "danger"

        # Guardar el estado actualizado en la sesión.
        session["stack"] = stack
        session["capacity"] = capacity

    return render_template(
        "index.html",
        stack=show(stack),
        capacity=capacity,
        total=len(stack),
        full=is_full(stack, capacity),
        empty=is_empty(stack),
        message=message,
        message_type=message_type,
        top=peek(stack),
    )


if __name__ == "__main__":
    app.run(debug=True)
