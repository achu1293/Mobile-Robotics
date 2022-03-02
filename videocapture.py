from robomaster import robot
import time
from robomaster import camera

if _name_ == '_main_':

    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")

    ep_chassis = ep_robot.chassis

    '''
    x = speed in x direction( meter/second) [-3.5,3.5]
    y = speed in y direction( meter/second) [-3.5,3.5]
    z = rotation about z axis ( degree/second)[-600,600]
    '''
    ep_camera = ep_robot.camera

    print("Camera streaming started...")
    ep_camera.start_video_stream(display=True, resolution=camera.STREAM_360P)    
    
    ep_chassis.move(x=2.7, y=0, z=0, xy_speed=0.75).wait_for_completed()

    ep_chassis.move(x=0, y=0, z=45, xy_speed=1).wait_for_completed()

    ep_chassis.move(x=3, y=0, z=0, xy_speed=0.75).wait_for_completed()
    ep_chassis.move(x=0, y=-0.2, z=0, xy_speed=0.75).wait_for_completed()
    
    ep_chassis.drive_speed(x=0.3,y=0,z=-17)
    time.sleep(15)

    ep_chassis.move(x=0, y=0.5, z=0, xy_speed=0.75).wait_for_completed()
 
    ep_chassis.move(x=2, y=0, z=0, xy_speed=0.75).wait_for_completed()
    
    ep_camera.stop_video_stream()
    print("Stopped video streaming...")
    
    ep_robot.close()