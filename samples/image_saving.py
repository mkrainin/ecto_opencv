#!/usr/bin/env python
#
# Simple vid cap
#
import ecto
from ecto_opencv import highgui, calib, imgproc

plasm = ecto.Plasm()
video_cap = highgui.VideoCapture(video_device=0)

fps = highgui.FPSDrawer()

video_display = highgui.imshow('imshow',
                               name='video_cap', waitKey=2, triggers=dict(save=ord('s')))

saver = ecto.If(cell=highgui.ImageSaver("saver", filename_format='ecto_image_%05d.jpg',
                                   start=1))


plasm.connect(video_cap['image'] >> fps['image'],
              fps['image'] >> video_display['input'],
              video_display['save'] >> saver['__test__'],
              fps['image'] >> saver['image'],
              )

if __name__ == '__main__':
    ecto.view_plasm(plasm)
    sched = ecto.schedulers.Threadpool(plasm)
    sched.execute()

