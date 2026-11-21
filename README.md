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
| [`datos/eclipse-2027-nubes.csv`](datos/eclipse-2027-nubes.csv) | Eclipse total del 2 de agosto de 2027, los 106 municipios de España con totalidad, ordenados por los segundos de totalidad que se pueden esperar ver según las nubes de esas mañanas de 1991 a 2020 (ERA5) | 106 |
| [`datos/municipios-espana.json`](datos/municipios-espana.json) | Los 8132 municipios de España con código INE, provincia, coordenadas y en qué eclipses de Sol de 2026 a 2028 ven la fase total o anular | 8132 |
| [`datos/eclipses-franjas.json`](datos/eclipses-franjas.json) | Línea central y límites norte y sur de la franja de los eclipses de Sol centrales, en latitud y longitud | 8 eclipses |
| [`datos/eclipses-besselianos.json`](datos/eclipses-besselianos.json) | Elementos de Bessel de los eclipses de Sol y de Luna, para calcular cada eclipse desde cualquier lugar | 24 |
| [`openapi.json`](openapi.json) | Definición OpenAPI 3.1 de la API | |

Cada tabla está también en JSON, y los calendarios en iCal (`.ics`) para suscribirse desde Google Calendar, Apple o Outlook.

El ranking del eclipse de 2027 se explica en [los mejores sitios para ver el eclipse](https://astroletra.com/eclipses/eclipse-solar-total-2-agosto-2027/mejores-sitios/). Es climatología, no una previsión.

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

### Actividad solar y auroras

Desde el 21-11-2026 la API tiene una segunda ruta con la actividad solar en directo, en castellano, con datos del Centro de Predicción del Clima Espacial de la NOAA (dominio público): el índice Kp, la previsión de tres días, las escalas G, S y R, el viento solar, los avisos y los dos óvalos de la aurora.

```
GET https://api.astroletra.com/api/v1/sol/actividad
```

Documentación en [astroletra.com/datos/api/#sol-actividad](https://astroletra.com/datos/api/#sol-actividad).

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

Fuentes de terceros que llevan algunos ficheros:

- Nubes del eclipse de 2027. Contains modified Copernicus Climate Change Service information (2026). Neither the European Commission nor ECMWF is responsible for any use that may be made of the Copernicus information or data it contains. ERA5, [doi:10.24381/cds.adbb2d47](https://doi.org/10.24381/cds.adbb2d47).
- Municipios. Relación de municipios del INE a 1 de enero de 2026 (fuente, INE). Coordenadas de [GeoNames](https://www.geonames.org/) (CC BY 4.0) y Wikidata (CC0).

---

## English summary

Open astronomical data in Spanish and a free public API from [astroletra.com](https://astroletra.com/).

- **Datasets** (CSV, JSON, iCal). New and full moons, solar and lunar eclipses and planetary retrogrades for 2026 to 2028, solar ingresses for 1930 to 2035 and the meteor showers of 2026 and 2027. Times in UTC and in local time for eight cities. Computed from JPL DE440, tropical zodiac, geocentric.
- **Total solar eclipse of 2 August 2027 in Spain**. The 106 municipalities in the path of totality ranked by the seconds of totality you can expect to see given the historical cloud cover of those mornings (ERA5, 1991-2020), plus all 8132 Spanish municipalities with the eclipses they see as total or annular, the central-eclipse paths and the Besselian elements.
- **Files for scripts**. The same files at `https://api.astroletra.com/api/v1/datos/<file>` (for example `lunaciones.csv`), reachable by any client, pandas included.
- **API**. `GET https://api.astroletra.com/api/v1/cielo` returns the Moon's phase and sign, exact aspects, retrogrades and the next lunation for any IANA time zone. No key, no signup, CORS enabled, 60 requests per minute. [OpenAPI 3.1 definition](openapi.json), [docs](https://astroletra.com/datos/api/).
- **Space weather**. `GET https://api.astroletra.com/api/v1/sol/actividad` returns live solar activity in Spanish from NOAA SWPC data: Kp index, three-day forecast, G, S and R scales, solar wind, alerts and both aurora ovals.
- **License**. CC BY 4.0. Attribute as "Datos de Astroletra" with a link to https://astroletra.com/.
