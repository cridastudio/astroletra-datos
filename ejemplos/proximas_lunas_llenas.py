"""Las próximas lunas llenas con la hora de tu ciudad, a partir de datos/lunaciones.csv."""
import csv
import datetime
import sys

ciudad = sys.argv[1] if len(sys.argv) > 1 else "madrid"  # madrid, mexico_city, bogota, santiago, buenos_aires, new_york, los_angeles, london
hoy = datetime.datetime.now(datetime.timezone.utc).isoformat()

with open("datos/lunaciones.csv", encoding="utf-8-sig") as f:
    for fila in csv.DictReader(f):
        if fila["phase"] == "full" and fila["datetime_utc"] >= hoy[:19]:
            print(fila[ciudad][:16].replace("T", " "), "Luna llena en", fila["sign_es"], "(eclipse)" if fila["eclipse"] else "")
