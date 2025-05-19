{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_L2_clinical_trial_gap_analysis_post_diagnosis_cost_summary_0",
    "database": "prophecy_sql_workshop_clone",
    "schema": "healthcare_sample"
  })
}}

WITH l0_bronze_clinical_study_details AS (

  SELECT * 
  
  FROM {{ source('prophecy_sql_workshop.healthcare_sample', 'l0_bronze_clinical_study_details') }}

),

cleanse_diagnosis_data AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_L2_clinical_trial_gap_analysis_source', 'prophecy__temp_L2_clinical_trial_gap_analysis_pre_diagnosis_clinical_study_join_0') }}

),

diagnosis_clinical_study_join AS (

  SELECT 
    in0.snomed_diagnosis AS snomed_diagnosis,
    in0.total_cost AS total_cost,
    in1.nctId AS nctId,
    in1.briefTitle AS briefTitle
  
  FROM cleanse_diagnosis_data AS in0
  LEFT JOIN l0_bronze_clinical_study_details AS in1
     ON in1.snomedCode = in0.snomed_diagnosis

),

diagnosis_cost_summary AS (

  SELECT 
    snomed_diagnosis AS snomed_diagnosis,
    total_cost AS total_cost,
    collect_set(nctId) AS nctIds
  
  FROM diagnosis_clinical_study_join AS in0
  
  GROUP BY 
    snomed_diagnosis, total_cost

)

SELECT *

FROM diagnosis_cost_summary
