from fastapi import FastAPI, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session
from src.database import get_db
from src.schemas import ResponseCost, CreateCost
from src import crud

app = FastAPI(title="Cost Management")

        

@app.get("/")
def root():
    return {"msg": "Welcome"}

@app.post("/cost", response_model=ResponseCost ,status_code=status.HTTP_201_CREATED, tags=["Cost"])
def creat_cost(cost: CreateCost, db: Session = Depends(get_db)):

    cost = crud.add_cost(cost, db)
    return cost


@app.get("/costs", response_model=list[ResponseCost], tags=["Cost"])
def get_costs(db: Session = Depends(get_db)):
    costs = crud.get_costs(db)
    return costs


@app.get("/cost/{id}", response_model=ResponseCost, tags=["Cost"])
def get_cost(
    id: int = Path(gt=0, description="Cost id"),
    db: Session = Depends(get_db)):

    cost = crud.get_cost(id, db)
    return cost


@app.put("/cost/{id}", response_model=ResponseCost, tags=["Cost"])
def edit_cost(
    now_cost: CreateCost,
    db: Session = Depends(get_db),
    id:int = Path(gt=0, description="Cost id")):

    cost = crud.edit_cost(id, now_cost, db)
    if not cost:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Cost with this {id}  not found.")
    
    return cost
    

@app.delete("/cost/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Cost"])
def delete_cost(
    id:int = Path(gt=0, description="Cost id"),
    db: Session = Depends(get_db)):

    cost = crud.delete_cost(id, db)

    if not cost:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Cost with this {id}  not found.")