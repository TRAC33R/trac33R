# Hospital Lab Reflection

#### Write a blog post for your website with responses to the following:

##### 1. Which county has the most hospital beds per person (regardless of bed type)?
The county with the most hospitals is Chemung, NY. (18,059 Beds)

##### 2. Discuss how you obtained and cleaned the dataset. Make sure to explain what methods you used and why.
_Obtaining the dataset_
I created a new "hospital.csv" file by running "w" rather than "r", and set an object to be associated with csv.writer.
~~~
with open ("hospital.csv", 'w') as csvfile:
    data = csv.writer(csvfile)
~~~
After that I created a loop that would run until it ran into an error code as that would mean either it didn't work or it ran into the end of the list. For each iteration of the loop it would update the query "id", updating to the next "row" of information from the API. Then that info is written on a new line in the .csv file.
~~~
if hospital.status_code == requests.codes.ok:
            #data = hospital.text
            #print(data)
            dataInfo = hospital.text
            dataList = list(dataInfo.split(","))
            print(dataList)
            data.writerow(dataList)
            idNum = idNum + 1
        else:
            #print(hospital.status_code)
            #print(hospital.text)
            breakLoop = True
~~~

_Cleaning the Dataset_
After coverting the file to a .csv, I opened it in Google Sheets. I then highlighted all of the header labels before creating two columns called "measure #" and "Total Beds (Exact)". Afterwards I ran a formula from column E "measure" as each had the characters "HAB" after their unit, so in this column I ran a formula such as "=ARRAYFORMULA(left(E2:E135,len(E2:E135)-3))" which would shorten each of the associated cells by 3 characters. Then to make sure they were casted as a Numerical Value by the Sheets, I selected the column and went to Data and selected the type as "Number". After that I multiplied the "beds"*"measure #" to get the exact number of beds. Afterwards, I ran the ROUND function to round those numbers down to a realistic number as you cannot exactly have half a bed in this case. And I got rid of the extra decimal places from the rounding.

##### 3. Discuss your process of how you worked on this lab. Include details such as who you worked with, what methods you tried, what worked or didn’t work, what could have gone better, and what you learned during this lab. Focus more on the programming side of the lab! Feel free to attach images, screenshots, pseudocode, etc to elaborate on your response.
For this lab, I consulted with Anthony. I ran into problems with calling the "id" as I was calling "id" rather than querying an actual integer itself. After changing that most of the code itself worked for pulling information from the API. The only other issue in this case was the need to take the string from the information pulled, formatting that into a List formatting with the ".split()" method, and then casting that entire thing to a list().

Originally I actually compiled and figured out the county with the most hospital beds within Google Sheets before realizing I had to run the code rather than doing that. So I just used my answers from the sheet to check if the numbers I ran in the coding file were correct.

In order to figure out which county had the most hospital beds in Python, I open the "hospital.csv" file that I created earlier. Then I transcribed the information from .csv file to a local dictionary within the file. However, when a key with the same name is added to the dictionary, it deletes the previous key's value. So in order to fix that, I wrote an if-else statement which if the previous entry exists, the previous value is stored in an temporary holder. The new value is then called from the .csv, casted to an int from a str, and then added that value to previous one, before updating that key with the new value. Afterwards, I just parsed through the dictionary I created from the .csv file, running an if statement that said if the current key's value that's being looked at is greater than the one stored currently as having the most beds, update that with the new number in addition to updating the string holder with the new county.
~~~
for num in hospitalBedPerCounty:
    if hospitalBedPerCounty[num] > mostBeds:
        mostBeds = hospitalBedPerCounty[num]
        mostBedsCounty = num
        #print(mostBedsCounty)
        #print(mostBeds)
print(mostBedsCounty)
print(mostBeds)
~~~
Overall the lab had a lot of little kinks but was not insanely difficult to work through. I learned that you can cast a string to a list(), how to create a csv file and write to it, what and how to use a the .split() method, in addition to how to work with an API.