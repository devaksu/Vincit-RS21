from fastapi import FastAPI

app = FastAPI()


@app.get("/downtrend")
def downtrend():
    pass

@app.get("/max-vol")
def max_vol():
    pass

@app.get("/best-days")
def best_days():
    pass


