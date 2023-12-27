import chaos_plot_classes as cp
import numpy as np

# max number of frames is 350

number_of_frames = 200
frames = np.linspace(0, 1, number_of_frames)
image_frame_number = 1
low_res = 500
medium_res = 1000
high_res = 10000
very_high_res = 100000
plot_dir = <path to plot directory>
try:
    print('number of frames: ', len(frames))
    for k in frames:
        print(k)
        plot = cp.ChaosTrigPlot(8, 12, 2, -1, 1, high_res, k, image_frame_number, plot_dir)
        plot.fplot()
        image_frame_number += 1
except Exception as err:
    print('Exception', err)
