import geopandas as gpd
import os

# Set the input file path
input_shapefile = r"D:\fiverrr\45_map_for_wall\cities\ne_10m_populated_places_simple.shp"

# Check if file exists
if not os.path.exists(input_shapefile):
    print(f"Error: File not found at {input_shapefile}")
    print("Please verify the file path and try again.")
else:
    try:
        # Print current working directory
        print(f"Current working directory: {os.getcwd()}")
        print(f"Attempting to read: {input_shapefile}")
        
        # Read the shapefile
        cities = gpd.read_file(input_shapefile)
        
        # Define the list of cities to extract
        city_names = [
            'Tokyo', 'Beijing', 'Mumbai', 'Jakarta', 'Cairo', 'Lagos', 'Johannesburg',
            'Nairobi', 'Buenos Aires', 'São Paulo', 'Santiago', 'Lima', 'New York City',
            'Toronto', 'Mexico City', 'Los Angeles', 'London', 'Berlin', 'Paris',
            'Madrid', 'Moscow', 'Canberra', 'Sydney', 'Melbourne'
        ]
        
        # Filter the cities dataframe to only include the specified cities
        selected_cities = cities[cities['name'].isin(city_names)]
        
        # Create output filename in the specified directory
        output_dir = r"D:\fiverrr\45_map_for_wall\cities"
        output_shapefile = os.path.join(output_dir, '24_Cities.shp')
        
        # Save the new shapefile
        selected_cities.to_file(output_shapefile)
        
        # Print the results
        print("\nExtracted 24 cities:")
        for idx, city in selected_cities.iterrows():
            print(f"{city['name']}: {city['pop_max']:,}")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("\nPossible solutions:")
        print("1. Verify the shapefile path is correct")
        print("2. Check if you have read permissions for the file")
        print("3. Ensure the shapefile is not corrupted")
        print("4. Verify all shapefile components (.shp, .dbf, .shx) are present")