from fastapi import FastAPI, Depends, HTTPException, status, Path
from src.model import ResponsCost, CreatCost, EditCost
app = FastAPI(title="Cost Management")


db = {}
count_id = 1

def get_cost_or_error(id: int) -> ResponsCost:
    if id in db.keys():
        return db[id]

    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cost with ID {id} not found"
        )
    
    

@app.get("/")
def root():
    return {"msg": "Welcome"}

@app.post("/cost", status_code=status.HTTP_201_CREATED, tags=["Cost"])
def creat_cost(cost: CreatCost):
    global count_id

    now_cost = ResponsCost(id = count_id, **cost.model_dump())
    db[count_id] = now_cost
    count_id += 1
    return now_cost

@app.get("/costs", response_model=list[ResponsCost], tags=["Cost"])
def get_costs():
    return list(db.values())


@app.get("/cost/{id}", response_model=ResponsCost, tags=["Cost"])
def get_cost(
    id:int = Path(gt=0, description="Cost id"),
    cost: ResponsCost = Depends(get_cost_or_error)):

    return cost

@app.put("/cost/{id}", response_model=ResponsCost, tags=["Cost"])
def edit_cost(
    id:int = Path(gt=0, description="Cost id"),
    now_cost: EditCost = ...,
    old_cost: ResponsCost = Depends(get_cost_or_error)):

    cost = ResponsCost(id=old_cost.id, **now_cost.model_dump())
    db[id] = cost
    return cost

@app.delete("/cost/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Cost"])
def delete_cost(
    id:int = Path(gt=0, description="Cost id"),
    cost=Depends(get_cost_or_error)):

    db.pop(id)