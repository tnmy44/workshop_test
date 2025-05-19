{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_L2_clinical_trial_gap_analysis_post_total_cost_by_diagnosis_0",
    "database": "prophecy_sql_workshop_clone",
    "schema": "healthcare_sample"
  })
}}

WITH l0_raw_encounters AS (

  SELECT * 
  
  FROM {{ source('prophecy_sql_workshop.healthcare_sample', 'l0_raw_encounters') }}

),

valid_encounters AS (

  SELECT * 
  
  FROM l0_raw_encounters AS in0
  
  WHERE baseEncounterCost > 0

),

total_cost_by_diagnosis AS (

  SELECT 
    reasonCode AS snomed_diagnosis,
    SUM(baseEncounterCost) AS total_cost
  
  FROM valid_encounters AS in0
  
  GROUP BY reasonCode

)

SELECT *

FROM total_cost_by_diagnosis
