![image](https://user-images.githubusercontent.com/82448514/179390368-d83e3c73-4510-405a-8306-f66a63110b21.png)
# Snap-To-Road

Implementation of the Snap-to-Roads functionality to correctly snap gps co-ordinates to their corresponding haul roads


# Problem statement:

A truck travelling on a Haul Road inside a Jobsite (a quarry, road construction site, mine site, etc.) will be sending GPS data back to Back Office. This GPS data that is based on GNSS satellites will typically have accuracy issues based on the visibility of the GNSS satellites to the GPS receiver. We would need capabilities to snap the GPS points back to the Haul Road.


A solution to this problem is to snap each point to the nearest road segment. Need a post-processing engine to align the GPS data on a lane of the road. This needs to be near real-time.

[Detailed Explation](https://github.com/xXAtoZXx/Snap-To-Road/blob/main/Snap%20to%20Road%20Functionality%20for%20off-road%20vehicles.pdf) 
