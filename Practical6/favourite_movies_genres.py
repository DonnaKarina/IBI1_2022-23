#first create a dictionary according to the data
#check if the key is in the dictionary and print it. Learn from https://blog.cs$
#print the whole dictionary
#use pyplot to create a pie chart
#name the labels and then defines their size as the numbers of student
#label the percentage of each genre
#ensure the pie is acircle
genre = {'Comedy':73, 'Action':42, 'Romance':38, 'Fantasy':28, 'Science-fiction$
print ("genre['Comedy']:", genre['Comedy'])
print (genre)
import matplotlib.pyplot as plt
labels='Comedy', 'Action', 'Romance', 'Fantasy', 'Science-fiction', 'Horror', '$
sizes=[73, 42, 38, 28, 22, 19, 18, 12, 8, 7]
fig, ax=plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
