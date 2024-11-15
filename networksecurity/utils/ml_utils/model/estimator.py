import os
import sys

from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import get_logger
logger=get_logger()

from networksecurity.constant.training_pipeline import SAVED_MODEL_DIR, MODEL_FILE_NAME

class NetworkModel:
    def __init__(self,preprocessor,model):
        try:
            self.preprocessor=preprocessor
            self.model=model
        except Exception as e:
            raise CustomException(e,sys)
        
    def predict(self, x):
        try:
            x_transform=self.preprocessor.transform(x)
            y_hat=self.model.predict(x_transform)
        except Exception as e:
            raise CustomException(e,sys)

