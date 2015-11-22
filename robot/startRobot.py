# Class that represents the physical robot.
# Interacts with the RobotSupervisorInterface.

import from4tronix.pi2go


class startRobot:
    def __init__(self):
        try:
           pi2go.init() 
           print("pi2go is initialized")
        except:
            print "Error in pi2go.init():", sys.exc_info()[0]
            raise

    def __del__(self):
        try:
           from4tronics.pi2go.cleanup() 
           print("pi2go is deactivated")
        except:
            print "Error in pi2go.cleanup():", sys.exc_info()[0]
            raise




