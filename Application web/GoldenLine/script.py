import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GoldenLine.settings")

import django
django.setup()


import os
import django
import random
from faker import Faker
from analyses.models import Client, Collecte


# Création de 100 données factices à l'aide de fake
fake = Faker()
quantite = 100  

for i in range(quantite):
    #Création des données factices du client
    identifiant_client = fake.unique.random_number()
    nombre_enfants = random.randint(0, 5)
    categorie_socio = fake.random_element(elements=('Etudiant', 'Employe', 'Independant'))
    
    #Création des données factices du panier
    prix_panier = round(random.uniform(50, 2000), 2)
    montant_alimentaire = round(random.uniform(0, prix_panier), 2)
    montant_multimedia = round(random.uniform(0, prix_panier - montant_alimentaire), 2)
    montant_autre = round(prix_panier - (montant_alimentaire + montant_multimedia), 2)
    detail_panier = {"alimentaire": montant_alimentaire, "multimedia": montant_multimedia, "autre": montant_autre}
    
    #Création de l'enregistement du panier de du client dans la base de données
    panier = Collecte.objects.create(identifiant_collecte=i+2, prix_panier=prix_panier, detail_panier=detail_panier)
    client = Client.objects.create(identifiant_client=identifiant_client, nombre_enfants=nombre_enfants, categorie_socioprofessionnelle = categorie_socio, identifiant_collecte = panier)