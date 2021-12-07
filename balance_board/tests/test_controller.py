"""
Unittest for the board_pid controller package

Inputs
    BoardPid - calls the BoardPid class in the board_pid package

"""
import rospy
import unittest
from board_pid import BoardPid

class ControllerTest(unittest.TestCase):
    def testcontrollerforzero(self):
        """ Sets the controller gains to 0 and checks whether the package returns a 0
        """
        Kp = 0
        Ki = 0 
        Kd = 0
        target = 255
        controller = BoardPid(
            kp=Kp,
            kd=Kd,
            ki = Ki,
            target=target
        )

        value = 2
        self.assertEquals(controller.get(value),0)

    def testcontrollertargetzero(self):
        """ Tests for when target and current position is the same
            The controller should return a zero
        """
        Kp = 32
        Ki = 4
        Kd = 1
        target = 255
        controller = BoardPid(
            kp=Kp,
            kd=Kd,
            ki = Ki,
            target=target
        )

        value = 255
        self.assertEquals(controller.get(value),0)



if __name__ == "__main__":
    import rosunit
    rosunit.unitrun('balance_board', 'ControllerTest', ControllerTest)