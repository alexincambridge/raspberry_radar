def check_alert(distance) :
    """Devuelve un mensaje de alerta según la distancia."""
    if distance < 10 :
        return "¡Alerta! Un objeto está demasiado cerca."
    elif distance < 20 :
        return "Precaución: Objeto a distancia media."
    else :
        return "Distancia segura."
