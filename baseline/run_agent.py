import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from env.environment import OpsDeskEnv
from env.models import Action

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

env = OpsDeskEnv()
obs = env.reset()

done = False

while not done:
    prompt = f"""
    You are a support agent.
    Tickets: {obs.model_dump_json()}
    Output JSON action.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    try:
        action = Action.model_validate_json(response.choices[0].message.content)
    except:
        break

    obs, reward, done, _ = env.step(action)
    print("Reward:", reward.score)