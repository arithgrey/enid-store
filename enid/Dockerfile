# Utiliza Python 3.8 Alpine como imagen base
ARG PYTHON_VERSION=python:3.8-alpine
FROM ${PYTHON_VERSION} 

RUN apk add --no-cache build-base

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo del contenedor
COPY requirements.txt /app/

# Actualiza pip e instala las dependencias
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto de los archivos al directorio de trabajo del contenedor
COPY . .

EXPOSE 8080
# Ejecuta el comando por defecto para iniciar el servidor en prod
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "enid.wsgi:application"]
CMD ["sh", "-c", "watchmedo auto-restart --directory=./ --pattern=*.py --recursive -- gunicorn -b 0.0.0.0:8080 enid.wsgi:application"]