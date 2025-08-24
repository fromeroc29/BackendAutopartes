from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from admin import routes as admin_routes
#from admin import routes as admin_routes
#from app.admin import routes as admin_routes
from app.admin.routes import admin_router, negocio_router


#from ventas import routes as ventas_routes
#from compras import routes as compras_routes

app = FastAPI(title="Inventario de Autopartes")

# Configuración CORS
origins = [
    "http://localhost:5173",  # frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # o ["*"] para permitir todos (solo en desarrollo)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(admin_router)
app.include_router(negocio_router)