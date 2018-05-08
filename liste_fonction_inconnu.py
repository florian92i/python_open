def fonction_inconnue(*parametres):
    """Test d'une fonction pouvant être appelée avec un nombre variable de paramètres"""

    print("J'ai reçu : {}.".format(parametres))

fonction_inconnue(84)
fonction_inconnue('ij')
fonction_inconnue('i','ok')
fonction_inconnue('i','ok','ok')
var = 3.5
fonction_inconnue(var, [4], "...")
