# Assumptions
Before proceeding further, we should outline assumptions and/or caveats we are making in this analysis. This ensures there is the appropriate transparency and awareness of situations where this analysis will not apply.

1. Our sample dataset after removing missing values (makes up ~20% of our dataset) is representative of the original population data for crime. Thus, it will not impact drastically our analysis.
1. The latest record of crime `Category` and `Outcome Category` is only shown. This means we do not have more than one record for the same crime committed. Thus, our approach to count the number of rows to represent `Crime Incidences` is valid.
   + Can check this in reality.
1. People report crime around the same day as the crime occurs. Thus, can use the `Outcome Date` column as a proxy for when the crime occurred and so our crime rates are the rates crime took place, instead of the rates crime was reported. This will be useful when we join this data with street lighting to understanding if street lighting has an impact on crime.
1. Population projections for Camden wards are close to current population numbers. Thus, our crime rates based on these projections are a good reflection of real crime rates.
1. Population levels in Camden wards do not change drastically within the same year. Thus, joining the yearly population data to monthly crime data is valid.
