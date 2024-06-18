
  CREATE OR REPLACE FORCE EDITIONABLE VIEW "KRICHA2"."MEDAILLES_NOC" ("CODENOC", "NBGOLD", "NBSILVER", "NBBRONZE", "TOTAL") AS 
  SELECT codenoc,
COUNT(CASE WHEN medaille = 'Gold' THEN 1 END) AS nbGold,
    COUNT(CASE WHEN medaille = 'Silver' THEN 1 END) AS nbSilver,
    COUNT(CASE WHEN medaille = 'Bronze' THEN 1 END) AS nbBronze,
    COUNT(medaille) AS total
FROM 
(SELECT 
    codenoc, nomnoc, medaille
FROM noc n
LEFT JOIN participation_individuelle pi ON n.codenoc = pi.noc
UNION ALL
SELECT 
    codenoc, nomnoc, medaille
FROM noc n
LEFT JOIN equipe e ON e.noc = n.codenoc
INNER JOIN participation_equipe pe ON pe.idequipe = e.idequipe)
GROUP BY codenoc, nomnoc
ORDER BY nbGold DESC, nbSilver DESC, nbBronze DESC, total DESC, codenoc;
