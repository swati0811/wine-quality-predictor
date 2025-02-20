from wine_quality_prediction.config.configuration import ConfigurationManager
from wine_quality_prediction.components.model_trainer import ModelTrainer
from wine_quality_prediction import logger 
from pathlib import Path

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()