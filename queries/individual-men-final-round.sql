INSERT INTO match_individuel VALUES (1, 2, 3, (SELECT idAthlete FROM athlete WHERE nomAthlete = 'Fairweather' AND prenomAthlete = 'Simon') , (SELECT idAthlete FROM athlete WHERE nomAthlete = 'Wunderle' AND prenomAthlete = 'Vic') , '113 – 106');
INSERT INTO match_individuel VALUES (1, 2, 3, (SELECT idAthlete FROM athlete WHERE nomAthlete = 'van Alten' AND prenomAthlete = 'Wietse') , (SELECT idAthlete FROM athlete WHERE nomAthlete = 'Petersson' AND prenomAthlete = 'Magnus') , '114 – 109');
