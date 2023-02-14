# simple graph for free dataset csv format

import pandas as pandas_library
import matplotlib.pyplot as plot_library
from matplotlib.backends.backend_pdf import PdfPages

# location of downloaded dataset (in my case is looks like this)
data_set = pandas_library.read_csv("E:\\graph_data_sales\\company_sales_data.csv")

# two types of information which you will use. Here I use column shampoo and number month from dataset
list_of_shampoo = data_set['shampoo'].tolist()
list_of_month = data_set['month_number'].tolist()

# location where pdf file should be downloaded and name is graph_shampoo.pdf
with PdfPages(r'E:\Downloads\graph_shampoo.pdf') as chart_to_pdf_file:
    # plotting graph by using two lists -> 1 list - list_of_month - x position, 2 list - list_of_shampoo - y position
    plot_library.plot(list_of_month, list_of_shampoo, label='Month of Shampoo data of last year')

    # creation of title
    plot_library.title('Company selling shampoo per month')

    # Name of x information -> horizontal position
    plot_library.xlabel('Number of month')
    # Name of y information -> vertical position
    plot_library.ylabel('Shampoo amount')

    # number months will appear in vertical position x and y values
    plot_library.xticks(list_of_month)
    plot_library.yticks([1000, 2000, 3000, 4000])

    # show output. But it will not be needed for downloading in pdf file
    # plot_library.show()

    plot_library.grid(True)
    chart_to_pdf_file.savefig()
    plot_library.close()
