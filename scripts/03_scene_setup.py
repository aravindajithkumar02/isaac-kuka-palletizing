"""Step 3: build the palletizing cell with placeholder geometry."""

from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

import isaacsim.core.experimental.utils.app as app_utils
import isaacsim.core.experimental.utils.stage as stage_utils
from isaacsim.core.experimental.materials import PreviewSurfaceMaterial
from isaacsim.core.experimental.objects import Cube, DistantLight, GroundPlane
from isaacsim.core.experimental.prims import Articulation, GeomPrim, RigidPrim, XformPrim
from isaacsim.storage.native import get_assets_root_path

# ---Section 1b cell layout( all values in meters)---

TABLE_SIZE = [1.2,0.8,0.8]
TABLE_POSITION = [0.0,1.6, TABLE_SIZE[2]/2]
TABLE_TOP_Z = TABLE_SIZE[2]

PALLET_SIZE = [1.2,0.8,0.15]
PALLET_POSITION = [1.6,0.0, PALLET_SIZE[2]/2]
PALLET_TOP_Z = PALLET_SIZE[2]

BOX_SIZE = 0.3
BOX_Z = TABLE_TOP_Z + BOX_SIZE/2

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
kuka_orange.set_input_values("diffuseColor", [1.0, 0.35, 0.0])

table_gray = PreviewSurfaceMaterial("/Visual_materials/dark_gray")
table_gray.set_input_values("diffuseColor", [0.3, 0.3, 0.3])

pallet_wood = PreviewSurfaceMaterial("/Visual_materials/light_wood")
pallet_wood.set_input_values("diffuseColor", [0.8, 0.6, 0.4])

box_cardboard = PreviewSurfaceMaterial("/Visual_materials/cardboard_brown")
box_cardboard.set_input_values("diffuseColor", [0.6, 0.45, 0.3])

XformPrim("/World/kuka").apply_visual_materials(kuka_orange)

# ---Section 4: pick table and pallets ---

pick_table_shape = Cube(
    paths="/World/pick_table",
    positions=TABLE_POSITION,
    sizes=1.0,
    scales=TABLE_SIZE,
)
pick_table_shape.apply_visual_materials(table_gray)
pick_table_geometry = GeomPrim(paths=pick_table_shape.paths, apply_collision_apis=True)

pallets_shape = Cube(
    paths="/World/pallets",
    positions=PALLET_POSITION,
    sizes=1.0,
    scales=PALLET_SIZE,
)
pallets_shape.apply_visual_materials(pallet_wood)
pallets_geometry = GeomPrim(paths=pallets_shape.paths, apply_collision_apis=True)

# ---Section 5: boxes ---

box_1_shape = Cube(
  paths="/World/box_1",
  positions=[-0.25,1.38,BOX_Z],
  sizes=1.0,
  scales=[BOX_SIZE, BOX_SIZE, BOX_SIZE],
)
box_1_shape.apply_visual_materials(box_cardboard)
box_1 = RigidPrim(paths=box_1_shape.paths)
box_1_geometry = GeomPrim(paths=box_1_shape.paths, apply_collision_apis=True)

box_2_shape = Cube(
  paths="/World/box_2",
  positions=[0.25,1.38,BOX_Z],
  sizes=1.0,
  scales=[BOX_SIZE, BOX_SIZE, BOX_SIZE],
)
box_2_shape.apply_visual_materials(box_cardboard)
box_2 = RigidPrim(paths=box_2_shape.paths)
box_2_geometry = GeomPrim(paths=box_2_shape.paths, apply_collision_apis=True)

box_3_shape = Cube(
  paths="/World/box_3",
  positions=[-0.25,1.82,BOX_Z],
  sizes=1.0,
  scales=[BOX_SIZE, BOX_SIZE, BOX_SIZE],
)
box_3_shape.apply_visual_materials(box_cardboard)
box_3 = RigidPrim(paths=box_3_shape.paths)
box_3_geometry = GeomPrim(paths=box_3_shape.paths, apply_collision_apis=True)

box_4_shape = Cube(
  paths="/World/box_4",
  positions=[0.25,1.82,BOX_Z],
  sizes=1.0,
  scales=[BOX_SIZE, BOX_SIZE, BOX_SIZE],
)
box_4_shape.apply_visual_materials(box_cardboard)
box_4 = RigidPrim(paths=box_4_shape.paths)
box_4_geometry = GeomPrim(paths=box_4_shape.paths, apply_collision_apis=True)



# --- Final section: run the simulation ---

app_utils.play()
simulation_app.update()

while simulation_app.is_running():
    simulation_app.update()

simulation_app.close()
