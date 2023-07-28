import os
from dataclasses import dataclass
from datetime import datetime
from cellSegmentation.constant.training_pipeline import *

@dataclass
class TrainingPipelineConfig:
    artifacts_dir: str = ARTIFACTS_DIR # artifacts


training_pipeline_config:TrainingPipelineConfig = TrainingPipelineConfig() 


@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME
    ) # artifacts/data_ingestion

    feature_store_file_path: str = os.path.join(
        data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR
    ) # artifacts/feature_store

    data_download_url: str = DATA_DOWNLOAD_URL

@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_VALIDATION_DIR_NAME
    ) # artifacts/data_validation

    valid_status_file_dir: str = os.path.join(data_validation_dir, DATA_VALIDATION_STATUS_FILE) #artifacts/data_validation/status.txt

    required_file_list = DATA_VALIDATION_ALL_REQUIRED_FILES # ["train", "valid", "test", "data.yaml"]


@dataclass
class ModelTrainerConfig:
    model_trainer_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, MODEL_TRAINER_DIR_NAME
    ) # artifacts/model_trainer

    weight_name = MODEL_TRAINER_PRETRAINED_WEIGHT_NAME # yolov8s-seg.pt

    no_epochs = MODEL_TRAINER_NO_EPOCHS 

    batch_size = MODEL_TRAINER_BATCH_SIZE

