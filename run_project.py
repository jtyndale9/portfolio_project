import ETL.perform_ETL as ETL
import data_viz.create_plot as plot

data = ETL.run()
plot.visualize(data)