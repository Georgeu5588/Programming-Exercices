#IN Python we have different data types su as:
#Numeric - Sequence - Dictionary - Boolean - Set
#Inside numeric we find: integer, float and complex number.
#Inside sequence we find: string, list and tuples.

age = 12
print('The variable, age is of type: ', type(age)) #the function 'type' returns the type of data that is stored in a variable. 

score = 3.6
print('The variable, score is of type: ', type(score))

complexx = 12 + 12j
print('The variable, complexx is of type: ', type(complexx))

name = 'Jorge'
print('The variable, name is of type: ', type(name))

courses = ['Python', 'Databases', 'HTML', 'CSS', 'JavaScript'] #A list contains a sequence of elements that is mutable or changeable. It can contain diffeten data types.
print('The variable, courses is of type: ', type(courses))

jorgeMunoz = ('Jorge', 'Muñoz', 27, 3003609585) #Tuples are a data structure that is very similar to lists, with the difference that this one is immutable. It can contain different data types.
print('The variable, jorgeMunoz is of type: ', type(jorgeMunoz))

countryCapitals = { 
    "Germany": "Berlin",
    "Colombia": "Bogota",
    "Canada": "Ottawa",
    "England": "London"
}
#A dictionary is a kind of data structure that stores items in key-value pairs. A key is a unique identifier for an item, and a value is the data associated with that key. You can manipulate the dictionary using different methods like dict.update(), dict.pop(), and dict.popitem().
print('The variable, countryCapitals is of type: ', type(countryCapitals))


