import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

project_name = "wine_quality_prediction"

list_of_file = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/init.py",
    f"src/{project_name}/utils/init_.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/init_.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/init_.py",
    f"src/{project_name}/entity/init_.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/init_.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} already exists")