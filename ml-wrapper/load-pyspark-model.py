import os
import json
import joblib
from pyspark.ml.classification import DecisionTreeClassifier, DecisionTreeClassificationModel
from pyspark.ml.feature import StringIndexer
from pyspark.ml import Pipeline
from pyspark.mllib.linalg import Vectors
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import Normalizer
 
 
def init():
   global model
  
  #if we work in Azure ml environment
   if os.getenv('AZUREML_MODEL_DIR') is not None:
       # load cloud path
       model_path = os.path.join(
           os.getenv('AZUREML_MODEL_DIR'),
           '/mnt/root/COVID19_TWEETS/ML-Models/V1'
       )
   else:
       # load from path
       model_path = '/mnt/root/COVID19_TWEETS/ML-Models/V1'
   )
 
   # deserialize the model file back into a pyspark model
   # read pickled model via pipeline api
   model = PipelineModel.load(model_path)
 
# when our server gets new request for classification/prediction/scoring, it calls the model run functionally with the raw_data
def run(raw_data):
   try:
       # Score using spark mllib decision tree pipeline
       result = model.transform(raw_data)
       # you can return any data type as long as it is JSON-serializable
       return result.tolist()
 
   except Exception as e:
       error = str(e)
       return error
