# Scraping German Car Ebay Data

The goal of this guided project is to clean and analyze German eBay data using the tools learned in the Numpy and Pandas Fundamentals section.


```python
import numpy as np
import pandas as pd

# Read data form csv in to pandas dataframe. Defauilt encoding gives unicode error, but Latin-1 and Windows-1252 work:
autos = pd.read_csv("autos.csv", encoding = "Latin-1")
# note: had to read this in without index set in order to change the column names later. Can't change index column names.

#test:
print(autos.iloc[1])

```

    dateCrawled                                   2016-04-04 13:38:56
    name                   BMW_740i_4_4_Liter_HAMANN_UMBAU_Mega_Optik
    seller                                                     privat
    offerType                                                 Angebot
    price                                                      $8,500
    abtest                                                    control
    vehicleType                                             limousine
    yearOfRegistration                                           1997
    gearbox                                                 automatik
    powerPS                                                       286
    model                                                         7er
    odometer                                                150,000km
    monthOfRegistration                                             6
    fuelType                                                   benzin
    brand                                                         bmw
    notRepairedDamage                                            nein
    dateCreated                                   2016-04-04 00:00:00
    nrOfPictures                                                    0
    postalCode                                                  71034
    lastSeen                                      2016-04-06 14:45:08
    Name: 1, dtype: object



```python
# Jupyter will render the first and last few values in a pandas object just by running the cell with the variable in it:
autos
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>dateCrawled</th>
      <th>name</th>
      <th>seller</th>
      <th>offerType</th>
      <th>price</th>
      <th>abtest</th>
      <th>vehicleType</th>
      <th>yearOfRegistration</th>
      <th>gearbox</th>
      <th>powerPS</th>
      <th>model</th>
      <th>odometer</th>
      <th>monthOfRegistration</th>
      <th>fuelType</th>
      <th>brand</th>
      <th>notRepairedDamage</th>
      <th>dateCreated</th>
      <th>nrOfPictures</th>
      <th>postalCode</th>
      <th>lastSeen</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016-03-26 17:47:46</td>
      <td>Peugeot_807_160_NAVTECH_ON_BOARD</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$5,000</td>
      <td>control</td>
      <td>bus</td>
      <td>2004</td>
      <td>manuell</td>
      <td>158</td>
      <td>andere</td>
      <td>150,000km</td>
      <td>3</td>
      <td>lpg</td>
      <td>peugeot</td>
      <td>nein</td>
      <td>2016-03-26 00:00:00</td>
      <td>0</td>
      <td>79588</td>
      <td>2016-04-06 06:45:54</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016-04-04 13:38:56</td>
      <td>BMW_740i_4_4_Liter_HAMANN_UMBAU_Mega_Optik</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$8,500</td>
      <td>control</td>
      <td>limousine</td>
      <td>1997</td>
      <td>automatik</td>
      <td>286</td>
      <td>7er</td>
      <td>150,000km</td>
      <td>6</td>
      <td>benzin</td>
      <td>bmw</td>
      <td>nein</td>
      <td>2016-04-04 00:00:00</td>
      <td>0</td>
      <td>71034</td>
      <td>2016-04-06 14:45:08</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-03-26 18:57:24</td>
      <td>Volkswagen_Golf_1.6_United</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$8,990</td>
      <td>test</td>
      <td>limousine</td>
      <td>2009</td>
      <td>manuell</td>
      <td>102</td>
      <td>golf</td>
      <td>70,000km</td>
      <td>7</td>
      <td>benzin</td>
      <td>volkswagen</td>
      <td>nein</td>
      <td>2016-03-26 00:00:00</td>
      <td>0</td>
      <td>35394</td>
      <td>2016-04-06 20:15:37</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-03-12 16:58:10</td>
      <td>Smart_smart_fortwo_coupe_softouch/F1/Klima/Pan...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$4,350</td>
      <td>control</td>
      <td>kleinwagen</td>
      <td>2007</td>
      <td>automatik</td>
      <td>71</td>
      <td>fortwo</td>
      <td>70,000km</td>
      <td>6</td>
      <td>benzin</td>
      <td>smart</td>
      <td>nein</td>
      <td>2016-03-12 00:00:00</td>
      <td>0</td>
      <td>33729</td>
      <td>2016-03-15 03:16:28</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-04-01 14:38:50</td>
      <td>Ford_Focus_1_6_Benzin_TÜV_neu_ist_sehr_gepfleg...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$1,350</td>
      <td>test</td>
      <td>kombi</td>
      <td>2003</td>
      <td>manuell</td>
      <td>0</td>
      <td>focus</td>
      <td>150,000km</td>
      <td>7</td>
      <td>benzin</td>
      <td>ford</td>
      <td>nein</td>
      <td>2016-04-01 00:00:00</td>
      <td>0</td>
      <td>39218</td>
      <td>2016-04-01 14:38:50</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>49995</th>
      <td>2016-03-27 14:38:19</td>
      <td>Audi_Q5_3.0_TDI_qu._S_tr.__Navi__Panorama__Xenon</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$24,900</td>
      <td>control</td>
      <td>limousine</td>
      <td>2011</td>
      <td>automatik</td>
      <td>239</td>
      <td>q5</td>
      <td>100,000km</td>
      <td>1</td>
      <td>diesel</td>
      <td>audi</td>
      <td>nein</td>
      <td>2016-03-27 00:00:00</td>
      <td>0</td>
      <td>82131</td>
      <td>2016-04-01 13:47:40</td>
    </tr>
    <tr>
      <th>49996</th>
      <td>2016-03-28 10:50:25</td>
      <td>Opel_Astra_F_Cabrio_Bertone_Edition___TÜV_neu+...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$1,980</td>
      <td>control</td>
      <td>cabrio</td>
      <td>1996</td>
      <td>manuell</td>
      <td>75</td>
      <td>astra</td>
      <td>150,000km</td>
      <td>5</td>
      <td>benzin</td>
      <td>opel</td>
      <td>nein</td>
      <td>2016-03-28 00:00:00</td>
      <td>0</td>
      <td>44807</td>
      <td>2016-04-02 14:18:02</td>
    </tr>
    <tr>
      <th>49997</th>
      <td>2016-04-02 14:44:48</td>
      <td>Fiat_500_C_1.2_Dualogic_Lounge</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$13,200</td>
      <td>test</td>
      <td>cabrio</td>
      <td>2014</td>
      <td>automatik</td>
      <td>69</td>
      <td>500</td>
      <td>5,000km</td>
      <td>11</td>
      <td>benzin</td>
      <td>fiat</td>
      <td>nein</td>
      <td>2016-04-02 00:00:00</td>
      <td>0</td>
      <td>73430</td>
      <td>2016-04-04 11:47:27</td>
    </tr>
    <tr>
      <th>49998</th>
      <td>2016-03-08 19:25:42</td>
      <td>Audi_A3_2.0_TDI_Sportback_Ambition</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$22,900</td>
      <td>control</td>
      <td>kombi</td>
      <td>2013</td>
      <td>manuell</td>
      <td>150</td>
      <td>a3</td>
      <td>40,000km</td>
      <td>11</td>
      <td>diesel</td>
      <td>audi</td>
      <td>nein</td>
      <td>2016-03-08 00:00:00</td>
      <td>0</td>
      <td>35683</td>
      <td>2016-04-05 16:45:07</td>
    </tr>
    <tr>
      <th>49999</th>
      <td>2016-03-14 00:42:12</td>
      <td>Opel_Vectra_1.6_16V</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$1,250</td>
      <td>control</td>
      <td>limousine</td>
      <td>1996</td>
      <td>manuell</td>
      <td>101</td>
      <td>vectra</td>
      <td>150,000km</td>
      <td>1</td>
      <td>benzin</td>
      <td>opel</td>
      <td>nein</td>
      <td>2016-03-13 00:00:00</td>
      <td>0</td>
      <td>45897</td>
      <td>2016-04-06 21:18:48</td>
    </tr>
  </tbody>
</table>
<p>50000 rows × 20 columns</p>
</div>




```python
# For info about the dataframe:
autos.info()
autos.head()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 50000 entries, 0 to 49999
    Data columns (total 20 columns):
     #   Column               Non-Null Count  Dtype 
    ---  ------               --------------  ----- 
     0   dateCrawled          50000 non-null  object
     1   name                 50000 non-null  object
     2   seller               50000 non-null  object
     3   offerType            50000 non-null  object
     4   price                50000 non-null  object
     5   abtest               50000 non-null  object
     6   vehicleType          44905 non-null  object
     7   yearOfRegistration   50000 non-null  int64 
     8   gearbox              47320 non-null  object
     9   powerPS              50000 non-null  int64 
     10  model                47242 non-null  object
     11  odometer             50000 non-null  object
     12  monthOfRegistration  50000 non-null  int64 
     13  fuelType             45518 non-null  object
     14  brand                50000 non-null  object
     15  notRepairedDamage    40171 non-null  object
     16  dateCreated          50000 non-null  object
     17  nrOfPictures         50000 non-null  int64 
     18  postalCode           50000 non-null  int64 
     19  lastSeen             50000 non-null  object
    dtypes: int64(5), object(15)
    memory usage: 7.6+ MB





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>dateCrawled</th>
      <th>name</th>
      <th>seller</th>
      <th>offerType</th>
      <th>price</th>
      <th>abtest</th>
      <th>vehicleType</th>
      <th>yearOfRegistration</th>
      <th>gearbox</th>
      <th>powerPS</th>
      <th>model</th>
      <th>odometer</th>
      <th>monthOfRegistration</th>
      <th>fuelType</th>
      <th>brand</th>
      <th>notRepairedDamage</th>
      <th>dateCreated</th>
      <th>nrOfPictures</th>
      <th>postalCode</th>
      <th>lastSeen</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016-03-26 17:47:46</td>
      <td>Peugeot_807_160_NAVTECH_ON_BOARD</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$5,000</td>
      <td>control</td>
      <td>bus</td>
      <td>2004</td>
      <td>manuell</td>
      <td>158</td>
      <td>andere</td>
      <td>150,000km</td>
      <td>3</td>
      <td>lpg</td>
      <td>peugeot</td>
      <td>nein</td>
      <td>2016-03-26 00:00:00</td>
      <td>0</td>
      <td>79588</td>
      <td>2016-04-06 06:45:54</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016-04-04 13:38:56</td>
      <td>BMW_740i_4_4_Liter_HAMANN_UMBAU_Mega_Optik</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$8,500</td>
      <td>control</td>
      <td>limousine</td>
      <td>1997</td>
      <td>automatik</td>
      <td>286</td>
      <td>7er</td>
      <td>150,000km</td>
      <td>6</td>
      <td>benzin</td>
      <td>bmw</td>
      <td>nein</td>
      <td>2016-04-04 00:00:00</td>
      <td>0</td>
      <td>71034</td>
      <td>2016-04-06 14:45:08</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-03-26 18:57:24</td>
      <td>Volkswagen_Golf_1.6_United</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$8,990</td>
      <td>test</td>
      <td>limousine</td>
      <td>2009</td>
      <td>manuell</td>
      <td>102</td>
      <td>golf</td>
      <td>70,000km</td>
      <td>7</td>
      <td>benzin</td>
      <td>volkswagen</td>
      <td>nein</td>
      <td>2016-03-26 00:00:00</td>
      <td>0</td>
      <td>35394</td>
      <td>2016-04-06 20:15:37</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-03-12 16:58:10</td>
      <td>Smart_smart_fortwo_coupe_softouch/F1/Klima/Pan...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$4,350</td>
      <td>control</td>
      <td>kleinwagen</td>
      <td>2007</td>
      <td>automatik</td>
      <td>71</td>
      <td>fortwo</td>
      <td>70,000km</td>
      <td>6</td>
      <td>benzin</td>
      <td>smart</td>
      <td>nein</td>
      <td>2016-03-12 00:00:00</td>
      <td>0</td>
      <td>33729</td>
      <td>2016-03-15 03:16:28</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-04-01 14:38:50</td>
      <td>Ford_Focus_1_6_Benzin_TÜV_neu_ist_sehr_gepfleg...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$1,350</td>
      <td>test</td>
      <td>kombi</td>
      <td>2003</td>
      <td>manuell</td>
      <td>0</td>
      <td>focus</td>
      <td>150,000km</td>
      <td>7</td>
      <td>benzin</td>
      <td>ford</td>
      <td>nein</td>
      <td>2016-04-01 00:00:00</td>
      <td>0</td>
      <td>39218</td>
      <td>2016-04-01 14:38:50</td>
    </tr>
  </tbody>
</table>
</div>



### Observations

Some values are null overall. The fields are in German. There are vehicle types called a kleinwagen and a kombi for instance, which would be helpful to translate for a meaningful analysis for English speakers. From the given observations on the following page: dataset contains 20 columns, most of which are strings. Column names are in camelcase instead of the more conventional snakecase for column names.


```python
# Existing column names:
autos.columns
```




    Index(['dateCrawled', 'name', 'seller', 'offerType', 'price', 'abtest',
           'vehicleType', 'yearOfRegistration', 'gearbox', 'powerPS', 'model',
           'odometer', 'monthOfRegistration', 'fuelType', 'brand',
           'notRepairedDamage', 'dateCreated', 'nrOfPictures', 'postalCode',
           'lastSeen'],
          dtype='object')




```python
newColumnNames = ['date_crawled', 'name', 'seller', 'offer_type', 'price', 'abtest', 'vehicle_type',
       'registration_year', 'gearbox', 'power_PS', 'model', 'odometer',
       'registration_month', 'fuel_type', 'brand', 'unrepaired_damage',
       'ad_created', 'nr_pictures', 'postal_code', 'last_seen']
autos.columns = newColumnNames
autos.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date_crawled</th>
      <th>name</th>
      <th>seller</th>
      <th>offer_type</th>
      <th>price</th>
      <th>abtest</th>
      <th>vehicle_type</th>
      <th>registration_year</th>
      <th>gearbox</th>
      <th>power_PS</th>
      <th>model</th>
      <th>odometer</th>
      <th>registration_month</th>
      <th>fuel_type</th>
      <th>brand</th>
      <th>unrepaired_damage</th>
      <th>ad_created</th>
      <th>nr_pictures</th>
      <th>postal_code</th>
      <th>last_seen</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016-03-26 17:47:46</td>
      <td>Peugeot_807_160_NAVTECH_ON_BOARD</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$5,000</td>
      <td>control</td>
      <td>bus</td>
      <td>2004</td>
      <td>manuell</td>
      <td>158</td>
      <td>andere</td>
      <td>150,000km</td>
      <td>3</td>
      <td>lpg</td>
      <td>peugeot</td>
      <td>nein</td>
      <td>2016-03-26 00:00:00</td>
      <td>0</td>
      <td>79588</td>
      <td>2016-04-06 06:45:54</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016-04-04 13:38:56</td>
      <td>BMW_740i_4_4_Liter_HAMANN_UMBAU_Mega_Optik</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$8,500</td>
      <td>control</td>
      <td>limousine</td>
      <td>1997</td>
      <td>automatik</td>
      <td>286</td>
      <td>7er</td>
      <td>150,000km</td>
      <td>6</td>
      <td>benzin</td>
      <td>bmw</td>
      <td>nein</td>
      <td>2016-04-04 00:00:00</td>
      <td>0</td>
      <td>71034</td>
      <td>2016-04-06 14:45:08</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-03-26 18:57:24</td>
      <td>Volkswagen_Golf_1.6_United</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$8,990</td>
      <td>test</td>
      <td>limousine</td>
      <td>2009</td>
      <td>manuell</td>
      <td>102</td>
      <td>golf</td>
      <td>70,000km</td>
      <td>7</td>
      <td>benzin</td>
      <td>volkswagen</td>
      <td>nein</td>
      <td>2016-03-26 00:00:00</td>
      <td>0</td>
      <td>35394</td>
      <td>2016-04-06 20:15:37</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-03-12 16:58:10</td>
      <td>Smart_smart_fortwo_coupe_softouch/F1/Klima/Pan...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$4,350</td>
      <td>control</td>
      <td>kleinwagen</td>
      <td>2007</td>
      <td>automatik</td>
      <td>71</td>
      <td>fortwo</td>
      <td>70,000km</td>
      <td>6</td>
      <td>benzin</td>
      <td>smart</td>
      <td>nein</td>
      <td>2016-03-12 00:00:00</td>
      <td>0</td>
      <td>33729</td>
      <td>2016-03-15 03:16:28</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-04-01 14:38:50</td>
      <td>Ford_Focus_1_6_Benzin_TÜV_neu_ist_sehr_gepfleg...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$1,350</td>
      <td>test</td>
      <td>kombi</td>
      <td>2003</td>
      <td>manuell</td>
      <td>0</td>
      <td>focus</td>
      <td>150,000km</td>
      <td>7</td>
      <td>benzin</td>
      <td>ford</td>
      <td>nein</td>
      <td>2016-04-01 00:00:00</td>
      <td>0</td>
      <td>39218</td>
      <td>2016-04-01 14:38:50</td>
    </tr>
  </tbody>
</table>
</div>



In the above code, the column names were changed to snakecase to improve the readability. 


```python
autos.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>registration_year</th>
      <th>power_PS</th>
      <th>registration_month</th>
      <th>nr_pictures</th>
      <th>postal_code</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>50000.000000</td>
      <td>50000.000000</td>
      <td>50000.000000</td>
      <td>50000.0</td>
      <td>50000.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2005.073280</td>
      <td>116.355920</td>
      <td>5.723360</td>
      <td>0.0</td>
      <td>50813.627300</td>
    </tr>
    <tr>
      <th>std</th>
      <td>105.712813</td>
      <td>209.216627</td>
      <td>3.711984</td>
      <td>0.0</td>
      <td>25779.747957</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1000.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>1067.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1999.000000</td>
      <td>70.000000</td>
      <td>3.000000</td>
      <td>0.0</td>
      <td>30451.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2003.000000</td>
      <td>105.000000</td>
      <td>6.000000</td>
      <td>0.0</td>
      <td>49577.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2008.000000</td>
      <td>150.000000</td>
      <td>9.000000</td>
      <td>0.0</td>
      <td>71540.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>9999.000000</td>
      <td>17700.000000</td>
      <td>12.000000</td>
      <td>0.0</td>
      <td>99998.000000</td>
    </tr>
  </tbody>
</table>
</div>



### Observations

nr_pictures appears not to have numeric data or all be equal to 0 because it has 50000 count and no statistics associated. It needs more investigation.


```python
autos["nr_pictures"]
```




    0        0
    1        0
    2        0
    3        0
    4        0
            ..
    49995    0
    49996    0
    49997    0
    49998    0
    49999    0
    Name: nr_pictures, Length: 50000, dtype: int64




```python
 autos["nr_pictures"]>0
```




    0        False
    1        False
    2        False
    3        False
    4        False
             ...  
    49995    False
    49996    False
    49997    False
    49998    False
    49999    False
    Name: nr_pictures, Length: 50000, dtype: bool




```python
autos[autos["nr_pictures"]>0]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date_crawled</th>
      <th>name</th>
      <th>seller</th>
      <th>offer_type</th>
      <th>price</th>
      <th>abtest</th>
      <th>vehicle_type</th>
      <th>registration_year</th>
      <th>gearbox</th>
      <th>power_PS</th>
      <th>model</th>
      <th>odometer</th>
      <th>registration_month</th>
      <th>fuel_type</th>
      <th>brand</th>
      <th>unrepaired_damage</th>
      <th>ad_created</th>
      <th>nr_pictures</th>
      <th>postal_code</th>
      <th>last_seen</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>



### Investigation

It appears all values for nr_pictures are equal to 0. Also, the Price and Odometer columns are stored as text, so don't show up in the statistics. 


```python
# Cleaning up Price and Odometer:
#pattern = '|'.join(["$", ","])
autos["price"] = autos["price"].str.replace('$','').str.replace(',','').astype(int)
autos["odometer"] = autos["odometer"].str.replace('km','').str.replace(',','').astype(int)
#print(autos["price"])
#print(autos["odometer"])
```


```python
autos.rename(columns={'odometer' : 'odometer_km'}, inplace=True)
```

## Exploring odometer and price columns


```python
# Odometer:
autos["odometer_km"].unique().shape
```




    (13,)




```python
autos["odometer_km"].describe()
```




    count     50000.000000
    mean     125732.700000
    std       40042.211706
    min        5000.000000
    25%      125000.000000
    50%      150000.000000
    75%      150000.000000
    max      150000.000000
    Name: odometer_km, dtype: float64




```python
autos["odometer_km"].value_counts()
```




    150000    32424
    125000     5170
    100000     2169
    90000      1757
    80000      1436
    70000      1230
    60000      1164
    50000      1027
    5000        967
    40000       819
    30000       789
    20000       784
    10000       264
    Name: odometer_km, dtype: int64




```python
autos["odometer_km"].sort_index(ascending=True)
```




    0        150000
    1        150000
    2         70000
    3         70000
    4        150000
              ...  
    49995    100000
    49996    150000
    49997      5000
    49998     40000
    49999    150000
    Name: odometer_km, Length: 50000, dtype: int64




```python
autos[autos["odometer_km"].between(5000, 15000)]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date_crawled</th>
      <th>name</th>
      <th>seller</th>
      <th>offer_type</th>
      <th>price</th>
      <th>abtest</th>
      <th>vehicle_type</th>
      <th>registration_year</th>
      <th>gearbox</th>
      <th>power_PS</th>
      <th>model</th>
      <th>odometer_km</th>
      <th>registration_month</th>
      <th>fuel_type</th>
      <th>brand</th>
      <th>unrepaired_damage</th>
      <th>ad_created</th>
      <th>nr_pictures</th>
      <th>postal_code</th>
      <th>last_seen</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>22</th>
      <td>2016-03-28 20:50:54</td>
      <td>MINI_Cooper_S_Cabrio</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>25450</td>
      <td>control</td>
      <td>cabrio</td>
      <td>2015</td>
      <td>manuell</td>
      <td>184</td>
      <td>cooper</td>
      <td>10000</td>
      <td>1</td>
      <td>benzin</td>
      <td>mini</td>
      <td>nein</td>
      <td>2016-03-28 00:00:00</td>
      <td>0</td>
      <td>44789</td>
      <td>2016-04-01 06:45:30</td>
    </tr>
    <tr>
      <th>52</th>
      <td>2016-03-25 18:50:03</td>
      <td>Senator_A_3.0E_Karosserie_restauriert_m._viele...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>3500</td>
      <td>test</td>
      <td>limousine</td>
      <td>1985</td>
      <td>NaN</td>
      <td>0</td>
      <td>andere</td>
      <td>5000</td>
      <td>0</td>
      <td>benzin</td>
      <td>opel</td>
      <td>nein</td>
      <td>2016-03-25 00:00:00</td>
      <td>0</td>
      <td>63500</td>
      <td>2016-04-07 00:46:00</td>
    </tr>
    <tr>
      <th>71</th>
      <td>2016-03-28 19:39:35</td>
      <td>Suche_Opel_Astra_F__Corsa_oder_Kadett_E_mit_Re...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>0</td>
      <td>control</td>
      <td>NaN</td>
      <td>1990</td>
      <td>manuell</td>
      <td>0</td>
      <td>NaN</td>
      <td>5000</td>
      <td>0</td>
      <td>benzin</td>
      <td>opel</td>
      <td>NaN</td>
      <td>2016-03-28 00:00:00</td>
      <td>0</td>
      <td>4552</td>
      <td>2016-04-07 01:45:48</td>
    </tr>
    <tr>
      <th>76</th>
      <td>2016-03-22 14:52:57</td>
      <td>BMW_318i_neustes_Model_0Km</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>31999</td>
      <td>control</td>
      <td>limousine</td>
      <td>2016</td>
      <td>manuell</td>
      <td>136</td>
      <td>3er</td>
      <td>5000</td>
      <td>2</td>
      <td>benzin</td>
      <td>bmw</td>
      <td>NaN</td>
      <td>2016-03-22 00:00:00</td>
      <td>0</td>
      <td>45149</td>
      <td>2016-04-06 05:15:42</td>
    </tr>
    <tr>
      <th>102</th>
      <td>2016-03-22 11:57:49</td>
      <td>Ford_Ka_dunkel_blau</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>320</td>
      <td>control</td>
      <td>kleinwagen</td>
      <td>2004</td>
      <td>manuell</td>
      <td>0</td>
      <td>ka</td>
      <td>5000</td>
      <td>6</td>
      <td>benzin</td>
      <td>ford</td>
      <td>ja</td>
      <td>2016-03-22 00:00:00</td>
      <td>0</td>
      <td>24109</td>
      <td>2016-04-02 01:47:21</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>49845</th>
      <td>2016-03-21 00:50:15</td>
      <td>Schlachte_VW_Sharan_vr6_Automatik___no_GTI_16V...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>1</td>
      <td>test</td>
      <td>NaN</td>
      <td>2000</td>
      <td>automatik</td>
      <td>174</td>
      <td>sharan</td>
      <td>5000</td>
      <td>6</td>
      <td>benzin</td>
      <td>volkswagen</td>
      <td>nein</td>
      <td>2016-03-20 00:00:00</td>
      <td>0</td>
      <td>14621</td>
      <td>2016-04-05 21:16:16</td>
    </tr>
    <tr>
      <th>49865</th>
      <td>2016-03-10 01:37:42</td>
      <td>Mercedes_CLK_270_CDI_TÜV_bis_11_2017_klimaauto...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>5200</td>
      <td>test</td>
      <td>coupe</td>
      <td>2004</td>
      <td>automatik</td>
      <td>0</td>
      <td>clk</td>
      <td>5000</td>
      <td>12</td>
      <td>diesel</td>
      <td>mercedes_benz</td>
      <td>NaN</td>
      <td>2016-03-09 00:00:00</td>
      <td>0</td>
      <td>80686</td>
      <td>2016-03-31 07:46:31</td>
    </tr>
    <tr>
      <th>49910</th>
      <td>2016-04-03 21:39:15</td>
      <td>Schoener_fast_neuer_Opel_Mokka_in_Zell_Mosel_m...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>22200</td>
      <td>test</td>
      <td>NaN</td>
      <td>9000</td>
      <td>automatik</td>
      <td>140</td>
      <td>andere</td>
      <td>10000</td>
      <td>3</td>
      <td>benzin</td>
      <td>opel</td>
      <td>NaN</td>
      <td>2016-04-03 00:00:00</td>
      <td>0</td>
      <td>56856</td>
      <td>2016-04-05 22:18:26</td>
    </tr>
    <tr>
      <th>49941</th>
      <td>2016-03-15 00:53:25</td>
      <td>Maserati_Ghibli_Diesel_Automatik</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>62000</td>
      <td>test</td>
      <td>limousine</td>
      <td>2015</td>
      <td>automatik</td>
      <td>275</td>
      <td>NaN</td>
      <td>10000</td>
      <td>8</td>
      <td>diesel</td>
      <td>sonstige_autos</td>
      <td>nein</td>
      <td>2016-03-14 00:00:00</td>
      <td>0</td>
      <td>10179</td>
      <td>2016-03-30 23:17:48</td>
    </tr>
    <tr>
      <th>49997</th>
      <td>2016-04-02 14:44:48</td>
      <td>Fiat_500_C_1.2_Dualogic_Lounge</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>13200</td>
      <td>test</td>
      <td>cabrio</td>
      <td>2014</td>
      <td>automatik</td>
      <td>69</td>
      <td>500</td>
      <td>5000</td>
      <td>11</td>
      <td>benzin</td>
      <td>fiat</td>
      <td>nein</td>
      <td>2016-04-02 00:00:00</td>
      <td>0</td>
      <td>73430</td>
      <td>2016-04-04 11:47:27</td>
    </tr>
  </tbody>
</table>
<p>1231 rows × 20 columns</p>
</div>




```python
#Price:

autos["price"].unique().shape
```




    (2357,)




```python
autos["price"].describe()
```




    count    5.000000e+04
    mean     9.840044e+03
    std      4.811044e+05
    min      0.000000e+00
    25%      1.100000e+03
    50%      2.950000e+03
    75%      7.200000e+03
    max      1.000000e+08
    Name: price, dtype: float64




```python
autos[autos["price"]==autos["price"].max()]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date_crawled</th>
      <th>name</th>
      <th>seller</th>
      <th>offer_type</th>
      <th>price</th>
      <th>abtest</th>
      <th>vehicle_type</th>
      <th>registration_year</th>
      <th>gearbox</th>
      <th>power_PS</th>
      <th>model</th>
      <th>odometer_km</th>
      <th>registration_month</th>
      <th>fuel_type</th>
      <th>brand</th>
      <th>unrepaired_damage</th>
      <th>ad_created</th>
      <th>nr_pictures</th>
      <th>postal_code</th>
      <th>last_seen</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39705</th>
      <td>2016-03-22 14:58:27</td>
      <td>Tausch_gegen_gleichwertiges</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>99999999</td>
      <td>control</td>
      <td>limousine</td>
      <td>1999</td>
      <td>automatik</td>
      <td>224</td>
      <td>s_klasse</td>
      <td>150000</td>
      <td>9</td>
      <td>benzin</td>
      <td>mercedes_benz</td>
      <td>NaN</td>
      <td>2016-03-22 00:00:00</td>
      <td>0</td>
      <td>73525</td>
      <td>2016-04-06 05:15:30</td>
    </tr>
  </tbody>
</table>
</div>




```python
autos["price"].sort_index(ascending=True)
```




    0         5000
    1         8500
    2         8990
    3         4350
    4         1350
             ...  
    49995    24900
    49996     1980
    49997    13200
    49998    22900
    49999     1250
    Name: price, Length: 50000, dtype: int64




```python
autos=autos[autos["price"].between(0, 99999998)]
```

### Observations

Removed an outlier in price because it was a single high value, far away from the top 75% of values.

## Understanding date range and data covers


```python
autos['date_crawled'].str[:10].value_counts(normalize=True, dropna = False).sort_index()
```




    2016-03-05    0.025381
    2016-03-06    0.013940
    2016-03-07    0.035961
    2016-03-08    0.033301
    2016-03-09    0.033221
    2016-03-10    0.032121
    2016-03-11    0.032481
    2016-03-12    0.036781
    2016-03-13    0.015560
    2016-03-14    0.036621
    2016-03-15    0.033981
    2016-03-16    0.029501
    2016-03-17    0.031521
    2016-03-18    0.013060
    2016-03-19    0.034901
    2016-03-20    0.037821
    2016-03-21    0.037521
    2016-03-22    0.032921
    2016-03-23    0.032381
    2016-03-24    0.029101
    2016-03-25    0.031741
    2016-03-26    0.032481
    2016-03-27    0.031041
    2016-03-28    0.034841
    2016-03-29    0.034181
    2016-03-30    0.033621
    2016-03-31    0.031921
    2016-04-01    0.033801
    2016-04-02    0.035401
    2016-04-03    0.038681
    2016-04-04    0.036521
    2016-04-05    0.013100
    2016-04-06    0.003180
    2016-04-07    0.001420
    Name: date_crawled, dtype: float64



### Observations
Appears there are generally fewer dates crawled closer to the end of tyhe time rsange, but mostly around 3% each.


```python
autos['ad_created'].str[:10].value_counts(normalize=True, dropna = False).sort_index()
```




    2015-06-11    0.000020
    2015-08-10    0.000020
    2015-09-09    0.000020
    2015-11-10    0.000020
    2015-12-05    0.000020
                    ...   
    2016-04-03    0.038921
    2016-04-04    0.036881
    2016-04-05    0.011840
    2016-04-06    0.003260
    2016-04-07    0.001280
    Name: ad_created, Length: 76, dtype: float64



### Observations
Appears there are a lot of different dates ads were created.


```python
autos['last_seen'].str[:10].value_counts(normalize=True, dropna = False).sort_index()
```




    2016-03-05    0.001080
    2016-03-06    0.004420
    2016-03-07    0.005360
    2016-03-08    0.007600
    2016-03-09    0.009860
    2016-03-10    0.010760
    2016-03-11    0.012520
    2016-03-12    0.023820
    2016-03-13    0.008980
    2016-03-14    0.012800
    2016-03-15    0.015880
    2016-03-16    0.016440
    2016-03-17    0.027921
    2016-03-18    0.007420
    2016-03-19    0.015740
    2016-03-20    0.020700
    2016-03-21    0.020740
    2016-03-22    0.021580
    2016-03-23    0.018580
    2016-03-24    0.019560
    2016-03-25    0.019200
    2016-03-26    0.016960
    2016-03-27    0.016020
    2016-03-28    0.020860
    2016-03-29    0.022340
    2016-03-30    0.024840
    2016-03-31    0.023840
    2016-04-01    0.023100
    2016-04-02    0.024900
    2016-04-03    0.025361
    2016-04-04    0.024620
    2016-04-05    0.124282
    2016-04-06    0.220984
    2016-04-07    0.130923
    Name: last_seen, dtype: float64



### Observations
All autos are last seen in March and April 2016, increasing over time.


```python
autos["registration_year"].describe()
```




    count    49999.000000
    mean      2005.073401
    std        105.713866
    min       1000.000000
    25%       1999.000000
    50%       2003.000000
    75%       2008.000000
    max       9999.000000
    Name: registration_year, dtype: float64



### Observations
The average registration year is 2005. The standard deviation looks high, 106 years. There aren't cars I am aware of that could be registered in the year 1000 or the future, so there are probably typos in a rows. 

It is reasonable to remove cars outside of the range 1900 to 2016 (when the dataset ends):


```python
autos = autos[autos["registration_year"].between(1900,2016)]
```


```python
autos["registration_year"].value_counts(normalize=True).sort_index()
```




    1910    0.000187
    1927    0.000021
    1929    0.000021
    1931    0.000021
    1934    0.000042
              ...   
    2012    0.027547
    2013    0.016782
    2014    0.013867
    2015    0.008308
    2016    0.027401
    Name: registration_year, Length: 78, dtype: float64




```python
# autos["registration_year"].describe()
autos["registration_year"].value_counts(normalize=True)
```




    2000    0.069836
    2005    0.062777
    1999    0.062444
    2004    0.056989
    2003    0.056781
              ...   
    1939    0.000021
    1927    0.000021
    1929    0.000021
    1948    0.000021
    1952    0.000021
    Name: registration_year, Length: 78, dtype: float64



### Observations  

This looks better. There is a higher percentage of cars registered at later dates, all within a reasonable time range.

## Exploring Brands


```python
autos["brand"].unique()
```




    array(['peugeot', 'bmw', 'volkswagen', 'smart', 'ford', 'chrysler',
           'seat', 'renault', 'mercedes_benz', 'audi', 'sonstige_autos',
           'opel', 'mazda', 'porsche', 'mini', 'toyota', 'dacia', 'nissan',
           'jeep', 'saab', 'volvo', 'mitsubishi', 'jaguar', 'fiat', 'skoda',
           'subaru', 'kia', 'citroen', 'chevrolet', 'hyundai', 'honda',
           'daewoo', 'suzuki', 'trabant', 'land_rover', 'alfa_romeo', 'lada',
           'rover', 'daihatsu', 'lancia'], dtype=object)




```python
autos["brand"].value_counts()
```




    volkswagen        10188
    bmw                5284
    opel               5195
    mercedes_benz      4579
    audi               4149
    ford               3352
    renault            2274
    peugeot            1418
    fiat               1242
    seat                873
    skoda               770
    mazda               727
    nissan              725
    citroen             669
    smart               668
    toyota              599
    sonstige_autos      526
    hyundai             473
    volvo               444
    mini                415
    mitsubishi          391
    honda               377
    kia                 341
    alfa_romeo          318
    porsche             293
    suzuki              284
    chevrolet           274
    chrysler            176
    dacia               123
    daihatsu            123
    jeep                108
    subaru              105
    land_rover           98
    saab                 77
    jaguar               76
    trabant              75
    daewoo               72
    rover                65
    lancia               52
    lada                 29
    Name: brand, dtype: int64




```python
autos["brand"].value_counts(normalize=True)
```




    volkswagen        0.212131
    bmw               0.110021
    opel              0.108168
    mercedes_benz     0.095342
    audi              0.086389
    ford              0.069794
    renault           0.047348
    peugeot           0.029525
    fiat              0.025860
    seat              0.018177
    skoda             0.016033
    mazda             0.015137
    nissan            0.015096
    citroen           0.013930
    smart             0.013909
    toyota            0.012472
    sonstige_autos    0.010952
    hyundai           0.009849
    volvo             0.009245
    mini              0.008641
    mitsubishi        0.008141
    honda             0.007850
    kia               0.007100
    alfa_romeo        0.006621
    porsche           0.006101
    suzuki            0.005913
    chevrolet         0.005705
    chrysler          0.003665
    dacia             0.002561
    daihatsu          0.002561
    jeep              0.002249
    subaru            0.002186
    land_rover        0.002041
    saab              0.001603
    jaguar            0.001582
    trabant           0.001562
    daewoo            0.001499
    rover             0.001353
    lancia            0.001083
    lada              0.000604
    Name: brand, dtype: float64




```python
autos["brand"].value_counts(normalize=True)>.05
```




    volkswagen         True
    bmw                True
    opel               True
    mercedes_benz      True
    audi               True
    ford               True
    renault           False
    peugeot           False
    fiat              False
    seat              False
    skoda             False
    mazda             False
    nissan            False
    citroen           False
    smart             False
    toyota            False
    sonstige_autos    False
    hyundai           False
    volvo             False
    mini              False
    mitsubishi        False
    honda             False
    kia               False
    alfa_romeo        False
    porsche           False
    suzuki            False
    chevrolet         False
    chrysler          False
    dacia             False
    daihatsu          False
    jeep              False
    subaru            False
    land_rover        False
    saab              False
    jaguar            False
    trabant           False
    daewoo            False
    rover             False
    lancia            False
    lada              False
    Name: brand, dtype: bool




```python
brand_list = []

# from this source: https://www.geeksforgeeks.org/how-to-extract-the-value-names-and-counts-from-value_counts-in-pandas/
for idx, name in enumerate(autos["brand"].value_counts(normalize=True).index.tolist()):
    if autos["brand"].value_counts(normalize=True)[idx]>.05:
        brand_list.append(name)
        #print(autos['brand'].value_counts(normalize=True)[idx]) 
    

print(brand_list)
```

    ['volkswagen', 'bmw', 'opel', 'mercedes_benz', 'audi', 'ford']


### Explanation:

I am choosing to explore (aggregate on) the top 5% of brands, which I made into a list above. In the following code, I will find the mean price of each brand in the top 5% of brands.


```python
brand_mean_prices_dictionary = {}

for brand in brand_list:
    auto_filter = autos[autos["brand"]==brand]
    brand_mean_prices_dictionary[brand] = auto_filter["price"].mean()

print(brand_mean_prices_dictionary)
```

    {'volkswagen': 6516.457597173145, 'bmw': 8334.645155185466, 'opel': 5252.61655437921, 'mercedes_benz': 8485.239571958942, 'audi': 9093.65003615329, 'ford': 7263.015811455847}


### Pandas Series and Dataframe Constructors

These constructors can form pandas series and dataframes from regular dictionaries.


```python
bmp_series = pd.Series(brand_mean_prices_dictionary)
print(bmp_series)
```

    volkswagen       6516.457597
    bmw              8334.645155
    opel             5252.616554
    mercedes_benz    8485.239572
    audi             9093.650036
    ford             7263.015811
    dtype: float64



```python
brand_mean_odometer_dictionary = {}

for brand in brand_list:
    auto_filter = autos[autos["brand"]==brand]
    brand_mean_odometer_dictionary[brand] = auto_filter["odometer_km"].mean()

print(brand_mean_odometer_dictionary)
```

    {'volkswagen': 128730.36906164115, 'bmw': 132434.70855412565, 'opel': 129227.14148219442, 'mercedes_benz': 130856.0821139987, 'audi': 129287.78018799711, 'ford': 124046.83770883054}



```python
bmo_series = pd.Series(brand_mean_odometer_dictionary)
print(bmo_series)
```

    volkswagen       128730.369062
    bmw              132434.708554
    opel             129227.141482
    mercedes_benz    130856.082114
    audi             129287.780188
    ford             124046.837709
    dtype: float64



```python
brand_price_km_dataframe = pd.DataFrame(bmp_series, columns = ["mean_price"])
print(brand_price_km_dataframe)
```

                    mean_price
    volkswagen     6516.457597
    bmw            8334.645155
    opel           5252.616554
    mercedes_benz  8485.239572
    audi           9093.650036
    ford           7263.015811



```python
brand_price_km_dataframe["mean_km"] = bmo_series
print(brand_price_km_dataframe)
```

                    mean_price        mean_km
    volkswagen     6516.457597  128730.369062
    bmw            8334.645155  132434.708554
    opel           5252.616554  129227.141482
    mercedes_benz  8485.239572  130856.082114
    audi           9093.650036  129287.780188
    ford           7263.015811  124046.837709



```python
print(brand_price_km_dataframe.sort_values(by=['mean_price'], ascending=False))
```

                    mean_price        mean_km
    audi           9093.650036  129287.780188
    mercedes_benz  8485.239572  130856.082114
    bmw            8334.645155  132434.708554
    ford           7263.015811  124046.837709
    volkswagen     6516.457597  128730.369062
    opel           5252.616554  129227.141482


### Observations
The final dataframe above displays the mean price and kilometer reading of each of the top 20% of registered cars. It is sorted by mean price, from highest to lowest. Audi was the highest priced car on average, and so on. The mileage is not that different between the automobiles, which means this factor probably didn't affect the price as much as brand.


## Translating German to English

There are a number of columns with German terms. The following exercise will use a mapping dictionary to quickly translate one of the columns to English.


```python
autos["vehicle_type"].unique()
```




    array(['bus', 'limousine', 'kleinwagen', 'kombi', nan, 'coupe', 'suv',
           'cabrio', 'andere'], dtype=object)




```python
mapping_dict = {
    "bus": "bus",
    "limousine" :"limousine",
    "kleinwagen" : "compact car",
    "kombi" : "station wagon",
    "cabrio" : "convertible",
    "andere": "other",
    "compact car" : "compact car",
    "station wagon": "station wagon",
    "convertible": "convertible",
    "other" : "other"
}

autos["vehicle_type"] = autos["vehicle_type"].map(mapping_dict)
print(autos["vehicle_type"].unique())
```

    ['bus' 'limousine' 'compact car' 'station wagon' nan 'convertible' 'other']


The reason some of the translated words were entered again as keys is to ensure these names don't get removed in case the command is run a second time in a row.
