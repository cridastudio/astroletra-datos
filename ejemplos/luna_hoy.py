"""La Luna de hoy en tu zona horaria, con la API pública de Astroletra (sin clave)."""
import json
import sys
import urllib.parse
import urllib.request

zona = sys.argv[1] if len(sys.argv) > 1 else "Europe/Madrid"
url = "https://api.astroletra.com/api/v1/cielo?" + urllib.parse.urlencode({"tz": zona})
cielo = json.load(urllib.request.urlopen(url))

luna = cielo["moon"]
print(f"Luna en {luna['sign_label']}, iluminada al {round(luna['illumination'] * 100)} %")
cambio = luna.get("next_sign_change")
if cambio:
    print(f"Cambio de signo, a {cambio['to_sign_label']} el {cambio['date_local']} a las {cambio['time']} ({zona})")
retro = [r["planet_label"] for r in cielo["retrogrades"]]
print("Retrógrados hoy,", ", ".join(retro) if retro else "ninguno")
print("Datos de Astroletra, https://astroletra.com/")
