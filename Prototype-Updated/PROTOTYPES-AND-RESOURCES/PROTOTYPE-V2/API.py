url = 'https://api.eia.gov/v2/electricity/rto/region-data/data/?frequency=hourly&data[0]=value&facets[respondent][]=CAL&start=2024-01-01T00&end=2024-04-16T00&sort[0][column]=period&sort[0][direction]=asc&offset=0&length=5000'
# The current paramaters are all eletric demand, forecast, net generation, and interchange data in California starting from Jan 1 2024 to April 16 2024.
X-Params: {
    "frequency": "hourly",
    "data": [
        "value"
    ],
    "facets": {
        "respondent": [
            "CAL"
        ]
    },
    "start": "2024-01-01T00",
    "end": "2024-04-16T00",
    "sort": [
        {
            "column": "period",
            "direction": "asc"
        }
    ],
    "offset": 0,
    "length": 5000
} # type: ignore
