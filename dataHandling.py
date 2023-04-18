import pandas
import statistics
import plotly.figure_factory as ff
import random

df = pandas.read_csv('medium_data.csv')
claps = df['claps'].to_list()

claps_mean = statistics.mean(claps)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(claps) - 1)
        value = claps[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_mean(10)
        mean_list.append(set_of_means)
    print(mean_list)
    show_fig(mean_list)

def show_fig(list_of_means):
    data = list_of_means
    fig = ff.create_distplot([data], ["temp"], show_hist=False, colors=['deeppink'])
    fig.show()

setup()