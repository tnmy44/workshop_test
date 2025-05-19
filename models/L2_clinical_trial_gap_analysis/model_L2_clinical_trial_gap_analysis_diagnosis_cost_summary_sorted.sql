{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_L2_clinical_trial_gap_analysis_post_diagnosis_cost_summary_sorted_0",
    "database": "prophecy_sql_workshop_clone",
    "schema": "healthcare_sample"
  })
}}

WITH diagnosis_cost_summary AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_L2_clinical_trial_gap_analysis_source', 'prophecy__temp_L2_clinical_trial_gap_analysis_post_diagnosis_cost_summary_0') }}

),

diagnosis_cost_summary_sorted AS (

  SELECT * 
  
  FROM diagnosis_cost_summary AS in0
  
  ORDER BY total_cost DESC

)

SELECT *

FROM diagnosis_cost_summary_sorted
