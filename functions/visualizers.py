from plotnine import *
import pandas as pd

def scatter_and_smooth(data_frame,
                       x, y,
                       smooth_method:str,
                       mean_transform:bool,
                       x_label:str, y_label:str,
                       save_fig:bool):
    """
    This function makes scatter plot and fits a curve at the same time.
    It makes serial plotting more easier.

    :param dataframe: Pandas dataframe object that contains variables to plot
    :param x: independent variable
    :param y: dependent variable
    :param smooth_method:str,Any smoothing method that is compatible with geom_smooth object of
    plotnine package.
    :param mean_transform: bool, When true, calculates the mean of Y at each of X and plots these mean values
    against the levels of X. Better way of plotting discrete vs discrete. Default is True
    :param x_label: string, Label of x to make plot look nicer
    :param y_label: string, Label of y to make plot look nicer
    :param save_fig: bool,
    :return: Plot
    """
    if mean_transform:
        plot_df = data_frame.groupby([x])[y].mean().reset_index().copy()
        plot_df.dropna(inplace=True)

    else:
        plot_df = data_frame.copy()

    plot = (ggplot(plot_df,
                   aes(x=x, y=y)) +
            geom_smooth(method=smooth_method, se=True, color="darkred") +
            geom_point(color="darkred") +
            xlab(x_label) +
            ylab(y_label) +
            ggtitle("Relationship Between {x} \n and {y}".format(x=x_label, y=y_label)))

    # save the plot
    if save_fig:
        ggplot.save(self=plot,
                    filename="{x}_vs_{y}.png".format(x=x, y=y),
                    path="plots/")

    return plot










def plotbars(data_frame,
             x, y,
             x_label, y_label,
             mean_transform:bool=True,
             save_fig:bool=True):
    """
    This function makes barplot with x and Y using plotnine package.
    It makes serial plotting more easier.

    :param data_frame:Pandas dataframe object that contains variables to plot
    :param x:Independent variable
    :param y:Dependent variable
    :param x_label: string, Label of x to make plot look nicer
    :param y_label: string, Label of y to make plot look nicer
    :param mean_transform: bool. When true, calculates the mean of Y at each of X and plots these mean values
    against the levels of X. Better way of plotting discrete vs discrete. Default is True
    :param save_fig: bool, save figure. Default is True
    :return:plot
    """
    if mean_transform:
        plot_df = data_frame.groupby([x])[y].mean().reset_index().copy()
        plot_df.dropna(inplace=True)

    else:
        plot_df = data_frame.copy()


    # Create the plot
    plot = (ggplot(plot_df,
                   aes(x=x, y=y)) +
            geom_col(fill="darkred") +
            xlab("{xlab}".format(xlab=x_label)) +
            ylab("{ylab}".format(ylab=y_label)) +
            ggtitle("Average {ylab} per {xlab}".format(ylab=y_label, xlab=x_label))
            )
    # save plot
    if save_fig:
        ggplot.save(self=plot,
                    filename="{x}_vs_{y}.png".format(x=x, y=y),
                    path="plots/")

    # display the plot
    return plot