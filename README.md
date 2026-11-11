# Astroletra, datos abiertos del cielo y API pública

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24132871.svg)](https://doi.org/10.5281/zenodo.24132871)

Fechas y horas de las lunas nuevas y llenas, los eclipses, los planetas retrógrados y la entrada del Sol en cada signo, calculadas con las efemérides JPL DE440 de la NASA y dadas en hora local de ocho ciudades. Más una API gratuita, sin clave, con el cielo de cada día.

Todo sale de [astroletra.com](https://astroletra.com/), un portal de horóscopo y efemérides en español para España y Latinoamérica. Los datos se publican con licencia [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.es). Puedes usarlos, también con fines comerciales, citando la fuente.

*English summary below.*

## Qué hay aquí

| Fichero | Contenido | Filas |
|---|---|---|
| [`datos/lunaciones.csv`](datos/lunaciones.csv) | Lunas nuevas y llenas de 2026 a 2028, con signo, grado y hora local | 75 |
| [`datos/eclipses.csv`](datos/eclipses.csv) | Eclipses de Sol y de Luna de 2026 a 2028, con tipo, saros y hora del máximo | 14 |
| [`datos/retrogrados.csv`](datos/retrogrados.csv) | Periodos retrógrados de Mercurio, Venus, Marte, Júpiter y Saturno, con las dos estaciones y la sombra | 18 |
| [`datos/ingresos-solares.csv`](datos/ingresos-solares.csv) | Instante en que el Sol entra en cada signo, de 1930 a 2035 | 1272 |
| [`datos/calendario-2027.csv`](datos/calendario-2027.csv) | Todo 2027 en una sola tabla | 50 |
| [`datos/lluvias-de-estrellas.csv`](datos/lluvias-de-estrellas.csv) | Lluvias de estrellas de 2026 y 2027, con la noche del máximo y la Luna de esa noche | 22 |
| [`openapi.json`](openapi.json) | Definición OpenAPI 3.1 de la API | |

Cada tabla está también en JSON, y los calendarios en iCal (`.ics`) para suscribirse desde Google Calendar, Apple o Outlook.

Las horas van en UTC y en la hora local de Madrid, Ciudad de México, Bogotá, Santiago, Buenos Aires, Nueva York, Los Ángeles y Londres. Los signos son los del zodiaco tropical y las posiciones son geocéntricas.

Los ficheros de este repositorio son una copia. La versión al día está siempre en [astroletra.com/datos/](https://astroletra.com/datos/).

Para descargarlos desde un programa, usa la API, que sirve los mismos ficheros con el mismo nombre y admite cualquier cliente:

```
https://api.astroletra.com/api/v1/datos/lunaciones.csv
```

```python
import pandas as pd
lunas = pd.read_csv("https://api.astroletra.com/api/v1/datos/lunaciones.csv", encoding="utf-8-sig")
```

## La API

Una sola llamada devuelve la fase y el signo de la Luna, los aspectos exactos con su hora local, los planetas retrógrados y la próxima lunación.

```
GET https://api.astroletra.com/api/v1/cielo?date=2026-11-24&tz=America/Mexico_City
```

| Parámetro | Valor | Por defecto |
|---|---|---|
| `date` | Fecha `AAAA-MM-DD`, hasta siete días antes o después de hoy | Hoy |
| `tz` | Zona horaria IANA, por ejemplo `America/Bogota` | `Europe/Madrid` |

No pide clave ni registro. Admite 60 peticiones por minuto, responde en JSON y permite llamadas desde el navegador (CORS abierto). La documentación completa está en [astroletra.com/datos/api/](https://astroletra.com/datos/api/).

```bash
curl -s "https://api.astroletra.com/api/v1/cielo?tz=America/Mexico_City"
```

```js
const r = await fetch("https://api.astroletra.com/api/v1/cielo?tz=America/Mexico_City");
const cielo = await r.json();
console.log(cielo.moon.sign_label, cielo.moon.illumination);
```

```python
import json, urllib.request
url = "https://api.astroletra.com/api/v1/cielo?tz=America/Mexico_City"
cielo = json.load(urllib.request.urlopen(url))
print(cielo["moon"]["sign_label"], [r["planet_label"] for r in cielo["retrogrades"]])
```

Hay más ejemplos en la carpeta [`ejemplos/`](ejemplos/).

## Un widget para tu web

Si solo quieres enseñar la fase de la Luna de hoy, hay un widget que se pega con dos líneas, pesa menos de 10 KB y no deja cookies. Se configura en [astroletra.com/widget/](https://astroletra.com/widget/).

## Cómo citar

> Astroletra (2026). Lunaciones, eclipses, planetas retrógrados e ingresos solares (JPL DE440), datos abiertos de Astroletra. Zenodo. https://doi.org/10.5281/zenodo.24132871

En una web basta una línea visible, «Datos de Astroletra», con un enlace a https://astroletra.com/.

## Cómo se calcula

Las posiciones salen de las efemérides JPL DE440. Cada instante (luna llena, estación de un planeta, entrada en un signo) se busca numéricamente hasta el segundo. Las entradas del Sol se han contrastado con las del Observatorio Naval de Estados Unidos, con una diferencia máxima de 45 segundos. El método completo está en [Cómo elaboramos los horóscopos](https://astroletra.com/como-elaboramos-los-horoscopos/).

## Errores y sugerencias

Si ves un dato que no cuadra, abre una incidencia en este repositorio o escribe a info@astroletra.com. Lo comprobamos y lo corregimos en origen.

## Licencia

Datos, [CC BY 4.0](LICENSE). Ejemplos de código, dominio público (CC0).

---

## English summary

Open astronomical data in Spanish and a free public API from [astroletra.com](https://astroletra.com/).

- **Datasets** (CSV, JSON, iCal). New and full moons, solar and lunar eclipses and planetary retrogrades for 2026 to 2028, solar ingresses for 1930 to 2035 and the meteor showers of 2026 and 2027. Times in UTC and in local time for eight cities. Computed from JPL DE440, tropical zodiac, geocentric.
- **Files for scripts**. The same files at `https://api.astroletra.com/api/v1/datos/<file>` (for example `lunaciones.csv`), reachable by any client, pandas included.
- **API**. `GET https://api.astroletra.com/api/v1/cielo` returns the Moon's phase and sign, exact aspects, retrogrades and the next lunation for any IANA time zone. No key, no signup, CORS enabled, 60 requests per minute. [OpenAPI 3.1 definition](openapi.json), [docs](https://astroletra.com/datos/api/).
- **License**. CC BY 4.0. Attribute as "Datos de Astroletra" with a link to https://astroletra.com/.
