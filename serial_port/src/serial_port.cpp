/***
 * This example expects the serial port has a loopback on it.
 *
 * Alternatively, you could use an Arduino:
 *
 * <pre>
 *  void setup() {
 *    Serial.begin(<insert your baudrate here>);
 *  }
 *
 *  void loop() {
 *    if (Serial.available()) {
 *      Serial.write(Serial.read());
 *    }
 *  }
 * </pre>
 */

#include <string>
#include <iostream>
#include <cstdio>
#include "ros/ros.h"
#include "std_msgs/String.h"

// OS Specific sleep
#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif

#include "serial/serial.h"

using std::string;
using std::exception;
using std::cout;
using std::cerr;
using std::endl;
using std::vector;

void my_sleep(unsigned long milliseconds) {
#ifdef _WIN32
      Sleep(milliseconds); // 100 ms
#else
      usleep(milliseconds*1000); // 100 ms
#endif
}

void enumerate_ports()
{
  vector<serial::PortInfo> devices_found = serial::list_ports();

  vector<serial::PortInfo>::iterator iter = devices_found.begin();

  while( iter != devices_found.end() )
  {
    serial::PortInfo device = *iter++;

    printf( "(%s, %s, %s)\n", device.port.c_str(), device.description.c_str(),
     device.hardware_id.c_str() );
  }
}

void print_usage()
{
  cerr << "Usage: test_serial {-e|<serial port address>} ";
    cerr << "<baudrate> [test string]" << endl;
}

int run(int argc, char **argv)
{
  if(argc < 2) {
    print_usage();
    return 0;
  }

  // Argument 1 is the serial port or enumerate flag
  string port(argv[1]);

  if( port == "-e" ) {
    enumerate_ports();
    return 0;
  }
  else if( argc < 3 ) {
    print_usage();
    return 1;
  }

  // Argument 2 is the baudrate
  unsigned long baud = 0;
#if defined(WIN32) && !defined(__MINGW32__)
  sscanf_s(argv[2], "%lu", &baud);
#else
  sscanf(argv[2], "%lu", &baud);
#endif

  // port, baudrate, timeout in milliseconds
  serial::Serial my_serial(port, baud, serial::Timeout::simpleTimeout(1000));

  cout << "Is the serial port open?";
  if(my_serial.isOpen())
    cout << " Yes." << endl;
  else
    cout << " No." << endl;

  // Get the Test string
  int count = 0;
  string test_string;
  if (argc == 4) {
    test_string = argv[3];
  } else {
    test_string = "Testing.";
  }

  // Test the timeout, there should be 1 second between prints
  cout << "Timeout == 1000ms, asking for 1 more byte than written." << endl;
  while (count < 10) {
    size_t bytes_wrote = my_serial.write(test_string);

    // string result = my_serial.read(test_string.length()+1);

    cout << "Iteration: " << count << ", Bytes written: "<<endl;
   /* cout << bytes_wrote << ", Bytes read: ";
    cout << result.length() << ", String read: " << result << endl;*/

    count += 1;
  }

  // Test the timeout at 250ms
  my_serial.setTimeout(serial::Timeout::max(), 250, 0, 250, 0);
  count = 0;
  cout << "Timeout == 250ms, asking for 1 more byte than written." << endl;
  while (count < 10) {
    size_t bytes_wrote = my_serial.write(test_string);

      //read the message from com1
    //    string result = my_serial.read(test_string.length()+1);

    cout << "Iteration: " << count << ", Bytes written: ";
    cout << bytes_wrote << ", Bytes read: ";
    // cout << result.length() << ", String read: " << result << endl;

    count += 1;
  }

  // Test the timeout at 250ms, but asking exactly for what was written
  count = 0;
  cout << "Timeout == 250ms, asking for exactly what was written." << endl;

  ros::init(argc,argv,"SerialPort");
  ros::NodeHandle nh;
  while (count < 10) {
    size_t bytes_wrote = my_serial.write(test_string);
    //read the message from com1
    //string result = my_serial.read(test_string.length());

    cout << "Iteration: " << count << ", Bytes written: "<<endl;
    cout << bytes_wrote << ", Bytes read: ";
    // cout << result.length() << ", String read: " << result << endl;

    count += 1;
  }

  // Test the timeout at 250ms, but asking for 1 less than what was written
  count = 0;
  cout << "Timeout == 250ms, asking for 1 less than was written." << endl;

/*  ros::Rate对象可以允许你指定自循环的频率。它会追踪记录自上一次调用Rate::sleep()后时间的流逝,并
 休眠直到一个频率周期的时间。*/
  ros::Rate loop_rate(10);

/*  roscpp会默认安装一个SIGINT句柄,它负责处理Ctrl-C键盘操作——使得ros::ok()返回FALSE。
  ros::ok()返回false,如果下列条件之一发生:
  SIGINT接收到(Ctrl-C)
  被另一同名节点踢出ROS网络
  ros::shutdown()被程序的另一部分调用
  所有的ros::NodeHandles (/NodeHandles)都已经被销毁*/
  while (ros::ok()) {
    size_t bytes_wrote = my_serial.write(test_string);
    //read the message from com1
    //string result = my_serial.read();/*test_string.length()-1*/
    /*ROS_INFO和类似的函数用来替代printf/cout*/
    ROS_INFO("%s", test_string.c_str());

    // ros::spinOnce() use for ros callback function
    ros::spinOnce();


    cout << "Iteration: " << count << ", Bytes written: "<<endl;
    cout << bytes_wrote << ", Bytes read: ";
    // cout << result.length() << ", String read: " << result << endl;

    // 这条语句是调用ros::Rate对象来休眠一段时间以使得发布频率为10hz
    loop_rate.sleep();

    count += 1;
  }

  return 0;
}

int main(int argc, char **argv) {
  try {
    return run(argc, argv);
  } catch (exception &e) {
    cerr << "Unhandled Exception: " << e.what() << endl;
  }
}
