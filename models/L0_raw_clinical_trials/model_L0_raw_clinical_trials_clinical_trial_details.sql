{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_L0_raw_clinical_trials_post_clinical_trial_details_0",
    "database": "tanmay",
    "schema": "default"
  })
}}

WITH l0_raw_clinical_trials AS (

  SELECT * 
  
  FROM {{ source('prophecy_sql_workshop.healthcare_sample', 'l0_raw_clinical_trials') }}

),

valid_clinical_trials AS (

  SELECT * 
  
  FROM l0_raw_clinical_trials AS in0
  
  WHERE _corrupt_record IS NULL

),

clinical_trial_details AS (

  SELECT 
    protocolSection.identificationModule.nctId AS nctId,
    protocolSection.identificationModule.briefTitle AS briefTitle,
    protocolSection.designModule.studyType AS studyType,
    protocolSection.statusModule.overallStatus AS overallStatus,
    conditions.col AS condition,
    interventions.col AS intervention,
    snomedCode AS snomedCode,
    conditionDescription AS conditionDescription
  
  FROM valid_clinical_trials AS in0, 
  LATERAL explode_outer(protocolSection.armsInterventionsModule.interventions) AS interventions, 
  LATERAL explode_outer(protocolSection.conditionsModule.conditions) AS conditions

)

SELECT *

FROM clinical_trial_details
