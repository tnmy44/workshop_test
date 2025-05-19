{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_L2_clinical_trial_gap_analysis_pre_diagnosis_clinical_study_join_0",
    "database": "prophecy_sql_workshop_clone",
    "schema": "healthcare_sample"
  })
}}

WITH total_cost_by_diagnosis AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_L2_clinical_trial_gap_analysis_source', 'prophecy__temp_L2_clinical_trial_gap_analysis_post_total_cost_by_diagnosis_0') }}

),

cleanse_diagnosis_data AS (

  {{
    DatabricksSqlBasics.DataCleansing(
      'total_cost_by_diagnosis', 
      [
        { "name": "snomed_diagnosis", "dataType": "String" }, 
        { "name": "total_cost", "dataType": "Double" }
      ], 
      'Keep original', 
      ['snomed_diagnosis'], 
      true, 
      'No Diagnosis', 
      false, 
      0, 
      false, 
      false, 
      false, 
      false, 
      false, 
      false, 
      false, 
      false, 
      '1970-01-01', 
      false, 
      '1970-01-01 00:00:00.0'
    )
  }}

)

SELECT *

FROM cleanse_diagnosis_data
