import random

def patrullar(bot):
    """El bot camina de un lado a otro"""
    if random.random() < 0.02:  # 2% de chance de cambiar dirección
        bot.direccion *= -1  
    bot.x += bot.direccion * bot.speed
    return True  
# Detecta si el enemigo está cerca
def detectar_enemigo(bot):
    """Simulación de detección de enemigos"""
    distancia = ((bot.target.x - bot.x) ** 2 + (bot.target.y - bot.y) ** 2) ** 0.5
    return distancia < 200  
    

def atacar(bot):
    """El bot dispara si el enemigo está en la mira"""
    if detectar_enemigo(bot):
        bot.disparar()
        return True  
    return False  

# Se aleja del peligro
def buscar_cobertura(bot):
    """Si el bot tiene poca vida, busca cobertura"""
    if bot.vida < 30:
        bot.x -= bot.direccion * bot.speed  
        return True  
    return False  