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

- **Ensure that the aerial imagery is loaded before running the script.**  
- **Rasters should be named in ascending order** for correct animation sequencing.  

---

## **⚙️ Installation & Dependencies**
### **🛠 Required Libraries**
Ensure you have the following Python libraries installed in QGIS:
```sh
pip install pillow

Or in Python console

---

import pip
pip.main(['install', 'pillow'])

## **🖥 User Inputs & Customization**
Modify these variables in the script to fit your project:

| **Feature**             | **How to Modify** | **Example** |
|-------------------------|------------------|-------------|
| **Aerial Imagery Name** | Change `aerial_layer_name` | `"Esri World Imagery"` |
| **Raster Naming Format** | Modify `pattern` regex | `"VEL_(\d+)m_ras"` |
| **Frame Duration (ms)** | Change `frame_duration = 500` | `frame_duration = 750` |
| **Output Folder** | Set `output_gif_path` | `"C:/Users/yourname/Desktop/animation.gif"` |

---

## **🛠 Troubleshooting & Common Issues**
| **Issue** | **Possible Cause & Solution** |
|-----------|------------------------------|
| **No rasters found** | Check that raster layers are loaded and match the naming pattern. |
| **GIF only shows aerial imagery** | The script isn't toggling layers properly. Try restarting QGIS and running again. |
| **Frames not capturing correctly** | Ensure that `iface.mapCanvas().refreshAllLayers()` is executing before frame capture. |
| **Incorrect ordering in GIF** | Ensure raster names contain time values in ascending order. The script sorts them automatically. |
| **QGIS crashes or hangs** | Try reducing the sleep delay (`time.sleep(1.5)`) to `time.sleep(1.0)`. |
| **GIF is too fast or too slow** | Adjust `frame_duration` (e.g., `frame_duration = 1000` for 1s per frame). |

---

## **📌 How It Works**
1. **Identifies all raster layers** that match the naming format (`DEPTH2D_Xm_raster`).  
2. **Sorts the layers** by time value (e.g., `5m → 10m → 15m`).  
3. **Ensures the aerial imagery layer stays on** at all times.  
4. **Toggles each raster layer on/off**, capturing a frame at each step.  
5. **Processes UI events to ensure the correct layer is displayed before capturing**.  
6. **Compiles the frames into a smooth GIF** using the specified frame duration.  

---

## **🌟 Example Use Cases**
🔹 **Flood simulation visualization**  
🔹 **Time-series analysis of raster changes**  
🔹 **Hydraulic modeling animation**  
🔹 **Animated mapping for presentations**  

---


