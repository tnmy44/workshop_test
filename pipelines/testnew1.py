Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "Asia/Kolkata")

with DAG(Schedule = Schedule):
    l0_raw_medications = Task(
        task_id = "l0_raw_medications", 
        component = "Dataset", 
        table = {
          "name": "l0_raw_medications", 
          "sourceType": "Source", 
          "sourceName": "prophecy_sql_workshop_clone.healthcare_sample", 
          "alias": ""
        }
    )
    OrchestrationTarget_1 = Task(
        task_id = "OrchestrationTarget_1", 
        component = "OrchestrationTarget", 
        kind = "OnedriveTarget", 
        connector = Connection(kind = "onedrive"), 
        properties = {}, 
        format = {
          "properties": {
            "allowLazyQuotes": False, 
            "allowEmptyColumnNames": True, 
            "separator": ",", 
            "nullValue": "", 
            "header": True
          }, 
          "kind": "csv", 
          "category": "file"
        }, 
        isNew = True
    )
