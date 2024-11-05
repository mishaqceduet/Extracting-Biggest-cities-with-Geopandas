# Global Major Cities Dataset Processing Script

This script reads a geospatial shapefile containing data on 24 major global cities and processes it to extract and save the top 20 cities by population.

## Overview

The provided Python script utilizes the GeoPandas library to read and process a shapefile of major global cities. It checks if the shapefile exists, reads the data, sorts the cities by population, and saves the top 20 cities to a new shapefile.

## Requirements

- Python 3.x
- GeoPandas library
- A shapefile of global cities from Natural Earth Data

## Installation

To run this script, you need to have Python and the required libraries installed. You can install GeoPandas using pip:

```bash
pip install geopandas
```

## Usage

1. **Set the Input File Path**: Modify the `input_shapefile` variable to point to the location of your shapefile.

2. **Run the Script**: Execute the script to process the shapefile and output the top 20 cities by population.

## Script Details

### 1. Import Libraries
```python
import geopandas as gpd
import os
```

### 2. Set the Input File Path
Specify the path to your shapefile.
```python
input_shapefile = r"D:\fiverrr\45_map_for_wall\cities\ne_10m_populated_places_simple.shp"
```

### 3. Check if File Exists
The script verifies the existence of the input shapefile.
```python
if not os.path.exists(input_shapefile):
    print(f"Error: File not found at {input_shapefile}")
    print("Please verify the file path and try again.")
else:
```

### 4. Read and Process the Shapefile
The script reads the shapefile, sorts cities by population, and saves the top 20 cities to a new shapefile.
```python
    try:
        # Print current working directory
        print(f"Current working directory: {os.getcwd()}")
        print(f"Attempting to read: {input_shapefile}")
        
        # Read the shapefile
        cities = gpd.read_file(input_shapefile)
        
        # Sort cities by population (pop_max) in descending order and get top 20
        largest_cities = cities.sort_values('pop_max', ascending=False).head(20)
        
        # Create output filename in the specified directory
        output_dir = r"D:\fiverrr\45_map_for_wall\cities"
        output_shapefile = os.path.join(output_dir, 'top_20_cities.shp')
        
        # Save the new shapefile
        largest_cities.to_file(output_shapefile)
        
        # Print the results
        print("\nTop 20 cities by population:")
        for idx, city in largest_cities.iterrows():
            print(f"{city['name']}: {city['pop_max']:,}")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("\nPossible solutions:")
        print("1. Verify the shapefile path is correct")
        print("2. Check if you have read permissions for the file")
        print("3. Ensure the shapefile is not corrupted")
        print("4. Verify all shapefile components (.shp, .dbf, .shx) are present")
```

## Output

The script saves the top 20 cities by population to a new shapefile named `top_20_cities.shp` in the specified output directory.

## Tech Stack

- GIS
- Python
- GeoPandas

## Keywords

GIS, shapefile, cities, urban geography, global distribution, metropolitan areas, spatial data, Natural Earth, population centers

## Cities Covered

Tokyo, New York, London, Paris, Moscow, Sydney, Beijing, Mumbai, Cairo, Lagos, São Paulo, and more.

## Applications

This script is perfect for urban analysis, demographic studies, and cartographic visualization.
