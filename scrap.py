# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import json
# import time

# # Set up Selenium WebDriver (using Chrome in this example)
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Run headless Chrome
# driver = webdriver.Chrome(options=options)

# # Google search URL for the list of pharmacies in Bonoua
# url = "https://www.google.com/search?client=firefox-b-d&sca_esv=a732dfa459a5577e&tbs=lf:1,lf_ui:3&tbm=lcl&sxsrf=ADLYWILcBohgLrDG2wC4hSCfhFosJPKqnQ:1717961543437&q=liste++pharmacies+de+bonoua&rflfq=1&num=10&sa=X&ved=2ahUKEwiY9KK8oc-GAxVQVKQEHdAjB48QjGp6BAgcEAE&biw=1280&bih=609&dpr=1.5#rlfi=hd:;si:;mv:[[5.2735945,-3.589961],[5.2657397,-3.599565299999999]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:3"

# # Navigate to the URL
# driver.get(url)
# time.sleep(3)  # Wait for the page to load

# # Extract the pharmacy entries
# pharmacy_elements = driver.find_elements(By.CSS_SELECTOR, 'div.VkpGBb') or driver.find_elements(By.CSS_SELECTOR, 'div.VkpQZd')

# pharmacy_data = []
# for pharmacy in pharmacy_elements:
#     name = pharmacy.find_element(By.CSS_SELECTOR, 'div.dbg0pd').text if pharmacy.find_elements(By.CSS_SELECTOR, 'div.dbg0pd') else "No name found"
#     location = pharmacy.find_element(By.CSS_SELECTOR, 'span.rllt__details').text.split(' · ')[0] if pharmacy.find_elements(By.CSS_SELECTOR, 'span.rllt__details') else "No location found"
#     hours = pharmacy.find_element(By.CSS_SELECTOR, 'span.rllt__details').text.split(' · ')[1] if pharmacy.find_elements(By.CSS_SELECTOR, 'span.rllt__details') and len(pharmacy.find_element(By.CSS_SELECTOR, 'span.rllt__details').text.split(' · ')) > 1 else "No hours listed"
    
#     # Extract latitude and longitude from URL if available
#     maps_url = pharmacy.find_element(By.CSS_SELECTOR, 'a').get_attribute('href') if pharmacy.find_elements(By.CSS_SELECTOR, 'a') else ""
#     lat_lng = maps_url.split('!2d')[1].split('!3d') if maps_url and '!2d' in maps_url and '!3d' in maps_url else ["0", "0"]
#     longitude = lat_lng[0]
#     latitude = lat_lng[1]
    
#     # Extract contact information if available
#     contact = pharmacy.find_element(By.CSS_SELECTOR, 'span.LrzXr.zdqRlf.kno-fv').text if pharmacy.find_elements(By.CSS_SELECTOR, 'span.LrzXr.zdqRlf.kno-fv') else "No contact found"

#     pharmacy_data.append({
#         'name': name,
#         'location': location,
#         'hours': hours,
#         'latitude': latitude,
#         'longitude': longitude,
#         'contact': contact
#     })

# # Convert the data to JSON format
# pharmacy_data_json = json.dumps(pharmacy_data, ensure_ascii=False, indent=4)

# # Save the JSON data to a file
# with open('pharmacies_bonoua.json', 'w', encoding='utf-8') as json_file:
#     json_file.write(pharmacy_data_json)

# print("Data has been written to pharmacies_bonoua.json")

# # Close the browser
# driver.quit()

# import json
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options

# # Configurer les options de Chrome pour ignorer les erreurs SSL
# chrome_options = Options()
# chrome_options.add_argument("--ignore-certificate-errors")

# # Initialiser le driver Chrome avec les options
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# # Naviguer vers la page cible
# driver.get("https://business.abidjan.net/pharmacies-de-cote-d-ivoire")

# # Attendre que la page soit complètement chargée
# wait = WebDriverWait(driver, 30)

# # Prendre une capture d'écran de la page initiale
# driver.save_screenshot('initial_page.png')

# # Trouver le filtre de localité
# try:
#     locality_filter = wait.until(EC.presence_of_element_located((By.ID, "localite")))
# except Exception as e:
#     print(f"Error locating the locality filter: {e}")
#     driver.quit()
#     exit()

# # Sélectionner la localité "Bonoua" dans le filtre
# select = Select(locality_filter)
# select.select_by_visible_text("Bonoua")

# # Prendre une capture d'écran après la sélection
# driver.save_screenshot('after_select.png')

# # Cliquer sur le bouton de recherche si nécessaire (adapter le sélecteur si nécessaire)
# try:
#     search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Rechercher']")))
#     search_button.click()
#     print("Search button clicked")
# except Exception as e:
#     print(f"Error clicking the search button: {e}")
#     driver.quit()
#     exit()

# # Attendre que les résultats se chargent
# time.sleep(10)

# # Prendre une capture d'écran après la recherche
# driver.save_screenshot('after_search.png')

# # Récupérer le contenu HTML de la page après la recherche
# html_content = driver.page_source

# # Fermer le navigateur
# driver.quit()

# # Sauvegarder le contenu HTML dans un fichier pour le débogage
# with open("page_content.html", "w", encoding="utf-8") as f:
#     f.write(html_content)

# print("Contenu HTML de la page enregistré dans page_content.html")

# import openpyxl
# from openpyxl.styles import Font

# # Création d'un nouveau classeur
# wb = openpyxl.Workbook()
# ws = wb.active
# ws.title = "Calculs de Monsieur Koffi"

# # Mise en forme des en-têtes
# bold_font = Font(bold=True)

# # Ajout des en-têtes pour les recettes et dépenses
# ws.append(["Type", "Détails", "Montant (FCFA)"])
# ws["A1"].font = bold_font
# ws["B1"].font = bold_font
# ws["C1"].font = bold_font

# # Ajout des recettes
# ws.append(["Recettes", "Salaire", 1312000])
# ws.append(["Recettes", "Récompense au travail", 650000])
# ws.append(["Recettes", "Soutien des amis et proches", 131200])
# ws.append(["Recettes", "Total des recettes", 2093200])

# # Ajout des dépenses
# ws.append(["Dépenses", "Enfants", 125000])
# ws.append(["Dépenses", "Loyer", 328000])
# ws.append(["Dépenses", "Facture d'hôpital", 459000])
# ws.append(["Dépenses", "Total des dépenses", 912000])

# # Calcul de l'épargne
# ws.append(["Épargne", "", 2093200 - 912000])

# # Sauvegarde du fichier Excel
# wb.save("calculs_monsieur_koffi.xlsx")

# print("Fichier Excel créé avec succès.")

# Importations nécessaires
import os
import django


# Spécifiez le module de configuration des paramètres de votre application Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Chargez les paramètres de votre application Django
django.setup()

from django.core.management.base import BaseCommand
from pharmacies.models import Pharmacie, Assurance
import json

import json
from pharmacies.models import Pharmacie, Assurance

with open('pharmacies_bonoua2.json', 'r') as f:
    pharmacies_data = json.load(f)

for pharmacy_data in pharmacies_data:
    assurance_data = pharmacy_data.pop('assurance')
    assurance, created = Assurance.objects.get_or_create(
        nom=assurance_data['nom'],
        entreprise=assurance_data['entreprise'],
        numero=assurance_data['numero']
    )
    pharmacy = Pharmacie.objects.create(assurance=assurance, **pharmacy_data)
    pharmacy.save()
