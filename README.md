# Assessing Distributed CDNs

#### -- Project Status: [Completed]

## Intro/Objective
The purpose of this project is to provide a framework that aims to reduce traffic to content distribution nodes and allows for further targeted content recommendations of Netflix users. Streaming services are pervasive in today's society and the amount of content being delivered via the internet is growing exponentially year over year. While CDNs were originally designed to reduce congestion on the root database, we're approaching a future where they themselves will be overwhelmed by traffic. In this project, we present a framework that addresses these concerns by leveraging a P2P-CDN hybrid architecture. With our focus on Netflix streaming, we begin by clustering content based on its genre listings and clustering consumers based on their genre preferences. We then map the consumer clusters to the content clusters to find optimal pairings for each group of consumers. The content within that cluster can then be shared via a P2P architecture and consumers can receive additional targeted recommendations based on the cluster they belong to.

### Methods Used
* Data Visualization
* Relational Database management
* Machine Learning
* Scaling/Normalization
* Clustering
* Algorithm Development
* Object-Oriented programming

### Technologies
* Python, jupyter
* Pandas, Numpy
* SKLearn
* K-means clustering
* Matplotlib

## Project Description
* Data  
   * Netflix Prize Data: 100 million+ user ratings (450,000+ users with 17,000+ titles)
   * themoviedb Data: Detailed information of 350,000+ movies
   * Joined the 2 datasets on movie title and release date to relate user ratings with particular characteristics of movies
* Clustering Considerations
   * Wanted a model that allowed for configurable cost functions and cluster sizes
   * Wanted low asymptotic time complexity during training
   * Chose to develop a custom k-means clustering algorithm that allowed for such configurations
* Content Clustering by Genre
   * Created bit vectors for each movie that corresponded to their genre listings
   * Penalized extreme cluster sizes as too small provides only marginal benefits, but too large realistically runs into memory constraints
* Consumer Clustering by Genre Preferences
   * Developed an algorithm to normalize user ratings and score each genre for each user based on their interests
   * Penalize small clusters as they wouldn't realistically meet memory requirements
* Mapping Consumer Clusters to Content Clusters
   * Find the pairings such that the average genre preferences of a consumer cluster most closely resemble the average genre makeup of a content cluster
   * Absolute difference used for distance measurement

## For more detail and discussion:
* [Blog Post](https://pjourgensen.github.io/distributedCDN.html)

