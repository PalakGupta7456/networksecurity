from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import get_logger
logger=get_logger()
import sys

if __name__=='__main__':
    try:
        Trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(Trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logger.info(f"Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        


    except Exception as e:
        raise CustomException(e,sys)