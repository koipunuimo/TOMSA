from Pose import Pose
from Header import Header

class   PoseWithHeader:
    def __init__(self):
        self.header = Header()
        self.pose = Pose()
        
    def __str__(self):
        return "Header: \n " + str(self.header) + "\nPose: \n " + str(self.pose)