from wine_quality_prediction.config.configuration import ConfigurationManager
from wine_quality_prediction.components.model_evaluation import ModelEvaluation
from wine_quality_prediction import logger 
from pathlib import Path

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config= model_evaluation_config)
        model_evaluation_config.save_results()