### 1. Which dataset did you work with?

For this lab, I decided to work with the airports dataset as it seemed straightforward and eas(ier) to comprehend and interpret the data.

### 2. Discuss your analysis of the dataset. You are encouraged to use DataFrames and other Python libraries! Include details such as: 
- The variables you looked at
- Distributions of variables (center and variability)
- Relationships between variables
- Visualizations of the dataset

AND (+)

### 3. What conclusions can you draw about this dataset? What is your supporting evidence?

First, I ran a quick summary on the data to see which "Country" had the most airports, before narrowing my focus into which "City" within that "Country" had the most airports overall. I also created a countplot graph that visually compared the amount of airports in the "United States" to the overall amount of airports in the world not including the US.
```
count              7698
unique              235
top       United States
freq               1512
```
This quick summary data tells us first the amount of cells in the dataset in one column: count = 7698. Furthermore, there are 235 instances of unique "Countries", with the United States appearing the most frequent in the dataset, for a total of 1512 times.

After running,
```
print(airports[airports["Country"] == "United States"].describe())
```
we pull the data below,
```
        Airport ID     Latitude    Longitude     Altitude
count   1512.000000  1512.000000  1512.000000  1512.000000
mean    6697.720238    40.353871  -101.790316  1108.869048
std     2875.261466    10.101375    26.832546  1546.707950
min     3411.000000   -35.960556  -176.645996  -115.000000
25%     3789.750000    33.938050  -116.782499   113.000000
50%     6992.500000    38.901550   -94.831600   601.000000
75%     8559.250000    43.800850   -82.749973  1225.000000
max    13803.000000    71.285402   174.113998  9070.000000
```
which describes the overall numerical data from the "Country" called "United States". From this data we can see the average Airport ID, in addition to the highest recorded Airport ID. Having an average of around 6600, which is around the halfpoint of the overall Airport IDs in the dataset (14110 is the max Airport ID overall), we can infer that the United States started building airports around the middle of age of airports. The max Airport ID of 13803 also suggest however that the United States are still creating more airports, in addition to it being quite recent. Looking at the 75%, we can also infer that most of the instances of United States tends to be around the 8500s in terms of Airport ID. So still close to the middle area, but also a little later, suggesting that the United States adopted more airports in the later half of their creation. Also looking at the mean Altitude, we can also see how most airports were created at a higher altitude than normal, so most likely on some sort of mountain / raised ground. (mean = ~1108)



