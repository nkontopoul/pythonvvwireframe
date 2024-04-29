import numpy as np
import visvis as vv
from pywavefront import Wavefront

# Load object (specify the local file path using a raw string)
object_file = 'https://naif.jpl.nasa.gov/pub/naif/ROSETTA/kernels/dsk/PHOBOS_M003_GAS_V01.OBJ'
obj = Wavefront(object_file, collect_faces=True)

# Get vertices and faces from the Wavefront object
vertices = np.array(obj.vertices, dtype=np.float32)  # Ensure vertices are in a NumPy array with type float32
mesh = obj.mesh_list[0]  # Assuming a single mesh in the OBJ file
faces = np.array([f[0] for f in mesh.faces], dtype=np.uint32)  # Extracting face indices, assuming they are properly indexed

# Check if faces is empty
print("Faces shape:", len(faces))
if len(faces) == 0:
    print("Error: Faces array is empty!")
    exit()

# Create a figure and a 3D axis
app = vv.use()
fig = vv.figure()
a3 = vv.gca()

# Create a mesh
surface = vv.mesh(vertices, faces)
surface.faceColor = (1, 1, 1)  # Set the color of the mesh to white





# Set up camera
a3.camera.fov = 45
a3.camera.position = (0, 0, 3)  # Position the camera in front of the object



# Rotation angle
angle = 0

# Main loop
while True:
    vv.processEvents()
    angle = (angle + 1) % 360  # Increment angle and loop from 0 to 359
    a3.camera.azimuth = angle  # Rotate the camera around the object
    # Run app
    app.Run()     

