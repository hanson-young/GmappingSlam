# cartConsole
Main RoboCartConsole

# 2016.1.31 
### problem:                                            
1. Can't do it realtime.                         
2. Can't stop automaticly.                        
3. need to excicute two process manually.         
4. ugly.                                          
                                                     

# realtime solution 
1. put readline() method into generator(done)       
2. read as many lines as you can at a time          
  

# 2016.2.1 
### problem:                                            
1. Can't stop automaticly.                        
2. Program will be block when no data send.       
3. Ugly.                                          
4. Need to run it using thread programming.       
                                                      

# 2016.2.17  
### update:                                             
1. Embedded the plot into Qt5(used to be Tkinter) 
2. Woring on complete the function                
3. Thread block problem still unhandled           
                                                      

# 2016.2.18 
### update:                                             
1. After added timeout=0 arg into serial init the thread block problem finnal solved. but program would still stuck after plotting began 
2. The problem above was because when no data received program stuck into a endless loop of method generatorself.                           
3. working on completing function                 
                                                      

# 2016.3.15 
### update:                                            
1. Solved many problems which was mentioned above 
                                                      
### problem:                                            
1. Clear function dosen't work correctly.         
                                                      
### blueprint:                                          
1. Now that we are able to use uart to transport data from PC to cart, which means that it is possible control cart by PC. It'll including these function:
* use keyboard as a joystick                 
* replace keyborad and LCD's function        
* make a full use of PC's performance to do some adjust work like PID adjustment       
* more to think and discuss.                 
                                                      

# 2016.4.2 
### update:                                             
1. Since I know that uart can do I/O the same time(almost), developed the control function.    
2. Now using Lowpass filtering to ajust speed figure and had a great effect.
3. Rewrite clear function, now it's good to use.
4. Rewrite axis limits autoreset function, now it will not take a long time to reset bit by bit.                                           
                                                      
### problem:                                            
1. But goRoute function can't work well since main control program changed, now click goRoute button with what click EnmergencyStop button to dirve the cart. Need to fix it.             
                                                      
### blueprint:                                          
1. To make this software more useful. use it at an analyse tool to have a speedup of our dear cart.                                          
                                                      

# 2016.4.12 
### update:                                             
1. Add 4 plots for four wheel rotation.           
2. completed save function(auto generate its name)                                          
                                                      
### blueprint:                                          
* Same as one above                                 
                                                      

# 2016.4.26
### update:                                             
1. Remove wheel's rotation plots 'cause it is too slow to update intime
2. Add a useless function to record time node manually, I don't know why there are people who wanna go to somewhere by carriage just for get their destination faster when a car available.
                                       
### blueprint:                                          
1. Record cart information automatic.             
2. Demotion plot function as an alternative option
                                                       
