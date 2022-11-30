from app import read_csv, charts


#def get_population_percentage(country_list):
#    population_percentage_dict = {}
#    for country in country_list:
#        population_percentage_dict[country]:


global_data = read_csv.read_csv("./app/world_population.csv")
# print(global_data)
print(len(global_data))

labels_countries = [global_data[i]['Country/Territory'] for i in range(1, len(global_data))]
values_pop_percentage = [float(global_data[i]['World Population Percentage']) for i in range(1, len(global_data))]

print(labels_countries, values_pop_percentage)

charts.generate_pie_chart(labels_countries, values_pop_percentage)

