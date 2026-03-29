# OpsDesk OpenEnv

## Overview
Real-world customer support simulation environment.

## Features
- OpenEnv compliant
- 3 tasks (triage, resolution, optimization)
- Reward shaping
- Baseline agent

## Run

### Install
pip install -r requirements.txt

### Generate Data
python data/generator.py

### Run Agent
python baseline/run_agent.py

### Run API
uvicorn ui.backend.api:app --reload

## Tasks
- Triage → classify tickets
- Resolution → solve tickets
- Optimization → full workflow

## Baseline Scores
- Task1: ~0.7+
- Task2: ~0.5+
- Task3: ~0.4+

## Deployment
Supports Docker + HuggingFace Spaces