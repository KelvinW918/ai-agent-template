import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_import():
    try:
        import streamlit_app
        assert hasattr(streamlit_app, 'calculadora')
        assert hasattr(streamlit_app, 'contar_caracteres')
        print("✅ Funciones encontradas")
    except ImportError as e:
        assert False, f"Error: {e}"
