Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    l0_raw_clinical_trials = Task(
        task_id = "l0_raw_clinical_trials", 
        component = "Dataset", 
        table = {
          "name": "l0_raw_clinical_trials", 
          "sourceType": "Table", 
          "sourceName": "prophecy_sql_workshop.healthcare_sample", 
          "alias": "", 
          "additionalProperties": None
        }, 
        writeOptions = {"writeMode" : "overwrite"}
    )
    model_dasdsafasdf_clean_clinical_trial_data = Task(
        task_id = "model_dasdsafasdf_clean_clinical_trial_data", 
        component = "Model", 
        modelName = "model_dasdsafasdf_clean_clinical_trial_data"
    )
    l0_raw_clinical_trials.out >> model_dasdsafasdf_clean_clinical_trial_data.in_0
