from fastapi import FastAPI
from .endpoints import heroes
from mangum import Mangum
#Si se pone la Línea "from .core import config" se pueden incluir el str
#config.settings.secret_key guardado en el .env como y el prefix en
# app.include_router(api_router, prefix=config.settings.prefix) guardado en
# el config file
app = FastAPI()
app.include_router(heroes.router, prefix="/heroes",tags=["Heroes"])

@app.get("/")
def root():
    """
    Método del directorio home en donde se muestra un mensaje de bienvenida a la app
    """
    mensaje="Bienvenido a la aplicación de superhéroes"
    return(mensaje)

# Función que lee AWS Lambdas. Internamente tiene variables events, context
handler = Mangum(app)