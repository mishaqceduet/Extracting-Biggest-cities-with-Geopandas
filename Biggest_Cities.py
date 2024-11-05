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