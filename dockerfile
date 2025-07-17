# Imagine de bază mică și compatibilă cu Python
FROM python:3.11-slim

# Setează directorul de lucru în container
WORKDIR /app

# Copiază toate fișierele din proiect (excludem prin .dockerignore)
COPY . .

# Instalează dependențele
RUN pip install --no-cache-dir -r requirements.txt

# Expune portul folosit de Hypercorn/Flask
EXPOSE 5000

# Rulăm aplicația folosind Hypercorn cu bind pe toate interfețele
CMD ["hypercorn", "app.main:app", "--bind", "0.0.0.0:5000"]
