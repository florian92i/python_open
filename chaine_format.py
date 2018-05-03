# formatage d'une adresse
adresse = """
{no_rue}, {nom_rue}
 {code_postal} {nom_ville} ({pays})
""".format(no_rue=5, nom_rue="rue des Postes", code_postal=75003, nom_ville="Paris", pays="France")
print(adresse)
