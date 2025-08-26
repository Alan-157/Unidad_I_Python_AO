from django.shortcuts import render

# Create your views here.
def inicio(request):
    contexto = {"nombre": "Alan"}
    productos = [
        {"nombre": "Sensor 1", "valor": 100},
        {"nombre": "Sensor 2", "valor": 200},
        {"nombre": "Sensor 3", "valor": 300}     
    ]
    
    return render(request, "dispositivos/inicio.html", {
        "contexto": contexto,
        "productos": productos
        })
    
def panel_dispositivos(request):
    dispositivos = [
        {"nombre": "Sensor Temperatura", "consumo": 50},
        {"nombre": "Medidor Solar", "consumo": 120},
        {"nombre": "Sensor Movimiento", "consumo": 30},
        {"nombre": "Calefactor", "consumo": 200},
    ]
    
    consumo_maximo = 40
    
    for d in dispositivos:
        if d["consumo"] > consumo_maximo:
            d["estado"] = "Exceso"
            d["color"] = "red"
        else:
            d["estado"] = "Correcto"
            d["color"] = "green"
    
    estado_critico = 0
    for d in dispositivos:
        if d["estado"] =="Exceso":
            estado_critico +=1
            
    contexto = {
        "dispositivos": dispositivos,
        "consumo_maximo": consumo_maximo,
        "estado_critico": estado_critico
    }
    
    return render(request, "dispositivos/panel.html", contexto)
