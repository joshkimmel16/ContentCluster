'''
This script cross-references the results of movie clustering analysis and genres to produce a user-friendly summary
'''

#imports
import sys
import json
import time
import statistics

### Helper Methods ###

#create a border for better viewing experience
def create_separator(major):
    if major == True:
        return "\n=========================\n"
    else:
        return "\n-------------------------\n"
    
#translate cluster mean into a readable interpretation of its corresponding genres
def genre_breakdown(mean, genres):
    output = ""
    l = len(mean)
    for x in range(l):
        output = output + (genres[x] + " rating = " + str(int(mean[x]*100)) + "%, ")
    output = output[:-2]
    return output

#load config
data_file_path = ""
genre_file_path = ""
algorithm = ""
with open('../config/movie_summary_config.json') as json_file:  
    data = json.load(json_file)
    data_file_path = data["data_file_path"]
    genre_file_path = data["genre_file_path"]
    algorithm = data["algorithm"]

#load data into script
results = None
with open(data_file_path) as json_file:
    results = json.load(json_file)
genres = None
with open(genre_file_path) as json_file:
    genres = json.load(json_file)

    
if algorithm == "kmeans":
    lines = []
    lines.append("Number of datapoints analyzed: " + str(results["dataset_size"]) if "data_size" in results else "Unknown")
    lines.append("Total runtime: " + str(results["end_time"] - results["start_time"]) if "start_time" in results and "end_time" in results else "Unknown" + " seconds")
    lines.append(create_separator(True))
    
    error_arr = []
    size_arr = []
    for result in results["results"]:
        lines.append("K Value: " + str(result["kValue"]))
        lines.append("Total Error: " + str(result["totalError"]))
        lines.append(create_separator(False))
        for group in result["groupings"]:
            size_arr.append(group["clusterSize"])
            error_arr.append(group["intraError"])
            lines.append("Cluster Size: " + str(group["clusterSize"]))
            lines.append("Genre Categorization: " + genre_breakdown(group["mean"], genres))
            lines.append("Total Error within Cluster: " + str(group["intraError"]))
            lines.append("Total Error to Other Clusters: " + str(group["interError"]))
            lines.append(create_separator(False))
        lines.append("Cluster Error Mean: " + str(statistics.mean(error_arr)))
        lines.append("Cluster Error Variance: " + str(statistics.variance(error_arr)))
        lines.append("Cluster Size Mean: " + str(statistics.mean(size_arr)))
        lines.append("Cluster Size Variance: " + str(statistics.variance(size_arr)))
        error_arr = []
        size_arr = []
        lines.append(create_separator(True))
        
    for line in lines:
        print (line)
else:
    print ("The algorithm specified has not been implemented yet!")