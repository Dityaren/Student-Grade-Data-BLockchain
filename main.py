import fastapi as _fastapi
import Block as _blockchain
from fastapi import Request, Body
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

blockchain = _blockchain.Blockchain()
app = _fastapi.FastAPI()

list_of_blockchain = list()
template = Jinja2Templates(directory="htmldirectory")


@app.get("/buat_block/")
def Buat_block(nama: str, kelas: str, bahasa_indonesia: int, bahasa_inggris: int, ipa: int, ips: int):
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400, detail="blockchain tidak valid!!"
        )
    data = nama + ";" + kelas + ";" + str(bahasa_indonesia) + ";" + \
        str(bahasa_inggris) + ";" + str(ipa) + ";" + str(ips)
    block = blockchain.mine_block(data=data)

    return block


@app.get("/blockchain/")
def Ambil_semua_blockchain():
    if not blockchain.is_chain_valid():
        return _fastapi.FastAPI(
            status_code=400, detail="blockchain tidak valid!!"
        )
    chain = blockchain.chain
    return chain


@app.get("/cek")
def web_home(request: Request):
    data = blockchain.is_chain_valid()
    return data


@app.get("/")
def web_home(request: Request):
    menu = "Data Nilai Siswa"
    data = Ambil_semua_blockchain()
    return template.TemplateResponse("index.html", {"request": request, "menu": menu, "data": data})


@app.get("/{menu}")
def web_home(request: Request, menu: str):
    if (menu == "tambah"):
        req = "tambah.html"
        menu = "Tambah Data Nilai Siswa"
    elif (menu == "lihat"):
        menu = "Lihat Data Nilai Siswa"
    elif (menu == "cek"):
        menu = "Cek Validasi Data Nilai Siswa"
    else:
        return

    data = Ambil_semua_blockchain()
    return template.TemplateResponse(req, {"request": request, "menu": menu})
