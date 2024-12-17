import carla
import cv2
import pygame

from CARLA.BasicAgent import BasicAgent
from CARLA.World import World
from Controls.KeyboardControl import KeyboardControl
from Detections.DetectionProcessor import DetectionProcessor
from Utils.HUD import HUD


class Simulation:
    def __init__(self, args):
        self.args = args
        self.client = None
        self.traffic_manager = None
        self.sim_world = None
        self.display = None
        self.hud = None
        self.world = None
        self.agent = None
        self.controller = None

    def initialize(self):
        """Initialize the simulation environment."""
        pygame.init()
        pygame.font.init()
        
        self.client = carla.Client(self.args.host, self.args.port)
        self.client.set_timeout(60.0)

        self.traffic_manager = self.client.get_trafficmanager()
        self.sim_world = self.client.get_world()

        if self.args.sync:
            self._configure_synchronous_mode()

        self.display = pygame.display.set_mode(
            (self.args.width, self.args.height),
            pygame.HWSURFACE | pygame.DOUBLEBUF)

        self.hud = HUD(self.args.width, self.args.height)
        self.hud.analysis.set_initial_time()
        self.world = World(self.client.get_world(), self.hud, self.args)

        self.agent = BasicAgent(self.world.player, self.args)
        self.agent.follow_speed_limits(False)
        self.agent.set_speed(37)

        self.controller = KeyboardControl(self.world)
        self._set_initial_destination()

    def _configure_synchronous_mode(self):
        """Configure the world and traffic manager for synchronous mode."""
        settings = self.sim_world.get_settings()
        settings.synchronous_mode = True
        settings.fixed_delta_seconds = 0.05
        self.sim_world.apply_settings(settings)
        self.traffic_manager.set_synchronous_mode(True)

    def _set_initial_destination(self):
        """Set the agent's initial destination."""
        spawn_points = self.world.map.get_spawn_points()
        destination = spawn_points[108].location
        self.agent.set_destination(destination)

    def cleanup(self):
        """Clean up resources at the end of the simulation."""
        self.hud.analysis.set_final_time()
        if self.world is not None:
            settings = self.world.world.get_settings()
            settings.synchronous_mode = False
            settings.fixed_delta_seconds = None
            self.world.world.apply_settings(settings)
            self.traffic_manager.set_synchronous_mode(False)
            self.world.destroy()
            self.hud.analysis.save_data_analytics()
        pygame.quit()
    def run(self):
        """Main simulation loop."""
        clock = pygame.time.Clock()
        try:
            while True:
                clock.tick()
                self._tick_world()
                if self.controller.parse_events():
                    break

                self.world.tick(clock)
                self.world.render(self.display)

                view = self._capture_frame()
                DetectionProcessor.process(self.agent, self.hud, view)

                cv2.imshow("CARLA Simulation", view)
                cv2.waitKey(1)
                pygame.display.flip()

                if self.agent.done():
                    if self.args.loop:
                        self._loop_agent()
                    else:
                        print("The target has been reached, stopping the simulation")
                        break

                control = self.agent.run_step()
                control.manual_gear_shift = False
                self.world.player.apply_control(control)
        finally:
            self.cleanup()

    def _tick_world(self):
        """Tick the world for synchronous or asynchronous mode."""
        if self.args.sync:
            self.world.world.tick()
        else:
            self.world.world.wait_for_tick()

    def _capture_frame(self):
        """Capture the current frame from the display."""
        view = pygame.surfarray.array3d(self.display)
        view = view.transpose([1, 0, 2])
        return cv2.cvtColor(view, cv2.COLOR_RGB2BGR)

    def _loop_agent(self):
        """Reset the agent destination for looping behavior."""
        spawn_points = self.world.map.get_spawn_points()
        self.agent.set_destination(random.choice(spawn_points).location)
        self.world.hud.notification("Target reached", seconds=4.0)
        print("The target has been reached, searching for another target")