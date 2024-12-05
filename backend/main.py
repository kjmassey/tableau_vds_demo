from fastapi import FastAPI, Request
from generate_tableau_jwt import generate_login_jwt
from generate_basic_query import do_basic_query
from fastapi.middleware.cors import CORSMiddleware
from library_queries import do_library_query
from order_query import do_orders_query
from customers_query import do_customers_query
from region_query import do_region_query
from support_desk_queries import do_support_desk_query

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/jwt')
def get_token():
    return generate_login_jwt()


@app.get('/basicQuery')
def run_basic_query():
    return do_basic_query()


@app.get('/libraryQuery')
def get_library_info():
    return do_library_query()


@app.get('/orders')
def get_orders():
    return do_orders_query()


@app.post('/customers')
async def get_customers(request: Request):
    return do_customers_query(await request.json())


@app.post('/regions')
async def get_regions(request: Request):
    return do_region_query(await request.json())


@app.get('/supportDesk')
async def get_service_desk_data(request: Request):
    return do_support_desk_query()
