#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class OdometryMonitor(Node):
    def __init__(self):
        super().__init__('odom_monitor')
        
        # Create subscriber: message type, topic name, callback function, queue size
        self.subscription = self.create_subscription(
            Odometry,               # Message type
            '/odom',                # Topic name
            self.odometry_callback, # Callback function
            10                      # Queue size
        )
        
        self.get_logger().info('Odometry Monitor started! Listening to /odom')
    
    def odometry_callback(self, msg):
        # Extract position
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        z = msg.pose.pose.position.z
        
        # Extract linear velocity
        vx = msg.twist.twist.linear.x
        vz = msg.twist.twist.angular.z
        
        self.get_logger().info(
            f'Position: x={x:.2f}, y={y:.2f} | Velocity: vx={vx:.2f}, vz={vz:.2f}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = OdometryMonitor()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()