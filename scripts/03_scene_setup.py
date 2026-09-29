"""Step 3: build the palletizing cell with placeholder geometry."""

from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

import isaacsim.core.experimental.utils.app as app_utils
import isaacsim.core.experimental.utils.stage as stage_utils
from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
from isaacsim.core.experimental.objects import Cube, DistantLight, GroundPlane
from isaacsim.core.experimental.prims import Articulation, GeomPrim, RigidPrim
from isaacsim.storage.native import get_assets_root_path

# --- Section 2: floor, light, robot ---

KUKA_USD = get_assets_root_path() + "/Isaac/Robots_Multiphysics/Kuka/KR210_L150/kr210_l150.usda"

stage_utils.create_new_stage()

GroundPlane("/World/GroundPlane", positions=[0, 0, 0])

light = DistantLight("/World/DistantLight")
light.set_intensities(300)

stage_utils.add_reference_to_stage(usd_path=KUKA_USD, path="/World/kuka")
robot = Articulation("/World/kuka")

# ---Section 3: materials ---

kuka_orange = PreviewSurfaceMaterial("/Visual_materials/orange")
kuka_orange.set_input_values("diffuseColor", [1.0, 0.5, 0.0])

table_gray = PreviewSurfaceMaterial("/Visual_materials/dark_grey")
table_gray.set_input_values("diffuseColor", [0.3, 0.3, 0.3])

pallet_wood = PreviewSurfaceMaterial("/Visual_materials/light_wood")
pallet_wood.set_input_values("diffuseColor", [0.8, 0.6, 0.4])

box_cardboard = PreviewSurfaceMaterial("/Visual_materials/cardboard_brawn")
box_cardboard.set_input_values("diffuseColor", [0.6, 0.45, 0.3])


# --- Final section: run the simulation ---

app_utils.play()
simulation_app.update()

while simulation_app.is_running():
    simulation_app.update()

simulation_app.close()
