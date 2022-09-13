# Settings Template for AgReFed Data-Harvester

## *Input and Output Specifications* 

### *Input File*
infile: ../testdata/Pointdata_Llara.csv

### *Output Path*
outpath: ../../dataresults/

### *Headername of Latitude in input file*
colname_lat: Lat

### *Headername of Longitude in input file*
colname_lng: Long

## *Settings for Spatial and Temporal Specifications*

### *Bounding Box as [lng_min, lat_min, lng_max, lat_max]*
target_bbox: ''

### *Select years*
target_dates:
  - 2021

### *Spatial Resolution [in arcsec]*
target_res: 6.0

## *Data Selection*

target_sources:
  ### *Satellite data from Digital Earth Australia [info](Data_Overview.md#Digital-Earth-Australia-Geoscience-Earth-Observations)*
  DEA:
  - landsat_barest_earth

  ### *National Digital Elevation Model (DEM) 1 Second [info](Data_Overview.md#National-Digital-Elevation-Model-1-Second-Hydrologically-Enforced)*
  DEM:
  - DEM
  
  ### *Landscape from SLGA [info](Data_Overview.md#Landscape-Data-SLGA)*
  Landscape:
  - Slope
  - Aspect
  - Relief_300m

  ### *Radiometric Data [info](Data_Overview.md#Radiometric-Data)*
  Radiometric:
  - radmap2019_grid_dose_terr_awags_rad_2019
  - radmap2019_grid_dose_terr_filtered_awags_rad_2019

  ### *SILO Climate Database (aggregation options: Median, Mean, Total) [info](Data_Overview.md#SILO-Climate-Database)*
  SILO:

    max_temp:
    - Median

    min_temp:
    - Median

    monthly_rain:
    - Total


  ### *Soil data from SLGA [info](Data_Overview.md#Soil-Data-3D-SLGA)
  SLGA:

   Bulk_Density:
    - 0-5cm

   Clay:
    - 0-5cm

  ### *Satellite data layers from Google Earth Engine*
  
  GEE: 

    preprocess:

      ### collection as defined in the Earth Engine Catalog
      collection: LANDSAT/LC09/C02/T1_L2

      #### if supplied, will use 'buffer' and 'bound'. else, will use bbox above
      coords: [149.769345, -30.335861]

      #### If date range is supplied, will use below. Else, will use `target_dates`
      date: 2021-01-01
      end_date: 2021-12-31

      #### circular buffer in metres
      buffer: null

      #### convert buffer into square bounding box instead
      bound: null

      #### cloud masking option
      mask_clouds: True

      #### if null, will download all available images. Else, will reduce to single

      #### composite image based on summary stat provided
      reduce: median

      #### spectral indices to calculate via Awesome Spectral Indices site
      spectral:
        - NDVI
        - NDWI
    aggregate:
      
      #### group data by period. Available: year, month, week
      frequency: year 
      #### summarise group by method
      method: mean  

    download:
      bands: 
        - NDVI
        - SR_B2
        - SR_B3
        - SR_B4
      scale: 100   # in metres
      format: tif  # available: tif, png
