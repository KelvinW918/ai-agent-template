"""
Entry point for Vercel deployment
Ejecuta: streamlit run vercel_app.py --server.port=$PORT --server.address=0.0.0.0
"""

import os
import subprocess
import sys

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8501))
    subprocess.run([
        "streamlit", "run", "streamlit_app.py",
        "--server.port", str(port),
        "--server.address", "0.0.0.0",
        "--server.enableCORS", "false",
        "--server.enableXsrfProtection", "false"
    ])