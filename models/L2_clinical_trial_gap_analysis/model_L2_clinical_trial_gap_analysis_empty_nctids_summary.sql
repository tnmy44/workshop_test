{{
  config({    
    "materialized": "table",
    "alias": "clinical_study_gap_analysis",
    "database": "prophecy_sql_workshop",
    "schema": "healthcare_sample"
  })
}}

WITH diagnosis_cost_summary AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_L2_clinical_trial_gap_analysis_source', 'prophecy__temp_L2_clinical_trial_gap_analysis_post_diagnosis_cost_summary_0') }}

),

empty_nctids_summary AS (

  SELECT * 
  
  FROM diagnosis_cost_summary AS in0
  
  WHERE size(nctIds) = 0

)

SELECT *

FROM empty_nctids_summary
