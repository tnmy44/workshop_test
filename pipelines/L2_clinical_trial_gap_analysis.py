Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    model_L2_clinical_trial_gap_analysis_empty_nctids_summary = Task(
        task_id = "model_L2_clinical_trial_gap_analysis_empty_nctids_summary", 
        component = "Model", 
        modelName = "model_L2_clinical_trial_gap_analysis_empty_nctids_summary"
    )
    model_L2_clinical_trial_gap_analysis_diagnosis_cost_summary = Task(
        task_id = "model_L2_clinical_trial_gap_analysis_diagnosis_cost_summary", 
        component = "Model", 
        modelName = "model_L2_clinical_trial_gap_analysis_diagnosis_cost_summary"
    )
    model_L2_clinical_trial_gap_analysis_total_cost_by_diagnosis = Task(
        task_id = "model_L2_clinical_trial_gap_analysis_total_cost_by_diagnosis", 
        component = "Model", 
        modelName = "model_L2_clinical_trial_gap_analysis_total_cost_by_diagnosis"
    )
    l0_raw_encounters = Task(
        task_id = "l0_raw_encounters", 
        component = "Dataset", 
        table = {
          "name": "l0_raw_encounters", 
          "sourceType": "Table", 
          "sourceName": "prophecy_sql_workshop.healthcare_sample", 
          "alias": "", 
          "additionalProperties": None
        }, 
        writeOptions = {"writeMode" : "overwrite"}
    )
    l0_bronze_clinical_study_details = Task(
        task_id = "l0_bronze_clinical_study_details", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {
          "name": "l0_bronze_clinical_study_details", 
          "sourceType": "Table", 
          "sourceName": "prophecy_sql_workshop.healthcare_sample", 
          "alias": "", 
          "additionalProperties": None
        }
    )
    model_L2_clinical_trial_gap_analysis_total_cost_desc = Task(
        task_id = "model_L2_clinical_trial_gap_analysis_total_cost_desc", 
        component = "Model", 
        modelName = "model_L2_clinical_trial_gap_analysis_total_cost_desc"
    )
    model_L2_clinical_trial_gap_analysis_cleanse_diagnosis_data = Task(
        task_id = "model_L2_clinical_trial_gap_analysis_cleanse_diagnosis_data", 
        component = "Model", 
        modelName = "model_L2_clinical_trial_gap_analysis_cleanse_diagnosis_data"
    )
    model_L2_clinical_trial_gap_analysis_diagnosis_cost_summary_sorted = Task(
        task_id = "model_L2_clinical_trial_gap_analysis_diagnosis_cost_summary_sorted", 
        component = "Model", 
        modelName = "model_L2_clinical_trial_gap_analysis_diagnosis_cost_summary_sorted"
    )
    l0_bronze_clinical_study_details.out >> model_L2_clinical_trial_gap_analysis_diagnosis_cost_summary.in_0
    (
        model_L2_clinical_trial_gap_analysis_total_cost_by_diagnosis.out_0
        >> [model_L2_clinical_trial_gap_analysis_total_cost_desc.in_0,
              model_L2_clinical_trial_gap_analysis_cleanse_diagnosis_data.in_0]
    )
    l0_raw_encounters.out >> model_L2_clinical_trial_gap_analysis_total_cost_by_diagnosis.in_0
    (
        model_L2_clinical_trial_gap_analysis_diagnosis_cost_summary.out_0
        >> [model_L2_clinical_trial_gap_analysis_empty_nctids_summary.in_0,
              model_L2_clinical_trial_gap_analysis_diagnosis_cost_summary_sorted.in_0]
    )
    (
        model_L2_clinical_trial_gap_analysis_cleanse_diagnosis_data.out_0
        >> model_L2_clinical_trial_gap_analysis_diagnosis_cost_summary.in_0
    )
