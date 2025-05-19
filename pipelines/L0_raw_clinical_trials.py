Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    model_L0_raw_clinical_trials_clean_clinical_trial_data = Task(
        task_id = "model_L0_raw_clinical_trials_clean_clinical_trial_data", 
        component = "Model", 
        modelName = "model_L0_raw_clinical_trials_clean_clinical_trial_data"
    )
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
    l0_raw_clinical_trials.out >> model_L0_raw_clinical_trials_clean_clinical_trial_data.in_0
