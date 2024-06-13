WITH
-- Q1 sesiones inciadas por el USER , deja fuera pushes
subQ1 AS (SELECT distinct session_id, session_creation_time FROM `botmaker-gcba-data.Metrics.session_metrics`
where extract(year from session_creation_time)= 2024
and extract(month from session_creation_time)= 6
and starting_cause in ('Organic')
),
--Q2 Sesiones que disparan modelo de IA
subQ2 AS (SELECT distinct session_id
FROM `botmaker-gcba-data.Metrics.intent_search`
where extract(year from ts)= 2024
and extract(month from ts)= 6),
--Q3 Sesiones Organicas que disparan el modelo de IA
subQ3 AS(
SELECT subQ1.session_id as id, subQ1.session_creation_time as session_creation_time
FROM subQ1
inner join subQ2
ON subQ1.session_id=subQ2.session_id)
--Query extrae hora y dia (ajustando a hs en BA) y cuenta los disparos de modelo
select extract (day from (DATETIME(session_creation_time, "America/Argentina/Buenos_Aires"))) as dia,EXTRACT(HOUR FROM (DATETIME(session_creation_time, "America/Argentina/Buenos_Aires"))) as hora, count(id) from subq3 group by dia,hora
order by dia,hora asc;