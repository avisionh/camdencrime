# About the Data

The data used in this project is:

1. [On Street Crime in Camden](https://opendata.camden.gov.uk/Crime-and-Criminal-Justice/On-Street-Crime-In-Camden/qeje-7ve7)
1. [Camden Ward Boundary](https://opendata.camden.gov.uk/Maps/Camden-Ward-Boundary/yqyi-6agf)
1. [Camden Population Projections](https://opendata.camden.gov.uk/People-Places/Population-Projections-latest-GLA-Set-/mnm7-vqke)
1. [Camden Street Lighting](https://opendata.camden.gov.uk/Environment/Camden-Street-Lighting/dfq3-8wzu)

The main data being analysed is *"On Street Crime in Camden"*. This has information on the type of crime and number of incidences of this crime within each Camden ward over time.

We supplement this with *"Camden Population Projections"* data so we can compute crime rates within each ward and henceforth compare across these wards and across time.

Moreover, we include *"Camden Ward Boundary"* data to map this crime data so that non-technical audiences can intuitively understand the data more.

Lastly, we add *"Camden Street Lighting"* data to explore potential hypotheses we can have on crime rates in each ward.

***

## Other data
Other data considered but not included in this project as of yet are:
1. [Road Collision Casualties in Camden](https://opendata.camden.gov.uk/Transport/Road-Collision-Casualties-In-Camden/puar-wf4h)
1. [National Statistics Postcode Lookup UK](https://opendata.camden.gov.uk/Maps/National-Statistics-Postcode-Lookup-UK/tr8t-gqz7)

We have omitted *"Road Collision Casualties in Camden"* data for now to focus the analysis. This dataset has a lot of information in and ignoring it for now ensures we can narrow down the problem space.

The *"National Statistics Postcode Lookup UK"* is essentially a mapping file for geographic data and we do not need it as we already have *"Camden Ward Boundary"* data.
