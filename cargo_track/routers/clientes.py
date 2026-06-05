from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models import Cliente
from schemas import ClienteCreate, ClienteRead

router = APIRouter(prefix="/clientes", tags=["Clientes"])



@router.get("/", response_model=list[ClienteRead])
def listar_clientes(session: Session = Depends(get_session)):
    return session.exec(select(Cliente)).all()


@router.get("/{cliente_id}", response_model=ClienteRead)
def obtener_cliente(cliente_id: int, session: Session = Depends(get_session)):
    cliente = session.get(Cliente, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente


@router.post("/", response_model=ClienteRead, status_code=201)
def crear_cliente(cliente: ClienteCreate, session: Session = Depends(get_session)):
    db_cliente = Cliente.model_validate(cliente)
    session.add(db_cliente)
    session.commit()
    session.refresh(db_cliente)
    return db_cliente
    