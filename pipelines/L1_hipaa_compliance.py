Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "Asia/Kolkata")

with DAG(Schedule = Schedule):
    l0_raw_patients = Task(
        task_id = "l0_raw_patients", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {
          "name": "l0_raw_patients", 
          "sourceType": "Table", 
          "sourceName": "prophecy_sql_workshop.healthcare_sample", 
          "alias": ""
        }
    )
