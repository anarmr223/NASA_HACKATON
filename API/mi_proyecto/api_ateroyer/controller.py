from datetime import date, timedelta, datetime
import json
import requests
from asteroide import Asteroid
import numpy as np
import re

def formatData(data):
    neo_por_fecha = data["near_earth_objects"]
    listAsteroides = []

    count = 0
    max_asteroides = 10

    for fecha, lista_asteroides in neo_por_fecha.items():
        for asteroide in lista_asteroides:
            if count >= max_asteroides:
                return listAsteroides

            name = asteroide['name']
            id = asteroide['id']
            absolute_magnitude = float(asteroide['absolute_magnitude_h'])
            diam_km = asteroide['estimated_diameter']['kilometers']
            diam_min = diam_km['estimated_diameter_min']
            diam_max = diam_km['estimated_diameter_max']
            estimated_diameter = (diam_min + diam_max) / 2
            is_potentially_hazardous = bool(asteroide['is_potentially_hazardous_asteroid'])
            close_approach = asteroide['close_approach_data'][0]
            close_aproach_data = close_approach['close_approach_date_full']
            velocity = float(close_approach['relative_velocity']['kilometers_per_second'])
            is_sentry_object = asteroide['is_sentry_object']

            x, y, z, mass = getHorizonData(close_aproach_data, id, estimated_diameter)
            print(f"x: {x}, y: {y}, z: {z}")
            asteroideOBJ = Asteroid(
                name, id, absolute_magnitude, estimated_diameter,
                is_potentially_hazardous, close_aproach_data,
                velocity, is_sentry_object, x, y, z, mass
            )

            print("esta es la x",asteroideOBJ.x)

            listAsteroides.append(asteroideOBJ)
            count += 1

    return listAsteroides

def getHorizonData(fecha_apr, horizons_id, ed):
    from datetime import datetime, timedelta
    import requests, json, re

    HORIZONS_URL = "https://ssd.jpl.nasa.gov/api/horizons.api"

    fecha_dt = datetime.strptime(fecha_apr, "%Y-%b-%d %H:%M")
    fecha_ini = fecha_dt.strftime("%Y-%m-%d %H:%M:%S")
    fecha_fin = (fecha_dt + timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")

    # 👇 Poner comillas simples a los campos requeridos
    params = {
        "format": "json",
        "COMMAND": f"'DES={horizons_id}'",
        "EPHEM_TYPE": "VECTORS",
        "CENTER": "'500@399'",
        "START_TIME": f"'{fecha_ini}'",
        "STOP_TIME": f"'{fecha_fin}'",
        "STEP_SIZE": "'1 d'"
    }

    response = requests.get(HORIZONS_URL, params=params)
    data_json = response.json()

    text = data_json.get("result", "")

    gm_match = re.search(r"GM=\s*([0-9.eE+-]+)", text)
    gm_value = float(gm_match.group(1)) if gm_match else None

    soe_match = re.search(
        r"\$\$SOE\s*(?:[^\n]*\n)?\s*X\s*=\s*([0-9.eE+-]+)\s*Y\s*=\s*([0-9.eE+-]+)\s*Z\s*=\s*([0-9.eE+-]+)",
        text
    )

    x, y, z = None, None, None
    if soe_match:
        x = float(soe_match.group(1))
        y = float(soe_match.group(2))
        z = float(soe_match.group(3))

    constanteGravUniversal = 6.67430e-11
    mass_kg = (gm_value * 1e9 / constanteGravUniversal) if gm_value else 0

    densidad = 2500 # kg/m^3 para un promedio ya que no sabemos el tipo de asteroide
    mass_kg = densidad*(((4/3)*np.pi)*(ed/2)**3)

    radio = (ed*1000) / 2
    volumen = (4/3) * np.pi * (radio**3)
    mass_kg = densidad * volumen

    return x, y, z, mass_kg
