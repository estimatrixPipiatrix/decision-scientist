import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

def image_filter(num_kernels,frame_rows,frame_cols):
    kernels = pd.read_csv('kernels.csv').to_numpy()
    kernels = kernels.reshape(num_kernels,frame_rows,frame_cols)

    num_plot_rows = round(num_kernels/6.0)+1
    num_plot_cols = num_plot_rows
    fig, axes = plt.subplots(num_plot_rows,num_plot_cols)
    for i, ax in enumerate(axes.flat):
        ax.imshow(kernels[i])
    plt.show()
