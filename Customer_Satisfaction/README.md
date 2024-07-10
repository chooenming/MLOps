# 1.2_Project.py
## Activate venv and zenml server
<br>Before running the code, create virtual environment
```bash
pip install "zenml["server"]"
zenml init
zenml up #activate zenml server (can view pipelines etc)
```

## Pipeline Setup
src = strategy
steps = all steps for ML
pipelines = ML pipeline

<br>After setting up all the pipelines, then run bash: `python run_pipeline.py`

## Strategy Setup
start the strategy setup, after that, develop the function in respective steps
