import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time


class RectangleMover(Node):
    def __init__(self):
        super().__init__('rectangle_mover')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def move(self, linear_x, angular_z, duration):
        msg = Twist()
        msg.linear.x = linear_x
        msg.angular.z = angular_z

        start = time.time()
        while time.time() - start < duration:
            self.publisher.publish(msg)
            time.sleep(0.1)

        stop_msg = Twist()
        self.publisher.publish(stop_msg)
        time.sleep(0.3)

    def run_rectangle(self):
        self.get_logger().info('Start rectangle movement')

        for i in range(2):
            self.move(1.0, 0.0, 3.0)
            self.move(0.0, 1.0, 1.57)
            self.move(1.0, 0.0, 2.0)
            self.move(0.0, 1.0, 1.57)

        self.get_logger().info('Rectangle movement finished')


def main():
    rclpy.init()
    node = RectangleMover()
    time.sleep(1)
    node.run_rectangle()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
