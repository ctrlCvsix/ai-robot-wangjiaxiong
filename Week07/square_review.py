import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time


class SquareReview(Node):
    def __init__(self):
        super().__init__('square_review')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def move(self, linear_x, angular_z, duration):
        msg = Twist()
        msg.linear.x = linear_x
        msg.angular.z = angular_z

        start = time.time()
        while time.time() - start < duration:
            self.publisher.publish(msg)
            time.sleep(0.1)

        self.publisher.publish(Twist())
        time.sleep(0.3)

    def run_square(self):
        self.get_logger().info('Start square movement')

        for i in range(4):
            self.get_logger().info(f'Side {i + 1}: move forward')
            self.move(1.0, 0.0, 2.0)

            self.get_logger().info(f'Corner {i + 1}: turn left')
            self.move(0.0, 1.0, 1.57)

        self.get_logger().info('Square movement finished')


def main():
    rclpy.init()
    node = SquareReview()
    time.sleep(1)
    node.run_square()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
