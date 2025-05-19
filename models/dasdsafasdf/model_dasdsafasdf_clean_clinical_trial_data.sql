{{
  config({    
    "materialized": "table",
    "alias": "l0_bronze_clinical_study_details",
    "database": "prophecy_sql_workshop",
    "schema": "healthcare_sample"
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

),

clean_clinical_trial_data AS (

  {{
    DatabricksSqlBasics.DataCleansing(
      'clinical_trial_details', 
      [
        { "name": "nctId", "dataType": "String" }, 
        { "name": "briefTitle", "dataType": "String" }, 
        { "name": "studyType", "dataType": "String" }, 
        { "name": "overallStatus", "dataType": "String" }, 
        { "name": "condition", "dataType": "String" }, 
        { "name": "intervention", "dataType": "Struct" }, 
        { "name": "snomedCode", "dataType": "String" }, 
        { "name": "conditionDescription", "dataType": "String" }
      ], 
      'Keep original', 
      ['conditionDescription'], 
      false, 
      'NA', 
      false, 
      0, 
      true, 
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

FROM clean_clinical_trial_data
