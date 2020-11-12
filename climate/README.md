# Climate changes on Leme-SP

Another bunch of charts in order to analyze the evolution of monthly temperature rage in the region of Leme-SP over the course of years.

This analysis can evolve to a web app in the future, so *stay awhile and listen*. De facto this is just a overcomplicated POC.


## The data

The monthly data is obtained by analysing the [CPTEC][1] Brazil heat maps, using the minimum, maximum and average data for each year and month.

This analysis will initially follow my [Strava][2] JSON based datasets style, but this will change as the data grows.

The CPTEC only offer temperature data in form of ranges, so for the chart generation this analysis will use the average of the range on the **min** and **max** fields, while keeping the raw range as string on the **min-range** and **max-range**.

### JSON structure

```json
"year": {
    "mounth": {
        "min": 21,
        "max": 31,
        "min-range": "20-22",
        "max-range": "30-32"
    }
}    
```


[1]: http://clima1.cptec.inpe.br/monitoramentobrasil/pt
[2]: https://github.com/ghp2201/data-analysis/tree/master/strava
