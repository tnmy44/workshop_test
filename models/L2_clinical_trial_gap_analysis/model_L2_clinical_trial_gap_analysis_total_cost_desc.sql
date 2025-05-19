{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_L2_clinical_trial_gap_analysis_post_total_cost_desc_0",
    "database": "prophecy_sql_workshop_clone",
    "schema": "healthcare_sample"
  })
}}

WITH total_cost_by_diagnosis AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_L2_clinical_trial_gap_analysis_source', 'prophecy__temp_L2_clinical_trial_gap_analysis_post_total_cost_by_diagnosis_0') }}

),

total_cost_desc AS (

  SELECT * 
  
  FROM total_cost_by_diagnosis AS in0
  
  ORDER BY total_cost DESC

)

SELECT *

FROM total_cost_desc
