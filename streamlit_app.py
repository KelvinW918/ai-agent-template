"""
KelvIA · Cognitive Engine - Interfaz Web Profesional
Ejecutar: streamlit run streamlit_app.py
"""

import streamlit as st
import os
import re
from datetime import datetime
from dotenv import load_dotenv

# Cargar API key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ============================================
# CONFIGURACIÓN DE PÁGINA
# ============================================

st.set_page_config(
    page_title="KelvIA · Cognitive Engine",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# CSS PERSONALIZADO
# ============================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Header personalizado - Estilo Cyber-Sleek */
    .main-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 2rem;
        border-radius: 1.5rem;
        margin-bottom: 1rem;
        text-align: center;
        border: 1px solid #334155;
    }
    
    .main-header h1 {
        color: #f8fafc;
        margin: 0;
        font-size: 2.5rem;
        font-weight: 800;
        letter-spacing: -0.05em;
    }
    
    .main-header p {
        color: #94a3b8;
        margin: 0.5rem 0 0 0;
        font-family: 'JetBrains Mono', monospace;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    
    .tool-card {
        background: #0f172a;
        padding: 0.8rem;
        border-radius: 0.8rem;
        margin: 0.3rem 0;
        border-left: 3px solid #38bdf8;
        transition: transform 0.2s;
    }
    
    .tool-card strong { color: #f1f5f9; }
    
    .tool-card code {
        color: #38bdf8;
        background: #000;
        padding: 0.2rem 0.4rem;
        border-radius: 0.3rem;
        font-size: 0.75rem;
    }
    
    .tool-card:hover { transform: translateX(5px); }
    
    .status-badge {
        display: inline-block;
        padding: 0.2rem 0.6rem;
        border-radius: 2rem;
        font-size: 0.7rem;
        font-weight: 600;
        background: #0ea5e922;
        color: #38bdf8;
        border: 1px solid #38bdf8;
    }
    
    .instruction-box {
        background: #1e293b;
        padding: 1rem;
        border-radius: 1rem;
        border: 1px dashed #475569;
        margin-bottom: 2rem;
        color: #e2e8f0;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# HERRAMIENTAS DEL AGENTE
# ============================================

def calculadora(expresion):
    try:
        expresion_limpia = expresion.replace('x', '*').replace('X', '*')
        partes = re.findall(r'[\d\.\-\+\*/]+', expresion_limpia)
        if partes:
            resultado = eval(partes[0])
            return f"⚙️ **{expresion}** = `{resultado}`"
        return "⚠️ No entendí la operación."
    except:
        return "⚠️ Error en el cálculo."

def contar_caracteres(texto):
    return f"📟 **{len(texto)}** chars | 🔣 {len([c for c in texto if c.isalpha()])} letters"

def contar_palabras(texto):
    palabras = texto.split()
    return f"📝 **{len(palabras)}** words | 📐 avg: `{sum(len(p) for p in palabras)/len(palabras):.1f}` len/word"

def invertir(texto):
    return f"🔄 `{texto}` → `{texto[::-1]}`"

def mayusculas(texto):
    return f"⬆️ `{texto}` → **{texto.upper()}**"

def minusculas(texto):
    return f"⬇️ `{texto}` → **{texto.lower()}**"

# ============================================
# INICIALIZAR MODELO
# ============================================

@st.cache_resource
def init_llm():
    try:
        from langchain_groq import ChatGroq
        llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            api_key=GROQ_API_KEY
        )
        return llm
    except Exception as e:
        st.error(f"❌ Error de inicialización: {e}")
        return None

# ============================================
# INTERFAZ
# ============================================

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div class="main-header">
        <h1>⚡ KelvIA</h1>
        <p>Cognitive Agentic Engine · v1.0.0</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="instruction-box">
        <b>💡 Quick Start:</b> Revisa el panel de la izquierda para ver los comandos disponibles. 
        Simplemente escribe el prefijo (ej. <code>calc:</code>) seguido de tu petición en el chat de abajo.
    </div>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 🔌 **System Control**")
    st.markdown('<span class="status-badge">🟢 KELVIA ONLINE</span>', unsafe_allow_html=True)
    st.markdown(f"**Core:** Llama 3.3 70B")
    
    st.markdown("---")
    st.markdown("### 🛠️ **Kernel Toolkit**")
    
    tools_list = [
        ("⚙️ Calculator", "calc: 15*8"),
        ("📟 Char Counter", "len: data"),
        ("📝 Word Count", "words: text"),
        ("🔄 Invert", "rev: string"),
        ("⬆️ Uppercase", "up: text"),
        ("⬇️ Lowercase", "low: TEXT"),
        ("🤖 Query AI", "chat: prompt")
    ]
    
    for tool_name, example in tools_list:
        st.markdown(f"""
        <div class="tool-card">
            <strong>{tool_name}</strong><br>
            <code>{example}</code>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    if "messages" in st.session_state:
        st.metric("📦 Processed Events", len(st.session_state.messages))

# ============================================
# LÓGICA Y CHAT
# ============================================

if not GROQ_API_KEY:
    st.error("### ❌ Missing API Key. Check your .env file.")
    st.stop()

llm = init_llm()
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    avatar = "👨‍💻" if message["role"] == "user" else "⚡"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

def procesar_mensaje(mensaje: str) -> str:
    mensaje = mensaje.strip()
    if mensaje.startswith('calc:'): return calculadora(mensaje[5:].strip())
    if mensaje.startswith('len:'): return contar_caracteres(mensaje[4:].strip())
    if mensaje.startswith('words:'): return contar_palabras(mensaje[6:].strip())
    if mensaje.startswith('rev:'): return invertir(mensaje[4:].strip())
    if mensaje.startswith('up:'): return mayusculas(mensaje[3:].strip())
    if mensaje.startswith('low:'): return minusculas(mensaje[4:].strip())
    
    try:
        with st.spinner("⚡ KelvIA está procesando..."):
            response = llm.invoke(mensaje)
            return f"⚡ {response.content}"
    except Exception as e:
        return f"⚠️ System Error: {e}"

prompt = st.chat_input("Enter command or query...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👨‍💻"):
        st.markdown(prompt)
    with st.chat_message("assistant", avatar="⚡"):
        respuesta = procesar_mensaje(prompt)
        st.markdown(respuesta)
    st.session_state.messages.append({"role": "assistant", "content": respuesta})
    st.rerun()