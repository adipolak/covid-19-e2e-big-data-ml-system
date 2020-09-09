# covid-19-e2e-big-data-ml-system
Covid-19 End to End Big Data and ML- from ingesting stream to deploying ML model in production 

This is an example of how you can leverage kafka, Apache Spark and Spark mllib to build your system and produce machine learning model with big data.

** this doesn't include CLI/Bash/[Powershell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7?WT.mc_id=article-infoq-adpolak)
for ops.

## Prerequisites:
1. [Azure account](https://azure.microsoft.com/en-us/free?WT.mc_id=article-infoq-adpolak)
2. [Eventhubs](https://docs.microsoft.com/en-us/azure/event-hubs/event-hubs-create?WT.mc_id=article-infoq-adpolak)
3. [Azure Databricks](https://docs.microsoft.com/en-us/azure/azure-databricks/quickstart-create-databricks-workspace-portal?WT.mc_id=article-infoq-adpolak) with MLFlow
4. [Azure Machine Learning](https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-1st-experiment-sdk-setup?WT.mc_id=article-infoq-adpolak)
5. [Azure KeyVault](https://docs.microsoft.com/en-us/azure/key-vault/secrets/quick-create-portal?WT.mc_id=article-infoq-adpolak)
6. [Kubernetes Environment](https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough?WT.mc_id=article-infoq-adpolak) / [Azure Container Instance](https://docs.microsoft.com/en-us/azure/container-instances/container-instances-quickstart-portal?WT.mc_id=article-infoq-adpolak)

--------

## Architecture layers
* Ingest the data with [Kafka on Azure](https://azure.microsoft.com/en-us/blog/processing-trillions-of-events-per-day-with-apache-kafka-on-azure?WT.mc_id=article-infoq-adpolak)
* Collect, analyze and process the data with [Databricks](https://docs.microsoft.com/en-us/azure/databricks/scenarios/quickstart-create-databricks-workspace-portal?WT.mc_id=article-geektime-adpolak&tabs=azure-portal)
* Enrich the data - in out case we add sentiment analysis based on tweet text
* Train, evaluate and [register](https://docs.microsoft.com/en-us/azure/databricks/applications/mlflow/?WT.mc_id=e2eml-infoQ-adpolak) machine learning models
* [Deploy to production](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-and-where?WT.mc_id=e2eml-infoQ-adpolak&tabs=azcli)


![](https://raw.githubusercontent.com/adipola/covid-19-e2e-big-data-ml-system/master/diagrams/ml-cycle.png)

---------
### Q&A
If you have questions/concerns or would like to chat, contact us:

* [Adi Polak](https://twitter.com/AdiPolak)

