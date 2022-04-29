from fastapi import FastAPI
from .endpoints import heroes
from mangum import Mangum

app = FastAPI()
app.include_router(heroes.router, prefix="/heroes",tags=["Heroes"])

@app.get("/")
def root():
    """
    Método del directorio home en donde se muestra un mensaje de bienvenida a la app
    """
    mensaje="Bienvenido a al aplicación de superhéroes"
    return(mensaje)

# Función que lee AWS Lambdas. Internamente tiene variables events, context
handler = Mangum(app)