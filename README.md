# Turtlesim
Simple project with turtle simulator, using ros2 nodes, topics, services, parameters and launch files. The master-turtle tries to catches all the other turtle that spawns within every 2 seconds. The nodes run in a endless loop and the entire simulation is run using a launch file.
The code is written in Python using Vscode.


![Screenshot 2024-06-09 210923](https://github.com/AmeyaB2005/Turtlesim/assets/146567207/374d3ac3-82a2-4f3a-aee2-c12b9baf6674)

# Setup Locally 
## Pre-requisite
* Ubuntu 22.04 LTS
* ROS2-Humble installed

### Follow the steps
1. Clone the repository.<br>


        git clone "https://github.com/lonebots/turtlesim-catch-them-all.git"

      
3. Navigate to source folder.<br>

        cd turtlesim-catch-them-all/src

5. build the packages.<br>

        colcon build

7. run the launch file.<br>

        ros2 launch turtlesim_ctall_bringup turtle_ctall_app.launch.py








# Flow of program



1. Locating random positions<br>
> random.randrange()
This function can output a random value between the range of value we give it as a input. So by using this we can locate and spawn a turtle in random positions of the turtlesim workspace.
2. Spawning new turtle<br>
>Turtle_spawn(goal,killer_name,spawn_name)
By using this function we can create a new turtle anywhere in the screen according to our inputs. The inputs are
goal = position
killer_name and spawn_name
So the turtle will be spawned at the goal position with the name of spawn_name
3. Identifying Distance<br>
>The distance between the spawned turtle and the catcher turtle is found using the function
>euclidean_distance(self, goal_pose)
4. Equating the distance<br>
>Equating the distance between the turtles with the tolerance level, the linear and angular velocities of the turtle is changed simultaneously
>while self.euclidean_distance(goal_pose) >= float(distance_tolerance):
With that the turtle moves for catching the new turtles
5. Killing the turtle
>Turtle_kill(killer_name)
>This function is used to kill the turtle whose input parameter is the name of the turtle. Once the catcher turtle catches the newly spawned turtle, then the Turtle_Kill function is been called
>self.Turtle_kill('turtle2')
>
>



 # ROS2 Node Graph
> 
  ![Screenshot 2024-07-10 194615](https://github.com/AmeyaB2005/Turtlesim/assets/146567207/eda00f14-3956-445a-bc1d-f6be161493e1)
