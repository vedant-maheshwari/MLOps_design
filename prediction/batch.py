from src.constants import *
from src. logger import logging
from src.exception import CustomException
import os, sys
from src.config.configuration import *
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainer
from src.components.data_ingestion import *
from dataclasses import dataclass

PREDICTION_FOLDER = 'batch_pred'
PREDICTION_CSV = 'prediction.csv'
PREDICTION_FILE = 'output_pred.csv'