#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install numpy matplotlib rasterio pysheds


# In[1]:


## Different Code>>>>>>>>>>>>
from skimage import measure
from shapely.geometry import Polygon, mapping
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
import rasterio
from rasterio.plot import show
from pysheds.grid import Grid

# Paths
DEM_PATH = r"D:\Ishfaqul\PaperJintu\Waterhsed_using_DEMs\SrtmDEM_30m_Watershed2000\SrtmDEM_Sonitpur30m_2000_Masked.tif"
OUTPUT_PATH = r"D:\Ishfaqul\PaperWithJintu\Watershed_using_DEMs\SrtmDEM_30m_Watershed2000\Outputs"


# In[2]:


# Load DEM
grid = Grid.from_raster(DEM_PATH, data_name='dem')
dem = grid.read_raster(DEM_PATH)

# Visualize DEM
plt.figure(figsize=(10, 8))
plt.title('Digital Elevation Model')
plt.imshow(dem, extent=grid.extent, cmap='terrain')
plt.colorbar(label='Elevation (m)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Fill depressions
dem_filled = grid.fill_depressions(dem)
plt.figure(figsize=(10, 8))
plt.title('Filled DEM')
plt.imshow(dem_filled, extent=grid.extent, cmap='terrain')
plt.colorbar(label='Elevation (m)')
plt.show()

# Resolve flats
dem_flats = grid.resolve_flats(dem_filled)
plt.figure(figsize=(10, 8))
plt.title('Resolved Flats')
plt.imshow(dem_flats, extent=grid.extent, cmap='terrain')
plt.colorbar(label='Elevation (m)')
plt.show()

# Remove NoData Cells
nodata = -9999  # Or check your DEM nodata value
dem_flats[dem_flats <= nodata] = np.nan  # Mask out NoData pixels

# Flow Direction
dirmap = (64, 128, 1, 2, 4, 8, 16, 32)
fdir = grid.flowdir(dem_flats, dirmap=dirmap)
plt.figure(figsize=(10, 8))
plt.title('Flow Direction')
plt.imshow(fdir, extent=grid.extent)
plt.colorbar(label='Flow Direction')
plt.show()

# Flow Accumulation
acc = grid.accumulation(fdir, dirmap=dirmap)
plt.figure(figsize=(10, 8))
plt.title('Flow Accumulation')
plt.imshow(np.log1p(acc), extent=grid.extent, cmap='cubehelix')
plt.colorbar(label='Flow Accumulation (Log Scale)')
plt.show()


# In[ ]:


# Pour Point Coordinates
pour_point = (92.47, 26.14)
x_snap, y_snap = grid.snap_to_mask(acc > 2500000, pour_point)

# Delineate Watershed (Apply NoData Mask)
catch = grid.catchment(x=x_snap, y=y_snap, fdir=fdir, dirmap=dirmap, xytype='coordinate')
catch = np.where((catch == 1) & (~np.isnan(dem_flats)), 1, np.nan)  # Mask out NoData

# Plot Final Watershed without Holes
plt.figure(figsize=(9, 7))
plt.title('Final Watershed Without Holes')
plt.imshow(catch, extent=grid.extent, cmap='viridis', alpha=0.6)
plt.colorbar(label='Watershed')
plt.show()


# In[4]:


from skimage import measure
from shapely.geometry import Polygon, mapping
import geopandas as gpd

def raster_to_vector(raster_file, output_shapefile):
    # Read raster
    with rasterio.open(raster_file) as src:
        img = src.read(1)  # Read first band
        transform = src.transform
        
        # Extract Features
        contours = measure.find_contours(img, 0.5)  # Contours at threshold 0.5
        
        polygons = []
        for contour in contours:
            coords = [(transform * (x, y)) for y, x in contour]
            polygon = Polygon(coords)
            if polygon.is_valid:
                polygons.append(polygon)
        
        # Create GeoDataFrame
        gdf = gpd.GeoDataFrame(geometry=polygons, crs=src.crs)
        
        # Save to Shapefile
        gdf.to_file(output_shapefile)
        print(f"✅ Vector Polygon Shapefile Saved: {output_shapefile}")

# Convert Raster to Vector
raster_to_vector(OUTPUT_PATH + '\\Watershed.tif', OUTPUT_PATH + '\\Watershed.shp')


# In[ ]:




