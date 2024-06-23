curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '688', '43', '15', '345 (1)', '343 (4)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 144969, '688', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '682', '41', '14', '337 (7)', '345 (1)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 111530, '682', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '681', '39', '18', '337 (9)', '344 (3)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 124388, '681', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '680', '37', '23', '340 (2)', '340 (5)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 134919, '680', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '678', '37', '12', '333 (18)', '345 (2)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 2103727, '678', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '675', '37', '9', '338 (4)', '337 (7)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 145535, '675', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '674', '35', '6', '338 (5)', '336 (10)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 141803, '674', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '670', '30', '15', '334 (16)', '336 (11)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 135226, '670', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '669', '34', '10', '338 (3)', '331 (17)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 126848, '669', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '669', '32', '9', '337 (6)', '332 (16)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 136120, '669', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '669', '31', '9', '332 (21)', '337 (6)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 141802, '669', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '668', '31', '8', '336 (11)', '332 (14)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 2504096, '668', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '668', '28', '10', '332 (22)', '336 (9)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 133130, '668', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '667', '29', '11', '334 (15)', '333 (13)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 145534, '667', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '666', '29', '8', '337 (10)', '329 (25)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 134406, '666', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '665', '27', '7', '328 (35)', '337 (8)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 111544, '665', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '662', '28', '10', '337 (8)', '325 (44)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 140936, '662', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '662', '27', '12', '331 (24)', '331 (20)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 141609, '662', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '662', '25', '13', '334 (17)', '328 (33)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 122283, '662', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '661', '28', '12', '335 (12)', '326 (40)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 126326, '661', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '661', '26', '8', '329 (28)', '332 (15)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 136070, '661', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '661', '26', '6', '332 (20)', '329 (26)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 144501, '661', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '660', '30', '12', '334 (14)', '326 (39)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 144000, '660', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '658', '28', '10', '328 (34)', '330 (22)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 111536, '658', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '658', '28', '9', '335 (13)', '323 (51)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 133959, '658', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '658', '26', '9', '331 (25)', '327 (34)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 143709, '658', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '657', '27', '9', '329 (29)', '328 (28)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 144763, '657', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '656', '27', '8', '332 (19)', '324 (=49)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 147048, '656', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '656', '26', '10', '325 (38)', '331 (19)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 147311, '656', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '656', '26', '9', '328 (36)', '328 (27)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 146850, '656', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '656', '22', '5', '329 (30)', '327 (38)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 143748, '656', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '655', '26', '10', '330 (26)', '325 (43)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 143710, '655', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '654', '23', '6', '330 (27)', '324 (=49)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 143339, '654', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '653', '24', '8', '322 (=49)', '331 (18)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 146210, '653', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '653', '24', '7', '329 (31)', '324 (48)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 134416, '653', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '653', '23', '7', '326 (37)', '327 (=35)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 133798, '653', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '652', '26', '6', '323 (45)', '329 (24)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 102875, '652', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '652', '21', '11', '329 (33)', '323 (52)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 143091, '652', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '651', '23', '8', '324 (43)', '327 (37)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 121560, '651', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '651', '21', '9', '325 (=39)', '326 (41)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 132752, '651', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '651', '21', '8', '321 (52)', '330 (23)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 146550, '651', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '650', '25', '8', '331 (23)', '319 (61)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 132453, '650', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '650', '23', '7', '322 (=49)', '328 (=31)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 140989, '650', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '650', '21', '6', '329 (32)', '321 (59)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 142460, '650', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '649', '26', '6', '316 (57)', '333 (12)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 142674, '649', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '649', '23', '5', '322 (48)', '327 (=35)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 102879, '649', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '649', '22', '5', '321 (51)', '328 (=31)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 126572, '649', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '649', '18', '7', '321 (53)', '328 (30)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 143092, '649', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '648', '25', '6', '323 (46)', '325 (42)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 124865, '648', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '648', '21', '11', '325 (41)', '323 (55)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 102853, '648', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '648', '21', '7', '325 (=39)', '323 (56)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 142799, '648', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '647', '22', '12', '319 (54)', '328 (29)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 144764, '647', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '647', '20', '5', '322 (47)', '325 (47)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 147597, '647', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '646', '22', '6', '325 (42)', '321 (58)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 145357, '646', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '646', '21', '7', '324 (44)', '322 (57)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 102885, '646', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '645', '28', '9', '315 (59)', '330 (21)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 2502893, '645', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '640', '21', '8', '315 (58)', '325 (46)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 111548, '640', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '639', '22', '7', '314 (60)', '325 (45)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 123462, '639', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '637', '19', '6', '317 (56)', '320 (60)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 2069, '637', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '635', '19', '8', '312 (61)', '323 (53)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 143957, '635', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '632', '15', '5', '319 (55)', '313 (63)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 143664, '632', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '631', '16', '4', '308 (63)', '323 (54)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 146900, '631', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '629', '18', '4', '312 (62)', '317 (62)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 127171, '629', 'Points', null, (SELECT COUNT(*) FROM resultat))")

curseur.execute(f"INSERT INTO resultat(idresultat, idevenement, idmanche, resultat1, resultat2, resultat3, resultat4, resultat5) VALUES ((SELECT COUNT(*)+1 FROM resultat),{idev}, {id_manche}, '582', '13', '2', '282 (64)', '300 (64)')")
curseur.execute(f"INSERT INTO performance_individuelle VALUES ({idev}, {id_manche}, 135095, '582', 'Points', null, (SELECT COUNT(*) FROM resultat))")

