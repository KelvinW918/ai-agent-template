"""
Tests básicos para el AI Agent Template
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_import_streamlit_app():
    try:
        import streamlit_app
        assert streamlit_app is not None
    except ImportError as e:
        assert False, f"Error: {e}"

def test_calculadora_function():
    from streamlit_app import calculadora
    result = calculadora("2+2")
    assert "4" in result or "Resultado" in result

def test_contar_caracteres():
    from streamlit_app import contar_caracteres
    result = contar_caracteres("Hola")
    assert "4" in result

def test_contar_palabras():
    from streamlit_app import contar_palabras
    result = contar_palabras("Hola mundo")
    assert "2" in result

def test_invertir():
    from streamlit_app import invertir
    result = invertir("Hola")
    assert "aloH" in result

def test_mayusculas():
    from streamlit_app import mayusculas
    result = mayusculas("hola")
    assert "HOLA" in result

def test_minusculas():
    from streamlit_app import minusculas
    result = minusculas("HOLA")
    assert "hola" in result

def test_app_has_required_functions():
    import streamlit_app
    required = ['calculadora', 'contar_caracteres', 'contar_palabras', 'invertir', 'mayusculas', 'minusculas', 'procesar_mensaje']
    for func in required:
        assert hasattr(streamlit_app, func), f"Falta {func}"
