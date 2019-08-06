# ORB_SLAM2_elsalab_ver

A modification of ORB_SLAM2 with map reloading and grid-map generating.

# License

ORB-SLAM2 is released under a [GPLv3 license](https://github.com/raulmur/ORB_SLAM2/blob/master/License-gpl.txt). For a list of all code/library dependencies (and associated licenses), please see [Dependencies.md](https://github.com/raulmur/ORB_SLAM2/blob/master/Dependencies.md).

**Authors:** [Raul Mur-Artal](http://webdiis.unizar.es/~raulmur/), [Juan D. Tardos](http://webdiis.unizar.es/~jdtardos/), [J. M. M. Montiel](http://webdiis.unizar.es/~josemari/) and [Dorian Galvez-Lopez](http://doriangalvez.com/) ([DBoW2](https://github.com/dorian3d/DBoW2))

# Execution

- commands is in Note.txt
- open 4 terminals

```
$ roscore
$ zedros # zed camera
$ monopub
$ monosub
```



## Save/Load map

- When terminating the ORB_SLAM2, the map will be saved as file.bin  automatically under $HOME

- - It may take a few minutes, Do Not close the terminal
  - Remember to change file name if necessary 

- When restarting the ORB_SLAM2, it will read the map at the beginning

- - Make sure that file.bin is under $HOME
  - The pointer of the terminal is also at $HOME
  - Cancel the Localization mode so that it can add new keyframes and publish the camera pose



## Fake AMCL Pose Usage

```
$ sudo su # admin mode Dangerous!!!!
$ sudo -H
$ source /home/elsalab/zed/zed-enb/bin/activate
$ source /home/elsalab/Desktop/catkin_ws/devel/setup.bash
$ rosrun fake_amcl_pose fake_amcl_pose.py

^ press esc to exit
```



## Grid Map Generating

```
$ python pointCloudToGridMap2D.py --help
  usage: pointCloudToGridMap2D.py [-h] [--point_cloud POINT_CLOUD_FNAME]
                                [--keyframe_trajectory KEYFRAME_TRAJECTORY_FNAME]
                                [--scale SCALE_FACTOR]
                                [--resize RESIZE_FACTOR]
                                [--filter FILTER_GROUND_POINTS]
                                [--counter LOAD_COUNTERS]
                                [--free_thresh FREE_THRESH]
                                [--occupied_thresh OCCUPIED_THRESH]
                                [--output_file_name OUTPUT_FILE_NAME]
^ press any key on cv-window to terminate
^ outputfiles includes a `pgm` file and a `yaml` file
```



## Screen Recording

```
kazam

# video converter 
ffmpeg -i 原檔名.mp4 -f mp4 -vcodec libx264 -preset fast -profile:v main -pix_fmt yuv420p -acodec aac 轉檔名.mp4 -hide_banner

```



## See Topic 

```
$ rosrun rqt_graph rqt_graph
```


## Reference
```
https://github.com/abhineet123/ORB_SLAM2 # grid map ver.
https://github.com/Alkaid-Benetnash/ORB_SLAM2 # save map ver.
```
