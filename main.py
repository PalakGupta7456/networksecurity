from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
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
        logger.info("Data Initiation completed")
        print(dataingestionartifact)

        data_validation_config=DataValidationConfig(Trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logger.info("Initiate the data validation ")
        data_validation_artifact=data_validation.initiate_data_validation()
        logger.info("Data Validation Completed")
        print(data_validation_artifact)


        



    except Exception as e:
        raise CustomException(e,sys)