gst-launch-1.0 -v nvarguscamerasrc sensor_id=0 ! 'video/x-raw(memory:NVMM),width=1280,height=720,framerate=120/1, format=NV12' ! fpsdisplaysink video-sink=fakesink text-overlay=false

