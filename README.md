# Siete_Y_Medio

## Pasos para configurar la aplicación

1. **Descarga la Release y los dos archivos adjuntos:**
   - Descarga los archivos que hay en la Release.
   - Descarga los archivos `VM-Server-Siete-y-Medio_key.pem` y `db_access.env` adjuntos en la entrega del proyecto.

3. **Configura las variables de entorno**
   - Abre `db_access.env`.
   - Edita la variable `SSH_PRIVATE_KEY` cambiándola a la dirección local de la clave privada en tu máquina:
     ```
     SSH_PRIVATE_KEY="/dirección/local/VM-Server-Siete-y-Medio_key.pem"
     ```

4. **Instala los requisitos**
   - Asegúrate que Python y las dependencias están instaladas (`pip install -r requirements.txt`).

5. **Ejecuta el script principal:**
     ```
     python main.py
     ```