from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    turtlesim_node=Node(  #name of the node

        package="turtlesim",#name of the pkg
        executable="turtlesim_node"#name of executable as per setup.py
    )
    turtle_spawner_node= Node(

        package="turtlesim_catch_them_all",
        executable="turtle_spawner",
        parameters=[
            {"spawn_frequency":0.5},
            {"turtle_name_prefix":"my_turtle"}
                    
                    
        ]
    )


    turtle_controller_node=Node(

        package="turtlesim_catch_them_all",
        executable="turtlesim_controller",
        parameters=[
            {"catch_closest_turtle_first":True}
            
                    
                    
        ]
    )



    


    #ld.add_action(turtle_spawner_node)#name of node
    ld.add_action(turtlesim_node)
    ld.add_action(turtle_spawner_node)
    ld.add_action(turtle_controller_node)
    #ld.add_action(turtle_spawner_node)
    return ld
