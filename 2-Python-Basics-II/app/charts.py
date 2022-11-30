import matplotlib.pyplot as plt
# https://matplotlib.org/

def generate_bar_chart(labels, values):
    # variables from matplotlib => figure and coordinates from where we will start to graphic
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis("equal")
    plt.show()


if __name__ == "__main__":
    labels = ["a", "b", "c"]
    values = [100, 400, 800]
    # bar chart
    # generate_bar_chart(labels, values)
    # pie chart
    generate_pie_chart(labels, values)

