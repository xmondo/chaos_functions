import os
import glob as gb
import cairosvg
from PIL import Image

svg_directory = <path to plot directory>
png_directory = <path to plot directory>
output_gif = <path to animated gif file>

os.chdir(svg_directory)
svg_list = gb.glob('*.svg')
limit = len(svg_list) + 1

if __name__ == '__main__':
    try:
        if limit > 1:
            print('processing plots...')
            for i in range(1, limit):
                svg_file = os.path.join(svg_directory, f'{i}.svg')
                png_file = os.path.join(png_directory, f'{i}.png')
                cairosvg.svg2png(url=svg_file, write_to=png_file)

            images = [Image.open(os.path.join(png_directory, f'{i}.png')) for i in range(1, limit)]
            images[0].save(output_gif, save_all=True, append_images=images[1:], duration=100, loop=0)

            print('animated gif created successfully...')
            print('clean up png and svg files...')

            for i in range(1, limit):
                svg_file = str(svg_directory) + str('/') + str(i) + str('.svg')
                png_file = str(png_directory) + str('/') + str(i) + str('.png')
                os.remove(svg_file)
                os.remove(png_file)
        else:
            print('check to see if trig plots have been generated...')
    except Exception as err:
        print(err)
