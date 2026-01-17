
# TurtleBot3 Maze Simulation using ROS2 and Gazebo

This project provides a complete ROS2-based simulation environment for TurtleBot3 (Burger model) to operate inside custom-designed maze worlds using the Gazebo simulator. It is intended for robotics students, developers, and autonomous navigation enthusiasts who want to experiment with robot control, mapping, localization, and path-planning algorithms in a controlled virtual environment.

The simulation is launched using a custom ROS2 Python launch file (`maze.launch.py`) which automates the entire startup process. The launch file first sets the TurtleBot3 model to the **Burger variant**, ensuring compatibility with the simulation environment. It then loads a selected custom Gazebo world file and starts both the Gazebo server and graphical client. After initializing the simulation environment, the robot state publisher is launched to broadcast joint and TF data. Finally, the TurtleBot3 robot is spawned into the maze at a predefined position and orientation, allowing consistent testing and repeatable experiments.

---

## 🌍 Available Simulation Worlds

This project includes multiple custom Gazebo world files that can be used for different testing scenarios:

* `maze_world_1.world` – Basic maze layout for beginner navigation testing
* `maze_world_2.world` – Intermediate maze with complex turns and corridors
* `z.world` – Advanced maze environment with tighter paths and obstacle structures

You can easily switch between these worlds by modifying the world file path inside the launch file.

---



## 🛠 Technologies Used

* ROS2
* Gazebo Simulator
* TurtleBot3 Packages
* Python Launch System
* Ubuntu Linux

---

## ▶ How to Run the Simulation

1. Clone this repository into your ROS2 workspace
2. Build the workspace:

```bash
colcon build
```

3. Source the workspace:

```bash
source install/setup.bash
```

4. Launch the simulation:

```bash
ros2 launch tb3_maze_sim maze.launch.py
```

Gazebo will start automatically with the TurtleBot3 robot placed inside the selected maze world.

---


Just tell me 👍
