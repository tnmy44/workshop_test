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
    cleanse_diagnosis_data = Task(
        task_id = "cleanse_diagnosis_data", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_L2_clinical_trial_gap_analysis_pre_diagnosis_clinical_study_join_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_L2_clinical_trial_gap_analysis_source", 
          "alias": ""
        }
    )
    cleanse_diagnosis_data = Task(
        task_id = "cleanse_diagnosis_data", 
        component = "DataCleansing", 
        trimWhiteSpace = False, 
        replaceNullForNumericFields = False, 
        cleanLetters = False, 
        replaceNullTextWith = "No Diagnosis", 
        removeRowNullAllCols = False, 
        replaceNullTextFields = True, 
        relation_name = ["total_cost_by_diagnosis"], 
        replaceNullDateWith = "1970-01-01", 
        columnNames = ["snomed_diagnosis"], 
        replaceNullTimeFields = False, 
        _oldMacroProperties = {
          "macroName": "DataCleansing", 
          "projectName": "DatabricksSqlBasics", 
          "parameters": [{"name" : "relation_name", "value" : "['total_cost_by_diagnosis']"},                           {
                            "name": "schema", 
                            "value": "[{"name": "snomed_diagnosis", "dataType": "String"}, {"name": "total_cost", "dataType": "Double"}]"
                          },                           {"name" : "modifyCase", "value" : "Keep original"},                           {"name" : "columnNames", "value" : "["snomed_diagnosis"]"},                           {"name" : "replaceNullTextFields", "value" : "true"},                           {"name" : "replaceNullTextWith", "value" : "No Diagnosis"},                           {"name" : "replaceNullForNumericFields", "value" : "false"},                           {"name" : "replaceNullNumericWith", "value" : "0"},                           {"name" : "trimWhiteSpace", "value" : "false"},                           {"name" : "removeTabsLineBreaksAndDuplicateWhitespace", "value" : "false"},                           {"name" : "allWhiteSpace", "value" : "false"},                           {"name" : "cleanLetters", "value" : "false"},                           {"name" : "cleanPunctuations", "value" : "false"},                           {"name" : "cleanNumbers", "value" : "false"},                           {"name" : "removeRowNullAllCols", "value" : "false"},                           {"name" : "replaceNullDateFields", "value" : "false"},                           {"name" : "replaceNullDateWith", "value" : "1970-01-01"},                           {"name" : "replaceNullTimeFields", "value" : "false"},                           {"name" : "replaceNullTimeWith", "value" : "1970-01-01 00:00:00.0"}]
        }, 
        replaceNullTimeWith = "1970-01-01 00:00:00.0", 
        schema = "[{"name": "snomed_diagnosis", "dataType": "String"}, {"name": "total_cost", "dataType": "Double"}]", 
        allWhiteSpace = False, 
        removeTabsLineBreaksAndDuplicateWhitespace = False, 
        modifyCase = "Keep original", 
        cleanPunctuations = False, 
        replaceNullDateFields = False, 
        cleanNumbers = False, 
        replaceNullNumericWith = 0
    )
    model_L2_clinical_trial_gap_analysis_total_cost_desc = Task(
        task_id = "model_L2_clinical_trial_gap_analysis_total_cost_desc", 
        component = "Model", 
        modelName = "model_L2_clinical_trial_gap_analysis_total_cost_desc"
    )
    model_L2_clinical_trial_gap_analysis_diagnosis_cost_summary_sorted = Task(
        task_id = "model_L2_clinical_trial_gap_analysis_diagnosis_cost_summary_sorted", 
        component = "Model", 
        modelName = "model_L2_clinical_trial_gap_analysis_diagnosis_cost_summary_sorted"
    )
    l0_bronze_clinical_study_details.out >> model_L2_clinical_trial_gap_analysis_diagnosis_cost_summary.in_0
    (
        model_L2_clinical_trial_gap_analysis_total_cost_by_diagnosis.out_0
        >> [cleanse_diagnosis_data.in0, model_L2_clinical_trial_gap_analysis_total_cost_desc.in_0]
    )
    cleanse_diagnosis_data.output_port_1_1 >> model_L2_clinical_trial_gap_analysis_diagnosis_cost_summary.in_1
    cleanse_diagnosis_data.out >> cleanse_diagnosis_data.input_port_1_1
    l0_raw_encounters.out >> model_L2_clinical_trial_gap_analysis_total_cost_by_diagnosis.in_0
    (
        model_L2_clinical_trial_gap_analysis_diagnosis_cost_summary.out_0
        >> [model_L2_clinical_trial_gap_analysis_empty_nctids_summary.in_0,
              model_L2_clinical_trial_gap_analysis_diagnosis_cost_summary_sorted.in_0]
    )
