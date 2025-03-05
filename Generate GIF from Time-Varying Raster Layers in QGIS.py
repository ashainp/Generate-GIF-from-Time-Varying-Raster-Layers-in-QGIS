from qgis.core import QgsProject
from PIL import Image
from PyQt5.QtWidgets import QApplication
import os
import re
import time

# === USER CONFIGURATIONS ===
output_gif_path = "C:/Users/enoks/Desktop/test qgis/TIME/animation.gif"
frame_duration = 500  # milliseconds
aerial_layer_name = "Orthophoto"  # Change if using another basemap
pattern = r"DEPTH2D_(\d+)m_raster"  # Change naming pattern if needed

# === Collect Rasters ===
raster_layers = []
layer_tree = QgsProject.instance().layerTreeRoot()

for layer in QgsProject.instance().mapLayers().values():
    match = re.match(pattern, layer.name())
    if match:
        time_value = int(match.group(1))  # Extract numerical value
        raster_layers.append((time_value, layer))
raster_layers.sort()  # Sort by time (ascending order)

if not raster_layers:
    print("❌ No valid rasters found! Check layer names.")
    exit()

# === Identify Aerial Imagery Layer ===
aerial_layer = QgsProject.instance().mapLayersByName(aerial_layer_name)
if aerial_layer:
    aerial_layer = aerial_layer[0]  # Use the first matching layer

# === Frame Capture Setup ===
frame_folder = os.path.join(os.path.dirname(output_gif_path), "frames")
os.makedirs(frame_folder, exist_ok=True)
frame_files = []

# === Toggle Rasters and Capture Frames ===
for i, (time_value, layer) in enumerate(raster_layers):
    print(f"🔄 Processing Frame {i+1}: {layer.name()}")

    # Turn OFF all rasters first
    for _, lyr in raster_layers:
        layer_node = layer_tree.findLayer(lyr.id())
        if layer_node:
            layer_node.setItemVisibilityChecked(False)

    # Turn ON the current raster
    layer_node = layer_tree.findLayer(layer.id())
    if layer_node:
        layer_node.setItemVisibilityChecked(True)

    # Keep Aerial Imagery Always Visible
    if aerial_layer:
        aerial_node = layer_tree.findLayer(aerial_layer.id())
        if aerial_node:
            aerial_node.setItemVisibilityChecked(True)

    # 🔄 **Force QGIS to process UI updates before capture**
    QApplication.processEvents()
    time.sleep(1.5)  # Ensure rendering before capturing frame

    # Force full refresh
    iface.mapCanvas().refreshAllLayers()
    iface.mapCanvas().refresh()
    QApplication.processEvents()
    time.sleep(1.5)  # Final delay to confirm rendering

    # 📸 Capture frame
    frame_path = os.path.join(frame_folder, f"frame_{i:02d}.png")
    iface.mapCanvas().saveAsImage(frame_path)
    frame_files.append(frame_path)
    print(f"✅ Captured: {frame_path}")

# === Create GIF ===
if frames := [Image.open(frame) for frame in frame_files]:
    frames[0].save(output_gif_path, save_all=True, append_images=frames[1:], duration=frame_duration, loop=0)
    print(f"\n🎉 GIF successfully saved at: {output_gif_path}")
else:
    print("❌ No frames were captured. Something went wrong.")

# === Cleanup ===
for frame in frame_files:
    os.remove(frame)
