from fastapi import FastAPI
from settings import HOST, PORT, RELOAD

# import das classes com as rotas/endpoints
from mod_funcionario import FuncionarioDAO

app = FastAPI()

# mapeamento das rotas/endpoints
app.include_router(FuncionarioDAO.router)

import db
db.criaTabelas()



if __name__ == "__main__":
    import uvicorn
    uvicorn.run('apiPastelaria:app', host=HOST, port=int(PORT), reload=RELOAD)