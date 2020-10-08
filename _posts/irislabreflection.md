# Iris Lab Reflection

#### Describe your process in finding these answers. Include details such as who you worked with, what methods you tried, what worked or didn’t work, what could have gone better, and what you learned during this lab. Feel free to attach images, screenshots, pseudocode, etc to elaborate on your response!
Worked on with Anthony White

This lab was fairly difficult in how many details had to be considered in what could be seen as simple steps.

I referred to the code I original coded from the previous assignment which checks for the species and petal-widths associated with each of those items, and placing all of the widths
into a separate list. Then it takes that list, treats it as one long string, then converts into a dictionary format, with the species as the "key" and list associated with that species
as the "value".

The code was pretty similar to what I needed to do for this assignment, so I implemented a lot of the code from before. 
First I changed all of the value holder's names in order to differentiate what was necessary.
~~~
Iris_setosaList1 = list() #List of Setosa petal lengths
Iris_versicolorList1 = list() #List of Versicolor petal lengths
Iris_virginicaList1 = list() #List of Virginica petal lengths
~~~
and
~~~
Iris_setosaList2 = list() #List of Setosa sepal widths
Iris_versicolorList2 = list() #List of Versicolor sepal widths
Iris_virginicaList2 = list() #List of Virginica sepals widths
~~~

In general, the code for appending the values of whatever I wanted to an empty list stayed the same, beyond the small value changes.

~~~
 for row in data: #Go through rows in compiled dataset
        if row["species"] == "Iris-setosa": #if in iris.csv file, "species" key's value == "Iris-setosa"
            Iris_setosaList1.append(row["petal-length"]) #add the "petal-length" key's value to list 'Iris_setosaList1'

        if row["species"] == "Iris-versicolor":
            Iris_versicolorList1.append(row["petal-length"])

        if row["species"] == "Iris-virginica":
            Iris_virginicaList1.append(row["petal-length"])
~~~
~~~
for row in data: #Go through rows in compiled dataset
        if row["species"] == "Iris-setosa": #if in iris.csv file, "species" key's value == "Iris-setosa"
            Iris_setosaList2.append(row["sepal-width"]) #add the "sepal-width" key's value to list 'Iris_setosaList2'

        if row["species"] == "Iris-versicolor":
            Iris_versicolorList2.append(row["sepal-width"])

        if row["species"] == "Iris-virginica":
            Iris_virginicaList2.append(row["sepal-width"])
~~~
{: .box-note}
**Note:** This information from the .csv file was written using _csv.DictReader()_, rather than _csv.reader()_.

However, a new part I needed to add code for was averaging all of the values, before implementing code to find which had the highest average.
So I started with the idea of parsing through the lists I had created with the previous code and adding those up to determine some total, before dividing by the
length of the list to find that average.
~~~
for i in range(0, len(Iris_setosaList2)):
        widthSepalsOfSetosa += float(Iris_setosaList2[i]) #adds all the widths from Iris_setosaList to widthSepalsOfSetosa
widthSepalsOfSetosa = widthSepalsOfSetosa / len(Iris_setosaList2) #average total by width of Iris_setosaList2
~~~
And repeat that for the other two species.

Some issues I ran into here however was with the for loop and then with the actual values stored within the list.

Firstly the for loop was originally set to just parse through the list itself using "i", like so:
~~~
for i in Iris_setosaList2:
~~~
This did not prove fruitful however as "i" was apparently being treated as an str / string, so I made sure to clarify using _range_ instead.

Next was the issue with the actual list.
When compiling the information into the lists earlier, what I failed to realize was that all of those values were string values, rather than being treated as numerical.
So when it game to _+=_, the code didn't run because it wasn't a numerical format within the values in the lists.
In order to fix this, I applied float() to each value to convert it to a numerical format that could be used to calculate the total.
(int() can not be used because all the values are at the very least doubles / contain decimal values.)

After that was fairly easy, I just needed add those values to the dictionary format before having a couple if-statements which would print-out the species which contained an average value that was larger than the rest.
~~~
#vv checks which average length is the longest out of all the species and spits out answer
    if widest_sepals["Iris_setosa"] > widest_sepals["Iris_versicolor"] and widest_sepals["Iris_setosa"] > widest_sepals["Iris_virginica"]:
        print("The [Iris-setosa] has the widest average sepal length.") 
    
    if widest_sepals["Iris_versicolor"] > widest_sepals["Iris_setosa"] and widest_sepals["Iris_versicolor"] > widest_sepals["Iris_virginica"]:
        print("The [Iris-versicolor] has the widest average sepal width.")

    if widest_sepals["Iris_virginica"] > widest_sepals["Iris_setosa"] and widest_sepals["Iris_virginica"] > widest_sepals["Iris_versicolor"]:
        print("The [Iris-virginica] has the widest average sepal width.")
~~~

_Similar code overall was applied the other assignment within the lab._


##### Conclusion
This lab required some fine tweaking, but overall was fairly straightfoward. Some things that could've went better were if I was better at Python, I could've ran some
code that would tell me what was the largest value in the dictionary rather than using a couple if-statements. I think I learned how to better code in Python for sure,
as the coding / syntax is fairly new to me as I have only coded in Java before. Great lab.

