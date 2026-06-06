"""
AI Agent Template - Sín dependencias conflictivas
Funciona con LangChain Groq (cualquier versión)
"""

import os
from dotenv import load_dotenv

# Cargar API key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    print("❌ Error: GROQ_API_KEY no encontrada")
    exit(1)

print("✅ API Key cargada")

# Verificar Groq
try:
    from langchain_groq import ChatGroq
    print("✅ LangChain Groq importado")
except Exception as e:
    print(f"❌ Error importando: {e}")
    print("Ejecuta: pip install langchain-groq")
    exit(1)

# ============================================
# FUNCIONES DE HERRAMIENTAS
# ============================================

def calculadora(expresion):
    try:
        expresion_limpia = expresion.replace('x', '*').replace('X', '*')
        # Extraer números y operadores
        import re
        # Eliminar texto no matemático
        partes = re.findall(r'[\d\.\-\+\*/]+', expresion_limpia)
        if partes:
            resultado = eval(partes[0])
            return f"📐 Resultado: {resultado}"
        return "❌ No entendí la operación"
    except:
        return "❌ No pude calcular"

def contar_caracteres(texto):
    return f"📝 {len(texto)} caracteres"

def contar_palabras(texto):
    return f"📖 {len(texto.split())} palabras"

def invertir(texto):
    return f"🔄 {texto[::-1]}"

def mayusculas(texto):
    return f"🔠 {texto.upper()}"

def minusculas(texto):
    return f"🔡 {texto.lower()}"

# ============================================
# INICIALIZAR MODELO
# ============================================

print("🔄 Inicializando Llama 3.3...")

try:
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",  # ✅ Modelo actualizado y gratuito
        temperature=0.7,
        api_key=GROQ_API_KEY
    )
    print("✅ Modelo listo!")
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)

# ============================================
# INTERFAZ
# ============================================

print("\n" + "=" * 50)
print("🤖 AI AGENT - GRATIS CON GROQ")
print("=" * 50)
print("Comandos:")
print("  • 'calc: 2+2' - Calculadora")
print("  • 'len: texto' - Contar caracteres")
print("  • 'words: texto' - Contar palabras")
print("  • 'rev: texto' - Invertir")
print("  • 'up: texto' - Mayúsculas")
print("  • 'low: texto' - Minúsculas")
print("  • 'chat: pregunta' - Usar IA")
print("  • 'exit' - Salir")
print("=" * 50 + "\n")

while True:
    try:
        user = input("🧠 Tú: ").strip()
        
        if not user:
            continue
        if user.lower() == 'exit':
            print("👋 Adiós!")
            break
        
        # Procesar comandos
        if user.startswith('calc:'):
            respuesta = calculadora(user[5:].strip())
        elif user.startswith('len:'):
            respuesta = contar_caracteres(user[4:].strip())
        elif user.startswith('words:'):
            respuesta = contar_palabras(user[6:].strip())
        elif user.startswith('rev:'):
            respuesta = invertir(user[4:].strip())
        elif user.startswith('up:'):
            respuesta = mayusculas(user[3:].strip())
        elif user.startswith('low:'):
            respuesta = minusculas(user[4:].strip())
        elif user.startswith('chat:'):
            print("🤖 Pensando...")
            pregunta = user[5:].strip()
            if not pregunta:
                respuesta = "¿Qué quieres preguntar?"
            else:
                try:
                    response = llm.invoke(pregunta)
                    respuesta = response.content
                except Exception as e:
                    respuesta = f"Error: {e}"
        else:
            # Si no usa comando, intentar detectar automáticamente
            if any(c in user for c in ['+', '-', '*', '/']) and any(d.isdigit() for d in user):
                respuesta = calculadora(user)
            elif 'caracteres' in user.lower() or 'letras' in user.lower():
                # Extraer texto después de la acción
                palabras = user.split()
                if len(palabras) > 2:
                    texto = ' '.join(palabras[2:])
                    respuesta = contar_caracteres(texto)
                else:
                    respuesta = "Ejemplo: 'cuenta caracteres de hola mundo'"
            elif 'palabras' in user.lower():
                palabras = user.split()
                if len(palabras) > 2:
                    texto = ' '.join(palabras[2:])
                    respuesta = contar_palabras(texto)
                else:
                    respuesta = "Ejemplo: 'cuenta palabras de hola mundo'"
            elif 'invierte' in user.lower():
                palabras = user.split()
                if len(palabras) > 1:
                    texto = ' '.join(palabras[1:])
                    respuesta = invertir(texto)
                else:
                    respuesta = "Ejemplo: 'invierte hola mundo'"
            else:
                # Usar IA
                print("🤖 Pensando...")
                try:
                    response = llm.invoke(user)
                    respuesta = response.content
                except Exception as e:
                    respuesta = f"Error: {e}"
        
        print(f"🤖 Agente: {respuesta}\n")
        
    except KeyboardInterrupt:
        print("\n👋 Adiós!")
        break
    except Exception as e:
        print(f"❌ Error: {e}\n")