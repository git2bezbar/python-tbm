# Fonctions

def rechercheArret(_lignes, _nomLignes, _arret):
  reponse = []
  numeroLigne = 0
  while numeroLigne < len(_lignes):
    numeroArret = 0
    while numeroArret < len(_lignes[numeroLigne]):
      if _lignes[numeroLigne][numeroArret] == _arret:
        reponse.append(_nomLignes[numeroLigne])
      numeroArret += 1
    numeroLigne += 1
  return reponse

def rechercherCorrespondance(_array1, _array2):
  set1 = set(_array1)
  set2 = set(_array2)
  intersection = list(set1 & set2)
  return intersection

def rechercheLigneEnCommun(_liste1, _liste2):
  print("============")
  print("VOTRE VOYAGE")
  print("============")

  set1 = set(_liste1)
  set2 = set(_liste2)
  intersection = list(set1 & set2)
  if not intersection:
    intersection = [_liste1[0], _liste2[0]]
  else:
    print("La ligne que vous devrez emprunter est : ", intersection[0])
  return intersection

def listerArrets(index1, index2, ligne):
  tempListeArrets = []
  for i, arret in enumerate(ligne):
    if i > min(index1, index2) and i < max(index1, index2):
      listeArrets.append(arret)
      tempListeArrets.append(arret)
  if(index1 > index2):
    tempListeArrets.reverse()

  print("------")
  print(ligne[index1])
  for index, arret in enumerate(tempListeArrets):
    print("|", arret)
  print(ligne[index2])
  print("------")

def determinerSens(_arret1, _arret2, _lignes):
  print(_lignes)
  for index, element in enumerate(_lignes):
    ligne = ListeLigne[NomLigne.index(element)]
    if len(_lignes) == 1:
      index1 = ligne.index(_arret1)
      index2 = ligne.index(_arret2)
    else:
      correspondance = rechercherCorrespondance(ListeLigne[NomLigne.index(_lignes[0])], ListeLigne[NomLigne.index(_lignes[1])])[0]
      if index == 0:
        index1 = ligne.index(_arret1)
        index2 = ligne.index(correspondance)
        listeCorrespondances.append(correspondance)
        listeArrets.append(" ")
      if index == 1:
        index1 = ligne.index(correspondance)
        index2 = ligne.index(_arret2)

    if index1 < index2:
      print("Prenez le tram direction : ==>", ligne[-1])
    else: 
      print("Prenez le tram direction : ==>", ligne[0])
    listerArrets(index1, index2, ligne)

# Initialisation de tableaux

listeArrets = []
listeCorrespondances = []

if __name__ == "__main__":

  # Définition des lignes de tramway

  ligneA = [
    "Le Haillan Rostand", 
    "Les Pins",
    "Frères Robinson", 
    "Hôtel de Ville Mérignac", 
    "Pin Galant",
    "Mérignac Centre", 
    "Lycées de Mérignac", 
    "Quatre Chemins", 
    "Pierre Mendès-France", 
    "Alfred de Vigny", 
    "Fontaine d'Arlac", 
    "Peychotte",
    "François Mitterrand", 
    "Saint-Augustin", "Hôpital Pellegrin", 
    "Stade Chaban-Delmas", 
    "Gaviniès", 
    "Hôtel de Police", 
    "Saint-Bruno - Hôtel de Région", 
    "Mériadeck", 
    "Palais de Justice", 
    "Hôtel de Ville",
    "Sainte-Catherine", 
    "Place du Palais", 
    "Porte de Bourgogne",
    "Stalingrad", 
    "Jardin botanique", 
    "Thiers - Benauge", 
    "Galin", 
    "Jean Jaurès", 
    "Cenon Gare", 
    "Carnot - Mairie de Cenon", 
    "Buttinière"
  ]

  ligneB = [
    "Berges de la Garonne",   
    "Claveau",
    "Brandenburg",
    "New-York",
    "Rue Achard",
    "Bassins à Flot", 
    "Les Hangars",
    "Cours du Médoc",
    "Chartrons", 
    "CAPC (Musée d'Art Contemporain)",
    "Quinconces",
    "Grand Théâtre",
    "Gambetta",
    "Hôtel de Ville",
    "Musée d'Aquitaine",
    "Victoire",
    "Saint-Nicolas",
    "Bergonié",
    "Barrière Saint-Genès",
    "Roustaing",
    "Forum",
    "Peixotto",
    "Béthanie",
    "Arts et Métiers",
    "François Bordes",
    "Doyen Brus",
    "Montaigne-Montesquieu",
    "UNITEC",
    "Saige",
    "Bougnard"
  ]

  ligneC = [
    "Parc des Expositions",
    "Palais des Congrès",
    "Quarante Journaux",
    "Berges du lac",
    "Les Aubiers",
    "Place Ravezies-Le Bouscat",
    "Grand Parc",
    "Émile Counord",
    "Camille Godard",
    "Place Paul Doumer",
    "Jardin Public",
    "Quinconces",
    "Place de la Bourse",
    "Porte de Bourgogne",
    "Saint-Michel",
    "Sainte-Croix",
    "Tauzia",
    "Gare Saint-Jean",
    "Belcier",
    "Carle Vernet",
    "Bègles Terres Neuves",
    "La Belle Rose",
    "Stade Musard",
    "Calais – Centujean",
    "Gare de Bègles",
    "Parc de Mussonville",
    "Lycée Vaclav Havel"
  ]

  ligneD = [
    "Quinconces",
    "Charles Gruet",
    "Marie Brizard",
    "Barrière du Médoc",
    "Courbet",
    "Calypso",
    "Mairie du Bouscat",
    "Les Ecus",
    "Sainte-Germaine",
    "Hippodrome",
    "Le Sulky",
    "Toulouse Lautrec",
    "Picot",
    "Eysines Centre",
    "Les Sources",
    "Cantinolle"
  ]

  NomLigne = [
    "TramA",
    "TramB",
    "TramC",
    "TramD",
  ]

  ListeLigne = [
    ligneA,
    ligneB,
    ligneC,
    ligneD,
  ]

  # Récupération du départ et de l'arrivée

  depart = input("Saisir le nom de l'arrêt de départ : ")
  while not any(depart in arret for arret in ListeLigne):
    print("Arrêt de tramway non trouvé.")
    depart = input("Saisir le nom de l'arrêt de départ : ")
  ListeLigneDepartTrouvees = rechercheArret(ListeLigne, NomLigne, depart)

  arrivee = input("Saisir le nom de l'arrêt d'arrivée : ")
  while not any(arrivee in arret for arret in ListeLigne):
    print("Arrêt de tramway non trouvé.")
    arrivee = input("Saisir le nom de l'arrêt de départ : ")
  ListeLigneArriveeTrouvees = rechercheArret(ListeLigne, NomLigne, arrivee)

  ligneEnCommun = rechercheLigneEnCommun(ListeLigneDepartTrouvees, ListeLigneArriveeTrouvees)
  determinerSens(depart, arrivee, ligneEnCommun)

  print("Vous avez", len(listeArrets), "arrêt(s) jusqu'à votre destination.")
  if len(listeCorrespondances) > 0:
    print("Vous avez", len(listeCorrespondances), "correspondance.")