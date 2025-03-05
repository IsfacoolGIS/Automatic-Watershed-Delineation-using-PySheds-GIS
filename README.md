# Automatic-Watershed-Delineation-using-PySheds-GIS
# Automatic Watershed Delineation using PySheds & GIS

This project demonstrates **Automatic Watershed Delineation** using **PySheds**, **WhiteboxTools**, and **Python GIS Libraries**. The watershed of **Sonitpur District, Assam** has been delineated from DEM using advanced hydrological modeling.

## 🔥 Project Overview
Watershed delineation is a crucial step in hydrological modeling and water resource management. This project automates the entire delineation process from Digital Elevation Models (DEM) using open-source Python libraries.

### Objectives:
- Automatic watershed boundary delineation
- Hydrological terrain preprocessing (Fill, Flats, Flow Direction, Flow Accumulation)
- Pour Point snapping using flow accumulation threshold
- Catchment extraction
- Raster to Vector conversion (Shapefile generation)

---

## 🚀 Technologies Used
| Library       | Purpose                 |
|--------------|------------------------|
| PySheds      | Flow Direction & Watershed Delineation |
| WhiteboxTools | Hydrological Analysis  |
| Rasterio     | DEM Handling          |
| Geopandas    | Vector Processing     |
| Matplotlib   | Data Visualization    |
| Shapely      | Geometry Manipulation |
| scikit-image | Contour Extraction    |

---

## 📌 Dataset
- **DEM Source**: SRTM 30m Digital Elevation Model (Sonitpur District, Assam)
- **Pour Point Coordinates**: Manually digitized pour point (91.9299°E, 26.2493°N)

---

## 🎯 Workflow
### 1. DEM Preprocessing
- Depression Filling
- Flat Surface Resolution
- NoData Masking

### 2. Flow Direction & Flow Accumulation
Flow directions are computed using **D8 flow algorithm** with PySheds.

### 3. Pour Point Snapping
Automatic snapping of pour point using flow accumulation threshold.

### 4. Watershed Delineation
Catchment extraction from flow direction grid.

### 5. Vector Conversion
Watershed raster is converted into **Shapefile (.shp)** using `scikit-image` and **Shapely**.

---

## 📌 Folder Structure
```bash
.
├── DEM/                          # Input DEM File
├── Outputs/                      # Watershed Output Raster & Vector
├── Code/                         # Python Scripts
└── README.md                     # Project Documentation
```

---

## 🔑 Code Highlights
```python
# Flow Direction
fdir = grid.flowdir(dem, dirmap=(64, 128, 1, 2, 4, 8, 16, 32))

# Flow Accumulation
acc = grid.accumulation(fdir)

# Watershed Delineation
catch = grid.catchment(x=x_snap, y=y_snap, fdir=fdir, dirmap=dirmap)
```

---

## 🎯 Results
| Layer                | Description          | Format |
|--------------------|-------------------|-------|
| Filled DEM         | Depression-Free DEM | TIF   |
| Flow Direction     | D8 Flow Direction | TIF   |
| Flow Accumulation  | Watershed Accumulation | TIF   |
| Watershed Boundary | Final Catchment   | SHP   |

---

## 🌍 Visualization
<div align="center">
  <img src="Outputs/Watershed_Plot.png" width="600" alt="Watershed">
</div>

---

## 📌 How to Run
1. Clone the Repository
```bash
git clone https://github.com/IsfacoolGIS/Automatic-Watershed-Delineation.git
cd Automatic-Watershed-Delineation
```

2. Install Requirements
```bash
pip install -r requirements.txt
```

3. Run the Code
```bash
python watershed_delineation.py
```

---

## 🔥 Credits
Developed by **Ishfaqul Haque**


If you found this project useful, please 🌟 star the repo and connect with me on **[LinkedIn]ishfaqul-haque-a24a61251**!


