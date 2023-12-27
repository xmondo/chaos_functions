import chaos_plot_classes as cp

font_size = 7
width = 5
height = 4
plots = 4
factor = 2.9
steps = 15
x = 0
y = 0.5

plot_dir = <output directory>

if __name__ == '__main__':
    try:
        logistic_map = cp.LogisticMap(font_size, width, height, plots, steps, factor, x, y, plot_dir)
        logistic_map.growth()
    except Exception as err:
        print(err)
