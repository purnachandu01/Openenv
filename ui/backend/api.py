from fastapi import FastAPI
from env.environment import OpsDeskEnv
from env.models import Action

app = FastAPI()

env = OpsDeskEnv()
obs = env.reset()

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/state")
def get_state():
    return obs.model_dump()

@app.post("/step")
def step(action: Action):
    global obs
    obs, reward, done, _ = env.step(action)
    return {
        "observation": obs.model_dump(),
        "reward": reward.model_dump(),
        "done": done
    }