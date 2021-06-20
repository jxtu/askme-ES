### Set up
- Download Elasticsearch 7.10.2 using this [link](https://www.elastic.co/downloads/past-releases#elasticsearch) and
start the engine:
```shell
cd elasticsearch-7.10.2/
./bin/elasticsearch
```
- Install dependencies:
```shell
pip install -r requirements.txt
```

### Build ES Index
```shell
# default index name is set to be 'cord_askme_idx'
python load_es_index.py raw_data/cord19 raw_data/cord19/metadata_subset.csv
```

### Query the Index
```shell
python run_query.py "immune treatment options"
```
Output:
```
ID      SCORE   PMC             TITLE
94      11.23   PMC1871602      Immune reconstitution inflammatory syndrome (IRIS): review of common infectious manifestations and treatment options
39      5.07    PMC1287064      An ontology for immune epitopes: application to the design of a broad scope database of immune reactivities
32      4.06    PMC1090610      GIDEON: a comprehensive Web-based resource for geographic medicine
91      3.56    PMC1847501      Immune pathways and defence mechanisms in honey bees Apis mellifera
79      3.26    PMC1751007      Open lung biopsy in early-stage acute respiratory distress syndrome

```