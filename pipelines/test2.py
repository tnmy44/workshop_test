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
    model_test2_clinical_trial_details = Task(
        task_id = "model_test2_clinical_trial_details", 
        component = "Model", 
        modelName = "model_test2_clinical_trial_details"
    )
    clean_clinical_trial_data = Task(
        task_id = "clean_clinical_trial_data", 
        component = "DataCleansing", 
        trimWhiteSpace = True, 
        replaceNullForNumericFields = False, 
        cleanLetters = False, 
        replaceNullTextWith = "NA", 
        removeRowNullAllCols = False, 
        replaceNullTextFields = False, 
        relation_name = ["clinical_trial_details"], 
        replaceNullDateWith = "1970-01-01", 
        columnNames = ["conditionDescription"], 
        replaceNullTimeFields = False, 
        _oldMacroProperties = {
          "macroName": "DataCleansing", 
          "projectName": "DatabricksSqlBasics", 
          "parameters": [{"name" : "relation_name", "value" : "['clinical_trial_details']"},                           {
                            "name": "schema", 
                            "value": "[{"name": "nctId", "dataType": "String"}, {"name": "briefTitle", "dataType": "String"}, {"name": "studyType", "dataType": "String"}, {"name": "overallStatus", "dataType": "String"}, {"name": "condition", "dataType": "String"}, {"name": "intervention", "dataType": "Struct"}, {"name": "snomedCode", "dataType": "String"}, {"name": "conditionDescription", "dataType": "String"}]"
                          },                           {"name" : "modifyCase", "value" : "Keep original"},                           {"name" : "columnNames", "value" : "["conditionDescription"]"},                           {"name" : "replaceNullTextFields", "value" : "false"},                           {"name" : "replaceNullTextWith", "value" : "NA"},                           {"name" : "replaceNullForNumericFields", "value" : "false"},                           {"name" : "replaceNullNumericWith", "value" : "0"},                           {"name" : "trimWhiteSpace", "value" : "true"},                           {"name" : "removeTabsLineBreaksAndDuplicateWhitespace", "value" : "false"},                           {"name" : "allWhiteSpace", "value" : "false"},                           {"name" : "cleanLetters", "value" : "false"},                           {"name" : "cleanPunctuations", "value" : "false"},                           {"name" : "cleanNumbers", "value" : "false"},                           {"name" : "removeRowNullAllCols", "value" : "false"},                           {"name" : "replaceNullDateFields", "value" : "false"},                           {"name" : "replaceNullDateWith", "value" : "1970-01-01"},                           {"name" : "replaceNullTimeFields", "value" : "false"},                           {"name" : "replaceNullTimeWith", "value" : "1970-01-01 00:00:00.0"}]
        }, 
        replaceNullTimeWith = "1970-01-01 00:00:00.0", 
        schema = "[{"name": "nctId", "dataType": "String"}, {"name": "briefTitle", "dataType": "String"}, {"name": "studyType", "dataType": "String"}, {"name": "overallStatus", "dataType": "String"}, {"name": "condition", "dataType": "String"}, {"name": "intervention", "dataType": "Struct"}, {"name": "snomedCode", "dataType": "String"}, {"name": "conditionDescription", "dataType": "String"}]", 
        allWhiteSpace = False, 
        removeTabsLineBreaksAndDuplicateWhitespace = False, 
        modifyCase = "Keep original", 
        cleanPunctuations = False, 
        replaceNullDateFields = False, 
        cleanNumbers = False, 
        replaceNullNumericWith = 0
    )
    l0_bronze_clinical_study_details = Task(
        task_id = "l0_bronze_clinical_study_details", 
        component = "Dataset", 
        table = {
          "name": "l0_bronze_clinical_study_details", 
          "sourceType": "Table", 
          "sourceName": "prophecy_sql_workshop.healthcare_sample", 
          "alias": "", 
          "additionalProperties": None
        }, 
        writeOptions = {"writeMode" : "overwrite"}
    )
    clean_clinical_trial_data.out >> l0_bronze_clinical_study_details.in0
    l0_raw_clinical_trials.out >> model_test2_clinical_trial_details.in_0
    model_test2_clinical_trial_details.out_0 >> clean_clinical_trial_data.in0
