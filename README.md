# Generate-GIF-from-Time-Varying-Raster-Layers-in-QGIS
This script automates the process of generating an animated GIF from time-varying raster layers in QGIS.   It toggles each raster layer sequentially while keeping the aerial basemap on, captures each frame, and exports the animation.

# **Generate GIF from Time-Varying Raster Layers in QGIS**

## **🌍 Overview**
This script automates the process of **generating an animated GIF from time-varying raster layers** in QGIS.  
It **toggles each raster layer sequentially** while keeping the aerial basemap on, captures each frame, and exports the animation.

---

## **🚀 Features**
✅ **Automates GIF creation** from time-varying rasters  
✅ **Customizable time steps** (e.g., 5 min, 10 min, etc.)  
✅ **Keeps aerial imagery always visible**  
✅ **Supports user-defined raster naming formats**  
✅ **Outputs GIF with custom frame duration**  

---

## **📂 Layer Organization**
To ensure the script runs properly, organize your layers as follows in QGIS:

📂 QGIS Layers Panel ├── Orthophoto (or any aerial basemap) ├── Time-Varying Depths │ ├── DEPTH2D_5m_raster │ ├── DEPTH2D_10m_raster │ ├── DEPTH2D_15m_raster │ ├── DEPTH2D_20m_raster │ ├── DEPTH2D_30m_raster ├── Data Boundaries (Optional)
