# Imagen base de Python
FROM python:3.9-slim
#crea un directorio de trabajo
WORKDIR /app
# Copia el archivo de Python al contenedor
COPY eje1.py .
# Ejecuta el script de Python
CMD ["python", "eje1.py"]
#ENTRYPOINT ["python", "eje1.py"]
# Ejecuta el script de Python en segundo plano
#CMD python eje1.py && tail -f /dev/null
#CMD tail -f /dev/null