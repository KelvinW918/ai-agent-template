# ⚡ KelvIA · Cognitive Agentic Engine
[![Tests](https://github.com/KelvinW918/ai-agent-template/actions/workflows/test.yml/badge.svg)](https://github.com/KelvinW918/ai-agent-template/actions/workflows/test.yml)

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.36-FF4B4B?style=for-the-badge&logo=streamlit)
![Groq](https://img.shields.io/badge/Groq-Llama_3.3-FF6600?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Live-00ff88?style=for-the-badge)

**Un agente cognitivo modular con interfaz profesional**  
*Toolkit integrado · IA en tiempo real · 100% gratuito*

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-Streamlit_Cloud-FF4B4B?style=for-the-badge)](https://ai-agent-template-kelvinw918.streamlit.app)

</div>

---

## 🎯 ¿Qué es KelvIA?

KelvIA es un **agente de IA cognitivo** que combina:
- 🧠 **Razonamiento con Llama 3.3** (vía Groq, gratuito)
- 🛠️ **Toolkit integrado** (calculadora, procesamiento de texto)
- 💬 **Interfaz conversacional** estilo ChatGPT
- ⚡ **Arquitectura modular** para extender herramientas

---

## 🚀 Demo en vivo

👉 [ai-agent-template-kelvinw918.streamlit.app](https://ai-agent-template-kelvinw918.streamlit.app)

| Comando | Función |
|---------|---------|
| `calc: 15*8+20` | Calculadora matemática |
| `len: Hola mundo` | Contar caracteres |
| `words: texto aquí` | Contar palabras |
| `rev: LangChain` | Invertir texto |
| `up: texto` | Convertir a MAYÚSCULAS |
| `low: TEXTO` | Convertir a minúsculas |
| `chat: pregunta` | Consulta a IA libre |

---

## 🛠️ Tecnologías

| Capa | Tecnología | Propósito |
|------|-----------|-----------|
| **Frontend UI** | Streamlit | Interfaz web profesional |
| **LLM** | Groq + Llama 3.3 70B | Razonamiento gratuito |
| **Herramientas** | Python puro | Cálculos y procesamiento |
| **Hosting** | Streamlit Cloud | Despliegue gratuito |

---

## 📁 Estructura
ai-agent-template/
├── streamlit_app.py # Interfaz principal
├── requirements.txt # Dependencias
├── runtime.txt # Python 3.11
├── packages.txt # Dependencias sistema
├── .env # API Keys (no se sube)
└── README.md # Documentación

text

---

## 🧠 Arquitectura
┌─────────────────────────────────────────────────────┐
│ KelvIA Engine │
├─────────────┬─────────────┬─────────────────────────┤
│ Toolkit │ LLM │ Interface │
│ · Calc │ · Groq │ · Streamlit Chat │
│ · Len │ · Llama │ · Sidebar Tools │
│ · Words │ 3.3 70B │ · Real-time Responses │
│ · Rev │ │ │
│ · Up/Low │ │ │
└─────────────┴─────────────┴─────────────────────────┘

text

---

## 🚀 Ejecutar localmente

```bash
# Clonar
git clone https://github.com/KelvinW918/ai-agent-template.git
cd ai-agent-template

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Crear archivo .env con tu API key
echo GROQ_API_KEY=tu_clave_aqui > .env

# Ejecutar
streamlit run streamlit_app.py
🔮 Hoja de ruta
Memoria conversacional persistente

Búsqueda web integrada (Tavily)

Análisis de documentos (PDF, CSV)

API REST para integraciones

Modo oscuro/claro toggle

👤 Autor
Kelvin W.
Systems Engineer · Product Architect

https://img.shields.io/badge/GitHub-KelvinW918-181717?style=flat-square&logo=github
https://img.shields.io/badge/LinkedIn-kelvin--williams-0A66C2?style=flat-square&logo=linkedin

📄 Licencia
MIT — Libre para uso, modificación y distribución.

<div align="center"> ⭐ Si KelvIA te es útil, dale una estrella ⭐ </div> ```
