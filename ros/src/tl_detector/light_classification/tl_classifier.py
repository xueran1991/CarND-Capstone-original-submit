from styx_msgs.msg import TrafficLight

class TLClassifier(object):
    def __init__(self):
        #TODO load classifier
        
        self.classes = {0: TrafficLight.RED,
                        1: TrafficLight.YELLOW,
                        2: TrafficLight.GREEN, 
                        4: TrafficLight.UNKNOWN}

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)
                uint8 UNKNOWN=4
                uint8 GREEN=2
                uint8 YELLOW=1
                uint8 RED=0    
        """
        #TODO implement light color prediction
        
        
        
        
        return TrafficLight.UNKNOWN
