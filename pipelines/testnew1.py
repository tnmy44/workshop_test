Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

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
