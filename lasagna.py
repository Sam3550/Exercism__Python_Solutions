#Samir
# Durée totale de cuisson attendue pour la lasagne (en minutes)
EXPECTED_BAKE_TIME = 40

# Temps de préparation par couche de lasagne (en minutes)
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time: int):
    """
    Calcule le temps de cuisson restant pour la lasagne.

    :param elapsed_bake_time: int
        Temps de cuisson déjà écoulé, en minutes.
    :return: int
        Temps restant avant que la lasagne ne soit complètement cuite,
        basé sur la constante EXPECTED_BAKE_TIME (40 minutes).
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int):
    """
    Calcule le temps de préparation de la lasagne en fonction du nombre de couches.

    :param number_of_layers: int
        Nombre de couches à préparer.
    :return: int
        Temps total de préparation, en minutes,
        basé sur la constante PREPARATION_TIME (2 minutes par couche).
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """
    Calcule le temps total passé depuis le début de la préparation de la lasagne.

    :param number_of_layers: int
        Nombre de couches préparées.
    :param elapsed_bake_time: int
        Temps déjà passé au four, en minutes.
    :return: int
        Temps total écoulé (préparation + cuisson actuelle).
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time