SELECT * FROM allwellprac.`sql ibm csv`; 
select distinct Launch_site 
FROM allwellprac.`sql ibm csv`; 
SELECT *
FROM allwellprac.`sql ibm csv`
WHERE Launch_Site LIKE 'CCA%'
LIMIT 5;
SELECT SUM(PAYLOAD_MASS__KG_) AS Total_Payload_Mass
FROM allwellprac.`sql ibm csv`
WHERE PAYLOAD_MASS__KG_ = Booster_Version;

SELECT avg(PAYLOAD_MASS__KG_) AS avg_Payload_Mass
FROM allwellprac.`sql ibm csv`;

SELECT MIN(Date)
FROM allwellprac.`sql ibm csv`
WHERE Landing_Outcome = 'Controlled (ocean)';

SELECT Booster_Version
FROM allwellprac.`sql ibm csv`
WHERE Landing_Outcome = 'Success (drone ship)'
AND PAYLOAD_MASS__KG_ > 4000
AND PAYLOAD_MASS__KG_ < 6000;

SELECT Landing_Outcome, COUNT(*) AS Total_Count
FROM allwellprac.`sql ibm csv`
WHERE Landing_Outcome IN ('Success', 'Failure')
GROUP BY Landing_Outcome;

SELECT Booster_Version
FROM allwellprac.`sql ibm csv`
WHERE PAYLOAD_MASS__KG_ = (
    SELECT MAX(PAYLOAD_MASS__KG_)
    FROM allwellprac.`sql ibm csv`
);

SELECT DATE_FORMAT(Date, '%M') AS Month_Name, Landing_Outcome, Booster_Version, Launch_Site
FROM allwellprac.`sql ibm csv`
WHERE YEAR(Date) = '2015'
AND Landing_Outcome = 'Failure (drone ship)';

SELECT Landing_Outcome, COUNT(*) AS Outcome_Count
FROM allwellprac.`sql ibm csv`
WHERE Date BETWEEN '2010-06-04' AND '2017-03-20'
AND Landing_Outcome IN ('Failure (drone ship)', 'Success (ground pad)')
GROUP BY Landing_Outcome
ORDER BY Outcome_Count DESC;

select  count("Mission_Outcome") as MISSION_OUTCOME_COUNT,Launch_Site  from SPACEXTBL group by "Launch_Site";









