# Assignment by HeilWare - Docs

1. Create a virtual environment using python.

```bash
python -m venv venv
source venv/bin/activate
```

2. Install the requirements.

```bash
pip install -r requirements.txt
```

3. Rnn the Django application on port 8000.

```
python manage.py runserver
```

4.  Open link in browser.

http://localhost:8000/

![s1](/images/s1.png) 5. Enter the geojson in the text area to calculate the union of the geometries.

get the geojson data from [here](/test_data.json)

```json
{
  "polygon1": {
    "type": "FeatureCollection",
    "features": [
      {
        "type": "Feature",
        "properties": {},
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [77.17037200927734, 28.507013881018153],
              [77.22169876098633, 28.507013881018153],
              [77.22169876098633, 28.57879352089678],
              [77.17037200927734, 28.57879352089678],
              [77.17037200927734, 28.507013881018153]
            ]
          ]
        }
      }
    ]
  },
  "polygon2": {
    "type": "FeatureCollection",
    "features": [
      {
        "type": "Feature",
        "properties": {},
        "geometry": {
          "type": "Polygon",
          "coordinates": [
            [
              [77.18891143798828, 28.52737652035115],
              [77.28229522705078, 28.52737652035115],
              [77.28229522705078, 28.56341628776094],
              [77.18891143798828, 28.56341628776094],
              [77.18891143798828, 28.52737652035115]
            ]
          ]
        }
      }
    ]
  }
}
```

![s1](/images/s2.png)

6. click on submit button to get the results.

![s3](/images/s3.png)
