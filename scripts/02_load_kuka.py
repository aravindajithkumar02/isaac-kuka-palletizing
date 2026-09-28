"""step 2:load the KUKA KR210 into a lit scene."""

from isaacsim import SimulationApp
simulation_app = SimulationApp({"headless": False})
import isaacsim.core.experimental.utils.stage as stage_utils
import omni.timeline
from isaacsim.core.experimental.prims import Articulation
from isaacsim.storage.native import get_assets_root_path
KUKA_USD = get_assets_root_path() + "/Isaac/Robots_Multiphysics/Kuka/KR210_L150/kr210_l150.usda"
stage_utils.create_new_stage(template="sunlight")
stage_utils.add_reference_to_stage(usd_path=KUKA_USD, path="/World/kuka")
robot = Articulation("/World/kuka")

omni.timeline.get_timeline_interface().play()
simulation_app.update()

print("Joint names:", robot.dof_names)
print("Number of joints:", robot.num_dofs)
while simulation_app.is_running():
    simulation_app.update()

simulation_app.close()