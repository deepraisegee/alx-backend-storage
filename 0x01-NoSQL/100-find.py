// lists all documents with name starting by Holberton in the collection school:
// The database name will be passed as option of mongo command

db.school.find({name: /^Holberton/}).pretty()